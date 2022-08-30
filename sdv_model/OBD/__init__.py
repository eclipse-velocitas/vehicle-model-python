#!/usr/bin/env python3

"""OBD model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointString,
    DataPointStringArray,
    DataPointUint32,
    DataPointUint8,
    Model,
    ModelCollection,
    NamedRange,
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

    def __init__(self, parent):
        """Create a new OBD model."""
        super().__init__(parent)

        self.PidsA = DataPointUint32("PidsA", self)
        self.Status = Status(self)
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
        self.O2 = ModelCollection[O2]([NamedRange("Sensor", 1, 8)], O2(self))
        self.OBDStandards = DataPointUint8("OBDStandards", self)
        self.OxygenSensorsIn4Banks = DataPointUint8("OxygenSensorsIn4Banks", self)
        self.IsPTOActive = DataPointBoolean("IsPTOActive", self)
        self.RunTime = DataPointFloat("RunTime", self)
        self.PidsB = DataPointUint32("PidsB", self)
        self.DistanceWithMIL = DataPointFloat("DistanceWithMIL", self)
        self.FuelRailPressureVac = DataPointFloat("FuelRailPressureVac", self)
        self.FuelRailPressureDirect = DataPointFloat("FuelRailPressureDirect", self)
        self.O2WR = ModelCollection[O2WR]([NamedRange("Sensor", 1, 8)], O2WR(self))
        self.CommandedEGR = DataPointFloat("CommandedEGR", self)
        self.EGRError = DataPointFloat("EGRError", self)
        self.CommandedEVAP = DataPointFloat("CommandedEVAP", self)
        self.FuelLevel = DataPointFloat("FuelLevel", self)
        self.WarmupsSinceDTCClear = DataPointUint8("WarmupsSinceDTCClear", self)
        self.DistanceSinceDTCClear = DataPointFloat("DistanceSinceDTCClear", self)
        self.EVAPVaporPressure = DataPointFloat("EVAPVaporPressure", self)
        self.BarometricPressure = DataPointFloat("BarometricPressure", self)
        self.Catalyst = Catalyst(self)
        self.PidsC = DataPointUint32("PidsC", self)
        self.DriveCycleStatus = DriveCycleStatus(self)
        self.ControlModuleVoltage = DataPointFloat("ControlModuleVoltage", self)
        self.AbsoluteLoad = DataPointFloat("AbsoluteLoad", self)
        self.CommandedEquivalenceRatio = DataPointFloat("CommandedEquivalenceRatio", self)
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
        self.EVAPVaporPressureAbsolute = DataPointFloat("EVAPVaporPressureAbsolute", self)
        self.EVAPVaporPressureAlternate = DataPointFloat("EVAPVaporPressureAlternate", self)
        self.ShortTermO2Trim1 = DataPointFloat("ShortTermO2Trim1", self)
        self.ShortTermO2Trim3 = DataPointFloat("ShortTermO2Trim3", self)
        self.LongTermO2Trim1 = DataPointFloat("LongTermO2Trim1", self)
        self.LongTermO2Trim3 = DataPointFloat("LongTermO2Trim3", self)
        self.ShortTermO2Trim2 = DataPointFloat("ShortTermO2Trim2", self)
        self.ShortTermO2Trim4 = DataPointFloat("ShortTermO2Trim4", self)
        self.LongTermO2Trim2 = DataPointFloat("LongTermO2Trim2", self)
        self.LongTermO2Trim4 = DataPointFloat("LongTermO2Trim4", self)
        self.FuelRailPressureAbsolute = DataPointFloat("FuelRailPressureAbsolute", self)
        self.RelativeAcceleratorPosition = DataPointFloat("RelativeAcceleratorPosition", self)
        self.HybridBatteryRemaining = DataPointFloat("HybridBatteryRemaining", self)
        self.OilTemperature = DataPointFloat("OilTemperature", self)
        self.FuelInjectionTiming = DataPointFloat("FuelInjectionTiming", self)
        self.FuelRate = DataPointFloat("FuelRate", self)
