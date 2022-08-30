#!/usr/bin/env python3

"""SteeringWheel model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointInt16,
    DataPointString,
    DataPointUint8,
    Model,
)


class SteeringWheel(Model):
    """SteeringWheel model.

    Attributes
    ----------
    Angle: sensor
        Steering wheel angle. Positive = degrees to the left. Negative = degrees to the right.

        Unit: degrees
    Tilt: actuator
        Steering wheel column tilt. 0 = Lowest position. 100 = Highest position.

        Value range: [0, 100]
        Unit: percent
    Extension: actuator
        Steering wheel column extension from dashboard. 0 = Closest to dashboard. 100 = Furthest from dashboard.

        Value range: [0, 100]
        Unit: percent
    Position: attribute (string)
        Position of the steering wheel on the left or right side of the vehicle.

        Allowed values: FRONT_LEFT, FRONT_RIGHT
    """

    def __init__(self, parent):
        """Create a new SteeringWheel model."""
        super().__init__(parent)

        self.Angle = DataPointInt16("Angle", self)
        self.Tilt = DataPointUint8("Tilt", self)
        self.Extension = DataPointUint8("Extension", self)
        self.Position = DataPointString("Position", self)
