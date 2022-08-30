#!/usr/bin/env python3

"""Massage model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class Massage(Model):
    """Massage model.

    Attributes
    ----------
    IsIncreaseEngaged: actuator
        Increase massage level switch engaged (SingleSeat.Massage).

    IsDecreaseEngaged: actuator
        Decrease massage level switch engaged (SingleSeat.Massage).

    """

    def __init__(self, parent):
        """Create a new Massage model."""
        super().__init__(parent)

        self.IsIncreaseEngaged = DataPointBoolean("IsIncreaseEngaged", self)
        self.IsDecreaseEngaged = DataPointBoolean("IsDecreaseEngaged", self)
