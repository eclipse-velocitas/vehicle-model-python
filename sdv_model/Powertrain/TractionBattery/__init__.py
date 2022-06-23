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

"""TractionBattery model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointUint16,
    DataPointUint32,
    Model,
)

from sdv_model.Powertrain.TractionBattery.Charging import Charging
from sdv_model.Powertrain.TractionBattery.StateOfCharge import StateOfCharge


class TractionBattery(Model):
    """TractionBattery model.

    Attributes
    ----------
    IsPowerConnected: sensor
        Indicating if the power (positive terminator) of the traction battery is connected to the powertrain.

        It might be possible to disconnect the traction battery used by an electric powertrain. This is achieved by connectors, typically one for plus and one for minus.

    IsGroundConnected: sensor
        Indicating if the ground (negative terminator) of the traction battery is connected to the powertrain.

        It might be possible to disconnect the traction battery used by an electric powertrain. This is achieved by connectors, typically one for plus and one for minus.

    Temperature: sensor
        Temperature of the battery pack.

        Unit: celsius
    StateOfCharge: branch
        Information on the state of charge of the vehicle's high voltage battery.

    GrossCapacity: attribute (uint16)
        Gross capacity of the battery.

        Unit: kWh
    NetCapacity: attribute (uint16)
        Net capacity of the battery.

        Unit: kWh
    NominalVoltage: attribute (uint16)
        Nominal Voltage of the battery.

        Unit: V
    ReferentVoltage: attribute (uint16)
        Referent Voltage of the battery.

        Unit: V
    AccumulatedChargedEnergy: sensor
        The accumulated energy delivered to the battery during charging over lifetime of the battery.

        Unit: kWh
    AccumulatedConsumedEnergy: sensor
        The accumulated energy leaving HV battery for propulsion and auxiliary loads over lifetime of the battery.

        Unit: kWh
    Range: sensor
        Remaining range in meters using only battery.

        Unit: m
    Charging: branch
        Properties related to battery charging.

    """

    def __init__(self, parent):
        """Create a new TractionBattery model."""
        super().__init__(parent)

        self.IsPowerConnected = DataPointBoolean("IsPowerConnected", self)
        self.IsGroundConnected = DataPointBoolean("IsGroundConnected", self)
        self.Temperature = DataPointFloat("Temperature", self)
        self.StateOfCharge = StateOfCharge(self)
        self.GrossCapacity = DataPointUint16("GrossCapacity", self)
        self.NetCapacity = DataPointUint16("NetCapacity", self)
        self.NominalVoltage = DataPointUint16("NominalVoltage", self)
        self.ReferentVoltage = DataPointUint16("ReferentVoltage", self)
        self.AccumulatedChargedEnergy = DataPointFloat("AccumulatedChargedEnergy", self)
        self.AccumulatedConsumedEnergy = DataPointFloat("AccumulatedConsumedEnergy", self)
        self.Range = DataPointUint32("Range", self)
        self.Charging = Charging(self)
