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

"""Seat model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointInt8,
    DataPointUint8,
    DataPointUint16,
    Model,
)

from sdv_model.Cabin.Seat.Airbag import Airbag
from sdv_model.Cabin.Seat.Backrest import Backrest
from sdv_model.Cabin.Seat.Headrest import Headrest
from sdv_model.Cabin.Seat.Occupant import Occupant
from sdv_model.Cabin.Seat.Seating import Seating
from sdv_model.Cabin.Seat.Switch import Switch


class Seat(Model):
    """Seat model.

    Attributes
    ----------
    IsOccupied: sensor
        Does the seat have a passenger in it.

    Occupant: branch
        Occupant data.

    IsBelted: sensor
        Is the belt engaged.

    Heating: actuator
        Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat.

        Value range: [-100, 100]
        Unit: percent
    Massage: actuator
        Seat massage level. 0 = off. 100 = max massage.

        Value range: [0, 100]
        Unit: percent
    Position: actuator
        Seat position on vehicle x-axis. Position is relative to the frontmost position supported by the seat. 0 = Frontmost position supported.

        Value range: [0, ]
        Unit: mm
    Height: actuator
        Seat position on vehicle z-axis. Position is relative within available movable range of the seating. 0 = Lowermost position supported.

        Value range: [0, ]
        Unit: mm
    Tilt: actuator
        Tilting of seat relative to vehicle z-axis. 0 = seating is flat, seat and vehicle z-axis are parallel. Positive degrees = seat tilted backwards, seat z-axis is tilted backward.

        Unit: degrees
    Backrest: branch
        Describes signals related to the backrest of the seat.

    Seating: branch
        Describes signals related to the seating/base of the seat.

        Seating is here considered as the part of the seat that supports the thighs. Additional cushions (if any) for support of lower legs is not covered by this branch.

    Headrest: branch
        Headrest settings.

    Airbag: branch
        Airbag signals.

    Switch: branch
        Seat switch signals

    """

    def __init__(self, name, parent):
        """Create a new Seat model."""
        super().__init__(parent)
        self.name = name

        self.IsOccupied = DataPointBoolean("IsOccupied", self)
        self.Occupant = Occupant("Occupant", self)
        self.IsBelted = DataPointBoolean("IsBelted", self)
        self.Heating = DataPointInt8("Heating", self)
        self.Massage = DataPointUint8("Massage", self)
        self.Position = DataPointUint16("Position", self)
        self.Height = DataPointUint16("Height", self)
        self.Tilt = DataPointFloat("Tilt", self)
        self.Backrest = Backrest("Backrest", self)
        self.Seating = Seating("Seating", self)
        self.Headrest = Headrest("Headrest", self)
        self.Airbag = Airbag("Airbag", self)
        self.Switch = Switch("Switch", self)
