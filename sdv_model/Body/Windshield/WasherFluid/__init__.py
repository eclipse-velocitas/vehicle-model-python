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

"""WasherFluid model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointBoolean, DataPointUint8, Model


class WasherFluid(Model):
    """WasherFluid model.

    Attributes
    ----------
    IsLevelLow: sensor
        Low level indication for washer fluid. True = Level Low. False = Level OK.

    Level: sensor
        Washer fluid level as a percent. 0 = Empty. 100 = Full.

        Value range: [, 100]
        Unit: percent
    """

    def __init__(self, name, parent):
        """Create a new WasherFluid model."""
        super().__init__(parent)
        self.name = name

        self.IsLevelLow = DataPointBoolean("IsLevelLow", self)
        self.Level = DataPointUint8("Level", self)
