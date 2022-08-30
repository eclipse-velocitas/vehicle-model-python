#!/usr/bin/env python3

"""ObstacleDetection model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class ObstacleDetection(Model):
    """ObstacleDetection model.

    Attributes
    ----------
    IsEnabled: actuator
        Indicates if obstacle sensor system is enabled (i.e. monitoring for obstacles). True = Enabled. False = Disabled.

    IsWarning: sensor
        Indicates if obstacle sensor system registered an obstacle.

    IsError: sensor
        Indicates if obstacle sensor system incurred an error condition. True = Error. False = No Error.

    """

    def __init__(self, parent):
        """Create a new ObstacleDetection model."""
        super().__init__(parent)

        self.IsEnabled = DataPointBoolean("IsEnabled", self)
        self.IsWarning = DataPointBoolean("IsWarning", self)
        self.IsError = DataPointBoolean("IsError", self)
