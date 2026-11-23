"""Servidor HTTP local para conectar a pagina HTML ao modulo teste.py."""

import json
import math
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

import teste


BASE_DIR: Path = Path(__file__).resolve().parent


class CalculadoraHandler(BaseHTTPRequestHandler):
    """Trata requisicoes da pagina e da API da calculadora."""

    def do_GET(self) -> None:
        """Serve a pagina principal da calculadora."""
        if self.path != "/":
            self.send_error(404)
            return

        pagina: bytes = (BASE_DIR / "index.html").read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(pagina)))
        self.end_headers()
        self.wfile.write(pagina)

    def do_POST(self) -> None:
        """Recebe operacoes e invoca as funcoes Python correspondentes."""
        if self.path != "/api/calcular":
            self.send_error(404)
            return

        try:
            tamanho: int = int(self.headers.get("Content-Length", "0"))
            dados: dict[str, Any] = json.loads(self.rfile.read(tamanho))
            operacao: str = dados["operacao"]
            a: float = float(dados["a"])
            b: float = float(dados["b"])

            if not math.isfinite(a) or not math.isfinite(b):
                raise ValueError("Os numeros devem ser finitos.")

            operacoes: dict[str, Any] = {
                "soma": teste.soma,
                "subtracao": teste.subtracao,
                "multiplicacao": teste.multiplicacao,
                "divisao": teste.divisao,
            }

            if operacao not in operacoes:
                raise ValueError("Operacao invalida.")

            resultado: float = operacoes[operacao](a, b)
            self._responder(200, {"resultado": resultado})
        except (KeyError, json.JSONDecodeError, TypeError, ValueError) as erro:
            self._responder(400, {"erro": str(erro)})
        except ZeroDivisionError as erro:
            self._responder(400, {"erro": str(erro)})

    def _responder(self, status: int, dados: dict[str, Any]) -> None:
        """Envia uma resposta JSON para o navegador."""
        conteudo: bytes = json.dumps(dados).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(conteudo)))
        self.end_headers()
        self.wfile.write(conteudo)


def main() -> None:
    """Inicializa o servidor local da calculadora."""
    servidor: ThreadingHTTPServer = ThreadingHTTPServer(
        ("0.0.0.0", 8000),
        CalculadoraHandler,
    )
    print("Calculadora disponivel em http://127.0.0.1:8000")
    try:
        servidor.serve_forever()
    finally:
        servidor.server_close()


if __name__ == "__main__":
    main()
