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

"""CruiseControl model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointBoolean, DataPointFloat, Model


class CruiseControl(Model):
    """CruiseControl model.

    Attributes
    ----------
    IsEnabled: actuator
        Indicates if cruise control system is enabled (e.g. ready to receive configurations and settings) True = Enabled. False = Disabled.

    IsActive: actuator
        Indicates if cruise control system is active (i.e. actively controls speed). True = Active. False = Inactive.

    SpeedSet: actuator
        Set cruise control speed in kilometers per hour.

        Unit: km/h
    IsError: sensor
        Indicates if cruise control system incurred an error condition. True = Error. False = No Error.

    """

    def __init__(self, name, parent):
        """Create a new CruiseControl model."""
        super().__init__(parent)
        self.name = name

        self.IsEnabled = DataPointBoolean("IsEnabled", self)
        self.IsActive = DataPointBoolean("IsActive", self)
        self.SpeedSet = DataPointFloat("SpeedSet", self)
        self.IsError = DataPointBoolean("IsError", self)
