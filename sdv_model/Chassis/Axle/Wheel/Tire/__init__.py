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

"""Tire model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointBoolean, DataPointFloat, DataPointUint16, Model


class Tire(Model):
    """Tire model.

    Attributes
    ----------
    Pressure: sensor
        Tire pressure in kilo-Pascal.

        Unit: kPa
    IsPressureLow: sensor
        Tire Pressure Status. True = Low tire pressure. False = Good tire pressure.

    Temperature: sensor
        Tire temperature in Celsius.

        Unit: celsius
    """

    def __init__(self, name, parent):
        """Create a new Tire model."""
        super().__init__(parent)
        self.name = name

        self.Pressure = DataPointUint16("Pressure", self)
        self.IsPressureLow = DataPointBoolean("IsPressureLow", self)
        self.Temperature = DataPointFloat("Temperature", self)
