#!/usr/bin/env python3

"""DriveCycleStatus model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointString,
    DataPointUint8,
    Model,
)


class DriveCycleStatus(Model):
    """DriveCycleStatus model.

    Attributes
    ----------
    IsMILOn: sensor
        Malfunction Indicator Light (MIL) - False = Off, True = On

    DTCCount: sensor
        Number of sensor Trouble Codes (DTC)

    IgnitionType: sensor
        Type of the ignition for ICE - spark = spark plug ignition, compression = self-igniting (Diesel engines)

        Allowed values: SPARK, COMPRESSION
    """

    def __init__(self, parent):
        """Create a new DriveCycleStatus model."""
        super().__init__(parent)

        self.IsMILOn = DataPointBoolean("IsMILOn", self)
        self.DTCCount = DataPointUint8("DTCCount", self)
        self.IgnitionType = DataPointString("IgnitionType", self)
