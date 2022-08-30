#!/usr/bin/env python3

"""Navigation model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    Model,
)

from sdv_model.Cabin.Infotainment.Navigation.DestinationSet import DestinationSet


class Navigation(Model):
    """Navigation model.

    Attributes
    ----------
    DestinationSet: branch
        A navigation has been selected.

    """

    def __init__(self, parent):
        """Create a new Navigation model."""
        super().__init__(parent)

        self.DestinationSet = DestinationSet(self)
