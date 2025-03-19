import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class APIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"status": "OK"}
            self.wfile.write(json.dumps(response).encode())

        if self.path == "/ping":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"ping": "pong"}
            self.wfile.write(json.dumps(response).encode())

        if self.path == "/healthy":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {
                "status": "fail",
                "time": "2023-04-21T14:21:54+00:00",
                "version": "1.0.0",
                "service_id": "f03e522f-1f44-4062-9b55-9587f91c9c41",
                "description": "RESTful API for the Mongoose service",
                "output": "",
                "checks": [
                    {
                        "component_id": "dfd6cf2b-1b6e-4412-a0b8-f6f7797a60d2",
                        "component_type": "database",
                        "status": "pass",
                        "time": "2023-04-21T14:21:54+00:00",
                        "output": "",
                        "links": {
                            "github": "https://github.com/dougramirez/mongoose-database",
                            "backstage": "https://backstage.io/dougramirez/mongoose-database",
                        },
                    },
                    {
                        "component_id": "d1870e7f-17a6-4f26-b124-9a07599ec0bb",
                        "component_type": "cache",
                        "status": "fail",
                        "time": "2023-04-21T14:21:54+00:00",
                        "output": "Redis::CannotConnectError (Error connecting to Redis on 127.0.0.1:6379)",
                        "links": {
                            "github": "https://github.com/dougramirez/mongoose-cache",
                            "backstage": "https://backstage.io/dougramirez/mongoose-cache",
                        },
                    },
                ],
                "links": {
                    "github": "https://github.com/dougramirez/mongoose",
                    "backstage": "https://backstage.io/dougramirez/mongoose",
                },
            }

            self.wfile.write(json.dumps(response).encode())


httpd = HTTPServer(("0.0.0.0", 8080), APIHandler)
httpd.serve_forever()
