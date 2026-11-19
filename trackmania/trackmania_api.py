import os
import socket
import struct
from http.server import BaseHTTPRequestHandler, HTTPServer
import xmlrpc.client

PASSWORD = os.environ["SUPER_ADMIN"]

def get_times():
    s = socket.create_connection(("127.0.0.1", 5000), timeout=5)
    s.settimeout(5)

    try:
        # Read complete initial handshake
        def recv_exact(n):
            data = b""
            while len(data) < n:
                chunk = s.recv(n - len(data))
                if not chunk:
                    raise ConnectionError("Server disconnected")
                data += chunk
            return data

        length = struct.unpack("<I", recv_exact(4))[0]
        handshake = recv_exact(length)
        print("Handshake:", handshake, flush=True)

        def call(handle, method, params=()):
            xml = xmlrpc.client.dumps(params, methodname=method, allow_none=True).encode("utf-8")

            s.sendall(struct.pack("<II", len(xml), handle) + xml)

            while True:
                size, response_handle = struct.unpack("<II", recv_exact(8))
                response = recv_exact(size)

                if response_handle == handle:
                    values, _ = xmlrpc.client.loads(response)
                    return values[0] if values else None

        authenticated = call(0x80000000, "Authenticate", ("SuperAdmin", PASSWORD))

        if not authenticated:
            raise RuntimeError("Trackmania authentication failed")

        return call(0x80000001, "GetCurrentRanking", (100, 0))

    finally:
        s.close()


def restart_map():
    s = socket.create_connection(("127.0.0.1", 5000), timeout=5)
    s.settimeout(5)
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
        if self.path not in ["/restart", "/times"]:
            self.send_error(404)
            return

        try:
            if self.path == "/restart":
                restart_map()
                data = b"OK\n"
                content_type = "text/plain"

            elif self.path == "/times":
                import json

                rankings = get_times()
                data = json.dumps(rankings, indent=2).encode("utf-8")
                content_type = "application/json"

            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        except Exception as e:
            print(f"ERROR: {e}", flush=True)
            self.send_error(500, str(e))

    def log_message(self, format, *args):
        print(format % args, flush=True)


print("Listening on port 5001", flush=True)
HTTPServer(("0.0.0.0", 5001), Handler).serve_forever()

