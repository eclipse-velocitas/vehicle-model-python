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



"""Vehicle model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointInt16,
    DataPointString,
    DataPointUint16,
    Model,
)

from sdv_model.ADAS import ADAS
from sdv_model.Acceleration import Acceleration
from sdv_model.AngularVelocity import AngularVelocity
from sdv_model.Body import Body
from sdv_model.Cabin import Cabin
from sdv_model.Chassis import Chassis
from sdv_model.Connectivity import Connectivity
from sdv_model.CurrentLocation import CurrentLocation
from sdv_model.Driver import Driver
from sdv_model.Exterior import Exterior
from sdv_model.OBD import OBD
from sdv_model.Powertrain import Powertrain
from sdv_model.Service import Service
from sdv_model.Trailer import Trailer
from sdv_model.VehicleIdentification import VehicleIdentification
from sdv_model.VersionVSS import VersionVSS


class Vehicle(Model):
    """Vehicle model.

    Attributes
    ----------
    VersionVSS: branch
        Supported Version of VSS.

    VehicleIdentification: branch
        Attributes that identify a vehicle.

    LowVoltageSystemState: sensor
        State of the supply voltage of the control units (usually 12V).

        Allowed values: UNDEFINED, LOCK, OFF, ACC, ON, START
    Speed: sensor
        Vehicle speed.

        Unit: km/h
    TravelledDistance: sensor
        Odometer reading, total distance travelled during the lifetime of the vehicle.

        Unit: km
    TripMeterReading: sensor
        Current trip meter reading.

        Unit: km
    IsBrokenDown: sensor
        Vehicle breakdown or any similar event causing vehicle to stop on the road, that might pose a risk to other road users. True = Vehicle broken down on the road, due to e.g. engine problems, flat tire, out of gas, brake problems. False = Vehicle not broken down.

        Actual criteria and method used to decide if a vehicle is broken down is implementation specific.

    IsMoving: sensor
        Indicates whether the vehicle is stationary or moving.

    AverageSpeed: sensor
        Average speed for the current trip.

        Unit: km/h
    Acceleration: branch
        Spatial acceleration. Axis definitions according to ISO 8855.

    AngularVelocity: branch
        Spatial rotation. Axis definitions according to ISO 8855.

    RoofLoad: attribute (int16)
        The permitted total weight of cargo and installations (e.g. a roof rack) on top of the vehicle.

        Unit: kg
    CargoVolume: attribute (float)
        The available volume for cargo or luggage. For automobiles, this is usually the trunk volume.

        Value range: [0, ]
        Unit: l
    EmissionsCO2: attribute (int16)
        The CO2 emissions.

        Unit: g/km
    CurrentOverallWeight: sensor
        Current overall Vehicle weight. Including passengers, cargo and other load inside the car.

        Unit: kg
    CurbWeight: attribute (uint16)
        Vehicle curb weight, including all liquids and full tank of fuel, but no cargo or passengers.

        Unit: kg
    GrossWeight: attribute (uint16)
        Curb weight of vehicle, including all liquids and full tank of fuel and full load of cargo and passengers.

        Unit: kg
    MaxTowWeight: attribute (uint16)
        Maximum weight of trailer.

        Unit: kg
    MaxTowBallWeight: attribute (uint16)
        Maximum vertical weight on the tow ball of a trailer.

        Unit: kg
    Length: attribute (uint16)
        Overall vehicle length.

        Unit: mm
    Height: attribute (uint16)
        Overall vehicle height.

        Unit: mm
    Width: attribute (uint16)
        Overall vehicle width.

        Unit: mm
    Trailer: branch
        Trailer signals.

    CurrentLocation: branch
        The current latitude and longitude of the vehicle.

    Powertrain: branch
        Powertrain data for battery management, etc.

    Body: branch
        All body components.

    Cabin: branch
        All in-cabin components, including doors.

    ADAS: branch
        All Advanced Driver Assist Systems data.

    Chassis: branch
        All data concerning steering, suspension, wheels, and brakes.

    OBD: branch
        OBD data.

    Driver: branch
        Driver data.

    Exterior: branch
        Information about exterior measured by vehicle.

    Service: branch
        Service data.

    Connectivity: branch
        Connectivity data.

    """

    def __init__(self):
        """Create a new Vehicle model."""
        super().__init__()

        self.VersionVSS = VersionVSS(self)
        self.VehicleIdentification = VehicleIdentification(self)
        self.LowVoltageSystemState = DataPointString("LowVoltageSystemState", self)
        self.Speed = DataPointFloat("Speed", self)
        self.TravelledDistance = DataPointFloat("TravelledDistance", self)
        self.TripMeterReading = DataPointFloat("TripMeterReading", self)
        self.IsBrokenDown = DataPointBoolean("IsBrokenDown", self)
        self.IsMoving = DataPointBoolean("IsMoving", self)
        self.AverageSpeed = DataPointFloat("AverageSpeed", self)
        self.Acceleration = Acceleration(self)
        self.AngularVelocity = AngularVelocity(self)
        self.RoofLoad = DataPointInt16("RoofLoad", self)
        self.CargoVolume = DataPointFloat("CargoVolume", self)
        self.EmissionsCO2 = DataPointInt16("EmissionsCO2", self)
        self.CurrentOverallWeight = DataPointUint16("CurrentOverallWeight", self)
        self.CurbWeight = DataPointUint16("CurbWeight", self)
        self.GrossWeight = DataPointUint16("GrossWeight", self)
        self.MaxTowWeight = DataPointUint16("MaxTowWeight", self)
        self.MaxTowBallWeight = DataPointUint16("MaxTowBallWeight", self)
        self.Length = DataPointUint16("Length", self)
        self.Height = DataPointUint16("Height", self)
        self.Width = DataPointUint16("Width", self)
        self.Trailer = Trailer(self)
        self.CurrentLocation = CurrentLocation(self)
        self.Powertrain = Powertrain(self)
        self.Body = Body(self)
        self.Cabin = Cabin(self)
        self.ADAS = ADAS(self)
        self.Chassis = Chassis(self)
        self.OBD = OBD(self)
        self.Driver = Driver(self)
        self.Exterior = Exterior(self)
        self.Service = Service(self)
        self.Connectivity = Connectivity(self)


vehicle = Vehicle()
