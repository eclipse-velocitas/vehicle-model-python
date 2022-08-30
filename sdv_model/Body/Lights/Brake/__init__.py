#!/usr/bin/env python3

"""Brake model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointString,
    Model,
)


class Brake(Model):
    """Brake model.

    Attributes
    ----------
    IsActive: actuator
        Indicates if break-light is active. INACTIVE means lights are off. ACTIVE means lights are on. ADAPTIVE means that break-light is indicating emergency-breaking.

        Allowed values: INACTIVE, ACTIVE, ADAPTIVE
    IsDefect: sensor
        Indicates if light is defect. True = Light is defect. False = Light has no defect.

    """

    def __init__(self, parent):
        """Create a new Brake model."""
        super().__init__(parent)

        self.IsActive = DataPointString("IsActive", self)
        self.IsDefect = DataPointBoolean("IsDefect", self)
