from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.storage_event_return import StorageEventReturn

T = TypeVar("T", bound="StorageEventCollection")


@attr.s(auto_attribs=True)
class StorageEventCollection:
    """ """

    hits: List[StorageEventReturn]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hits = []
        for hits_item_data in self.hits:
            hits_item = hits_item_data.to_dict()

            hits.append(hits_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hits": hits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hits = []
        _hits = d.pop("hits")
        for hits_item_data in _hits:
            hits_item = StorageEventReturn.from_dict(hits_item_data)

            hits.append(hits_item)

        storage_event_collection = cls(
            hits=hits,
        )

        storage_event_collection.additional_properties = d
        return storage_event_collection

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
