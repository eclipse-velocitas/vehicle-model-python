#!/usr/bin/env python3

"""EBA model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class EBA(Model):
    """EBA model.

    Attributes
    ----------
    IsEnabled: actuator
        Indicates if EBA is enabled. True = Enabled. False = Disabled.

    IsError: sensor
        Indicates if EBA incurred an error condition. True = Error. False = No Error.

    IsEngaged: sensor
        Indicates if EBA is currently regulating brake pressure. True = Engaged. False = Not Engaged.

    """

    def __init__(self, parent):
        """Create a new EBA model."""
        super().__init__(parent)

        self.IsEnabled = DataPointBoolean("IsEnabled", self)
        self.IsError = DataPointBoolean("IsError", self)
        self.IsEngaged = DataPointBoolean("IsEngaged", self)
