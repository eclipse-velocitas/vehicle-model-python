#!/usr/bin/env python3

# Copyright (c) 2022 Robert Bosch GmbH and Microsoft Corporation
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0


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
