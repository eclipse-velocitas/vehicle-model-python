#!/usr/bin/env python3

"""VersionVSS model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointString,
    DataPointUint32,
    Model,
)


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

    def __init__(self, parent):
        """Create a new VersionVSS model."""
        super().__init__(parent)

        self.Major = DataPointUint32("Major", self)
        self.Minor = DataPointUint32("Minor", self)
        self.Patch = DataPointUint32("Patch", self)
        self.Label = DataPointString("Label", self)
