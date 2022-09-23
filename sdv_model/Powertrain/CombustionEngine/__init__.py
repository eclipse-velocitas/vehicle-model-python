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

"""CombustionEngine model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointInt16,
    DataPointInt32,
    DataPointString,
    DataPointUint8,
    DataPointUint16,
    Model,
)

from sdv_model.Powertrain.CombustionEngine.DieselExhaustFluid import DieselExhaustFluid
from sdv_model.Powertrain.CombustionEngine.DieselParticulateFilter import (
    DieselParticulateFilter,
)


class CombustionEngine(Model):
    """CombustionEngine model.

    Attributes
    ----------
    EngineCode: attribute (string)
        Engine code designation, as specified by vehicle manufacturer.

        For hybrid vehicles the engine code may refer to the combination of combustion and electric engine.

    Displacement: attribute (uint16)
        Displacement in cubic centimetres.

        Unit: cm^3
    StrokeLength: attribute (float)
        Stroke length in millimetres.

        Unit: mm
    Bore: attribute (float)
        Bore in millimetres.

        Unit: mm
    Configuration: attribute (string)
        Engine configuration.

        Allowed values: UNKNOWN, STRAIGHT, V, BOXER, W, ROTARY, RADIAL, SQUARE, H, U, OPPOSED, X
    NumberOfCylinders: attribute (uint16)
        Number of cylinders.

    NumberOfValvesPerCylinder: attribute (uint16)
        Number of valves per cylinder.

    CompressionRatio: attribute (string)
        Engine compression ratio, specified in the format 'X:1', e.g. '9.2:1'.

    EngineOilCapacity: attribute (float)
        Engine oil capacity in liters.

        Unit: l
    EngineCoolantCapacity: attribute (float)
        Engine coolant capacity in liters.

        Unit: l
    MaxPower: attribute (uint16)
        Peak power, in kilowatts, that engine can generate.

        Unit: kW
    MaxTorque: attribute (uint16)
        Peak torque, in newton meter, that the engine can generate.

        Unit: Nm
    AspirationType: attribute (string)
        Type of aspiration (natural, turbocharger, supercharger etc).

        Allowed values: UNKNOWN, NATURAL, SUPERCHARGER, TURBOCHARGER
    EngineOilLevel: sensor
        Engine oil level.

        Allowed values: CRITICALLY_LOW, LOW, NORMAL, HIGH, CRITICALLY_HIGH
    OilLifeRemaining: sensor
        Remaining engine oil life in seconds. Negative values can be used to indicate that lifetime has been exceeded.

        In addition to this a signal a vehicle can report remaining time to service (including e.g. oil change) by Vehicle.Service.TimeToService.

        Unit: s
    IsRunning: sensor
        Engine Running. True if engine is rotating (Speed > 0).

    Speed: sensor
        Engine speed measured as rotations per minute.

        Unit: rpm
    EngineHours: sensor
        Accumulated time during engine lifetime with 'engine speed (rpm) > 0'.

        Unit: h
    IdleHours: sensor
        Accumulated idling time during engine lifetime. Definition of idling is not standardized.

        Vehicles may calculate accumulated idle time for an engine. It might be based on engine speed (rpm) below a certain limit or any other mechanism.

        Unit: h
    ECT: sensor
        Engine coolant temperature.

        Unit: celsius
    EOT: sensor
        Engine oil temperature.

        Unit: celsius
    MAP: sensor
        Manifold absolute pressure possibly boosted using forced induction.

        Unit: kPa
    MAF: sensor
        Grams of air drawn into engine per second.

        Unit: g/s
    TPS: sensor
        Current throttle position.

        Value range: [, 100]
        Unit: percent
    EOP: sensor
        Engine oil pressure.

        Unit: kPa
    Power: sensor
        Current engine power output. Shall be reported as 0 during engine breaking.

        Unit: kW
    Torque: sensor
        Current engine torque. Shall be reported as 0 during engine breaking.

        During engine breaking the engine delivers a negative torque to the transmission. This negative torque shall be ignored, instead 0 shall be reported.

        Unit: Nm
    DieselExhaustFluid: branch
        Signals related to Diesel Exhaust Fluid (DEF). DEF is called AUS32 in ISO 22241.

        In retail and marketing other names are typically used for the fluid.

    DieselParticulateFilter: branch
        Diesel Particulate Filter signals.

    """

    def __init__(self, name, parent):
        """Create a new CombustionEngine model."""
        super().__init__(parent)
        self.name = name

        self.EngineCode = DataPointString("EngineCode", self)
        self.Displacement = DataPointUint16("Displacement", self)
        self.StrokeLength = DataPointFloat("StrokeLength", self)
        self.Bore = DataPointFloat("Bore", self)
        self.Configuration = DataPointString("Configuration", self)
        self.NumberOfCylinders = DataPointUint16("NumberOfCylinders", self)
        self.NumberOfValvesPerCylinder = DataPointUint16(
            "NumberOfValvesPerCylinder", self
        )
        self.CompressionRatio = DataPointString("CompressionRatio", self)
        self.EngineOilCapacity = DataPointFloat("EngineOilCapacity", self)
        self.EngineCoolantCapacity = DataPointFloat("EngineCoolantCapacity", self)
        self.MaxPower = DataPointUint16("MaxPower", self)
        self.MaxTorque = DataPointUint16("MaxTorque", self)
        self.AspirationType = DataPointString("AspirationType", self)
        self.EngineOilLevel = DataPointString("EngineOilLevel", self)
        self.OilLifeRemaining = DataPointInt32("OilLifeRemaining", self)
        self.IsRunning = DataPointBoolean("IsRunning", self)
        self.Speed = DataPointUint16("Speed", self)
        self.EngineHours = DataPointFloat("EngineHours", self)
        self.IdleHours = DataPointFloat("IdleHours", self)
        self.ECT = DataPointInt16("ECT", self)
        self.EOT = DataPointInt16("EOT", self)
        self.MAP = DataPointUint16("MAP", self)
        self.MAF = DataPointUint16("MAF", self)
        self.TPS = DataPointUint8("TPS", self)
        self.EOP = DataPointUint16("EOP", self)
        self.Power = DataPointUint16("Power", self)
        self.Torque = DataPointUint16("Torque", self)
        self.DieselExhaustFluid = DieselExhaustFluid("DieselExhaustFluid", self)
        self.DieselParticulateFilter = DieselParticulateFilter(
            "DieselParticulateFilter", self
        )
