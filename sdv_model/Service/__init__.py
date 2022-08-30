#!/usr/bin/env python3

"""Service model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointInt32,
    Model,
)


class Service(Model):
    """Service model.

    Attributes
    ----------
    IsServiceDue: sensor
        Indicates if vehicle needs service (of any kind). True = Service needed now or in the near future. False = No known need for service.

    DistanceToService: sensor
        Remaining distance to service (of any kind). Negative values indicate service overdue.

        Unit: km
    TimeToService: sensor
        Remaining time to service (of any kind). Negative values indicate service overdue.

        Unit: s
    """

    def __init__(self, parent):
        """Create a new Service model."""
        super().__init__(parent)

        self.IsServiceDue = DataPointBoolean("IsServiceDue", self)
        self.DistanceToService = DataPointFloat("DistanceToService", self)
        self.TimeToService = DataPointInt32("TimeToService", self)
