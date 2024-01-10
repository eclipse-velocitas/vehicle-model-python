#!/usr/bin/env python3

# Copyright (c) 2022-2024 Contributors to the Eclipse Foundation
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

"""Infotainment model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import Model

from sdv_model.Cabin.Infotainment.HMI import HMI
from sdv_model.Cabin.Infotainment.Media import Media
from sdv_model.Cabin.Infotainment.Navigation import Navigation


class Infotainment(Model):
    """Infotainment model.

    Attributes
    ----------
    Media: branch
        All Media actions

    Navigation: branch
        All navigation actions

    HMI: branch
        HMI related signals

    """

    def __init__(self, name, parent):
        """Create a new Infotainment model."""
        super().__init__(parent)
        self.name = name

        self.Media = Media("Media", self)
        self.Navigation = Navigation("Navigation", self)
        self.HMI = HMI("HMI", self)
