from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    uuid: str,
) -> Dict[str, Any]:
    url = "{}/metadata/studies/{uuid}".format(client.base_url, uuid=uuid)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[HTTPValidationError, None]]:
    if response.status_code == 200:
        response_200 = None

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HTTPValidationError, None]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    uuid: str,
) -> Response[Union[HTTPValidationError, None]]:
    kwargs = _get_kwargs(
        client=client,
        uuid=uuid,
    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    uuid: str,
) -> Optional[Union[HTTPValidationError, None]]:
    """ """

    return sync_detailed(
        client=client,
        uuid=uuid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    uuid: str,
) -> Response[Union[HTTPValidationError, None]]:
    kwargs = _get_kwargs(
        client=client,
        uuid=uuid,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    uuid: str,
) -> Optional[Union[HTTPValidationError, None]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            uuid=uuid,
        )
    ).parsed
