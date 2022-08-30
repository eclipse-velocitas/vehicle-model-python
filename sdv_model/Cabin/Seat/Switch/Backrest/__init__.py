#!/usr/bin/env python3

"""Backrest model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)

from sdv_model.Cabin.Seat.Switch.Backrest.Lumbar import Lumbar
from sdv_model.Cabin.Seat.Switch.Backrest.SideBolster import SideBolster


class Backrest(Model):
    """Backrest model.

    Attributes
    ----------
    IsReclineForwardEngaged: actuator
        Backrest recline forward switch engaged (SingleSeat.Backrest.Recline).

    IsReclineBackwardEngaged: actuator
        Backrest recline backward switch engaged (SingleSeat.Backrest.Recline).

    Lumbar: branch
        Switches for SingleSeat.Backrest.Lumbar.

    SideBolster: branch
        Switches for SingleSeat.Backrest.SideBolster.

    """

    def __init__(self, parent):
        """Create a new Backrest model."""
        super().__init__(parent)

        self.IsReclineForwardEngaged = DataPointBoolean("IsReclineForwardEngaged", self)
        self.IsReclineBackwardEngaged = DataPointBoolean("IsReclineBackwardEngaged", self)
        self.Lumbar = Lumbar(self)
        self.SideBolster = SideBolster(self)
