#!/usr/bin/env python3

"""Running model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class Running(Model):
    """Running model.

    Attributes
    ----------
    IsOn: actuator
        Indicates if light is on or off. True = On. False = Off.

    IsDefect: sensor
        Indicates if light is defect. True = Light is defect. False = Light has no defect.

    """

    def __init__(self, parent):
        """Create a new Running model."""
        super().__init__(parent)

        self.IsOn = DataPointBoolean("IsOn", self)
        self.IsDefect = DataPointBoolean("IsDefect", self)
