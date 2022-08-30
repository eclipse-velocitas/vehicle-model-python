#!/usr/bin/env python3

"""Trailer model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class Trailer(Model):
    """Trailer model.

    Attributes
    ----------
    IsConnected: sensor
        Signal indicating if trailer is connected or not.

    """

    def __init__(self, parent):
        """Create a new Trailer model."""
        super().__init__(parent)

        self.IsConnected = DataPointBoolean("IsConnected", self)
