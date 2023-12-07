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

"""Status model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointBoolean, DataPointString, DataPointUint8, Model


class Status(Model):
    """Status model.

    Attributes
    ----------
    IsMILOn: sensor
        Malfunction Indicator Light (MIL) False = Off, True = On

    DTCCount: sensor
        Number of sensor Trouble Codes (DTC)

    IgnitionType: sensor
        Type of the ignition for ICE - spark = spark plug ignition, compression = self-igniting (Diesel engines)

        Allowed values: SPARK, COMPRESSION
    """

    def __init__(self, name, parent):
        """Create a new Status model."""
        super().__init__(parent)
        self.name = name

        self.IsMILOn = DataPointBoolean("IsMILOn", self)
        self.DTCCount = DataPointUint8("DTCCount", self)
        self.IgnitionType = DataPointString("IgnitionType", self)
