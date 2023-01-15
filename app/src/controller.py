from http.server import BaseHTTPRequestHandler, HTTPServer
import json

"""
Este código cria uma classe chamada "RequestHandler" 
que herda de BaseHTTPRequestHandler e sobrescreve o método "do_GET".
"""

class RequestHandler(BaseHTTPRequestHandler):

    def _send_response(self, message):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(message).encode())

    """
    Verifica-se se a rota inicia com "/hello",
       se sim, extrai o 'id' do path e o 'codigo' do header,
       e retorna ambos no corpo da resposta no formato json.
    """
    def do_GET(self):
        if self.path.startswith("/hello"):
            id = self.path.split("/")[-1]
            code = self.headers['codigo']
            message = {"id": id, "codigo": code}
            self._send_response(message)

httpd = HTTPServer(('localhost', 8000), RequestHandler)
httpd.serve_forever()
