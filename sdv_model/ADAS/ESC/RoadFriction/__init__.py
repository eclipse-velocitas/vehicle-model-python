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

"""RoadFriction model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointFloat, Model


class RoadFriction(Model):
    """RoadFriction model.

    Attributes
    ----------
    MostProbable: sensor
        Most probable road friction, as calculated by the ESC system. Exact meaning of most probable is implementation specific. 0 = no friction, 100 = maximum friction.

        Value range: [0, 100]
        Unit: percent
    LowerBound: sensor
        Lower bound road friction, as calculated by the ESC system. 5% possibility that road friction is below this value. 0 = no friction, 100 = maximum friction.

        Value range: [0, 100]
        Unit: percent
    UpperBound: sensor
        Upper bound road friction, as calculated by the ESC system. 95% possibility that road friction is below this value. 0 = no friction, 100 = maximum friction.

        Value range: [0, 100]
        Unit: percent
    """

    def __init__(self, name, parent):
        """Create a new RoadFriction model."""
        super().__init__(parent)
        self.name = name

        self.MostProbable = DataPointFloat("MostProbable", self)
        self.LowerBound = DataPointFloat("LowerBound", self)
        self.UpperBound = DataPointFloat("UpperBound", self)
