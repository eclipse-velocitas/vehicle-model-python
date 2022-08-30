#!/usr/bin/env python3

"""ParkingBrake model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class ParkingBrake(Model):
    """ParkingBrake model.

    Attributes
    ----------
    IsEngaged: actuator
        Parking brake status. True = Parking Brake is Engaged. False = Parking Brake is not Engaged.

    """

    def __init__(self, parent):
        """Create a new ParkingBrake model."""
        super().__init__(parent)

        self.IsEngaged = DataPointBoolean("IsEngaged", self)
