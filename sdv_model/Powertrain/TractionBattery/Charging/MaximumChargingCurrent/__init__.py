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

"""MaximumChargingCurrent model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointFloat, Model


class MaximumChargingCurrent(Model):
    """MaximumChargingCurrent model.

    Attributes
    ----------
    DC: sensor
        Maximum DC charging current at inlet that can be accepted by the system.

        Unit: A
    Phase1: sensor
        Maximum AC charging current (rms) at inlet for Phase 1 that can be accepted by the system.

        Unit: A
    Phase2: sensor
        Maximum AC charging current (rms) at inlet for Phase 2 that can be accepted by the system.

        Unit: A
    Phase3: sensor
        Maximum AC charging current (rms) at inlet for Phase 3 that can be accepted by the system.

        Unit: A
    """

    def __init__(self, name, parent):
        """Create a new MaximumChargingCurrent model."""
        super().__init__(parent)
        self.name = name

        self.DC = DataPointFloat("DC", self)
        self.Phase1 = DataPointFloat("Phase1", self)
        self.Phase2 = DataPointFloat("Phase2", self)
        self.Phase3 = DataPointFloat("Phase3", self)
