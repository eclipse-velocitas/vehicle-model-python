#!/usr/bin/env python3

"""Door model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)

from sdv_model.Cabin.Door.Shade import Shade
from sdv_model.Cabin.Door.Window import Window


class Door(Model):
    """Door model.

    Attributes
    ----------
    IsOpen: actuator
        Is door open or closed

    IsLocked: actuator
        Is door locked or unlocked. True = Locked. False = Unlocked.

    Window: branch
        Door window status

    IsChildLockActive: sensor
        Is door child lock engaged. True = Engaged. False = Disengaged.

    Shade: branch
        Side window shade

    """

    def __init__(self, parent):
        """Create a new Door model."""
        super().__init__(parent)

        self.IsOpen = DataPointBoolean("IsOpen", self)
        self.IsLocked = DataPointBoolean("IsLocked", self)
        self.Window = Window(self)
        self.IsChildLockActive = DataPointBoolean("IsChildLockActive", self)
        self.Shade = Shade(self)
