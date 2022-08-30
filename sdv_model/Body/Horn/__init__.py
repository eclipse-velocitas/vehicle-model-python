#!/usr/bin/env python3

"""Horn model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class Horn(Model):
    """Horn model.

    Attributes
    ----------
    IsActive: actuator
        Horn active or inactive. True = Active. False = Inactive.

    """

    def __init__(self, parent):
        """Create a new Horn model."""
        super().__init__(parent)

        self.IsActive = DataPointBoolean("IsActive", self)
