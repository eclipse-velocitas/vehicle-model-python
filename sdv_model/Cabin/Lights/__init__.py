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

"""Lights model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointUint8,
    Model,
    ModelCollection,
    NamedRange,
)

from sdv_model.Cabin.Lights.Spotlight import Spotlight


class Lights(Model):
    """Lights model.

    Attributes
    ----------
    IsGloveBoxOn: actuator
        Is glove box light on

    IsTrunkOn: actuator
        Is trunk light light on

    IsDomeOn: actuator
        Is central dome light light on

    AmbientLight: sensor
        How much ambient light is detected in cabin. 0 = No ambient light. 100 = Full brightness

        Value range: [0, 100]
        Unit: percent
    LightIntensity: sensor
        Intensity of the interior lights. 0 = Off. 100 = Full brightness.

        Value range: [0, 100]
        Unit: percent
    Spotlight: branch
        Spotlight for a specific area in the vehicle.

    """

    def __init__(self, parent):
        """Create a new Lights model."""
        super().__init__(parent)

        self.IsGloveBoxOn = DataPointBoolean("IsGloveBoxOn", self)
        self.IsTrunkOn = DataPointBoolean("IsTrunkOn", self)
        self.IsDomeOn = DataPointBoolean("IsDomeOn", self)
        self.AmbientLight = DataPointUint8("AmbientLight", self)
        self.LightIntensity = DataPointUint8("LightIntensity", self)
        self.Spotlight = ModelCollection[Spotlight]([NamedRange("Row", 1, 4)], Spotlight(self))
