#!/usr/bin/env python3

"""Acceleration model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    Model,
)


class Acceleration(Model):
    """Acceleration model.

    Attributes
    ----------
    Longitudinal: sensor
        Vehicle acceleration in X (longitudinal acceleration).

        Unit: m/s^2
    Lateral: sensor
        Vehicle acceleration in Y (lateral acceleration).

        Unit: m/s^2
    Vertical: sensor
        Vehicle acceleration in Z (vertical acceleration).

        Unit: m/s^2
    """

    def __init__(self, parent):
        """Create a new Acceleration model."""
        super().__init__(parent)

        self.Longitudinal = DataPointFloat("Longitudinal", self)
        self.Lateral = DataPointFloat("Lateral", self)
        self.Vertical = DataPointFloat("Vertical", self)
