#!/usr/bin/env python3

"""Hood model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class Hood(Model):
    """Hood model.

    Attributes
    ----------
    IsOpen: actuator
        Hood open or closed. True = Open. False = Closed.

    """

    def __init__(self, parent):
        """Create a new Hood model."""
        super().__init__(parent)

        self.IsOpen = DataPointBoolean("IsOpen", self)
