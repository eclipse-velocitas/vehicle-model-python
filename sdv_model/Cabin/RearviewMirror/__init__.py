#!/usr/bin/env python3

"""RearviewMirror model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointUint8,
    Model,
)


class RearviewMirror(Model):
    """RearviewMirror model.

    Attributes
    ----------
    DimmingLevel: actuator
        Dimming level of rearview mirror. 0 = undimmed. 100 = fully dimmed.

        Value range: [, 100]
        Unit: percent
    """

    def __init__(self, parent):
        """Create a new RearviewMirror model."""
        super().__init__(parent)

        self.DimmingLevel = DataPointUint8("DimmingLevel", self)
