from __future__ import annotations
from typing import Any, cast, Literal, TypedDict


class ProxyResponse(TypedDict):
    statusCode: int
    headers: dict[str, str | None]
    body: str

def s200(val: object = ...) -> ProxyResponse:
    ...

def s500(val: object = ...) -> ProxyResponse:
    ...
