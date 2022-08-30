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


"""GNSSReceiver model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointString,
    Model,
)

from sdv_model.CurrentLocation.GNSSReceiver.MountingPosition import MountingPosition


class GNSSReceiver(Model):
    """GNSSReceiver model.

    Attributes
    ----------
    FixType: sensor
        Fix status of GNSS receiver.

        Allowed values: NONE, TWO_D, TWO_D_SATELLITE_BASED_AUGMENTATION, TWO_D_GROUND_BASED_AUGMENTATION, TWO_D_SATELLITE_AND_GROUND_BASED_AUGMENTATION, THREE_D, THREE_D_SATELLITE_BASED_AUGMENTATION, THREE_D_GROUND_BASED_AUGMENTATION, THREE_D_SATELLITE_AND_GROUND_BASED_AUGMENTATION
    MountingPosition: branch
        Mounting position of GNSS receiver antenna relative to vehicle coordinate system. Axis definitions according to ISO 8855. Origin at center of (first) rear axle.

    """

    def __init__(self, parent):
        """Create a new GNSSReceiver model."""
        super().__init__(parent)

        self.FixType = DataPointString("FixType", self)
        self.MountingPosition = MountingPosition(self)
