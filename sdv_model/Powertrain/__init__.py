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

"""Powertrain model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    DataPointString,
    DataPointUint32,
    Model,
)

from sdv_model.Powertrain.CombustionEngine import CombustionEngine
from sdv_model.Powertrain.ElectricMotor import ElectricMotor
from sdv_model.Powertrain.FuelSystem import FuelSystem
from sdv_model.Powertrain.TractionBattery import TractionBattery
from sdv_model.Powertrain.Transmission import Transmission


class Powertrain(Model):
    """Powertrain model.

    Attributes
    ----------
    AccumulatedBrakingEnergy: sensor
        The accumulated energy from regenerative braking over lifetime.

        Unit: kWh
    Range: sensor
        Remaining range in meters using all energy sources available in the vehicle.

        Unit: m
    Type: attribute (string)
        Defines the powertrain type of the vehicle.

        For vehicles with a combustion engine (including hybrids) more detailed information on fuels supported can be found in FuelSystem.SupportedFuelTypes and FuelSystem.SupportedFuels.

        Allowed values: COMBUSTION, HYBRID, ELECTRIC
    CombustionEngine: branch
        Engine-specific data, stopping at the bell housing.

    Transmission: branch
        Transmission-specific data, stopping at the drive shafts.

    ElectricMotor: branch
        Electric Motor specific data.

    TractionBattery: branch
        Battery Management data.

    FuelSystem: branch
        Fuel system data.

    """

    def __init__(self, parent):
        """Create a new Powertrain model."""
        super().__init__(parent)

        self.AccumulatedBrakingEnergy = DataPointFloat("AccumulatedBrakingEnergy", self)
        self.Range = DataPointUint32("Range", self)
        self.Type = DataPointString("Type", self)
        self.CombustionEngine = CombustionEngine(self)
        self.Transmission = Transmission(self)
        self.ElectricMotor = ElectricMotor(self)
        self.TractionBattery = TractionBattery(self)
        self.FuelSystem = FuelSystem(self)
