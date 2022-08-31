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


"""Cabin model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointUint8,
    DataPointUint8Array,
    Dictionary,
    Model,
    ModelCollection,
    NamedRange,
)

from sdv_model.Cabin.Convertible import Convertible
from sdv_model.Cabin.Door import Door
from sdv_model.Cabin.HVAC import HVAC
from sdv_model.Cabin.Infotainment import Infotainment
from sdv_model.Cabin.Lights import Lights
from sdv_model.Cabin.RearShade import RearShade
from sdv_model.Cabin.RearviewMirror import RearviewMirror
from sdv_model.Cabin.Seat import Seat
from sdv_model.Cabin.SeatService import SeatService
from sdv_model.Cabin.Sunroof import Sunroof


class Cabin(Model):
    """Cabin model.

    Attributes
    ----------
    RearShade: branch
        Rear window shade.

    HVAC: branch
        Climate control

    Infotainment: branch
        Infotainment system.

    Sunroof: branch
        Sun roof status.

    RearviewMirror: branch
        Rearview mirror.

    Lights: branch
        Interior lights signals and sensors.

    Door: branch
        All doors, including windows and switches.

    DoorCount: attribute (uint8)
        Number of doors in vehicle.

    Seat: branch
        All seats.

    DriverPosition: attribute (uint8)
        The position of the driver seat in row 1.

        Default value is position 1, i.e. a typical LHD vehicle.

    SeatRowCount: attribute (uint8)
        Number of seat rows in vehicle.

        Default value corresponds to two rows of seats.

    SeatPosCount: attribute (uint8[])
        Number of seats across each row from the front to the rear.

        Default value corresponds to two seats in front row and 3 seats in second row.

    Convertible: branch
        Convertible roof.

    """

    def __init__(self, parent):
        """Create a new Cabin model."""
        super().__init__(parent)

        self.RearShade = RearShade(self)
        self.HVAC = HVAC(self)
        self.Infotainment = Infotainment(self)
        self.Sunroof = Sunroof(self)
        self.RearviewMirror = RearviewMirror(self)
        self.Lights = Lights(self)
        self.Door = ModelCollection[Door](
            [NamedRange("Row", 1, 2), Dictionary(["Left", "Right"])], Door(self))
        self.DoorCount = DataPointUint8("DoorCount", self)
        self.SeatService = SeatService()
        self.Seat = ModelCollection[Seat](
            [NamedRange("Row", 1, 2), NamedRange("Pos", 1, 3)], Seat(self))
        self.DriverPosition = DataPointUint8("DriverPosition", self)
        self.SeatRowCount = DataPointUint8("SeatRowCount", self)
        self.SeatPosCount = DataPointUint8Array("SeatPosCount", self)
        self.Convertible = Convertible(self)
