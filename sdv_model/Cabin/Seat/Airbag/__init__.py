#!/usr/bin/env python3

"""Airbag model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class Airbag(Model):
    """Airbag model.

    Attributes
    ----------
    IsDeployed: sensor
        Airbag deployment status. True = Airbag deployed. False = Airbag not deployed.

    """

    def __init__(self, parent):
        """Create a new Airbag model."""
        super().__init__(parent)

        self.IsDeployed = DataPointBoolean("IsDeployed", self)
