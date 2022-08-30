#!/usr/bin/env python3

"""Infotainment model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    Model,
)

from sdv_model.Cabin.Infotainment.HMI import HMI
from sdv_model.Cabin.Infotainment.Media import Media
from sdv_model.Cabin.Infotainment.Navigation import Navigation


class Infotainment(Model):
    """Infotainment model.

    Attributes
    ----------
    Media: branch
        All Media actions

    Navigation: branch
        All navigation actions

    HMI: branch
        HMI related signals

    """

    def __init__(self, parent):
        """Create a new Infotainment model."""
        super().__init__(parent)

        self.Media = Media(self)
        self.Navigation = Navigation(self)
        self.HMI = HMI(self)
