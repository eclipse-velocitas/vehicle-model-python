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

"""Transmission model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointInt16,
    DataPointInt8,
    DataPointString,
    DataPointUint8,
    Model,
)


class Transmission(Model):
    """Transmission model.

    Attributes
    ----------
    Type: attribute (string)
        Transmission type.

        Allowed values: UNKNOWN, SEQUENTIAL, H, AUTOMATIC, DSG, CVT
    GearCount: attribute (int8)
        Number of forward gears in the transmission. -1 = CVT.

    DriveType: attribute (string)
        Drive type.

        Allowed values: UNKNOWN, FORWARD_WHEEL_DRIVE, REAR_WHEEL_DRIVE, ALL_WHEEL_DRIVE
    TravelledDistance: sensor
        Odometer reading, total distance travelled during the lifetime of the transmission.

        Unit: km
    CurrentGear: sensor
        The current gear. 0=Neutral, 1/2/..=Forward, -1/-2/..=Reverse.

    SelectedGear: actuator
        The selected gear. 0=Neutral, 1/2/..=Forward, -1/-2/..=Reverse, 126=Park, 127=Drive.

    IsParkLockEngaged: actuator
        Is the transmission park lock engaged or not. False = Disengaged. True = Engaged.

    IsLowRangeEngaged: actuator
        Is gearbox in low range mode or not. False = Normal/High range engaged. True = Low range engaged.

        The possibility to switch between low and high gear range is typically only available in heavy vehicles and off-road vehicles.

    IsElectricalPowertrainEngaged: actuator
        Is electrical powertrain mechanically connected/engaged to the drivetrain or not. False = Disconnected/Disengaged. True = Connected/Engaged.

        In some hybrid solutions it is possible to disconnect/disengage the electrical powertrain mechanically to avoid induced voltage reaching a too high level when driving at high speed.

    PerformanceMode: actuator
        Current gearbox performance mode.

        Allowed values: NORMAL, SPORT, ECONOMY, SNOW, RAIN
    GearChangeMode: actuator
        Is the gearbox in automatic or manual (paddle) mode.

        Allowed values: MANUAL, AUTOMATIC
    Temperature: sensor
        The current gearbox temperature.

        Unit: celsius
    ClutchEngagement: actuator
        Clutch engagement. 0% = Clutch fully disengaged. 100% = Clutch fully engaged.

        Value range: [0, 100]
        Unit: percent
    ClutchWear: sensor
        Clutch wear as a percent. 0 = no wear. 100 = worn.

        Value range: [, 100]
        Unit: percent
    DiffLockFrontEngagement: actuator
        Front Diff Lock engagement. 0% = Diff lock fully disengaged. 100% = Diff lock fully engaged.

        Value range: [0, 100]
        Unit: percent
    DiffLockRearEngagement: actuator
        Rear Diff Lock engagement. 0% = Diff lock fully disengaged. 100% = Diff lock fully engaged.

        Value range: [0, 100]
        Unit: percent
    TorqueDistribution: actuator
        Torque distribution between front and rear axle in percent. -100% = Full torque to front axle, 0% = 50:50 Front/Rear, 100% = Full torque to rear axle.

        Value range: [-100, 100]
        Unit: percent
    """

    def __init__(self, parent):
        """Create a new Transmission model."""
        super().__init__(parent)

        self.Type = DataPointString("Type", self)
        self.GearCount = DataPointInt8("GearCount", self)
        self.DriveType = DataPointString("DriveType", self)
        self.TravelledDistance = DataPointFloat("TravelledDistance", self)
        self.CurrentGear = DataPointInt8("CurrentGear", self)
        self.SelectedGear = DataPointInt8("SelectedGear", self)
        self.IsParkLockEngaged = DataPointBoolean("IsParkLockEngaged", self)
        self.IsLowRangeEngaged = DataPointBoolean("IsLowRangeEngaged", self)
        self.IsElectricalPowertrainEngaged = DataPointBoolean("IsElectricalPowertrainEngaged", self)
        self.PerformanceMode = DataPointString("PerformanceMode", self)
        self.GearChangeMode = DataPointString("GearChangeMode", self)
        self.Temperature = DataPointInt16("Temperature", self)
        self.ClutchEngagement = DataPointFloat("ClutchEngagement", self)
        self.ClutchWear = DataPointUint8("ClutchWear", self)
        self.DiffLockFrontEngagement = DataPointFloat("DiffLockFrontEngagement", self)
        self.DiffLockRearEngagement = DataPointFloat("DiffLockRearEngagement", self)
        self.TorqueDistribution = DataPointFloat("TorqueDistribution", self)
