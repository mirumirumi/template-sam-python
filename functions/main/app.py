from __future__ import annotations
from typing import Any, Final, NoReturn, TypedDict

import os
import json
import boto3
import secret
from aws_lambda_powertools.logging import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

# PowerTools
logger = Logger()

# Env Vars
ENVIRONMENT_NAME = os.environ["ENVIRONMENT_NAME"]


@logger.inject_lambda_context
def lambda_handler(event: object, context: LambdaContext) -> None:
    logger.info(event)









    logger.info("✅ Succeeded!")
    return
