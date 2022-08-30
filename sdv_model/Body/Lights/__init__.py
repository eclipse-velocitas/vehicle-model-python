#!/usr/bin/env python3

"""Lights model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    Dictionary,
    Model,
    ModelCollection,
)

from sdv_model.Body.Lights.Backup import Backup
from sdv_model.Body.Lights.Beam import Beam
from sdv_model.Body.Lights.Brake import Brake
from sdv_model.Body.Lights.DirectionIndicator import DirectionIndicator
from sdv_model.Body.Lights.Fog import Fog
from sdv_model.Body.Lights.Hazard import Hazard
from sdv_model.Body.Lights.LicensePlate import LicensePlate
from sdv_model.Body.Lights.Parking import Parking
from sdv_model.Body.Lights.Running import Running


class Lights(Model):
    """Lights model.

    Attributes
    ----------
    Beam: branch
        Beam lights.

    Running: branch
        Running lights.

    Backup: branch
        Backup lights.

    Parking: branch
        Parking lights.

    Fog: branch
        Fog lights.

    LicensePlate: branch
        License plate lights.

    Brake: branch
        None

    Hazard: branch
        Hazard lights.

    DirectionIndicator: branch
        Indicator lights.

    """

    def __init__(self, parent):
        """Create a new Lights model."""
        super().__init__(parent)

        self.Beam = ModelCollection[Beam]([Dictionary(["Low", "High"])], Beam(self))
        self.Running = Running(self)
        self.Backup = Backup(self)
        self.Parking = Parking(self)
        self.Fog = ModelCollection[Fog]([Dictionary(["Rear", "Front"])], Fog(self))
        self.LicensePlate = LicensePlate(self)
        self.Brake = Brake(self)
        self.Hazard = Hazard(self)
        self.DirectionIndicator = ModelCollection[DirectionIndicator]([Dictionary(["Left", "Right"])], DirectionIndicator(self))
