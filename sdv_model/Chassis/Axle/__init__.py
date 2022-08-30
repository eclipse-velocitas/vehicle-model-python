#!/usr/bin/env python3

"""Axle model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    DataPointUint16,
    DataPointUint8,
    Dictionary,
    Model,
    ModelCollection,
)

from sdv_model.Chassis.Axle.Wheel import Wheel


class Axle(Model):
    """Axle model.

    Attributes
    ----------
    WheelCount: attribute (uint8)
        Number of wheels on the axle

    WheelDiameter: attribute (float)
        Diameter of wheels (rims without tires), in inches, as per ETRTO / TRA standard.

        Unit: inch
    WheelWidth: attribute (float)
        Width of wheels (rims without tires), in inches, as per ETRTO / TRA standard.

        Unit: inch
    TireDiameter: attribute (float)
        Outer diameter of tires, in inches, as per ETRTO / TRA standard.

        Unit: inch
    TireWidth: attribute (uint16)
        Nominal section width of tires, in mm, as per ETRTO / TRA standard.

        Unit: mm
    TireAspectRatio: attribute (uint8)
        Aspect ratio between tire section height and tire section width, as per ETRTO / TRA standard.

        Unit: percent
    Wheel: branch
        Wheel signals for axle

    """

    def __init__(self, parent):
        """Create a new Axle model."""
        super().__init__(parent)

        self.WheelCount = DataPointUint8("WheelCount", self)
        self.WheelDiameter = DataPointFloat("WheelDiameter", self)
        self.WheelWidth = DataPointFloat("WheelWidth", self)
        self.TireDiameter = DataPointFloat("TireDiameter", self)
        self.TireWidth = DataPointUint16("TireWidth", self)
        self.TireAspectRatio = DataPointUint8("TireAspectRatio", self)
        self.Wheel = ModelCollection[Wheel]([Dictionary(["Left", "Right"])], Wheel(self))
