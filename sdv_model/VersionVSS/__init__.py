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

"""VersionVSS model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import DataPointString, DataPointUint32, Model


class VersionVSS(Model):
    """VersionVSS model.

    Attributes
    ----------
    Major: attribute (uint32)
        Supported Version of VSS - Major version.

    Minor: attribute (uint32)
        Supported Version of VSS - Minor version.

    Patch: attribute (uint32)
        Supported Version of VSS - Patch version.

    Label: attribute (string)
        Label to further describe the version.

    """

    def __init__(self, name, parent):
        """Create a new VersionVSS model."""
        super().__init__(parent)
        self.name = name

        self.Major = DataPointUint32("Major", self)
        self.Minor = DataPointUint32("Minor", self)
        self.Patch = DataPointUint32("Patch", self)
        self.Label = DataPointString("Label", self)
