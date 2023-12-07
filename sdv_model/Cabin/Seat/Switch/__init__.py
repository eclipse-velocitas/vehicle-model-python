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

"""Switch model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointBoolean, Model

from sdv_model.Cabin.Seat.Switch.Backrest import Backrest
from sdv_model.Cabin.Seat.Switch.Headrest import Headrest
from sdv_model.Cabin.Seat.Switch.Massage import Massage
from sdv_model.Cabin.Seat.Switch.Seating import Seating


class Switch(Model):
    """Switch model.

    Attributes
    ----------
    IsWarmerEngaged: actuator
        Warmer switch for Seat heater (SingleSeat.Heating).

    IsCoolerEngaged: actuator
        Cooler switch for Seat heater (SingleSeat.Heating).

    IsForwardEngaged: actuator
        Seat forward switch engaged (SingleSeat.Position).

    IsBackwardEngaged: actuator
        Seat backward switch engaged (SingleSeat.Position).

    IsUpEngaged: actuator
        Seat up switch engaged (SingleSeat.Height).

    IsDownEngaged: actuator
        Seat down switch engaged (SingleSeat.Height).

    IsTiltForwardEngaged: actuator
        Tilt forward switch engaged (SingleSeat.Tilt).

    IsTiltBackwardEngaged: actuator
        Tilt backward switch engaged (SingleSeat.Tilt).

    Backrest: branch
        Describes switches related to the backrest of the seat.

    Seating: branch
        Describes switches related to the seating of the seat.

    Headrest: branch
        Switches for SingleSeat.Headrest.

    Massage: branch
        Switches for SingleSeat.Massage.

    """

    def __init__(self, name, parent):
        """Create a new Switch model."""
        super().__init__(parent)
        self.name = name

        self.IsWarmerEngaged = DataPointBoolean("IsWarmerEngaged", self)
        self.IsCoolerEngaged = DataPointBoolean("IsCoolerEngaged", self)
        self.IsForwardEngaged = DataPointBoolean("IsForwardEngaged", self)
        self.IsBackwardEngaged = DataPointBoolean("IsBackwardEngaged", self)
        self.IsUpEngaged = DataPointBoolean("IsUpEngaged", self)
        self.IsDownEngaged = DataPointBoolean("IsDownEngaged", self)
        self.IsTiltForwardEngaged = DataPointBoolean("IsTiltForwardEngaged", self)
        self.IsTiltBackwardEngaged = DataPointBoolean("IsTiltBackwardEngaged", self)
        self.Backrest = Backrest("Backrest", self)
        self.Seating = Seating("Seating", self)
        self.Headrest = Headrest("Headrest", self)
        self.Massage = Massage("Massage", self)
