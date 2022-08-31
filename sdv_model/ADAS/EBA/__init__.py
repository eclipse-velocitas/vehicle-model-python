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


"""EBA model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class EBA(Model):
    """EBA model.

    Attributes
    ----------
    IsEnabled: actuator
        Indicates if EBA is enabled. True = Enabled. False = Disabled.

    IsError: sensor
        Indicates if EBA incurred an error condition. True = Error. False = No Error.

    IsEngaged: sensor
        Indicates if EBA is currently regulating brake pressure. True = Engaged. False = Not Engaged.

    """

    def __init__(self, parent):
        """Create a new EBA model."""
        super().__init__(parent)

        self.IsEnabled = DataPointBoolean("IsEnabled", self)
        self.IsError = DataPointBoolean("IsError", self)
        self.IsEngaged = DataPointBoolean("IsEngaged", self)
