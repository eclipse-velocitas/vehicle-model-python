#!/usr/bin/env python3

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
        Exterior lights.

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
