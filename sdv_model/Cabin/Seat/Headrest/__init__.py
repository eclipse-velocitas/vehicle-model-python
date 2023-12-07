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

"""Headrest model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointFloat, DataPointUint8, Model


class Headrest(Model):
    """Headrest model.

    Attributes
    ----------
    Height: actuator
        Position of headrest relative to movable range of the head rest. 0 = Bottommost position supported.

        Value range: [0, ]
        Unit: mm
    Angle: actuator
        Headrest angle, relative to backrest, 0 degrees if parallel to backrest, Positive degrees = tilted forward.

        Unit: degrees
    """

    def __init__(self, name, parent):
        """Create a new Headrest model."""
        super().__init__(parent)
        self.name = name

        self.Height = DataPointUint8("Height", self)
        self.Angle = DataPointFloat("Angle", self)
