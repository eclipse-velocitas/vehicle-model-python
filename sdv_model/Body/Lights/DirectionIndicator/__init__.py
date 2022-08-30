#!/usr/bin/env python3

"""DirectionIndicator model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class DirectionIndicator(Model):
    """DirectionIndicator model.

    Attributes
    ----------
    IsSignaling: actuator
        Indicates if light is signaling or off. True = signaling. False = Off.

    IsDefect: sensor
        Indicates if light is defect. True = Light is defect. False = Light has no defect.

    """

    def __init__(self, parent):
        """Create a new DirectionIndicator model."""
        super().__init__(parent)

        self.IsSignaling = DataPointBoolean("IsSignaling", self)
        self.IsDefect = DataPointBoolean("IsDefect", self)