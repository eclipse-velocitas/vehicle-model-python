#!/usr/bin/env python3

"""Chassis model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointUint16,
    DataPointUint8,
    Model,
    ModelCollection,
    NamedRange,
)

from sdv_model.Chassis.Accelerator import Accelerator
from sdv_model.Chassis.Axle import Axle
from sdv_model.Chassis.Brake import Brake
from sdv_model.Chassis.ParkingBrake import ParkingBrake
from sdv_model.Chassis.SteeringWheel import SteeringWheel


class Chassis(Model):
    """Chassis model.

    Attributes
    ----------
    Wheelbase: attribute (uint16)
        Overall wheel base, in mm.

        Unit: mm
    Track: attribute (uint16)
        Overall wheel tracking, in mm.

        Unit: mm
    Axle: branch
        Axle signals

    AxleCount: attribute (uint8)
        Number of axles on the vehicle

    ParkingBrake: branch
        Parking brake signals

    SteeringWheel: branch
        Steering wheel signals

    Accelerator: branch
        Accelerator signals

    Brake: branch
        Brake system signals

    """

    def __init__(self, parent):
        """Create a new Chassis model."""
        super().__init__(parent)

        self.Wheelbase = DataPointUint16("Wheelbase", self)
        self.Track = DataPointUint16("Track", self)
        self.Axle = ModelCollection[Axle]([NamedRange("Row", 1, 2)], Axle(self))
        self.AxleCount = DataPointUint8("AxleCount", self)
        self.ParkingBrake = ParkingBrake(self)
        self.SteeringWheel = SteeringWheel(self)
        self.Accelerator = Accelerator(self)
        self.Brake = Brake(self)
