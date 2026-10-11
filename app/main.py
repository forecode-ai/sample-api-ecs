"""Payments quote API: a tiny HTTP service with no dependencies."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


def quote(amount_cents: int, currency: str) -> dict:
    fee = max(30, round(amount_cents * 0.0175))
    return {"amount": amount_cents, "currency": currency.upper(), "fee": fee, "total": amount_cents + fee}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/healthz":
            body, status = {"status": "ok"}, 200
        elif self.path.startswith("/quote/"):
            _, _, amount, currency = self.path.split("/", 3)
            body, status = quote(int(amount), currency), 200
        else:
            body, status = {"error": "not found"}, 404
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
