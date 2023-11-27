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

"""OBD model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointString,
    DataPointStringArray,
    DataPointUint8,
    DataPointUint32,
    Model,
)

from sdv_model.OBD.Catalyst import Catalyst
from sdv_model.OBD.DriveCycleStatus import DriveCycleStatus
from sdv_model.OBD.O2 import O2
from sdv_model.OBD.O2WR import O2WR
from sdv_model.OBD.Status import Status


class OBD(Model):
    """OBD model.

    Attributes
    ----------
    PidsA: sensor
        PID 00 - Bit array of the supported pids 01 to 20

    Status: branch
        PID 01 - OBD status

    DTCList: sensor
        List of currently active DTCs formatted according OBD II (SAE-J2012DA_201812) standard ([P|C|B|U]XXXXX )

    FreezeDTC: sensor
        PID 02 - DTC that triggered the freeze frame

    FuelStatus: sensor
        PID 03 - Fuel status

    EngineLoad: sensor
        PID 04 - Engine load in percent - 0 = no load, 100 = full load

        Unit: percent
    CoolantTemperature: sensor
        PID 05 - Coolant temperature

        Unit: celsius
    ShortTermFuelTrim1: sensor
        PID 06 - Short Term (immediate) Fuel Trim - Bank 1 - negative percent leaner, positive percent richer

        Unit: percent
    LongTermFuelTrim1: sensor
        PID 07 - Long Term (learned) Fuel Trim - Bank 1 - negative percent leaner, positive percent richer

        Unit: percent
    ShortTermFuelTrim2: sensor
        PID 08 - Short Term (immediate) Fuel Trim - Bank 2 - negative percent leaner, positive percent richer

        Unit: percent
    LongTermFuelTrim2: sensor
        PID 09 - Long Term (learned) Fuel Trim - Bank 2 - negative percent leaner, positive percent richer

        Unit: percent
    FuelPressure: sensor
        PID 0A - Fuel pressure

        Unit: kPa
    MAP: sensor
        PID 0B - Intake manifold pressure

        Unit: kPa
    EngineSpeed: sensor
        PID 0C - Engine speed measured as rotations per minute

        Unit: rpm
    Speed: sensor
        PID 0D - Vehicle speed

        Unit: km/h
    TimingAdvance: sensor
        PID 0E - Time advance

        Unit: degrees
    IntakeTemp: sensor
        PID 0F - Intake temperature

        Unit: celsius
    MAF: sensor
        PID 10 - Grams of air drawn into engine per second

        Unit: g/s
    ThrottlePosition: sensor
        PID 11 - Throttle position - 0 = closed throttle, 100 = open throttle

        Unit: percent
    AirStatus: sensor
        PID 12 - Secondary air status

    OxygenSensorsIn2Banks: sensor
        PID 13 - Presence of oxygen sensors in 2 banks. [A0..A3] == Bank 1, Sensors 1-4. [A4..A7] == Bank 2, Sensors 1-4

    O2: branch
        Oxygen sensors (PID 14 - PID 1B)

    OBDStandards: attribute (uint8)
        PID 1C - OBD standards this vehicle conforms to

    OxygenSensorsIn4Banks: sensor
        PID 1D - Presence of oxygen sensors in 4 banks. Similar to PID 13, but [A0..A7] == [B1S1, B1S2, B2S1, B2S2, B3S1, B3S2, B4S1, B4S2]

    IsPTOActive: sensor
        PID 1E - Auxiliary input status (power take off)

    RunTime: sensor
        PID 1F - Engine run time

        Unit: s
    PidsB: sensor
        PID 20 - Bit array of the supported pids 21 to 40

    DistanceWithMIL: sensor
        PID 21 - Distance traveled with MIL on

        Unit: km
    FuelRailPressureVac: sensor
        PID 22 - Fuel rail pressure relative to vacuum

        Unit: kPa
    FuelRailPressureDirect: sensor
        PID 23 - Fuel rail pressure direct inject

        Unit: kPa
    O2WR: branch
        Wide range/band oxygen sensors (PID 24 - 2B and PID 34 - 3B)

    CommandedEGR: sensor
        PID 2C - Commanded exhaust gas recirculation (EGR)

        Unit: percent
    EGRError: sensor
        PID 2D - Exhaust gas recirculation (EGR) error

        Unit: percent
    CommandedEVAP: sensor
        PID 2E - Commanded evaporative purge (EVAP) valve

        Unit: percent
    FuelLevel: sensor
        PID 2F - Fuel level in the fuel tank

        Unit: percent
    WarmupsSinceDTCClear: sensor
        PID 30 - Number of warm-ups since codes cleared

    DistanceSinceDTCClear: sensor
        PID 31 - Distance traveled since codes cleared

        Unit: km
    EVAPVaporPressure: sensor
        PID 32 - Evaporative purge (EVAP) system pressure

        Unit: Pa
    BarometricPressure: sensor
        PID 33 - Barometric pressure

        Unit: kPa
    Catalyst: branch
        Catalyst signals

    PidsC: sensor
        PID 40 - Bit array of the supported pids 41 to 60

    DriveCycleStatus: branch
        PID 41 - OBD status for the current drive cycle

    ControlModuleVoltage: sensor
        PID 42 - Control module voltage

        Unit: V
    AbsoluteLoad: sensor
        PID 43 - Absolute load value

        Unit: percent
    CommandedEquivalenceRatio: sensor
        PID 44 - Commanded equivalence ratio

        Unit: ratio
    RelativeThrottlePosition: sensor
        PID 45 - Relative throttle position

        Unit: percent
    AmbientAirTemperature: sensor
        PID 46 - Ambient air temperature

        Unit: celsius
    ThrottlePositionB: sensor
        PID 47 - Absolute throttle position B

        Unit: percent
    ThrottlePositionC: sensor
        PID 48 - Absolute throttle position C

        Unit: percent
    AcceleratorPositionD: sensor
        PID 49 - Accelerator pedal position D

        Unit: percent
    AcceleratorPositionE: sensor
        PID 4A - Accelerator pedal position E

        Unit: percent
    AcceleratorPositionF: sensor
        PID 4B - Accelerator pedal position F

        Unit: percent
    ThrottleActuator: sensor
        PID 4C - Commanded throttle actuator

        Unit: percent
    RunTimeMIL: sensor
        PID 4D - Run time with MIL on

        Unit: min
    TimeSinceDTCCleared: sensor
        PID 4E - Time since trouble codes cleared

        Unit: min
    MaxMAF: sensor
        PID 50 - Maximum flow for mass air flow sensor

        Unit: g/s
    FuelType: sensor
        PID 51 - Fuel type

    EthanolPercent: sensor
        PID 52 - Percentage of ethanol in the fuel

        Unit: percent
    EVAPVaporPressureAbsolute: sensor
        PID 53 - Absolute evaporative purge (EVAP) system pressure

        Unit: kPa
    EVAPVaporPressureAlternate: sensor
        PID 54 - Alternate evaporative purge (EVAP) system pressure

        Unit: Pa
    ShortTermO2Trim1: sensor
        PID 55 (byte A) - Short term secondary O2 trim - Bank 1

        Unit: percent
    ShortTermO2Trim3: sensor
        PID 55 (byte B) - Short term secondary O2 trim - Bank 3

        Unit: percent
    LongTermO2Trim1: sensor
        PID 56 (byte A) - Long term secondary O2 trim - Bank 1

        Unit: percent
    LongTermO2Trim3: sensor
        PID 56 (byte B) - Long term secondary O2 trim - Bank 3

        Unit: percent
    ShortTermO2Trim2: sensor
        PID 57 (byte A) - Short term secondary O2 trim - Bank 2

        Unit: percent
    ShortTermO2Trim4: sensor
        PID 57 (byte B) - Short term secondary O2 trim - Bank 4

        Unit: percent
    LongTermO2Trim2: sensor
        PID 58 (byte A) - Long term secondary O2 trim - Bank 2

        Unit: percent
    LongTermO2Trim4: sensor
        PID 58 (byte B) - Long term secondary O2 trim - Bank 4

        Unit: percent
    FuelRailPressureAbsolute: sensor
        PID 59 - Absolute fuel rail pressure

        Unit: kPa
    RelativeAcceleratorPosition: sensor
        PID 5A - Relative accelerator pedal position

        Unit: percent
    HybridBatteryRemaining: sensor
        PID 5B - Remaining life of hybrid battery

        Unit: percent
    OilTemperature: sensor
        PID 5C - Engine oil temperature

        Unit: celsius
    FuelInjectionTiming: sensor
        PID 5D - Fuel injection timing

        Unit: degrees
    FuelRate: sensor
        PID 5E - Engine fuel rate

        Unit: l/h
    """

    def __init__(self, name, parent):
        """Create a new OBD model."""
        super().__init__(parent)
        self.name = name

        self.PidsA = DataPointUint32("PidsA", self)
        self.Status = Status("Status", self)
        self.DTCList = DataPointStringArray("DTCList", self)
        self.FreezeDTC = DataPointString("FreezeDTC", self)
        self.FuelStatus = DataPointString("FuelStatus", self)
        self.EngineLoad = DataPointFloat("EngineLoad", self)
        self.CoolantTemperature = DataPointFloat("CoolantTemperature", self)
        self.ShortTermFuelTrim1 = DataPointFloat("ShortTermFuelTrim1", self)
        self.LongTermFuelTrim1 = DataPointFloat("LongTermFuelTrim1", self)
        self.ShortTermFuelTrim2 = DataPointFloat("ShortTermFuelTrim2", self)
        self.LongTermFuelTrim2 = DataPointFloat("LongTermFuelTrim2", self)
        self.FuelPressure = DataPointFloat("FuelPressure", self)
        self.MAP = DataPointFloat("MAP", self)
        self.EngineSpeed = DataPointFloat("EngineSpeed", self)
        self.Speed = DataPointFloat("Speed", self)
        self.TimingAdvance = DataPointFloat("TimingAdvance", self)
        self.IntakeTemp = DataPointFloat("IntakeTemp", self)
        self.MAF = DataPointFloat("MAF", self)
        self.ThrottlePosition = DataPointFloat("ThrottlePosition", self)
        self.AirStatus = DataPointString("AirStatus", self)
        self.OxygenSensorsIn2Banks = DataPointUint8("OxygenSensorsIn2Banks", self)
        self.O2 = O2Collection("O2", self)
        self.OBDStandards = DataPointUint8("OBDStandards", self)
        self.OxygenSensorsIn4Banks = DataPointUint8("OxygenSensorsIn4Banks", self)
        self.IsPTOActive = DataPointBoolean("IsPTOActive", self)
        self.RunTime = DataPointFloat("RunTime", self)
        self.PidsB = DataPointUint32("PidsB", self)
        self.DistanceWithMIL = DataPointFloat("DistanceWithMIL", self)
        self.FuelRailPressureVac = DataPointFloat("FuelRailPressureVac", self)
        self.FuelRailPressureDirect = DataPointFloat("FuelRailPressureDirect", self)
        self.O2WR = O2WRCollection("O2WR", self)
        self.CommandedEGR = DataPointFloat("CommandedEGR", self)
        self.EGRError = DataPointFloat("EGRError", self)
        self.CommandedEVAP = DataPointFloat("CommandedEVAP", self)
        self.FuelLevel = DataPointFloat("FuelLevel", self)
        self.WarmupsSinceDTCClear = DataPointUint8("WarmupsSinceDTCClear", self)
        self.DistanceSinceDTCClear = DataPointFloat("DistanceSinceDTCClear", self)
        self.EVAPVaporPressure = DataPointFloat("EVAPVaporPressure", self)
        self.BarometricPressure = DataPointFloat("BarometricPressure", self)
        self.Catalyst = Catalyst("Catalyst", self)
        self.PidsC = DataPointUint32("PidsC", self)
        self.DriveCycleStatus = DriveCycleStatus("DriveCycleStatus", self)
        self.ControlModuleVoltage = DataPointFloat("ControlModuleVoltage", self)
        self.AbsoluteLoad = DataPointFloat("AbsoluteLoad", self)
        self.CommandedEquivalenceRatio = DataPointFloat(
            "CommandedEquivalenceRatio", self
        )
        self.RelativeThrottlePosition = DataPointFloat("RelativeThrottlePosition", self)
        self.AmbientAirTemperature = DataPointFloat("AmbientAirTemperature", self)
        self.ThrottlePositionB = DataPointFloat("ThrottlePositionB", self)
        self.ThrottlePositionC = DataPointFloat("ThrottlePositionC", self)
        self.AcceleratorPositionD = DataPointFloat("AcceleratorPositionD", self)
        self.AcceleratorPositionE = DataPointFloat("AcceleratorPositionE", self)
        self.AcceleratorPositionF = DataPointFloat("AcceleratorPositionF", self)
        self.ThrottleActuator = DataPointFloat("ThrottleActuator", self)
        self.RunTimeMIL = DataPointFloat("RunTimeMIL", self)
        self.TimeSinceDTCCleared = DataPointFloat("TimeSinceDTCCleared", self)
        self.MaxMAF = DataPointFloat("MaxMAF", self)
        self.FuelType = DataPointString("FuelType", self)
        self.EthanolPercent = DataPointFloat("EthanolPercent", self)
        self.EVAPVaporPressureAbsolute = DataPointFloat(
            "EVAPVaporPressureAbsolute", self
        )
        self.EVAPVaporPressureAlternate = DataPointFloat(
            "EVAPVaporPressureAlternate", self
        )
        self.ShortTermO2Trim1 = DataPointFloat("ShortTermO2Trim1", self)
        self.ShortTermO2Trim3 = DataPointFloat("ShortTermO2Trim3", self)
        self.LongTermO2Trim1 = DataPointFloat("LongTermO2Trim1", self)
        self.LongTermO2Trim3 = DataPointFloat("LongTermO2Trim3", self)
        self.ShortTermO2Trim2 = DataPointFloat("ShortTermO2Trim2", self)
        self.ShortTermO2Trim4 = DataPointFloat("ShortTermO2Trim4", self)
        self.LongTermO2Trim2 = DataPointFloat("LongTermO2Trim2", self)
        self.LongTermO2Trim4 = DataPointFloat("LongTermO2Trim4", self)
        self.FuelRailPressureAbsolute = DataPointFloat("FuelRailPressureAbsolute", self)
        self.RelativeAcceleratorPosition = DataPointFloat(
            "RelativeAcceleratorPosition", self
        )
        self.HybridBatteryRemaining = DataPointFloat("HybridBatteryRemaining", self)
        self.OilTemperature = DataPointFloat("OilTemperature", self)
        self.FuelInjectionTiming = DataPointFloat("FuelInjectionTiming", self)
        self.FuelRate = DataPointFloat("FuelRate", self)


class O2Collection(Model):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.Sensor1 = O2("Sensor1", self)
        self.Sensor2 = O2("Sensor2", self)
        self.Sensor3 = O2("Sensor3", self)
        self.Sensor4 = O2("Sensor4", self)
        self.Sensor5 = O2("Sensor5", self)
        self.Sensor6 = O2("Sensor6", self)
        self.Sensor7 = O2("Sensor7", self)
        self.Sensor8 = O2("Sensor8", self)

    def Sensor(self, index: int):
        if index < 1 or index > 8:
            raise IndexError(f"Index {index} is out of range [1, 8]")
        _options = {
            1: self.Sensor1,
            2: self.Sensor2,
            3: self.Sensor3,
            4: self.Sensor4,
            5: self.Sensor5,
            6: self.Sensor6,
            7: self.Sensor7,
            8: self.Sensor8,
        }
        return _options.get(index)


class O2WRCollection(Model):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.Sensor1 = O2WR("Sensor1", self)
        self.Sensor2 = O2WR("Sensor2", self)
        self.Sensor3 = O2WR("Sensor3", self)
        self.Sensor4 = O2WR("Sensor4", self)
        self.Sensor5 = O2WR("Sensor5", self)
        self.Sensor6 = O2WR("Sensor6", self)
        self.Sensor7 = O2WR("Sensor7", self)
        self.Sensor8 = O2WR("Sensor8", self)

    def Sensor(self, index: int):
        if index < 1 or index > 8:
            raise IndexError(f"Index {index} is out of range [1, 8]")
        _options = {
            1: self.Sensor1,
            2: self.Sensor2,
            3: self.Sensor3,
            4: self.Sensor4,
            5: self.Sensor5,
            6: self.Sensor6,
            7: self.Sensor7,
            8: self.Sensor8,
        }
        return _options.get(index)
