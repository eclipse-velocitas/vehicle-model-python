#!/usr/bin/env python3

"""Windshield model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)

from sdv_model.Body.Windshield.WasherFluid import WasherFluid
from sdv_model.Body.Windshield.Wiping import Wiping


class Windshield(Model):
    """Windshield model.

    Attributes
    ----------
    Wiping: branch
        Windshield wiper signals.

    IsHeatingOn: actuator
        Windshield heater status. False - off, True - on.

    WasherFluid: branch
        Windshield washer fluid signals

    """

    def __init__(self, parent):
        """Create a new Windshield model."""
        super().__init__(parent)

        self.Wiping = Wiping(self)
        self.IsHeatingOn = DataPointBoolean("IsHeatingOn", self)
        self.WasherFluid = WasherFluid(self)
