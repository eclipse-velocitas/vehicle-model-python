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

"""Headrest model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointBoolean, Model


class Headrest(Model):
    """Headrest model.

    Attributes
    ----------
    IsUpEngaged: actuator
        Head rest up switch engaged (SingleSeat.Headrest.Height).

    IsDownEngaged: actuator
        Head rest down switch engaged (SingleSeat.Headrest.Height).

    IsForwardEngaged: actuator
        Head rest forward switch engaged (SingleSeat.Headrest.Angle).

    IsBackwardEngaged: actuator
        Head rest backward switch engaged (SingleSeat.Headrest.Angle).

    """

    def __init__(self, name, parent):
        """Create a new Headrest model."""
        super().__init__(parent)
        self.name = name

        self.IsUpEngaged = DataPointBoolean("IsUpEngaged", self)
        self.IsDownEngaged = DataPointBoolean("IsDownEngaged", self)
        self.IsForwardEngaged = DataPointBoolean("IsForwardEngaged", self)
        self.IsBackwardEngaged = DataPointBoolean("IsBackwardEngaged", self)
