#!/usr/bin/env python3

# Copyright (c) 2022-2024 Contributors to the Eclipse Foundation
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
    DataPointString,
    DataPointUint16,
    DataPointUint32,
    Model,
)

from sdv_model.Powertrain.TractionBattery.Charging import Charging
from sdv_model.Powertrain.TractionBattery.DCDC import DCDC
from sdv_model.Powertrain.TractionBattery.StateOfCharge import StateOfCharge
from sdv_model.Powertrain.TractionBattery.Temperature import Temperature


class TractionBattery(Model):
    """TractionBattery model.

    Attributes
    ----------
    Id: attribute (string)
        Battery Identification Number as assigned by OEM.

        This could be serial number, part number plus serial number, UUID, or any other identifier that the OEM want to use to uniquely identify the battery individual.

    ProductionDate: attribute (string)
        Production date of battery in ISO8601 format, e.g. YYYY-MM-DD.

    IsPowerConnected: sensor
        Indicating if the power (positive terminator) of the traction battery is connected to the powertrain.

        It might be possible to disconnect the traction battery used by an electric powertrain. This is achieved by connectors, typically one for plus and one for minus.

    IsGroundConnected: sensor
        Indicating if the ground (negative terminator) of the traction battery is connected to the powertrain.

        It might be possible to disconnect the traction battery used by an electric powertrain. This is achieved by connectors, typically one for plus and one for minus.

    Temperature: branch
        Temperature Information for the battery pack.

    GrossCapacity: attribute (uint16)
        Gross capacity of the battery.

        Unit: kWh
    NetCapacity: sensor
        Total net capacity of the battery considering aging.

        Unit: kWh
    StateOfHealth: sensor
        Calculated battery state of health at standard conditions.

        Exact formula is implementation dependent. Could be e.g. current capacity at 20 degrees Celsius divided with original capacity at the same temperature.

        Value range: [0, 100]
        Unit: percent
    StateOfCharge: branch
        Information on the state of charge of the vehicle's high voltage battery.

    NominalVoltage: attribute (uint16)
        Nominal Voltage of the battery.

        Nominal voltage typically refers to voltage of fully charged battery when delivering rated capacity.

        Unit: V
    MaxVoltage: attribute (uint16)
        Max allowed voltage of the battery, e.g. during charging.

        Unit: V
    CurrentVoltage: sensor
        Current Voltage of the battery.

        Unit: V
    CurrentCurrent: sensor
        Current current flowing in/out of battery. Positive = Current flowing in to battery, e.g. during charging. Negative = Current flowing out of battery, e.g. during driving.

        Unit: A
    CurrentPower: sensor
        Current electrical energy flowing in/out of battery. Positive = Energy flowing in to battery, e.g. during charging. Negative = Energy flowing out of battery, e.g. during driving.

        Unit: W
    AccumulatedChargedEnergy: sensor
        The accumulated energy delivered to the battery during charging over lifetime of the battery.

        Unit: kWh
    AccumulatedConsumedEnergy: sensor
        The accumulated energy leaving HV battery for propulsion and auxiliary loads over lifetime of the battery.

        Unit: kWh
    AccumulatedChargedThroughput: sensor
        The accumulated charge throughput delivered to the battery during charging over lifetime of the battery.

        Unit: Ah
    AccumulatedConsumedThroughput: sensor
        The accumulated charge throughput leaving HV battery for propulsion and auxiliary loads over lifetime of the battery.

        Unit: Ah
    PowerLoss: sensor
        Electrical energy lost by power dissipation to heat inside the battery.

        Unit: W
    Range: sensor
        Remaining range in meters using only battery.

        Unit: m
    Charging: branch
        Properties related to battery charging.

    DCDC: branch
        Properties related to DC/DC converter converting high voltage (from high voltage battery) to vehicle low voltage (supply voltage, typically 12 Volts).

    """

    def __init__(self, name, parent):
        """Create a new TractionBattery model."""
        super().__init__(parent)
        self.name = name

        self.Id = DataPointString("Id", self)
        self.ProductionDate = DataPointString("ProductionDate", self)
        self.IsPowerConnected = DataPointBoolean("IsPowerConnected", self)
        self.IsGroundConnected = DataPointBoolean("IsGroundConnected", self)
        self.Temperature = Temperature("Temperature", self)
        self.GrossCapacity = DataPointUint16("GrossCapacity", self)
        self.NetCapacity = DataPointUint16("NetCapacity", self)
        self.StateOfHealth = DataPointFloat("StateOfHealth", self)
        self.StateOfCharge = StateOfCharge("StateOfCharge", self)
        self.NominalVoltage = DataPointUint16("NominalVoltage", self)
        self.MaxVoltage = DataPointUint16("MaxVoltage", self)
        self.CurrentVoltage = DataPointFloat("CurrentVoltage", self)
        self.CurrentCurrent = DataPointFloat("CurrentCurrent", self)
        self.CurrentPower = DataPointFloat("CurrentPower", self)
        self.AccumulatedChargedEnergy = DataPointFloat("AccumulatedChargedEnergy", self)
        self.AccumulatedConsumedEnergy = DataPointFloat(
            "AccumulatedConsumedEnergy", self
        )
        self.AccumulatedChargedThroughput = DataPointFloat(
            "AccumulatedChargedThroughput", self
        )
        self.AccumulatedConsumedThroughput = DataPointFloat(
            "AccumulatedConsumedThroughput", self
        )
        self.PowerLoss = DataPointFloat("PowerLoss", self)
        self.Range = DataPointUint32("Range", self)
        self.Charging = Charging("Charging", self)
        self.DCDC = DCDC("DCDC", self)
