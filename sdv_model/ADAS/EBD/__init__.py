#!/usr/bin/env python3

"""EBD model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class EBD(Model):
    """EBD model.

    Attributes
    ----------
    IsEnabled: actuator
        Indicates if EBD is enabled. True = Enabled. False = Disabled.

    IsError: sensor
        Indicates if EBD incurred an error condition. True = Error. False = No Error.

    IsEngaged: sensor
        Indicates if EBD is currently regulating vehicle brakeforce distribution. True = Engaged. False = Not Engaged.

    """

    def __init__(self, parent):
        """Create a new EBD model."""
        super().__init__(parent)

        self.IsEnabled = DataPointBoolean("IsEnabled", self)
        self.IsError = DataPointBoolean("IsError", self)
        self.IsEngaged = DataPointBoolean("IsEngaged", self)
