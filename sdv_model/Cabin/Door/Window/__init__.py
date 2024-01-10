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

"""Window model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointBoolean, DataPointString, DataPointUint8, Model


class Window(Model):
    """Window model.

    Attributes
    ----------
    IsOpen: sensor
        Is window open or closed?

    Position: sensor
        Window position. 0 = Fully closed 100 = Fully opened.

        Value range: [0, 100]
        Unit: percent
    IsChildLockEngaged: sensor
        Is window child lock engaged. True = Engaged. False = Disengaged.

    Switch: actuator
        Switch controlling sliding action such as window, sunroof, or blind.

        Allowed values: INACTIVE, CLOSE, OPEN, ONE_SHOT_CLOSE, ONE_SHOT_OPEN
    """

    def __init__(self, name, parent):
        """Create a new Window model."""
        super().__init__(parent)
        self.name = name

        self.IsOpen = DataPointBoolean("IsOpen", self)
        self.Position = DataPointUint8("Position", self)
        self.IsChildLockEngaged = DataPointBoolean("IsChildLockEngaged", self)
        self.Switch = DataPointString("Switch", self)
