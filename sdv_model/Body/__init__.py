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

"""Body model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    DataPointString,
    Dictionary,
    Model,
    ModelCollection,
)

from sdv_model.Body.Hood import Hood
from sdv_model.Body.Horn import Horn
from sdv_model.Body.Lights import Lights
from sdv_model.Body.Mirrors import Mirrors
from sdv_model.Body.Raindetection import Raindetection
from sdv_model.Body.Trunk import Trunk
from sdv_model.Body.Windshield import Windshield


class Body(Model):
    """Body model.

    Attributes
    ----------
    BodyType: attribute (string)
        Body type code as defined by ISO 3779.

    RefuelPosition: attribute (string)
        Location of the fuel cap or charge port.

        Allowed values: FRONT_LEFT, FRONT_RIGHT, MIDDLE_LEFT, MIDDLE_RIGHT, REAR_LEFT, REAR_RIGHT
    Hood: branch
        Hood status.

    Trunk: branch
        Trunk status.

    Horn: branch
        Horn signals.

    Raindetection: branch
        Rainsensor signals.

    Windshield: branch
        Windshield signals.

    Lights: branch
        All lights.

    Mirrors: branch
        All mirrors.

    RearMainSpoilerPosition: actuator
        Rear spoiler position, 0% = Spoiler fully stowed. 100% = Spoiler fully exposed.

        Value range: [0, 100]
        Unit: percent
    """

    def __init__(self, parent):
        """Create a new Body model."""
        super().__init__(parent)

        self.BodyType = DataPointString("BodyType", self)
        self.RefuelPosition = DataPointString("RefuelPosition", self)
        self.Hood = Hood(self)
        self.Trunk = ModelCollection[Trunk]([Dictionary(["Front", "Rear"])], Trunk(self))
        self.Horn = Horn(self)
        self.Raindetection = Raindetection(self)
        self.Windshield = ModelCollection[Windshield]([Dictionary(["Front", "Rear"])], Windshield(self))
        self.Lights = Lights(self)
        self.Mirrors = ModelCollection[Mirrors]([Dictionary(["Left", "Right"])], Mirrors(self))
        self.RearMainSpoilerPosition = DataPointFloat("RearMainSpoilerPosition", self)
