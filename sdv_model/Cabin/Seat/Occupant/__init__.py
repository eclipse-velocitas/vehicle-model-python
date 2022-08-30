#!/usr/bin/env python3

"""Occupant model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    Model,
)

from sdv_model.Cabin.Seat.Occupant.Identifier import Identifier


class Occupant(Model):
    """Occupant model.

    Attributes
    ----------
    Identifier: branch
        Identifier attributes based on OAuth 2.0.

    """

    def __init__(self, parent):
        """Create a new Occupant model."""
        super().__init__(parent)

        self.Identifier = Identifier(self)
