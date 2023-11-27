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

"""Windshield model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointBoolean, Model

from sdv_model.Body.Windshield.WasherFluid import WasherFluid
from sdv_model.Body.Windshield.Wiping import Wiping


class Windshield(Model):
    """Windshield model.

    Attributes
    ----------
    Wiping: branch
        Windshield wiper signals.

    IsHeatingOn: actuator
        Windshield heater status. False - off, True - on.

    WasherFluid: branch
        Windshield washer fluid signals

    """

    def __init__(self, name, parent):
        """Create a new Windshield model."""
        super().__init__(parent)
        self.name = name

        self.Wiping = Wiping("Wiping", self)
        self.IsHeatingOn = DataPointBoolean("IsHeatingOn", self)
        self.WasherFluid = WasherFluid("WasherFluid", self)
