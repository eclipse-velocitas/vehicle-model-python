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

"""Charging model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointString,
    DataPointUint32,
    DataPointUint8,
    Model,
)

from sdv_model.Powertrain.TractionBattery.Charging.Timer import Timer


class Charging(Model):
    """Charging model.

    Attributes
    ----------
    ChargeLimit: actuator
        Maximum charge level for battery, can potentially be set manually.

        Value range: [0, 100]
        Unit: percent
    MaximumChargingCurrent: sensor
        Maximum charging current that can be accepted by the system.

        Unit: A
    ChargePortFlap: actuator
        Status of the charge port cover, can potentially be controlled manually.

        Allowed values: OPEN, CLOSED
    IsChargingCableConnected: sensor
        Indicates if a charging cable is connected to the vehicle or not.

    ChargePlugType: attribute (string)
        Type of charge plug (charging connector) available on the vehicle. IEC types refer to IEC 62196,  GBT refers to  GB/T 20234.

        IEC_TYPE_1_AC refers to Type 1 as defined in IEC 62196-2. Also known as Yazaki or J1772 connector. IEC_TYPE_2_AC refers to Type 2 as defined in IEC 62196-2. Also known as Mennekes connector. IEC_TYPE_3_AC refers to Type 3 as defined in IEC 62196-2. Also known as Scame connector. IEC_TYPE_4_DC refers to AA configuration as defined in IEC 62196-3. Also known as Type 4 or CHAdeMO connector. IEC_TYPE_1_CCS_DC refers to EE Configuration as defined in IEC 62196-3. Also known as CCS1 or Combo1 connector. IEC_TYPE_2_CCS_DC refers to FF Configuration as defined in IEC 62196-3. Also known as CCS2 or Combo2 connector. TESLA_ROADSTER, TESLA_HPWC (High Power Wall Connector) and TESLA_SUPERCHARGER refer to non-standardized charging plugs/methods used by Tesla. GBT_AC refers to connector specified in GB/T 20234.2. GBT_DC refers to connector specified in GB/T 20234.3. Also specified as BB Configuration in IEC 62196-3. OTHER shall be used if the vehicle has a charging connector, but not one of the connectors listed above. For additional information see https://en.wikipedia.org/wiki/IEC_62196.

        Allowed values: IEC_TYPE_1_AC, IEC_TYPE_2_AC, IEC_TYPE_3_AC, IEC_TYPE_4_DC, IEC_TYPE_1_CCS_DC, IEC_TYPE_2_CCS_DC, TESLA_ROADSTER, TESLA_HPWC, TESLA_SUPERCHARGER, GBT_AC, GBT_DC, OTHER
    Mode: actuator
        Control of the charge process - manually initiated (plug-in event, companion app, etc), timer-based or grid-controlled (eg ISO 15118).

        Allowed values: MANUAL, TIMER, GRID
    IsCharging: sensor
        True if charging is ongoing. Charging is considered to be ongoing if energy is flowing from charger to vehicle.

    StartStopCharging: actuator
        Start or stop the charging process.

        Allowed values: START, STOP
    ChargeCurrent: sensor
        Current charging current.

        Unit: A
    ChargeVoltage: sensor
        Current charging voltage.

        Unit: V
    ChargeRate: sensor
        Current charging rate, as in kilometers of range added per hour.

        Unit: km/h
    TimeToComplete: sensor
        The time needed for the current charging process to reach StateOfCharge.Target. 0 if charging is complete or no charging process is active or planned.

        Shall consider time set by Charging.Timer.Time. E.g. if charging shall start in 3 hours and 2 hours of charging is needed, then Charging.TimeToComplete shall report 5 hours.

        Unit: s
    Timer: branch
        Properties related to timing of battery charging sessions.

    """

    def __init__(self, parent):
        """Create a new Charging model."""
        super().__init__(parent)

        self.ChargeLimit = DataPointUint8("ChargeLimit", self)
        self.MaximumChargingCurrent = DataPointFloat("MaximumChargingCurrent", self)
        self.ChargePortFlap = DataPointString("ChargePortFlap", self)
        self.IsChargingCableConnected = DataPointBoolean("IsChargingCableConnected", self)
        self.ChargePlugType = DataPointString("ChargePlugType", self)
        self.Mode = DataPointString("Mode", self)
        self.IsCharging = DataPointBoolean("IsCharging", self)
        self.StartStopCharging = DataPointString("StartStopCharging", self)
        self.ChargeCurrent = DataPointFloat("ChargeCurrent", self)
        self.ChargeVoltage = DataPointFloat("ChargeVoltage", self)
        self.ChargeRate = DataPointFloat("ChargeRate", self)
        self.TimeToComplete = DataPointUint32("TimeToComplete", self)
        self.Timer = Timer(self)
