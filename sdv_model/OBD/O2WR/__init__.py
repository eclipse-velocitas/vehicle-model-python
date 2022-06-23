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

"""O2WR model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    Model,
)


class O2WR(Model):
    """O2WR model.

    Attributes
    ----------
    Lambda: sensor
        PID 2x (byte AB) and PID 3x (byte AB) - Lambda for wide range/band oxygen sensor

    Voltage: sensor
        PID 2x (byte CD) - Voltage for wide range/band oxygen sensor

        Unit: V
    Current: sensor
        PID 3x (byte CD) - Current for wide range/band oxygen sensor

        Unit: A
    """

    def __init__(self, parent):
        """Create a new O2WR model."""
        super().__init__(parent)

        self.Lambda = DataPointFloat("Lambda", self)
        self.Voltage = DataPointFloat("Voltage", self)
        self.Current = DataPointFloat("Current", self)
