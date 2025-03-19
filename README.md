# Healthy Check Response Format

## Overview
Imagine being a new developer on a small, autonomous team.  It’s your first week on-call.  And you get paged.  At 2:00 AM.  There’s a voicemail from Tier 1 support saying your service is down.  A health check returned a status code of >= 400.  The first question you’re likely to ask yourself is “Why?”.

This proposal is to define an endpoint for returning data about _why_ a service is healthy, or not.  This will help humans rapidly address the root issue when an API is down, and help machines to surface that info for the humans.

## Goals and Non-Goals

### Goals
* to create a consistent experience for developers who wish to offer a `/healthy` endpoint to surface why an API is healthy, or not

### Non-goals
* this has nothing to do with health checks
* this does not prescribe how the healthy check is implemented or consumed
* this does not prescribe how to determine whether a service is healthy, or not, as that is up to the implementer

## Background and Motivation
This proposal is intended to guide developers who want to know what response format to use for a `/healthy` endpoint so that humans and machines can have the requisite information that’s needed to understand why an API is healthy, or not.

This schema is based on [Irakli Nadareishvili’s](https://www.linkedin.com/in/inadarei) draft (now expired) [Internet RFC](https://www.ietf.org/archive/id/draft-inadarei-api-health-check-06.txt).  Irakli Nadareishvili is a co-author of Microservices Up and Running (2020) and  Microservice Architecture (O'Reilly, 2016).

[Kin Lane](https://www.linkedin.com/in/kinlane/) is a proponent of Irakli’s proposal, which he wrote about on his [API Evangelist blog](https://apievangelist.com/2018/01/19/a-health-check-response-format-for-http-apis/).  

## Design
* **status** - one of “pass”, “warn”, “fail”
* **time** -  when reading was recorded in ISO 8601 format
* **version** - the version of the running service
* **service_id** - a uuid for the internal representation of the service
* **description** - one line description of the service
* **output** - unstructured, raw output from checks
* **checks**
  * **component_id** - a uuid for the internal representation of the component
  * **component_type** - one of “database”, “cache”, “pubsub”
  * **status** - one of “pass”, “warn”, “fail”
  * **time** -  when reading was recorded in ISO 8601 format
  * **output** - unstructured, raw output from checks
  * **links** - see below
* **links**
  * **key** - label for the link
  * **value**- the link

### Example

```
curl --location --request \
    GET 'https://a9e40c19-24af-410a-bede-402908ed4d27.mock.pstmn.io/health' \
    --data-raw ''
```

```
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
                "github": "https://github.com/dougramirez/mongoose-database",
                "backstage": "https://backstage.io/dougramirez/mongoose-database"
            }
        },
        {
            "component_id": "d1870e7f-17a6-4f26-b124-9a07599ec0bb",
            "component_type": "cache",
            "status": "fail",
            "time": "2023-04-21T14:21:54+00:00",
            "output": "Redis::CannotConnectError (Error connecting to Redis on 127.0.0.1:6379)",
            "links": {
                "github": "https://github.com/dougramirez/mongoose-cache",
                "backstage": "https://backstage.io/dougramirez/mongoose-cache"
            }
        }
    ],
    "links": {
        "github": "https://github.com/dougramirez/mongoose",
        "backstage": "https://backstage.io/dougramirez/mongoose"
    }
}
```

<details><summary>Schema</summary>

```{
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
                    }
                }
            ],
            "links": {
                "github": "https://github.com/dougramirez/mongoose"
            }
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
        "links"
    ],
    "properties": {
        "status": {
            "$id": "#/properties/status",
            "type": "string",
            "title": "The status schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "fail"
            ]
        },
        "time": {
            "$id": "#/properties/time",
            "type": "string",
            "title": "The time schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "2023-04-21T14:21:54+00:00"
            ]
        },
        "version": {
            "$id": "#/properties/version",
            "type": "string",
            "title": "The version schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "1.0.0"
            ]
        },
        "service_id": {
            "$id": "#/properties/service_id",
            "type": "string",
            "title": "The service_id schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "f03e522f-1f44-4062-9b55-9587f91c9c41"
            ]
        },
        "description": {
            "$id": "#/properties/description",
            "type": "string",
            "title": "The description schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                "RESTful API for the Mongoose service"
            ]
        },
        "output": {
            "$id": "#/properties/output",
            "type": "string",
            "title": "The output schema",
            "description": "An explanation about the purpose of this instance.",
            "default": "",
            "examples": [
                ""
            ]
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
                        }
                    }
                ]
            ],
            "additionalItems": true,
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
                                }
                            }
                        ],
                        "required": [
                            "component_id",
                            "component_type",
                            "status",
                            "time",
                            "output",
                            "links"
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
                                ]
                            },
                            "component_type": {
                                "$id": "#/properties/checks/items/anyOf/0/properties/component_type",
                                "type": "string",
                                "title": "The component_type schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "database"
                                ]
                            },
                            "status": {
                                "$id": "#/properties/checks/items/anyOf/0/properties/status",
                                "type": "string",
                                "title": "The status schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "pass"
                                ]
                            },
                            "time": {
                                "$id": "#/properties/checks/items/anyOf/0/properties/time",
                                "type": "string",
                                "title": "The time schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "2023-04-21T14:21:54+00:00"
                                ]
                            },
                            "output": {
                                "$id": "#/properties/checks/items/anyOf/0/properties/output",
                                "type": "string",
                                "title": "The output schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    ""
                                ]
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
                                "required": [
                                    "github"
                                ],
                                "properties": {
                                    "github": {
                                        "$id": "#/properties/checks/items/anyOf/0/properties/links/properties/github",
                                        "type": "string",
                                        "title": "The github schema",
                                        "description": "An explanation about the purpose of this instance.",
                                        "default": "",
                                        "examples": [
                                            "https://github.com/dougramirez/mongoose-database"
                                        ]
                                    }
                                },
                                "additionalProperties": true
                            }
                        },
                        "additionalProperties": true
                    }
                ]
            }
        },
        "links": {
            "$id": "#/properties/links",
            "type": "object",
            "title": "The links schema",
            "description": "An explanation about the purpose of this instance.",
            "default": {},
            "examples": [
                {
                    "github": "https://github.com/dougramirez/mongoose"
                }
            ],
            "required": [
                "github"
            ],
            "properties": {
                "github": {
                    "$id": "#/properties/links/properties/github",
                    "type": "string",
                    "title": "The github schema",
                    "description": "An explanation about the purpose of this instance.",
                    "default": "",
                    "examples": [
                        "https://github.com/dougramirez/mongoose"
                    ]
                }
            },
            "additionalProperties": true
        }
    },
    "additionalProperties": true
}
```
</details>
</br>

## Alternatives Considered
This is largely based off of this alternative, which is referenced in the Overview.  [Health Check Response Format for HTTP APIs](https://www.ietf.org/archive/id/draft-inadarei-api-health-check-06.txt) (draft-inadarei-api-health-check-06).

## Cost Considerations
At some point the lost opportunity costs can be calculated.  And, the costs of increased time to resolution without having proper visibility into the health of an API.  Other than that, there are no additive costs.

## Operations
Subjectively, this will help with SLIs as the indicator will be informative enough to surface the actual reason why a service is healthy, or not.

## Security, Privacy, and Compliance
As with all services, no PII, secrets, or credentials should be exposed in the response payload.
