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


"""Axle model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    DataPointUint16,
    DataPointUint8,
    Dictionary,
    Model,
    ModelCollection,
)

from sdv_model.Chassis.Axle.Wheel import Wheel


class Axle(Model):
    """Axle model.

    Attributes
    ----------
    WheelCount: attribute (uint8)
        Number of wheels on the axle

    WheelDiameter: attribute (float)
        Diameter of wheels (rims without tires), in inches, as per ETRTO / TRA standard.

        Unit: inch
    WheelWidth: attribute (float)
        Width of wheels (rims without tires), in inches, as per ETRTO / TRA standard.

        Unit: inch
    TireDiameter: attribute (float)
        Outer diameter of tires, in inches, as per ETRTO / TRA standard.

        Unit: inch
    TireWidth: attribute (uint16)
        Nominal section width of tires, in mm, as per ETRTO / TRA standard.

        Unit: mm
    TireAspectRatio: attribute (uint8)
        Aspect ratio between tire section height and tire section width, as per ETRTO / TRA standard.

        Unit: percent
    Wheel: branch
        Wheel signals for axle

    """

    def __init__(self, parent):
        """Create a new Axle model."""
        super().__init__(parent)

        self.WheelCount = DataPointUint8("WheelCount", self)
        self.WheelDiameter = DataPointFloat("WheelDiameter", self)
        self.WheelWidth = DataPointFloat("WheelWidth", self)
        self.TireDiameter = DataPointFloat("TireDiameter", self)
        self.TireWidth = DataPointUint16("TireWidth", self)
        self.TireAspectRatio = DataPointUint8("TireAspectRatio", self)
        self.Wheel = ModelCollection[Wheel](
            [Dictionary(["Left", "Right"])], Wheel(self))
