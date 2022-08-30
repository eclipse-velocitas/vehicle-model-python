#!/usr/bin/env python3

"""SideBolster model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class SideBolster(Model):
    """SideBolster model.

    Attributes
    ----------
    IsMoreSupportEngaged: actuator
        Is switch for more side bolster support engaged (SingleSeat.Backrest.SideBolster.Support).

    IsLessSupportEngaged: actuator
        Is switch for less side bolster support engaged (SingleSeat.Backrest.SideBolster.Support).

    """

    def __init__(self, parent):
        """Create a new SideBolster model."""
        super().__init__(parent)

        self.IsMoreSupportEngaged = DataPointBoolean("IsMoreSupportEngaged", self)
        self.IsLessSupportEngaged = DataPointBoolean("IsLessSupportEngaged", self)
