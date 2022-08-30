#!/usr/bin/env python3

"""VehicleIdentification model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointString,
    DataPointUint16,
    Model,
)


class VehicleIdentification(Model):
    """VehicleIdentification model.

    Attributes
    ----------
    VIN: attribute (string)
        17-character Vehicle Identification Number (VIN) as defined by ISO 3779.

    WMI: attribute (string)
        3-character World Manufacturer Identification (WMI) as defined by ISO 3780.

    Brand: attribute (string)
        Vehicle brand or manufacturer.

    Model: attribute (string)
        Vehicle model.

    Year: attribute (uint16)
        Model year of the vehicle.

    AcrissCode: attribute (string)
        The ACRISS Car Classification Code is a code used by many car rental companies.

    BodyType: attribute (string)
        Indicates the design and body style of the vehicle (e.g. station wagon, hatchback, etc.).

    DateVehicleFirstRegistered: attribute (string)
        The date in ISO 8601 format of the first registration of the vehicle with the respective public authorities.

    MeetsEmissionStandard: attribute (string)
        Indicates that the vehicle meets the respective emission standard.

    ProductionDate: attribute (string)
        The date in ISO 8601 format of production of the item, e.g. vehicle.

    PurchaseDate: attribute (string)
        The date in ISO 8601 format of the item e.g. vehicle was purchased by the current owner.

    VehicleModelDate: attribute (string)
        The release date in ISO 8601 format of a vehicle model (often used to differentiate versions of the same make and model).

    VehicleConfiguration: attribute (string)
        A short text indicating the configuration of the vehicle, e.g. '5dr hatchback ST 2.5 MT 225 hp' or 'limited edition'.

    VehicleSeatingCapacity: attribute (uint16)
        The number of passengers that can be seated in the vehicle, both in terms of the physical space available, and in terms of limitations set by law.

    VehicleSpecialUsage: attribute (string)
        Indicates whether the vehicle has been used for special purposes, like commercial rental, driving school.

    VehicleInteriorColor: attribute (string)
        The color or color combination of the interior of the vehicle.

    VehicleInteriorType: attribute (string)
        The type or material of the interior of the vehicle (e.g. synthetic fabric, leather, wood, etc.).

    KnownVehicleDamages: attribute (string)
        A textual description of known damages, both repaired and unrepaired.

    """

    def __init__(self, parent):
        """Create a new VehicleIdentification model."""
        super().__init__(parent)

        self.VIN = DataPointString("VIN", self)
        self.WMI = DataPointString("WMI", self)
        self.Brand = DataPointString("Brand", self)
        self.Model = DataPointString("Model", self)
        self.Year = DataPointUint16("Year", self)
        self.AcrissCode = DataPointString("AcrissCode", self)
        self.BodyType = DataPointString("BodyType", self)
        self.DateVehicleFirstRegistered = DataPointString("DateVehicleFirstRegistered", self)
        self.MeetsEmissionStandard = DataPointString("MeetsEmissionStandard", self)
        self.ProductionDate = DataPointString("ProductionDate", self)
        self.PurchaseDate = DataPointString("PurchaseDate", self)
        self.VehicleModelDate = DataPointString("VehicleModelDate", self)
        self.VehicleConfiguration = DataPointString("VehicleConfiguration", self)
        self.VehicleSeatingCapacity = DataPointUint16("VehicleSeatingCapacity", self)
        self.VehicleSpecialUsage = DataPointString("VehicleSpecialUsage", self)
        self.VehicleInteriorColor = DataPointString("VehicleInteriorColor", self)
        self.VehicleInteriorType = DataPointString("VehicleInteriorType", self)
        self.KnownVehicleDamages = DataPointString("KnownVehicleDamages", self)
