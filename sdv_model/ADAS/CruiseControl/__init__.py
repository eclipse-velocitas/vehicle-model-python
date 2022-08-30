#!/usr/bin/env python3

"""CruiseControl model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    Model,
)


class CruiseControl(Model):
    """CruiseControl model.

    Attributes
    ----------
    IsEnabled: actuator
        Indicates if cruise control system is enabled (e.g. ready to receive configurations and settings) True = Enabled. False = Disabled.

    IsActive: actuator
        Indicates if cruise control system is active (i.e. actively controls speed). True = Active. False = Inactive.

    SpeedSet: actuator
        Set cruise control speed in kilometers per hour.

        Unit: km/h
    IsError: sensor
        Indicates if cruise control system incurred an error condition. True = Error. False = No Error.

    """

    def __init__(self, parent):
        """Create a new CruiseControl model."""
        super().__init__(parent)

        self.IsEnabled = DataPointBoolean("IsEnabled", self)
        self.IsActive = DataPointBoolean("IsActive", self)
        self.SpeedSet = DataPointFloat("SpeedSet", self)
        self.IsError = DataPointBoolean("IsError", self)
