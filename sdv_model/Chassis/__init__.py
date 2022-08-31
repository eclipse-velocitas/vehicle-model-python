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


"""Chassis model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointUint16,
    DataPointUint8,
    Model,
    ModelCollection,
    NamedRange,
)

from sdv_model.Chassis.Accelerator import Accelerator
from sdv_model.Chassis.Axle import Axle
from sdv_model.Chassis.Brake import Brake
from sdv_model.Chassis.ParkingBrake import ParkingBrake
from sdv_model.Chassis.SteeringWheel import SteeringWheel


class Chassis(Model):
    """Chassis model.

    Attributes
    ----------
    Wheelbase: attribute (uint16)
        Overall wheel base, in mm.

        Unit: mm
    Track: attribute (uint16)
        Overall wheel tracking, in mm.

        Unit: mm
    Axle: branch
        Axle signals

    AxleCount: attribute (uint8)
        Number of axles on the vehicle

    ParkingBrake: branch
        Parking brake signals

    SteeringWheel: branch
        Steering wheel signals

    Accelerator: branch
        Accelerator signals

    Brake: branch
        Brake system signals

    """

    def __init__(self, parent):
        """Create a new Chassis model."""
        super().__init__(parent)

        self.Wheelbase = DataPointUint16("Wheelbase", self)
        self.Track = DataPointUint16("Track", self)
        self.Axle = ModelCollection[Axle](
            [NamedRange("Row", 1, 2)], Axle(self))
        self.AxleCount = DataPointUint8("AxleCount", self)
        self.ParkingBrake = ParkingBrake(self)
        self.SteeringWheel = SteeringWheel(self)
        self.Accelerator = Accelerator(self)
        self.Brake = Brake(self)
