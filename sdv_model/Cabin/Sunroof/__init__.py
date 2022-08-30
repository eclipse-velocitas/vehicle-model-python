#!/usr/bin/env python3

"""Sunroof model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointInt8,
    DataPointString,
    Model,
)

from sdv_model.Cabin.Sunroof.Shade import Shade


class Sunroof(Model):
    """Sunroof model.

    Attributes
    ----------
    Position: sensor
        Sunroof position. 0 = Fully closed 100 = Fully opened. -100 = Fully tilted.

        Value range: [-100, 100]
    Switch: actuator
        Switch controlling sliding action such as window, sunroof, or shade.

        Allowed values: INACTIVE, CLOSE, OPEN, ONE_SHOT_CLOSE, ONE_SHOT_OPEN, TILT_UP, TILT_DOWN
    Shade: branch
        Sun roof shade status.

    """

    def __init__(self, parent):
        """Create a new Sunroof model."""
        super().__init__(parent)

        self.Position = DataPointInt8("Position", self)
        self.Switch = DataPointString("Switch", self)
        self.Shade = Shade(self)
