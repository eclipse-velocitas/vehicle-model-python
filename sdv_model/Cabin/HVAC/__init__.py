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

"""HVAC model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointBoolean, DataPointFloat, Model

from sdv_model.Cabin.HVAC.Station import Station


class HVAC(Model):
    """HVAC model.

    Attributes
    ----------
    Station: branch
        HVAC for single station in the vehicle

    IsRecirculationActive: actuator
        Is recirculation active.

    IsFrontDefrosterActive: actuator
        Is front defroster active.

    IsRearDefrosterActive: actuator
        Is rear defroster active.

    IsAirConditioningActive: actuator
        Is Air conditioning active.

    AmbientAirTemperature: sensor
        Ambient air temperature inside the vehicle.

        Unit: celsius
    """

    def __init__(self, name, parent):
        """Create a new HVAC model."""
        super().__init__(parent)
        self.name = name

        self.Station = StationCollection("Station", self)
        self.IsRecirculationActive = DataPointBoolean("IsRecirculationActive", self)
        self.IsFrontDefrosterActive = DataPointBoolean("IsFrontDefrosterActive", self)
        self.IsRearDefrosterActive = DataPointBoolean("IsRearDefrosterActive", self)
        self.IsAirConditioningActive = DataPointBoolean("IsAirConditioningActive", self)
        self.AmbientAirTemperature = DataPointFloat("AmbientAirTemperature", self)


class StationCollection(Model):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.Row1 = self.StationType("Row1", self)
        self.Row2 = self.StationType("Row2", self)
        self.Row3 = self.StationType("Row3", self)
        self.Row4 = self.StationType("Row4", self)

    def Row(self, index: int):
        if index < 1 or index > 4:
            raise IndexError(f"Index {index} is out of range")
        _options = {
            1: self.Row1,
            2: self.Row2,
            3: self.Row3,
            4: self.Row4,
        }
        return _options.get(index)

    class StationType(Model):
        def __init__(self, name, parent):
            super().__init__(parent)
            self.name = name
            self.Left = Station("Left", self)
            self.Right = Station("Right", self)

        def element(self, index: int):
            if index < 1 or index > 2:
                raise IndexError(f"Index {index} is out of range")
            _options = {
                1: self.Left,
                2: self.Right,
            }
            return _options.get(index)
