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


"""Backrest model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    Model,
)

from sdv_model.Cabin.Seat.Backrest.Lumbar import Lumbar
from sdv_model.Cabin.Seat.Backrest.SideBolster import SideBolster


class Backrest(Model):
    """Backrest model.

    Attributes
    ----------
    Recline: actuator
        Backrest recline compared to seat z-axis (seat vertical axis). 0 degrees = Upright/Vertical backrest. Negative degrees for forward recline. Positive degrees for backward recline.

        Seat z-axis depends on seat tilt. This means that movement of backrest due to seat tilting will not affect Backrest.Recline as long as the angle between Seating and Backrest are constant. Absolute recline relative to vehicle z-axis can be calculated as Tilt + Backrest.Recline.

        Unit: degrees
    Lumbar: branch
        Adjustable lumbar support mechanisms in seats allow the user to change the seat back shape.

    SideBolster: branch
        Backrest side bolster (lumbar side support) settings.

    """

    def __init__(self, parent):
        """Create a new Backrest model."""
        super().__init__(parent)

        self.Recline = DataPointFloat("Recline", self)
        self.Lumbar = Lumbar(self)
        self.SideBolster = SideBolster(self)
