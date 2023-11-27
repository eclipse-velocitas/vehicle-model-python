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

"""Lights model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointBoolean, Model


class Lights(Model):
    """Lights model.

    Attributes
    ----------
    IsHighBeamOn: actuator
        Is high beam on?

    IsLowBeamOn: actuator
        Is low beam on?

    IsRunningOn: actuator
        Are running lights on?

    IsBackupOn: actuator
        Is backup (reverse) light on?

    IsParkingOn: actuator
        Is parking light on?

    IsBrakeOn: actuator
        Is brake light on?

    IsRearFogOn: actuator
        Is rear fog light on?

    IsFrontFogOn: actuator
        Is front fog light on?

    IsHazardOn: actuator
        Are hazards on?

    IsLeftIndicatorOn: actuator
        Is left indicator flashing?

    IsRightIndicatorOn: actuator
        Is right indicator flashing?

    """

    def __init__(self, name, parent):
        """Create a new Lights model."""
        super().__init__(parent)
        self.name = name

        self.IsHighBeamOn = DataPointBoolean("IsHighBeamOn", self)
        self.IsLowBeamOn = DataPointBoolean("IsLowBeamOn", self)
        self.IsRunningOn = DataPointBoolean("IsRunningOn", self)
        self.IsBackupOn = DataPointBoolean("IsBackupOn", self)
        self.IsParkingOn = DataPointBoolean("IsParkingOn", self)
        self.IsBrakeOn = DataPointBoolean("IsBrakeOn", self)
        self.IsRearFogOn = DataPointBoolean("IsRearFogOn", self)
        self.IsFrontFogOn = DataPointBoolean("IsFrontFogOn", self)
        self.IsHazardOn = DataPointBoolean("IsHazardOn", self)
        self.IsLeftIndicatorOn = DataPointBoolean("IsLeftIndicatorOn", self)
        self.IsRightIndicatorOn = DataPointBoolean("IsRightIndicatorOn", self)
