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

"""HMI model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointString, Model


class HMI(Model):
    """HMI model.

    Attributes
    ----------
    CurrentLanguage: sensor
        ISO 639-1 standard language code for the current HMI

    DateFormat: actuator
        Date format used in the current HMI

        Allowed values: YYYY_MM_DD, DD_MM_YYYY, MM_DD_YYYY, YY_MM_DD, DD_MM_YY, MM_DD_YY
    TimeFormat: actuator
        Time format used in the current HMI

        Allowed values: HR_12, HR_24
    DistanceUnit: actuator
        Distance unit used in the current HMI

        Allowed values: MILES, KILOMETERS
    FuelEconomyUnits: actuator
        Fuel economy unit used in the current HMI

        Allowed values: MPG_UK, MPG_US, MILES_PER_LITER, KILOMETERS_PER_LITER, LITERS_PER_100_KILOMETERS
    EVEconomyUnits: actuator
        EV fuel economy unit used in the current HMI

        Allowed values: MILES_PER_KILOWATT_HOUR, KILOMETERS_PER_KILOWATT_HOUR, KILOWATT_HOURS_PER_100_MILES, KILOWATT_HOURS_PER_100_KILOMETERS, WATT_HOURS_PER_MILE, WATT_HOURS_PER_KILOMETER
    TemperatureUnit: actuator
        Temperature unit used in the current HMI

        Allowed values: C, F
    DayNightMode: actuator
        Current display theme

        Allowed values: DAY, NIGHT
    """

    def __init__(self, name, parent):
        """Create a new HMI model."""
        super().__init__(parent)
        self.name = name

        self.CurrentLanguage = DataPointString("CurrentLanguage", self)
        self.DateFormat = DataPointString("DateFormat", self)
        self.TimeFormat = DataPointString("TimeFormat", self)
        self.DistanceUnit = DataPointString("DistanceUnit", self)
        self.FuelEconomyUnits = DataPointString("FuelEconomyUnits", self)
        self.EVEconomyUnits = DataPointString("EVEconomyUnits", self)
        self.TemperatureUnit = DataPointString("TemperatureUnit", self)
        self.DayNightMode = DataPointString("DayNightMode", self)
