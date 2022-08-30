#!/usr/bin/env python3

"""Connectivity model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class Connectivity(Model):
    """Connectivity model.

    Attributes
    ----------
    IsConnectivityAvailable: sensor
        Indicates if connectivity between vehicle and cloud is available. True = Connectivity is available. False = Connectivity is not available.

        This signal can be used by onboard vehicle services to decide what features that shall be offered to the driver, for example disable the 'check for update' button if vehicle does not have connectivity.

    """

    def __init__(self, parent):
        """Create a new Connectivity model."""
        super().__init__(parent)

        self.IsConnectivityAvailable = DataPointBoolean("IsConnectivityAvailable", self)
