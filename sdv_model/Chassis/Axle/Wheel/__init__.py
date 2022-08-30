#!/usr/bin/env python3

"""Wheel model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    Model,
)

from sdv_model.Chassis.Axle.Wheel.Brake import Brake
from sdv_model.Chassis.Axle.Wheel.Tire import Tire


class Wheel(Model):
    """Wheel model.

    Attributes
    ----------
    Brake: branch
        Brake signals for wheel

    Tire: branch
        Tire signals for wheel.

    Speed: sensor
        Rotational speed of a vehicle's wheel.

        Unit: km/h
    """

    def __init__(self, parent):
        """Create a new Wheel model."""
        super().__init__(parent)

        self.Brake = Brake(self)
        self.Tire = Tire(self)
        self.Speed = DataPointFloat("Speed", self)
