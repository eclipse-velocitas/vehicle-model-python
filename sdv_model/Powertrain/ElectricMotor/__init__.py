#!/usr/bin/env python3

"""ElectricMotor model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointInt16,
    DataPointInt32,
    DataPointString,
    DataPointUint16,
    Model,
)


class ElectricMotor(Model):
    """ElectricMotor model.

    Attributes
    ----------
    EngineCode: attribute (string)
        Engine code designation, as specified by vehicle manufacturer.

    MaxPower: attribute (uint16)
        Peak power, in kilowatts, that motor(s) can generate.

        Unit: kW
    MaxTorque: attribute (uint16)
        Peak power, in newton meter, that the motor(s) can generate.

        Unit: Nm
    MaxRegenPower: attribute (uint16)
        Peak regen/brake power, in kilowatts, that motor(s) can generate.

        Unit: kW
    MaxRegenTorque: attribute (uint16)
        Peak regen/brake torque, in newton meter, that the motor(s) can generate.

        Unit: Nm
    Speed: sensor
        Motor rotational speed measured as rotations per minute. Negative values indicate reverse driving mode.

        Unit: rpm
    Temperature: sensor
        Motor temperature.

        Unit: celsius
    CoolantTemperature: sensor
        Motor coolant temperature (if applicable).

        Unit: celsius
    Power: sensor
        Current motor power output. Negative values indicate regen mode.

        Unit: kW
    Torque: sensor
        Current motor torque. Negative values indicate regen mode.

        Unit: Nm
    """

    def __init__(self, parent):
        """Create a new ElectricMotor model."""
        super().__init__(parent)

        self.EngineCode = DataPointString("EngineCode", self)
        self.MaxPower = DataPointUint16("MaxPower", self)
        self.MaxTorque = DataPointUint16("MaxTorque", self)
        self.MaxRegenPower = DataPointUint16("MaxRegenPower", self)
        self.MaxRegenTorque = DataPointUint16("MaxRegenTorque", self)
        self.Speed = DataPointInt32("Speed", self)
        self.Temperature = DataPointInt16("Temperature", self)
        self.CoolantTemperature = DataPointInt16("CoolantTemperature", self)
        self.Power = DataPointInt16("Power", self)
        self.Torque = DataPointInt16("Torque", self)
