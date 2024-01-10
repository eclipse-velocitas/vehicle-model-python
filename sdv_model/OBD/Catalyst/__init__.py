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

"""Catalyst model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import Model

from sdv_model.OBD.Catalyst.Bank1 import Bank1
from sdv_model.OBD.Catalyst.Bank2 import Bank2


class Catalyst(Model):
    """Catalyst model.

    Attributes
    ----------
    Bank1: branch
        Catalyst bank 1 signals

    Bank2: branch
        Catalyst bank 2 signals

    """

    def __init__(self, name, parent):
        """Create a new Catalyst model."""
        super().__init__(parent)
        self.name = name

        self.Bank1 = Bank1("Bank1", self)
        self.Bank2 = Bank2("Bank2", self)
