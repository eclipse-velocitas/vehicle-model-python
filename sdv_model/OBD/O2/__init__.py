#!/usr/bin/env python3

"""O2 model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    Model,
)


class O2(Model):
    """O2 model.

    Attributes
    ----------
    Voltage: sensor
        PID 1x (byte A) - Sensor voltage

        Unit: V
    ShortTermFuelTrim: sensor
        PID 1x (byte B) - Short term fuel trim

        Unit: percent
    """

    def __init__(self, parent):
        """Create a new O2 model."""
        super().__init__(parent)

        self.Voltage = DataPointFloat("Voltage", self)
        self.ShortTermFuelTrim = DataPointFloat("ShortTermFuelTrim", self)
