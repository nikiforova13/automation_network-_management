import enum

from pydantic import ConfigDict
from starlette import status


class BaseCase:
    model_config = ConfigDict(from_attributes=True)


class APIResponseStatusCode(enum.IntEnum):
    ok = status.HTTP_200_OK
    created = status.HTTP_201_CREATED
    nok = status.HTTP_503_SERVICE_UNAVAILABLE
    valid_error = status.HTTP_422_UNPROCESSABLE_ENTITY


STATUS_CODE_AND_MESSAGE_MAP = {
    APIResponseStatusCode.ok: "Operation is successful",
    APIResponseStatusCode.created: "Created",
    APIResponseStatusCode.nok: "Operation is not successful",
    APIResponseStatusCode.valid_error: "Validation Error",
}
BaseAPIResponse = {
    APIResponseStatusCode.ok: {
        "description": STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.ok]
    },
    APIResponseStatusCode.created: {
        "description": STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.created]
    },
    APIResponseStatusCode.nok: {
        "description": STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.nok],
        "content": {"application/json": {}},
    },
    APIResponseStatusCode.valid_error: {
        "description": STATUS_CODE_AND_MESSAGE_MAP[APIResponseStatusCode.valid_error],
        "content": {"application/json": {}},
    },
}
