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

"""AngularVelocity model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointFloat, Model


class AngularVelocity(Model):
    """AngularVelocity model.

    Attributes
    ----------
    Roll: sensor
        Vehicle rotation rate along X (longitudinal).

        Unit: degrees/s
    Pitch: sensor
        Vehicle rotation rate along Y (lateral).

        Unit: degrees/s
    Yaw: sensor
        Vehicle rotation rate along Z (vertical).

        Unit: degrees/s
    """

    def __init__(self, name, parent):
        """Create a new AngularVelocity model."""
        super().__init__(parent)
        self.name = name

        self.Roll = DataPointFloat("Roll", self)
        self.Pitch = DataPointFloat("Pitch", self)
        self.Yaw = DataPointFloat("Yaw", self)
