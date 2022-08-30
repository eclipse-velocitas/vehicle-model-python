#!/usr/bin/env python3

"""SideBolster model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    Model,
)


class SideBolster(Model):
    """SideBolster model.

    Attributes
    ----------
    Support: actuator
        Side bolster support. 0 = Minimum support (widest side bolster setting). 100 = Maximum support.

        Value range: [0, 100]
        Unit: percent
    """

    def __init__(self, parent):
        """Create a new SideBolster model."""
        super().__init__(parent)

        self.Support = DataPointFloat("Support", self)
