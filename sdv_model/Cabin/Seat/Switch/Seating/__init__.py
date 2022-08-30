#!/usr/bin/env python3

"""Seating model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class Seating(Model):
    """Seating model.

    Attributes
    ----------
    IsForwardEngaged: actuator
        Is switch to increase seating length engaged (SingleSeat.Seating.Length).

    IsBackwardEngaged: actuator
        Is switch to decrease seating length engaged (SingleSeat.Seating.Length).

    """

    def __init__(self, parent):
        """Create a new Seating model."""
        super().__init__(parent)

        self.IsForwardEngaged = DataPointBoolean("IsForwardEngaged", self)
        self.IsBackwardEngaged = DataPointBoolean("IsBackwardEngaged", self)
