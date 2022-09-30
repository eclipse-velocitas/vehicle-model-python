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


from sdv.model import DataPointUint8, DataPointUint8Array, Model

from sdv_model.Cabin.Convertible import Convertible
from sdv_model.Cabin.Door import Door
from sdv_model.Cabin.HVAC import HVAC
from sdv_model.Cabin.Infotainment import Infotainment
from sdv_model.Cabin.Lights import Lights
from sdv_model.Cabin.RearShade import RearShade
from sdv_model.Cabin.RearviewMirror import RearviewMirror
from sdv_model.Cabin.Seat import Seat
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

    def __init__(self, name, parent):
        """Create a new Cabin model."""
        super().__init__(parent)
        self.name = name

        self.RearShade = RearShade("RearShade", self)
        self.HVAC = HVAC("HVAC", self)
        self.Infotainment = Infotainment("Infotainment", self)
        self.Sunroof = Sunroof("Sunroof", self)
        self.RearviewMirror = RearviewMirror("RearviewMirror", self)
        self.Lights = Lights("Lights", self)
        self.Door = DoorCollection("Door", self)
        self.DoorCount = DataPointUint8("DoorCount", self)
        self.Seat = SeatCollection("Seat", self)
        self.DriverPosition = DataPointUint8("DriverPosition", self)
        self.SeatRowCount = DataPointUint8("SeatRowCount", self)
        self.SeatPosCount = DataPointUint8Array("SeatPosCount", self)
        self.Convertible = Convertible("Convertible", self)


class DoorCollection(Model):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.Row1 = self.RowType("Row1", self)
        self.Row2 = self.RowType("Row2", self)

    def Row(self, index: int):
        if index < 1 or index > 2:
            raise IndexError(f"Index {index} is out of range")
        _options = {
            1: self.Row1,
            2: self.Row2,
        }
        return _options.get(index)

    class RowType(Model):
        def __init__(self, name, parent):
            super().__init__(parent)
            self.name = name
            self.Left = Door("Left", self)
            self.Right = Door("Right", self)

        def element(self, index: int):
            if index < 1 or index > 2:
                raise IndexError(f"Index {index} is out of range")
            _options = {
                1: self.Left,
                2: self.Right,
            }
            return _options.get(index)


class SeatCollection(Model):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.Row1 = self.RowType("Row1", self)
        self.Row2 = self.RowType("Row2", self)

    def Row(self, index: int):
        if index < 1 or index > 2:
            raise IndexError(f"Index {index} is out of range")
        _options = {
            1: self.Row1,
            2: self.Row2,
        }
        return _options.get(index)

    class RowType(Model):
        def __init__(self, name, parent):
            super().__init__(parent)
            self.name = name
            self.Pos1 = Seat("Pos1", self)
            self.Pos2 = Seat("Pos2", self)
            self.Pos3 = Seat("Pos3", self)

        def Pos(self, index: int):
            if index < 1 or index > 3:
                raise IndexError(f"Index {index} is out of range")
            _options = {
                1: self.Pos1,
                2: self.Pos2,
                3: self.Pos3,
            }
            return _options.get(index)
