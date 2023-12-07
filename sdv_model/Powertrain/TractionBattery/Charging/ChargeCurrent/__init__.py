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

"""ChargeCurrent model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointFloat, Model


class ChargeCurrent(Model):
    """ChargeCurrent model.

    Attributes
    ----------
    DC: sensor
        Current DC charging current at inlet. Negative if returning energy to grid.

        Unit: A
    Phase1: sensor
        Current AC charging current (rms) at inlet for Phase 1. Negative if returning energy to grid.

        Unit: A
    Phase2: sensor
        Current AC charging current (rms) at inlet for Phase 2. Negative if returning energy to grid.

        Unit: A
    Phase3: sensor
        Current AC charging current (rms) at inlet for Phase 3. Negative if returning energy to grid.

        Unit: A
    """

    def __init__(self, name, parent):
        """Create a new ChargeCurrent model."""
        super().__init__(parent)
        self.name = name

        self.DC = DataPointFloat("DC", self)
        self.Phase1 = DataPointFloat("Phase1", self)
        self.Phase2 = DataPointFloat("Phase2", self)
        self.Phase3 = DataPointFloat("Phase3", self)
