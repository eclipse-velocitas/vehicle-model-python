#!/usr/bin/env python3

# Copyright (c) 2022 Contributors to the Eclipse Foundation
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


from sdv.model import DataPointBoolean, Model

from sdv_model.Cabin.Seat.Switch.Backrest.Lumbar import Lumbar
from sdv_model.Cabin.Seat.Switch.Backrest.SideBolster import SideBolster


class Backrest(Model):
    """Backrest model.

    Attributes
    ----------
    IsReclineForwardEngaged: actuator
        Backrest recline forward switch engaged (SingleSeat.Backrest.Recline).

    IsReclineBackwardEngaged: actuator
        Backrest recline backward switch engaged (SingleSeat.Backrest.Recline).

    Lumbar: branch
        Switches for SingleSeat.Backrest.Lumbar.

    SideBolster: branch
        Switches for SingleSeat.Backrest.SideBolster.

    """

    def __init__(self, name, parent):
        """Create a new Backrest model."""
        super().__init__(parent)
        self.name = name

        self.IsReclineForwardEngaged = DataPointBoolean("IsReclineForwardEngaged", self)
        self.IsReclineBackwardEngaged = DataPointBoolean(
            "IsReclineBackwardEngaged", self
        )
        self.Lumbar = Lumbar("Lumbar", self)
        self.SideBolster = SideBolster("SideBolster", self)
