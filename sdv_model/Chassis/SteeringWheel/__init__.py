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

"""SteeringWheel model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointInt16, DataPointString, DataPointUint8, Model


class SteeringWheel(Model):
    """SteeringWheel model.

    Attributes
    ----------
    Angle: sensor
        Steering wheel angle. Positive = degrees to the left. Negative = degrees to the right.

        Unit: degrees
    Tilt: actuator
        Steering wheel column tilt. 0 = Lowest position. 100 = Highest position.

        Value range: [0, 100]
        Unit: percent
    Extension: actuator
        Steering wheel column extension from dashboard. 0 = Closest to dashboard. 100 = Furthest from dashboard.

        Value range: [0, 100]
        Unit: percent
    Position: attribute (string)
        Position of the steering wheel on the left or right side of the vehicle.

        Allowed values: FRONT_LEFT, FRONT_RIGHT
    """

    def __init__(self, name, parent):
        """Create a new SteeringWheel model."""
        super().__init__(parent)
        self.name = name

        self.Angle = DataPointInt16("Angle", self)
        self.Tilt = DataPointUint8("Tilt", self)
        self.Extension = DataPointUint8("Extension", self)
        self.Position = DataPointString("Position", self)
