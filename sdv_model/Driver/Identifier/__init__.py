#!/usr/bin/env python3

"""Identifier model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointString,
    Model,
)


class Identifier(Model):
    """Identifier model.

    Attributes
    ----------
    Subject: sensor
        Subject for the authentication of the occupant. E.g. UserID 7331677.

    Issuer: sensor
        Unique Issuer for the authentication of the occupant. E.g. https://accounts.funcorp.com.

    """

    def __init__(self, parent):
        """Create a new Identifier model."""
        super().__init__(parent)

        self.Subject = DataPointString("Subject", self)
        self.Issuer = DataPointString("Issuer", self)
