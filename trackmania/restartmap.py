import os
import socket
import struct
from http.server import BaseHTTPRequestHandler, HTTPServer

PASSWORD = os.environ["SUPER_ADMIN"]

def restart_map():
    s = socket.create_connection(("127.0.0.1", 5000))
    s.recv(1024)

    def call(handle, method, params=[]):
        params_xml = "".join(
            f"<param><value><string>{p}</string></value></param>"
            for p in params
        )
        xml = f'<?xml version="1.0"?><methodCall><methodName>{method}</methodName><params>{params_xml}</params></methodCall>'.encode()
        s.sendall(struct.pack("<II", len(xml), handle) + xml)
        return s.recv(65536)

    try:
        auth = call(0x80000000, "Authenticate", ["SuperAdmin", PASSWORD])
        print(f"Authenticate: {auth}", flush=True)

        result = call(0x80000001, "RestartMap")
        print(f"RestartMap: {result}", flush=True)

        return result

    finally:
        s.close()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/restart":
            self.send_response(404)
            self.end_headers()
            return

        try:
            restart_map()

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK\n")

        except Exception as e:
            print(f"ERROR: {e}", flush=True)

            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"{e}\n".encode())

    def log_message(self, format, *args):
        print(format % args, flush=True)


print("Listening on port 5001", flush=True)
HTTPServer(("0.0.0.0", 5001), Handler).serve_forever()
