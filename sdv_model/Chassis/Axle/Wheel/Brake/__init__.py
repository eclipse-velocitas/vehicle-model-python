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

"""Brake model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointUint8,
    Model,
)


class Brake(Model):
    """Brake model.

    Attributes
    ----------
    FluidLevel: sensor
        Brake fluid level as percent. 0 = Empty. 100 = Full.

        Unit: percent
    IsFluidLevelLow: sensor
        Brake fluid level status. True = Brake fluid level low. False = Brake fluid level OK.

    PadWear: sensor
        Brake pad wear as percent. 0 = No Wear. 100 = Worn.

    IsBrakesWorn: sensor
        Brake pad wear status. True = Worn. False = Not Worn.

    """

    def __init__(self, parent):
        """Create a new Brake model."""
        super().__init__(parent)

        self.FluidLevel = DataPointUint8("FluidLevel", self)
        self.IsFluidLevelLow = DataPointBoolean("IsFluidLevelLow", self)
        self.PadWear = DataPointUint8("PadWear", self)
        self.IsBrakesWorn = DataPointBoolean("IsBrakesWorn", self)
