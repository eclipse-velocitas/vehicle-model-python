#!/usr/bin/env python3

"""Station model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointInt8,
    DataPointString,
    DataPointUint8,
    Model,
)


class Station(Model):
    """Station model.

    Attributes
    ----------
    FanSpeed: actuator
        Fan Speed, 0 = off. 100 = max

        Value range: [0, 100]
        Unit: percent
    Temperature: actuator
        Temperature

        Unit: celsius
    AirDistribution: actuator
        Direction of airstream

        Allowed values: UP, MIDDLE, DOWN
    """

    def __init__(self, parent):
        """Create a new Station model."""
        super().__init__(parent)

        self.FanSpeed = DataPointUint8("FanSpeed", self)
        self.Temperature = DataPointInt8("Temperature", self)
        self.AirDistribution = DataPointString("AirDistribution", self)
