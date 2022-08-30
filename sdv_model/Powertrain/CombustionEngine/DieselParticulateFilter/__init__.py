#!/usr/bin/env python3

"""DieselParticulateFilter model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    Model,
)


class DieselParticulateFilter(Model):
    """DieselParticulateFilter model.

    Attributes
    ----------
    InletTemperature: sensor
        Inlet temperature of Diesel Particulate Filter.

        Unit: celsius
    OutletTemperature: sensor
        Outlet temperature of Diesel Particulate Filter.

        Unit: celsius
    DeltaPressure: sensor
        Delta Pressure of Diesel Particulate Filter.

        Unit: Pa
    """

    def __init__(self, parent):
        """Create a new DieselParticulateFilter model."""
        super().__init__(parent)

        self.InletTemperature = DataPointFloat("InletTemperature", self)
        self.OutletTemperature = DataPointFloat("OutletTemperature", self)
        self.DeltaPressure = DataPointFloat("DeltaPressure", self)
