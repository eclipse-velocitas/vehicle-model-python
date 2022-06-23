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

"""Station model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointInt8,
    DataPointString,
    DataPointUint8,
    Model,
)


class Station(Model):
    """Station model.

    Attributes
    ----------
    FanSpeed: actuator
        Fan Speed, 0 = off. 100 = max

        Value range: [0, 100]
        Unit: percent
    Temperature: actuator
        Temperature

        Unit: celsius
    AirDistribution: actuator
        Direction of airstream

        Allowed values: UP, MIDDLE, DOWN
    """

    def __init__(self, parent):
        """Create a new Station model."""
        super().__init__(parent)

        self.FanSpeed = DataPointUint8("FanSpeed", self)
        self.Temperature = DataPointInt8("Temperature", self)
        self.AirDistribution = DataPointString("AirDistribution", self)
