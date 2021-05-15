import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.nf_return_metadata import NFReturnMetadata
from ..models.nf_return_trace import NFReturnTrace
from ..types import UNSET, Unset

T = TypeVar("T", bound="NFReturn")


@attr.s(auto_attribs=True)
class NFReturn:
    """Represents a nextflow event"""

    run_name: str
    run_id: str
    event: str
    utc_time: datetime.datetime
    event_id: int
    trace: Union[Unset, NFReturnTrace] = UNSET
    metadata: Union[Unset, NFReturnMetadata] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        run_name = self.run_name
        run_id = self.run_id
        event = self.event
        utc_time = self.utc_time.isoformat()

        event_id = self.event_id
        trace: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trace, Unset):
            trace = self.trace.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runName": run_name,
                "runId": run_id,
                "event": event,
                "utcTime": utc_time,
                "event_id": event_id,
            }
        )
        if trace is not UNSET:
            field_dict["trace"] = trace
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        run_name = d.pop("runName")

        run_id = d.pop("runId")

        event = d.pop("event")

        utc_time = isoparse(d.pop("utcTime"))

        event_id = d.pop("event_id")

        _trace = d.pop("trace", UNSET)
        trace: Union[Unset, NFReturnTrace]
        if isinstance(_trace, Unset):
            trace = UNSET
        else:
            trace = NFReturnTrace.from_dict(_trace)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, NFReturnMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = NFReturnMetadata.from_dict(_metadata)

        nf_return = cls(
            run_name=run_name,
            run_id=run_id,
            event=event,
            utc_time=utc_time,
            event_id=event_id,
            trace=trace,
            metadata=metadata,
        )

        nf_return.additional_properties = d
        return nf_return

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
