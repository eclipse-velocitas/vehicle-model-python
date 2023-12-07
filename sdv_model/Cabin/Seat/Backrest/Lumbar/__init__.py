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

"""Lumbar model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointFloat, DataPointUint8, Model


class Lumbar(Model):
    """Lumbar model.

    Attributes
    ----------
    Support: actuator
        Lumbar support (in/out position). 0 = Innermost position. 100 = Outermost position.

        Value range: [0, 100]
        Unit: percent
    Height: actuator
        Height of lumbar support. Position is relative within available movable range of the lumbar support. 0 = Lowermost position supported.

        Value range: [0, ]
        Unit: mm
    """

    def __init__(self, name, parent):
        """Create a new Lumbar model."""
        super().__init__(parent)
        self.name = name

        self.Support = DataPointFloat("Support", self)
        self.Height = DataPointUint8("Height", self)
