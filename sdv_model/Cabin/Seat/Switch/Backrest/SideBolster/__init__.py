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


"""SideBolster model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    Model,
)


class SideBolster(Model):
    """SideBolster model.

    Attributes
    ----------
    IsMoreSupportEngaged: actuator
        Is switch for more side bolster support engaged (SingleSeat.Backrest.SideBolster.Support).

    IsLessSupportEngaged: actuator
        Is switch for less side bolster support engaged (SingleSeat.Backrest.SideBolster.Support).

    """

    def __init__(self, parent):
        """Create a new SideBolster model."""
        super().__init__(parent)

        self.IsMoreSupportEngaged = DataPointBoolean(
            "IsMoreSupportEngaged", self)
        self.IsLessSupportEngaged = DataPointBoolean(
            "IsLessSupportEngaged", self)
