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

"""Driver model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointBoolean, DataPointFloat, DataPointUint16, Model

from sdv_model.Driver.Identifier import Identifier


class Driver(Model):
    """Driver model.

    Attributes
    ----------
    Identifier: branch
        Identifier attributes based on OAuth 2.0.

    DistractionLevel: sensor
        Distraction level of the driver will be the level how much the driver is distracted, by multiple factors. E.g. Driving situation, acustical or optical signales inside the cockpit, phone calls.

        Value range: [0, 100]
        Unit: percent
    IsEyesOnRoad: sensor
        Has driver the eyes on road or not?

    AttentiveProbability: sensor
        Probability of attentiveness of the driver.

        Value range: [0, 100]
        Unit: percent
    FatigueLevel: sensor
        Fatigueness level of driver. Evaluated by multiple factors like trip time, behaviour of steering, eye status.

        Value range: [0, 100]
        Unit: percent
    HeartRate: sensor
        Heart rate of the driver.

    """

    def __init__(self, name, parent):
        """Create a new Driver model."""
        super().__init__(parent)
        self.name = name

        self.Identifier = Identifier("Identifier", self)
        self.DistractionLevel = DataPointFloat("DistractionLevel", self)
        self.IsEyesOnRoad = DataPointBoolean("IsEyesOnRoad", self)
        self.AttentiveProbability = DataPointFloat("AttentiveProbability", self)
        self.FatigueLevel = DataPointFloat("FatigueLevel", self)
        self.HeartRate = DataPointUint16("HeartRate", self)
