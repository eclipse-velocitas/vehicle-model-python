#!/usr/bin/env python3

"""Wiping model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointString,
    DataPointUint8,
    Model,
)

from sdv_model.Body.Windshield.Wiping.System import System


class Wiping(Model):
    """Wiping model.

    Attributes
    ----------
    Mode: actuator
        Wiper mode requested by user/driver. INTERVAL indicates intermittent wiping, with fixed time interval between each wipe. RAIN_SENSOR indicates intermittent wiping based on rain intensity.

        Allowed values: OFF, SLOW, MEDIUM, FAST, INTERVAL, RAIN_SENSOR
    Intensity: actuator
        Relative intensity/sensitivity for interval and rain sensor mode as requested by user/driver. Has no significance if Windshield.Wiping.Mode is OFF/SLOW/MEDIUM/FAST 0 - wipers inactive. 1 - minimum intensity (lowest frequency/sensitivity, longest interval). 2/3/4/... - higher intensity (higher frequency/sensitivity, shorter interval). Maximum value supported is vehicle specific.

    System: branch
        Signals to control behavior of wipers in detail. By default VSS expects only one instance.

        These signals are typically not directly available to the user/driver of the vehicle. The overlay in overlays/extensions/dual_wiper_systems.vspec can be used to modify this branch to support two instances; Primary and Secondary.

    WiperWear: sensor
        Wiper wear as percent. 0 = No Wear. 100 = Worn. Replacement required. Method for calculating or estimating wiper wear is vehicle specific. For windshields with multiple wipers the wear reported shall correspond to the most worn wiper.

        Value range: [, 100]
    IsWipersWorn: sensor
        Wiper wear status. True = Worn, Replacement recommended or required. False = Not Worn.

    """

    def __init__(self, parent):
        """Create a new Wiping model."""
        super().__init__(parent)

        self.Mode = DataPointString("Mode", self)
        self.Intensity = DataPointUint8("Intensity", self)
        self.System = System(self)
        self.WiperWear = DataPointUint8("WiperWear", self)
        self.IsWipersWorn = DataPointBoolean("IsWipersWorn", self)
