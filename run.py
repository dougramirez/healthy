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
                "$schema": "http://json-schema.org/draft-07/schema",
                "$id": "http://example.com/example.json",
                "type": "object",
                "title": "The root schema",
                "description": "The root schema comprises the entire JSON document.",
                "default": {},
                "examples": [
                    {
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
                                    "github": "https://github.com/dougramirez/mongoose-database"
                                },
                            }
                        ],
                        "links": {"github": "https://github.com/dougramirez/mongoose"},
                    }
                ],
                "required": [
                    "status",
                    "time",
                    "version",
                    "service_id",
                    "description",
                    "output",
                    "checks",
                    "links",
                ],
                "properties": {
                    "status": {
                        "$id": "#/properties/status",
                        "type": "string",
                        "title": "The status schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": ["fail"],
                    },
                    "time": {
                        "$id": "#/properties/time",
                        "type": "string",
                        "title": "The time schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": ["2023-04-21T14:21:54+00:00"],
                    },
                    "version": {
                        "$id": "#/properties/version",
                        "type": "string",
                        "title": "The version schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": ["1.0.0"],
                    },
                    "service_id": {
                        "$id": "#/properties/service_id",
                        "type": "string",
                        "title": "The service_id schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": ["f03e522f-1f44-4062-9b55-9587f91c9c41"],
                    },
                    "description": {
                        "$id": "#/properties/description",
                        "type": "string",
                        "title": "The description schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": ["RESTful API for the Mongoose service"],
                    },
                    "output": {
                        "$id": "#/properties/output",
                        "type": "string",
                        "title": "The output schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [""],
                    },
                    "checks": {
                        "$id": "#/properties/checks",
                        "type": "array",
                        "title": "The checks schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": [],
                        "examples": [
                            [
                                {
                                    "component_id": "dfd6cf2b-1b6e-4412-a0b8-f6f7797a60d2",
                                    "component_type": "database",
                                    "status": "pass",
                                    "time": "2023-04-21T14:21:54+00:00",
                                    "output": "",
                                    "links": {
                                        "github": "https://github.com/dougramirez/mongoose-database"
                                    },
                                }
                            ]
                        ],
                        "additionalItems": True,
                        "items": {
                            "$id": "#/properties/checks/items",
                            "anyOf": [
                                {
                                    "$id": "#/properties/checks/items/anyOf/0",
                                    "type": "object",
                                    "title": "The first anyOf schema",
                                    "description": "An explanation about the purpose of this instance.",
                                    "default": {},
                                    "examples": [
                                        {
                                            "component_id": "dfd6cf2b-1b6e-4412-a0b8-f6f7797a60d2",
                                            "component_type": "database",
                                            "status": "pass",
                                            "time": "2023-04-21T14:21:54+00:00",
                                            "output": "",
                                            "links": {
                                                "github": "https://github.com/dougramirez/mongoose-database"
                                            },
                                        }
                                    ],
                                    "required": [
                                        "component_id",
                                        "component_type",
                                        "status",
                                        "time",
                                        "output",
                                        "links",
                                    ],
                                    "properties": {
                                        "component_id": {
                                            "$id": "#/properties/checks/items/anyOf/0/properties/component_id",
                                            "type": "string",
                                            "title": "The component_id schema",
                                            "description": "An explanation about the purpose of this instance.",
                                            "default": "",
                                            "examples": [
                                                "dfd6cf2b-1b6e-4412-a0b8-f6f7797a60d2"
                                            ],
                                        },
                                        "component_type": {
                                            "$id": "#/properties/checks/items/anyOf/0/properties/component_type",
                                            "type": "string",
                                            "title": "The component_type schema",
                                            "description": "An explanation about the purpose of this instance.",
                                            "default": "",
                                            "examples": ["database"],
                                        },
                                        "status": {
                                            "$id": "#/properties/checks/items/anyOf/0/properties/status",
                                            "type": "string",
                                            "title": "The status schema",
                                            "description": "An explanation about the purpose of this instance.",
                                            "default": "",
                                            "examples": ["pass"],
                                        },
                                        "time": {
                                            "$id": "#/properties/checks/items/anyOf/0/properties/time",
                                            "type": "string",
                                            "title": "The time schema",
                                            "description": "An explanation about the purpose of this instance.",
                                            "default": "",
                                            "examples": ["2023-04-21T14:21:54+00:00"],
                                        },
                                        "output": {
                                            "$id": "#/properties/checks/items/anyOf/0/properties/output",
                                            "type": "string",
                                            "title": "The output schema",
                                            "description": "An explanation about the purpose of this instance.",
                                            "default": "",
                                            "examples": [""],
                                        },
                                        "links": {
                                            "$id": "#/properties/checks/items/anyOf/0/properties/links",
                                            "type": "object",
                                            "title": "The links schema",
                                            "description": "An explanation about the purpose of this instance.",
                                            "default": {},
                                            "examples": [
                                                {
                                                    "github": "https://github.com/dougramirez/mongoose-database"
                                                }
                                            ],
                                            "required": ["github"],
                                            "properties": {
                                                "github": {
                                                    "$id": "#/properties/checks/items/anyOf/0/properties/links/properties/github",
                                                    "type": "string",
                                                    "title": "The github schema",
                                                    "description": "An explanation about the purpose of this instance.",
                                                    "default": "",
                                                    "examples": [
                                                        "https://github.com/dougramirez/mongoose-database"
                                                    ],
                                                }
                                            },
                                            "additionalProperties": True,
                                        },
                                    },
                                    "additionalProperties": True,
                                }
                            ],
                        },
                    },
                    "links": {
                        "$id": "#/properties/links",
                        "type": "object",
                        "title": "The links schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {"github": "https://github.com/dougramirez/mongoose"}
                        ],
                        "required": ["github"],
                        "properties": {
                            "github": {
                                "$id": "#/properties/links/properties/github",
                                "type": "string",
                                "title": "The github schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": ["https://github.com/dougramirez/mongoose"],
                            }
                        },
                        "additionalProperties": True,
                    },
                },
                "additionalProperties": True,
            }

            self.wfile.write(json.dumps(response).encode())


httpd = HTTPServer(("0.0.0.0", 8080), APIHandler)
httpd.serve_forever()
