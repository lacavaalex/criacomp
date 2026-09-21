#!/usr/bin/env python3
"""Receptor OTLP mínimo, para ver o que um agente conta sobre si.

Sobe um servidor HTTP em :4318 que aceita o protocolo OTLP/HTTP e imprime
os spans recebidos em forma de árvore. Só biblioteca padrão.

Não é observabilidade de verdade: é uma janela para o dado cru.
"""
import json
import gzip
from http.server import BaseHTTPRequestHandler, HTTPServer

PORTA = 4318
INTERESSANTES = ("invoke_agent", "chat", "execute_tool", "gen_ai")


def achata(v):
    """O valor de um atributo OTLP vem embrulhado por tipo."""
    if not isinstance(v, dict):
        return v
    for chave in ("stringValue", "intValue", "doubleValue", "boolValue"):
        if chave in v:
            return v[chave]
    return v


class Receptor(BaseHTTPRequestHandler):
    def do_POST(self):
        corpo = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        if self.headers.get("Content-Encoding") == "gzip":
            corpo = gzip.decompress(corpo)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b"{}")

        try:
            dado = json.loads(corpo)
        except Exception:
            print("  (corpo não é JSON: provavelmente protobuf; use OTEL_EXPORTER_OTLP_PROTOCOL=http/json)")
            return

        for recurso in dado.get("resourceSpans", []):
            for escopo in recurso.get("scopeSpans", []):
                for span in escopo.get("spans", []):
                    self.imprime(span)

    def imprime(self, span):
        nome = span.get("name", "?")
        ini = int(span.get("startTimeUnixNano", 0))
        fim = int(span.get("endTimeUnixNano", 0))
        dur = (fim - ini) / 1e9 if fim > ini else 0
        pai = span.get("parentSpanId") or ""
        recuo = "  " if pai else ""

        marca = "*" if any(k in nome for k in INTERESSANTES) else " "
        print("%s%s %-28s %7.2fs" % (recuo, marca, nome, dur))

        atr = {a.get("key"): achata(a.get("value")) for a in span.get("attributes", [])}
        for chave in ("gen_ai.request.model", "gen_ai.operation.name",
                      "gen_ai.tool.name", "gen_ai.usage.input_tokens",
                      "gen_ai.usage.output_tokens"):
            if chave in atr:
                print("%s     %-32s %s" % (recuo, chave, atr[chave]))

    def log_message(self, *args):
        pass  # o log do servidor competiria com a saída que interessa


if __name__ == "__main__":
    print("receptor OTLP em http://localhost:%d" % PORTA)
    print("aponte o agente com OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:%d" % PORTA)
    print("e, se o agente permitir, OTEL_EXPORTER_OTLP_PROTOCOL=http/json")
    print("Ctrl-C para sair\n")
    try:
        HTTPServer(("", PORTA), Receptor).serve_forever()
    except KeyboardInterrupt:
        print("\nfim")
