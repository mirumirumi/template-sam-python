import os
import json
import dynamodb
from __future__ import annotations

API_ALLOW_ORIGIN = os.getenv("API_ALLOW_ORIGIN")


def _200(val: object = None) -> dict[str, int | dict[str, str | None] | str]:
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": API_ALLOW_ORIGIN
        },
        "body": json.dumps(
            val if val is not None else "no response data",
            default=dynamodb.decimal_to_float
        )
    }

def _500(val: object = None) -> dict[str, int | dict[str, str | None] | str]:
    return {
        "statusCode": 500,
        "headers": {
            "Access-Control-Allow-Origin": API_ALLOW_ORIGIN
        },
        "body": json.dumps(
            val if val is not None else "no response data",
            default=dynamodb.decimal_to_float
        )
    }
