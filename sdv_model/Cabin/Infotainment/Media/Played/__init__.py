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

"""Played model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointString, Model


class Played(Model):
    """Played model.

    Attributes
    ----------
    Source: actuator
        Media selected for playback

        Allowed values: UNKNOWN, SIRIUS_XM, AM, FM, DAB, TV, CD, DVD, AUX, USB, DISK, BLUETOOTH, INTERNET, VOICE, BEEP
    Artist: sensor
        Name of artist being played

    Album: sensor
        Name of album being played

    Track: sensor
        Name of track being played

    URI: sensor
        User Resource associated with the media

    """

    def __init__(self, name, parent):
        """Create a new Played model."""
        super().__init__(parent)
        self.name = name

        self.Source = DataPointString("Source", self)
        self.Artist = DataPointString("Artist", self)
        self.Album = DataPointString("Album", self)
        self.Track = DataPointString("Track", self)
        self.URI = DataPointString("URI", self)
