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

"""Media model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointString, DataPointUint8, Model

from sdv_model.Cabin.Infotainment.Media.Played import Played


class Media(Model):
    """Media model.

    Attributes
    ----------
    Action: actuator
        Tells if the media was

        Allowed values: UNKNOWN, STOP, PLAY, FAST_FORWARD, FAST_BACKWARD, SKIP_FORWARD, SKIP_BACKWARD
    Played: branch
        Collection of signals updated in concert when a new media is played

    DeclinedURI: sensor
        URI of suggested media that was declined

    SelectedURI: actuator
        URI of suggested media that was selected

    Volume: actuator
        Current Media Volume

        Value range: [0, 100]
    """

    def __init__(self, name, parent):
        """Create a new Media model."""
        super().__init__(parent)
        self.name = name

        self.Action = DataPointString("Action", self)
        self.Played = Played("Played", self)
        self.DeclinedURI = DataPointString("DeclinedURI", self)
        self.SelectedURI = DataPointString("SelectedURI", self)
        self.Volume = DataPointUint8("Volume", self)
