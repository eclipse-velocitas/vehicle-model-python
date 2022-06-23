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

"""Sunroof model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointInt8,
    DataPointString,
    Model,
)

from sdv_model.Cabin.Sunroof.Shade import Shade


class Sunroof(Model):
    """Sunroof model.

    Attributes
    ----------
    Position: sensor
        Sunroof position. 0 = Fully closed 100 = Fully opened. -100 = Fully tilted.

        Value range: [-100, 100]
    Switch: actuator
        Switch controlling sliding action such as window, sunroof, or shade.

        Allowed values: INACTIVE, CLOSE, OPEN, ONE_SHOT_CLOSE, ONE_SHOT_OPEN, TILT_UP, TILT_DOWN
    Shade: branch
        Sun roof shade status.

    """

    def __init__(self, parent):
        """Create a new Sunroof model."""
        super().__init__(parent)

        self.Position = DataPointInt8("Position", self)
        self.Switch = DataPointString("Switch", self)
        self.Shade = Shade(self)
