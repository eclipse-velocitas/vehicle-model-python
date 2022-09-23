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

"""ESC model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointBoolean, Model

from sdv_model.ADAS.ESC.RoadFriction import RoadFriction


class ESC(Model):
    """ESC model.

    Attributes
    ----------
    IsEnabled: actuator
        Indicates if ESC is enabled. True = Enabled. False = Disabled.

    IsError: sensor
        Indicates if ESC incurred an error condition. True = Error. False = No Error.

    IsEngaged: sensor
        Indicates if ESC is currently regulating vehicle stability. True = Engaged. False = Not Engaged.

    IsStrongCrossWindDetected: sensor
        Indicates if the ESC system is detecting strong cross winds. True = Strong cross winds detected. False = No strong cross winds detected.

    RoadFriction: branch
        Road friction values reported by the ESC system.

    """

    def __init__(self, name, parent):
        """Create a new ESC model."""
        super().__init__(parent)
        self.name = name

        self.IsEnabled = DataPointBoolean("IsEnabled", self)
        self.IsError = DataPointBoolean("IsError", self)
        self.IsEngaged = DataPointBoolean("IsEngaged", self)
        self.IsStrongCrossWindDetected = DataPointBoolean(
            "IsStrongCrossWindDetected", self
        )
        self.RoadFriction = RoadFriction("RoadFriction", self)
