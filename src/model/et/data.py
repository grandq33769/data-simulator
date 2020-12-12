# Standard Library
from dataclasses import dataclass

from ..model import Attribute, DataModel, _DataModelBase, _DataModelDefaultBase


@dataclass
class _DRBidCEMSBase(_DataModelBase):
    uuid: Attribute
    start_time: Attribute
    end_time: Attribute


@dataclass
class _DRBidBEMSBase(_DataModelBase):
    volume: Attribute
    price: Attribute


@dataclass
class _BidSubmitBase(_DataModelBase):
    bid_type: Attribute
    start_time: Attribute
    end_time: Attribute
    value: Attribute
    price: Attribute


@dataclass
class DRBidCEMS(DataModel, _DataModelDefaultBase, _DRBidCEMSBase):
    pass


@dataclass
class DRBidBEMS(DataModel, _DataModelDefaultBase, _DRBidBEMSBase):
    pass


@dataclass
class BidSubmit(DataModel, _DataModelDefaultBase, _BidSubmitBase):
    pass
