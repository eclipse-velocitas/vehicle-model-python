#!/usr/bin/env python3

"""Catalyst model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    Model,
)

from sdv_model.OBD.Catalyst.Bank1 import Bank1
from sdv_model.OBD.Catalyst.Bank2 import Bank2


class Catalyst(Model):
    """Catalyst model.

    Attributes
    ----------
    Bank1: branch
        Catalyst bank 1 signals

    Bank2: branch
        Catalyst bank 2 signals

    """

    def __init__(self, parent):
        """Create a new Catalyst model."""
        super().__init__(parent)

        self.Bank1 = Bank1(self)
        self.Bank2 = Bank2(self)
