#!/usr/bin/env python3

"""Lumbar model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class Lumbar(Model):
    """Lumbar model.

    Attributes
    ----------
    IsMoreSupportEngaged: actuator
        Is switch for more lumbar support engaged (SingleSeat.Backrest.Lumbar.Support).

    IsLessSupportEngaged: actuator
        Is switch for less lumbar support engaged (SingleSeat.Backrest.Lumbar.Support).

    IsUpEngaged: actuator
        Lumbar up switch engaged (SingleSeat.Backrest.Lumbar.Support).

    IsDownEngaged: actuator
        Lumbar down switch engaged (SingleSeat.Backrest.Lumbar.Support).

    """

    def __init__(self, parent):
        """Create a new Lumbar model."""
        super().__init__(parent)

        self.IsMoreSupportEngaged = DataPointBoolean("IsMoreSupportEngaged", self)
        self.IsLessSupportEngaged = DataPointBoolean("IsLessSupportEngaged", self)
        self.IsUpEngaged = DataPointBoolean("IsUpEngaged", self)
        self.IsDownEngaged = DataPointBoolean("IsDownEngaged", self)
