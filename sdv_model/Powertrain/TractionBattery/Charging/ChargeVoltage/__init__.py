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

"""ChargeVoltage model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointFloat, Model


class ChargeVoltage(Model):
    """ChargeVoltage model.

    Attributes
    ----------
    DC: sensor
        Current DC charging voltage at charging inlet.

        Unit: V
    Phase1: sensor
        Current AC charging voltage (rms) at inlet for Phase 1.

        Unit: V
    Phase2: sensor
        Current AC charging voltage (rms) at inlet for Phase 2.

        Unit: V
    Phase3: sensor
        Current AC charging voltage (rms) at inlet for Phase 3.

        Unit: V
    """

    def __init__(self, name, parent):
        """Create a new ChargeVoltage model."""
        super().__init__(parent)
        self.name = name

        self.DC = DataPointFloat("DC", self)
        self.Phase1 = DataPointFloat("Phase1", self)
        self.Phase2 = DataPointFloat("Phase2", self)
        self.Phase3 = DataPointFloat("Phase3", self)
