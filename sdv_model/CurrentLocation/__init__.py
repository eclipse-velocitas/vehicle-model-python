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

"""CurrentLocation model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointDouble, DataPointString, Model

from sdv_model.CurrentLocation.GNSSReceiver import GNSSReceiver


class CurrentLocation(Model):
    """CurrentLocation model.

    Attributes
    ----------
    Timestamp: sensor
        Timestamp from GNSS system for current location, formatted according to ISO 8601 with UTC time zone.

    Latitude: sensor
        Current latitude of vehicle in WGS 84 geodetic coordinates, as measured at the position of GNSS receiver antenna.

        Value range: [-90, 90]
        Unit: degrees
    Longitude: sensor
        Current longitude of vehicle in WGS 84 geodetic coordinates, as measured at the position of GNSS receiver antenna.

        Value range: [-180, 180]
        Unit: degrees
    Heading: sensor
        Current heading relative to geographic north. 0 = North, 90 = East, 180 = South, 270 = West.

        Value range: [0, 360]
        Unit: degrees
    HorizontalAccuracy: sensor
        Accuracy of the latitude and longitude coordinates.

        Unit: m
    Altitude: sensor
        Current altitude relative to WGS 84 reference ellipsoid, as measured at the position of GNSS receiver antenna.

        Unit: m
    VerticalAccuracy: sensor
        Accuracy of altitude.

        Unit: m
    GNSSReceiver: branch
        Information on the GNSS receiver used for determining current location.

    """

    def __init__(self, name, parent):
        """Create a new CurrentLocation model."""
        super().__init__(parent)
        self.name = name

        self.Timestamp = DataPointString("Timestamp", self)
        self.Latitude = DataPointDouble("Latitude", self)
        self.Longitude = DataPointDouble("Longitude", self)
        self.Heading = DataPointDouble("Heading", self)
        self.HorizontalAccuracy = DataPointDouble("HorizontalAccuracy", self)
        self.Altitude = DataPointDouble("Altitude", self)
        self.VerticalAccuracy = DataPointDouble("VerticalAccuracy", self)
        self.GNSSReceiver = GNSSReceiver("GNSSReceiver", self)
