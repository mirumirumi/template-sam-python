from __future__ import annotations
from typing import Any, cast, Literal, TypedDict

import os
import json
import boto3
from proxy_response import *
from aws_lambda_powertools.logging import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

# PowerTools
logger = Logger()


@logger.inject_lambda_context
def lambda_handler(event: dict[str, Any], context: LambdaContext) -> ProxyResponse:
    logger.info(event)









    return
