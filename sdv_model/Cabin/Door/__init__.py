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

"""Door model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointBoolean, Model

from sdv_model.Cabin.Door.Shade import Shade
from sdv_model.Cabin.Door.Window import Window


class Door(Model):
    """Door model.

    Attributes
    ----------
    IsOpen: actuator
        Is door open or closed

    IsLocked: actuator
        Is door locked or unlocked. True = Locked. False = Unlocked.

    Window: branch
        Door window status

    IsChildLockActive: sensor
        Is door child lock engaged. True = Engaged. False = Disengaged.

    Shade: branch
        Side window shade

    """

    def __init__(self, name, parent):
        """Create a new Door model."""
        super().__init__(parent)
        self.name = name

        self.IsOpen = DataPointBoolean("IsOpen", self)
        self.IsLocked = DataPointBoolean("IsLocked", self)
        self.Window = Window("Window", self)
        self.IsChildLockActive = DataPointBoolean("IsChildLockActive", self)
        self.Shade = Shade("Shade", self)
