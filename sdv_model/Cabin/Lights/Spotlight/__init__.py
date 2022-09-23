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

"""Spotlight model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointBoolean, Model


class Spotlight(Model):
    """Spotlight model.

    Attributes
    ----------
    IsSharedOn: sensor
        Is a shared light across a specific row on

    IsLeftOn: actuator
        Is light on the left side switched on

    IsRightOn: actuator
        Is light on the right side switched on

    """

    def __init__(self, name, parent):
        """Create a new Spotlight model."""
        super().__init__(parent)
        self.name = name

        self.IsSharedOn = DataPointBoolean("IsSharedOn", self)
        self.IsLeftOn = DataPointBoolean("IsLeftOn", self)
        self.IsRightOn = DataPointBoolean("IsRightOn", self)
