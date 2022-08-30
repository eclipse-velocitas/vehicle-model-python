#!/usr/bin/env python3

"""O2WR model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    Model,
)


class O2WR(Model):
    """O2WR model.

    Attributes
    ----------
    Lambda: sensor
        PID 2x (byte AB) and PID 3x (byte AB) - Lambda for wide range/band oxygen sensor

    Voltage: sensor
        PID 2x (byte CD) - Voltage for wide range/band oxygen sensor

        Unit: V
    Current: sensor
        PID 3x (byte CD) - Current for wide range/band oxygen sensor

        Unit: A
    """

    def __init__(self, parent):
        """Create a new O2WR model."""
        super().__init__(parent)

        self.Lambda = DataPointFloat("Lambda", self)
        self.Voltage = DataPointFloat("Voltage", self)
        self.Current = DataPointFloat("Current", self)
