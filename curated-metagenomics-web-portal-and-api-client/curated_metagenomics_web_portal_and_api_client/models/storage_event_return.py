import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageEventReturn")


@attr.s(auto_attribs=True)
class StorageEventReturn:
    """ """

    kind: str
    id: str
    self_link: str
    name: str
    bucket: str
    generation: int
    metageneration: int
    content_type: str
    time_created: datetime.datetime
    updated: datetime.datetime
    size: int
    md_5_hash: str
    media_link: str
    crc_32_c: str
    etag: str
    event_type: str
    event_time: datetime.datetime
    event_id: str
    download_url: str
    content_language: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kind = self.kind
        id = self.id
        self_link = self.self_link
        name = self.name
        bucket = self.bucket
        generation = self.generation
        metageneration = self.metageneration
        content_type = self.content_type
        time_created = self.time_created.isoformat()

        updated = self.updated.isoformat()

        size = self.size
        md_5_hash = self.md_5_hash
        media_link = self.media_link
        crc_32_c = self.crc_32_c
        etag = self.etag
        event_type = self.event_type
        event_time = self.event_time.isoformat()

        event_id = self.event_id
        download_url = self.download_url
        content_language = self.content_language

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "id": id,
                "selfLink": self_link,
                "name": name,
                "bucket": bucket,
                "generation": generation,
                "metageneration": metageneration,
                "contentType": content_type,
                "timeCreated": time_created,
                "updated": updated,
                "size": size,
                "md5Hash": md_5_hash,
                "mediaLink": media_link,
                "crc32c": crc_32_c,
                "etag": etag,
                "eventType": event_type,
                "eventTime": event_time,
                "event_id": event_id,
                "download_url": download_url,
            }
        )
        if content_language is not UNSET:
            field_dict["contentLanguage"] = content_language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kind = d.pop("kind")

        id = d.pop("id")

        self_link = d.pop("selfLink")

        name = d.pop("name")

        bucket = d.pop("bucket")

        generation = d.pop("generation")

        metageneration = d.pop("metageneration")

        content_type = d.pop("contentType")

        time_created = isoparse(d.pop("timeCreated"))

        updated = isoparse(d.pop("updated"))

        size = d.pop("size")

        md_5_hash = d.pop("md5Hash")

        media_link = d.pop("mediaLink")

        crc_32_c = d.pop("crc32c")

        etag = d.pop("etag")

        event_type = d.pop("eventType")

        event_time = isoparse(d.pop("eventTime"))

        event_id = d.pop("event_id")

        download_url = d.pop("download_url")

        content_language = d.pop("contentLanguage", UNSET)

        storage_event_return = cls(
            kind=kind,
            id=id,
            self_link=self_link,
            name=name,
            bucket=bucket,
            generation=generation,
            metageneration=metageneration,
            content_type=content_type,
            time_created=time_created,
            updated=updated,
            size=size,
            md_5_hash=md_5_hash,
            media_link=media_link,
            crc_32_c=crc_32_c,
            etag=etag,
            event_type=event_type,
            event_time=event_time,
            event_id=event_id,
            download_url=download_url,
            content_language=content_language,
        )

        storage_event_return.additional_properties = d
        return storage_event_return

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
