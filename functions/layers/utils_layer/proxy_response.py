from __future__ import annotations
from typing import TypedDict

import os
import json
import dynamodb

API_ALLOW_ORIGIN = os.getenv("API_ALLOW_ORIGIN")

# types
class ProxyResponse(TypedDict):
    statusCode: int
    headers: dict[str, str | None]
    body: str


def s200(val: object = None) -> ProxyResponse:
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": API_ALLOW_ORIGIN
        },
        "body": json.dumps(
            val if val is not None else "no response data",
            default=dynamodb.decimal_to_float,
        )
    }


def s500(val: object = None) -> ProxyResponse:
    return {
        "statusCode": 500,
        "headers": {
            "Access-Control-Allow-Origin": API_ALLOW_ORIGIN
        },
        "body": json.dumps(
            val if val is not None else "no response data",
            default=dynamodb.decimal_to_float,
        )
    }
