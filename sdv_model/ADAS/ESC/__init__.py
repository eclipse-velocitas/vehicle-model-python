#!/usr/bin/env python3

"""ESC model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)

from sdv_model.ADAS.ESC.RoadFriction import RoadFriction


class ESC(Model):
    """ESC model.

    Attributes
    ----------
    IsEnabled: actuator
        Indicates if ESC is enabled. True = Enabled. False = Disabled.

    IsError: sensor
        Indicates if ESC incurred an error condition. True = Error. False = No Error.

    IsEngaged: sensor
        Indicates if ESC is currently regulating vehicle stability. True = Engaged. False = Not Engaged.

    IsStrongCrossWindDetected: sensor
        Indicates if the ESC system is detecting strong cross winds. True = Strong cross winds detected. False = No strong cross winds detected.

    RoadFriction: branch
        Road friction values reported by the ESC system.

    """

    def __init__(self, parent):
        """Create a new ESC model."""
        super().__init__(parent)

        self.IsEnabled = DataPointBoolean("IsEnabled", self)
        self.IsError = DataPointBoolean("IsError", self)
        self.IsEngaged = DataPointBoolean("IsEngaged", self)
        self.IsStrongCrossWindDetected = DataPointBoolean("IsStrongCrossWindDetected", self)
        self.RoadFriction = RoadFriction(self)
