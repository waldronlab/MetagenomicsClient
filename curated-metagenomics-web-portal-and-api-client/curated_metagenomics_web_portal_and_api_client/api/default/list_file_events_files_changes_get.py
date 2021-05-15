import datetime
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...models.storage_event_collection import StorageEventCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    filename_regex: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/files/changes".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()

    params: Dict[str, Any] = {
        "limit": limit,
        "offset": offset,
        "start_date": json_start_date,
        "end_date": json_end_date,
        "filename_regex": filename_regex,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[HTTPValidationError, StorageEventCollection]]:
    if response.status_code == 200:
        response_200 = StorageEventCollection.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HTTPValidationError, StorageEventCollection]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    filename_regex: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, StorageEventCollection]]:
    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
        start_date=start_date,
        end_date=end_date,
        filename_regex=filename_regex,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    filename_regex: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, StorageEventCollection]]:
    """ """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        start_date=start_date,
        end_date=end_date,
        filename_regex=filename_regex,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    filename_regex: Union[Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, StorageEventCollection]]:
    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
        start_date=start_date,
        end_date=end_date,
        filename_regex=filename_regex,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    start_date: Union[Unset, datetime.date] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    filename_regex: Union[Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, StorageEventCollection]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            start_date=start_date,
            end_date=end_date,
            filename_regex=filename_regex,
        )
    ).parsed
