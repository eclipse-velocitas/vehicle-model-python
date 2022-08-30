#!/usr/bin/env python3

"""Trunk model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class Trunk(Model):
    """Trunk model.

    Attributes
    ----------
    IsOpen: actuator
        Trunk open or closed. True = Open. False = Closed.

    IsLocked: actuator
        Is trunk locked or unlocked. True = Locked. False = Unlocked.

    """

    def __init__(self, parent):
        """Create a new Trunk model."""
        super().__init__(parent)

        self.IsOpen = DataPointBoolean("IsOpen", self)
        self.IsLocked = DataPointBoolean("IsLocked", self)
