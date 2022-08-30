#!/usr/bin/env python3

"""Spotlight model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class Spotlight(Model):
    """Spotlight model.

    Attributes
    ----------
    IsSharedOn: sensor
        Is a shared light across a specific row on

    IsLeftOn: actuator
        Is light on the left side switched on

    IsRightOn: actuator
        Is light on the right side switched on

    """

    def __init__(self, parent):
        """Create a new Spotlight model."""
        super().__init__(parent)

        self.IsSharedOn = DataPointBoolean("IsSharedOn", self)
        self.IsLeftOn = DataPointBoolean("IsLeftOn", self)
        self.IsRightOn = DataPointBoolean("IsRightOn", self)
