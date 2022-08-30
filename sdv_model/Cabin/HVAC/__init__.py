#!/usr/bin/env python3

"""HVAC model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    Dictionary,
    Model,
    ModelCollection,
    NamedRange,
)

from sdv_model.Cabin.HVAC.Station import Station


class HVAC(Model):
    """HVAC model.

    Attributes
    ----------
    Station: branch
        HVAC for single station in the vehicle

    IsRecirculationActive: actuator
        Is recirculation active.

    IsFrontDefrosterActive: actuator
        Is front defroster active.

    IsRearDefrosterActive: actuator
        Is rear defroster active.

    IsAirConditioningActive: actuator
        Is Air conditioning active.

    AmbientAirTemperature: sensor
        Ambient air temperature inside the vehicle.

        Unit: celsius
    """

    def __init__(self, parent):
        """Create a new HVAC model."""
        super().__init__(parent)

        self.Station = ModelCollection[Station]([NamedRange("Row", 1, 4), Dictionary(["Left", "Right"])], Station(self))
        self.IsRecirculationActive = DataPointBoolean("IsRecirculationActive", self)
        self.IsFrontDefrosterActive = DataPointBoolean("IsFrontDefrosterActive", self)
        self.IsRearDefrosterActive = DataPointBoolean("IsRearDefrosterActive", self)
        self.IsAirConditioningActive = DataPointBoolean("IsAirConditioningActive", self)
        self.AmbientAirTemperature = DataPointFloat("AmbientAirTemperature", self)
