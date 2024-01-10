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

"""Bank1 model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointFloat, Model


class Bank1(Model):
    """Bank1 model.

    Attributes
    ----------
    Temperature1: sensor
        PID 3C - Catalyst temperature from bank 1, sensor 1

        Unit: celsius
    Temperature2: sensor
        PID 3E - Catalyst temperature from bank 1, sensor 2

        Unit: celsius
    """

    def __init__(self, name, parent):
        """Create a new Bank1 model."""
        super().__init__(parent)
        self.name = name

        self.Temperature1 = DataPointFloat("Temperature1", self)
        self.Temperature2 = DataPointFloat("Temperature2", self)
