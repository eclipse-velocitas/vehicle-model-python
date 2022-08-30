#!/usr/bin/env python3

"""StateOfCharge model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    Model,
)


class StateOfCharge(Model):
    """StateOfCharge model.

    Attributes
    ----------
    Current: sensor
        Physical state of charge of the high voltage battery, relative to net capacity. This is not necessarily the state of charge being displayed to the customer.

        Value range: [0, 100.0]
        Unit: percent
    Displayed: sensor
        State of charge displayed to the customer.

        Value range: [0, 100.0]
        Unit: percent
    """

    def __init__(self, parent):
        """Create a new StateOfCharge model."""
        super().__init__(parent)

        self.Current = DataPointFloat("Current", self)
        self.Displayed = DataPointFloat("Displayed", self)
