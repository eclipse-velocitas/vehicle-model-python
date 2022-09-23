#!/usr/bin/env python3

"""LowVoltageBattery model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    DataPointUint16,
    Model,
)


class LowVoltageBattery(Model):
    """LowVoltageBattery model.

    Attributes
    ----------
    NominalVoltage: attribute (uint16)
        Nominal Voltage of the battery.

        Nominal voltage typically refers to voltage of fully charged battery when delivering rated capacity.

        Unit: V
    NominalCapacity: attribute (uint16)
        Nominal capacity of the low voltage battery.

        Unit: Ah
    CurrentVoltage: sensor
        Current Voltage of the low voltage battery.

        Unit: V
    CurrentCurrent: sensor
        Current current flowing in/out of the low voltage battery. Positive = Current flowing in to battery, e.g. during charging or driving. Negative = Current flowing out of battery, e.g. when using the battery to start a combustion engine.

        Unit: A
    """

    def __init__(self, parent):
        """Create a new LowVoltageBattery model."""
        super().__init__(parent)

        self.NominalVoltage = DataPointUint16("NominalVoltage", self)
        self.NominalCapacity = DataPointUint16("NominalCapacity", self)
        self.CurrentVoltage = DataPointFloat("CurrentVoltage", self)
        self.CurrentCurrent = DataPointFloat("CurrentCurrent", self)

