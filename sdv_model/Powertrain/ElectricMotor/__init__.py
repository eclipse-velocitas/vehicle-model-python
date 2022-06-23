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

"""ElectricMotor model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointInt16,
    DataPointInt32,
    DataPointString,
    DataPointUint16,
    Model,
)


class ElectricMotor(Model):
    """ElectricMotor model.

    Attributes
    ----------
    EngineCode: attribute (string)
        Engine code designation, as specified by vehicle manufacturer.

    MaxPower: attribute (uint16)
        Peak power, in kilowatts, that motor(s) can generate.

        Unit: kW
    MaxTorque: attribute (uint16)
        Peak power, in newton meter, that the motor(s) can generate.

        Unit: Nm
    MaxRegenPower: attribute (uint16)
        Peak regen/brake power, in kilowatts, that motor(s) can generate.

        Unit: kW
    MaxRegenTorque: attribute (uint16)
        Peak regen/brake torque, in newton meter, that the motor(s) can generate.

        Unit: Nm
    Rpm: sensor
        Motor rotational speed measured as rotations per minute. Negative values indicate reverse driving mode.

        Unit: rpm
    Temperature: sensor
        Motor temperature.

        Unit: celsius
    CoolantTemperature: sensor
        Motor coolant temperature (if applicable).

        Unit: celsius
    Power: sensor
        Current motor power output. Negative values indicate regen mode.

        Unit: kW
    Torque: sensor
        Current motor torque. Negative values indicate regen mode.

        Unit: Nm
    """

    def __init__(self, parent):
        """Create a new ElectricMotor model."""
        super().__init__(parent)

        self.EngineCode = DataPointString("EngineCode", self)
        self.MaxPower = DataPointUint16("MaxPower", self)
        self.MaxTorque = DataPointUint16("MaxTorque", self)
        self.MaxRegenPower = DataPointUint16("MaxRegenPower", self)
        self.MaxRegenTorque = DataPointUint16("MaxRegenTorque", self)
        self.Rpm = DataPointInt32("Rpm", self)
        self.Temperature = DataPointInt16("Temperature", self)
        self.CoolantTemperature = DataPointInt16("CoolantTemperature", self)
        self.Power = DataPointInt16("Power", self)
        self.Torque = DataPointInt16("Torque", self)
