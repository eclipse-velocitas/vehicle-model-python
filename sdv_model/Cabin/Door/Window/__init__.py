#!/usr/bin/env python3

"""Window model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointString,
    DataPointUint8,
    Model,
)


class Window(Model):
    """Window model.

    Attributes
    ----------
    IsOpen: sensor
        Is window open or closed?

    Position: sensor
        Window position. 0 = Fully closed 100 = Fully opened.

        Value range: [0, 100]
        Unit: percent
    IsChildLockEngaged: sensor
        Is window child lock engaged. True = Engaged. False = Disengaged.

    Switch: actuator
        Switch controlling sliding action such as window, sunroof, or blind.

        Allowed values: INACTIVE, CLOSE, OPEN, ONE_SHOT_CLOSE, ONE_SHOT_OPEN
    """

    def __init__(self, parent):
        """Create a new Window model."""
        super().__init__(parent)

        self.IsOpen = DataPointBoolean("IsOpen", self)
        self.Position = DataPointUint8("Position", self)
        self.IsChildLockEngaged = DataPointBoolean("IsChildLockEngaged", self)
        self.Switch = DataPointString("Switch", self)
