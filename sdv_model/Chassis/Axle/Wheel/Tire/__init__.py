#!/usr/bin/env python3

"""Tire model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointUint16,
    Model,
)


class Tire(Model):
    """Tire model.

    Attributes
    ----------
    Pressure: sensor
        Tire pressure in kilo-Pascal.

        Unit: kPa
    IsPressureLow: sensor
        Tire Pressure Status. True = Low tire pressure. False = Good tire pressure.

    Temperature: sensor
        Tire temperature in Celsius.

        Unit: celsius
    """

    def __init__(self, parent):
        """Create a new Tire model."""
        super().__init__(parent)

        self.Pressure = DataPointUint16("Pressure", self)
        self.IsPressureLow = DataPointBoolean("IsPressureLow", self)
        self.Temperature = DataPointFloat("Temperature", self)
