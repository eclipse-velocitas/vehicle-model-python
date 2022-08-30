#!/usr/bin/env python3

"""Mirrors model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointInt8,
    Model,
)


class Mirrors(Model):
    """Mirrors model.

    Attributes
    ----------
    Tilt: actuator
        Mirror tilt as a percent. 0 = Center Position. 100 = Fully Upward Position. -100 = Fully Downward Position.

        Value range: [-100, 100]
        Unit: percent
    Pan: actuator
        Mirror pan as a percent. 0 = Center Position. 100 = Fully Left Position. -100 = Fully Right Position.

        Value range: [-100, 100]
        Unit: percent
    IsHeatingOn: actuator
        Mirror Heater on or off. True = Heater On. False = Heater Off.

    """

    def __init__(self, parent):
        """Create a new Mirrors model."""
        super().__init__(parent)

        self.Tilt = DataPointInt8("Tilt", self)
        self.Pan = DataPointInt8("Pan", self)
        self.IsHeatingOn = DataPointBoolean("IsHeatingOn", self)
