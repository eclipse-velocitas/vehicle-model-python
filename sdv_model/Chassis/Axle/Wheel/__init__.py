#!/usr/bin/env python3

# Copyright (c) 2022-2024 Contributors to the Eclipse Foundation
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

"""Wheel model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointFloat, Model

from sdv_model.Chassis.Axle.Wheel.Brake import Brake
from sdv_model.Chassis.Axle.Wheel.Tire import Tire


class Wheel(Model):
    """Wheel model.

    Attributes
    ----------
    Brake: branch
        Brake signals for wheel

    Tire: branch
        Tire signals for wheel.

    Speed: sensor
        Rotational speed of a vehicle's wheel.

        Unit: km/h
    """

    def __init__(self, name, parent):
        """Create a new Wheel model."""
        super().__init__(parent)
        self.name = name

        self.Brake = Brake("Brake", self)
        self.Tire = Tire("Tire", self)
        self.Speed = DataPointFloat("Speed", self)
