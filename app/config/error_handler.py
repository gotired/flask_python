"""Error Handler Module"""

import json
import traceback
from http import HTTPStatus

from pydantic import ValidationError

from app.utils.extract_error import Error
from app.models.response import Response


def validation_error_handler(error):
    """Validation error handler"""
    location = Error.extract_location(traceback.format_exc())
    response = [
        detail["msg"] + ":" + json.dumps(detail["loc"]) for detail in error.errors()
    ]
    return Response(detail=response).failure(), HTTPStatus.BAD_REQUEST


def register_error_handler(app):
    app.errorhandler(ValidationError)(validation_error_handler)
