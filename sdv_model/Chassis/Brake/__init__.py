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


"""Brake model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointUint8,
    Model,
)


class Brake(Model):
    """Brake model.

    Attributes
    ----------
    PedalPosition: sensor
        Brake pedal position as percent. 0 = Not depressed. 100 = Fully depressed.

        Value range: [0, 100]
        Unit: percent
    IsDriverEmergencyBrakingDetected: sensor
        Indicates if emergency braking initiated by driver is detected. True = Emergency braking detected. False = Emergency braking not detected.

        Detection of emergency braking can trigger Emergency Brake Assist (EBA) to engage.

    """

    def __init__(self, parent):
        """Create a new Brake model."""
        super().__init__(parent)

        self.PedalPosition = DataPointUint8("PedalPosition", self)
        self.IsDriverEmergencyBrakingDetected = DataPointBoolean(
            "IsDriverEmergencyBrakingDetected", self)
