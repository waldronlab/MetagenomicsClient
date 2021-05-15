import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.nf_model_metadata import NFModelMetadata
from ..models.nf_model_trace import NFModelTrace
from ..types import UNSET, Unset

T = TypeVar("T", bound="NFModel")


@attr.s(auto_attribs=True)
class NFModel:
    """ """

    run_name: str
    run_id: str
    event: str
    utc_time: datetime.datetime
    trace: Union[Unset, NFModelTrace] = UNSET
    metadata: Union[Unset, NFModelMetadata] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        run_name = self.run_name
        run_id = self.run_id
        event = self.event
        utc_time = self.utc_time.isoformat()

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

        _trace = d.pop("trace", UNSET)
        trace: Union[Unset, NFModelTrace]
        if isinstance(_trace, Unset):
            trace = UNSET
        else:
            trace = NFModelTrace.from_dict(_trace)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, NFModelMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = NFModelMetadata.from_dict(_metadata)

        nf_model = cls(
            run_name=run_name,
            run_id=run_id,
            event=event,
            utc_time=utc_time,
            trace=trace,
            metadata=metadata,
        )

        nf_model.additional_properties = d
        return nf_model

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
