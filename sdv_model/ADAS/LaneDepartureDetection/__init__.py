#!/usr/bin/env python3

"""LaneDepartureDetection model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class LaneDepartureDetection(Model):
    """LaneDepartureDetection model.

    Attributes
    ----------
    IsEnabled: actuator
        Indicates if lane departure detection system is enabled. True = Enabled. False = Disabled.

    IsWarning: sensor
        Indicates if lane departure detection registered a lane departure.

    IsError: sensor
        Indicates if lane departure system incurred an error condition. True = Error. False = No Error.

    """

    def __init__(self, parent):
        """Create a new LaneDepartureDetection model."""
        super().__init__(parent)

        self.IsEnabled = DataPointBoolean("IsEnabled", self)
        self.IsWarning = DataPointBoolean("IsWarning", self)
        self.IsError = DataPointBoolean("IsError", self)
