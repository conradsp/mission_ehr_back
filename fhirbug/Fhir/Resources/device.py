#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Device) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class Device(domainresource.DomainResource):
    """ Item used in healthcare.

    A type of a manufactured item that is used in the provision of healthcare
    without being substantially changed through that activity. The device may
    be a medical or non-medical device.
    """

    resource_type = "Device"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Instance identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.definition = None
        """ The reference to the definition for the device.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.udiCarrier = None
        """ Unique Device Identifier (UDI) Barcode string.
        List of `DeviceUdiCarrier` items (represented as `dict` in JSON). """

        self.status = None
        """ active | inactive | entered-in-error | unknown.
        Type `str`. """

        self.statusReason = None
        """ online | paused | standby | offline | not-ready | transduc-discon |
        hw-discon | off.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.distinctIdentifier = None
        """ The distinct identification string.
        Type `str`. """

        self.manufacturer = None
        """ Name of device manufacturer.
        Type `str`. """

        self.manufactureDate = None
        """ Date when the device was made.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.expirationDate = None
        """ Date and time of expiry of this device (if applicable).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.lotNumber = None
        """ Lot number of manufacture.
        Type `str`. """

        self.serialNumber = None
        """ Serial number assigned by the manufacturer.
        Type `str`. """

        self.deviceName = None
        """ The name of the device as given by the manufacturer.
        List of `DeviceDeviceName` items (represented as `dict` in JSON). """

        self.modelNumber = None
        """ The manufacturer's model number for the device.
        Type `str`. """

        self.partNumber = None
        """ The part number or catalog number of the device.
        Type `str`. """

        self.type = None
        """ The kind or type of device.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.specialization = None
        """ The capabilities supported on a  device, the standards to which the
        device conforms for a particular purpose, and used for the
        communication.
        List of `DeviceSpecialization` items (represented as `dict` in JSON). """

        self.version = None
        """ The actual design of the device or software version running on the
        device.
        List of `DeviceVersion` items (represented as `dict` in JSON). """

        self.property = None
        """ The actual configuration settings of a device as it actually
        operates, e.g., regulation status, time properties.
        List of `DeviceProperty` items (represented as `dict` in JSON). """

        self.patient = None
        """ Patient to whom Device is affixed.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.owner = None
        """ Organization responsible for device.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.contact = None
        """ Details for human/organization for support.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        self.location = None
        """ Where the device is found.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.url = None
        """ Network address to contact device.
        Type `str`. """

        self.note = None
        """ Device notes and comments.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.safety = None
        """ Safety Characteristics of Device.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.parent = None
        """ The device that this device is attached to or is part of.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(Device, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Device, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("definition", "definition", fhirreference.FHIRReference, False, None, False),
            ("udiCarrier", "udiCarrier", DeviceUdiCarrier, True, None, False),
            ("status", "status", FHIRDeviceStatus.str, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False),
            ("distinctIdentifier", "distinctIdentifier", str, False, None, False),
            ("manufacturer", "manufacturer", str, False, None, False),
            ("manufactureDate", "manufactureDate", fhirdate.FHIRDate, False, None, False),
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("serialNumber", "serialNumber", str, False, None, False),
            ("deviceName", "deviceName", DeviceDeviceName, True, None, False),
            ("modelNumber", "modelNumber", str, False, None, False),
            ("partNumber", "partNumber", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("specialization", "specialization", DeviceSpecialization, True, None, False),
            ("version", "version", DeviceVersion, True, None, False),
            ("property", "property", DeviceProperty, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("url", "url", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("safety", "safety", codeableconcept.CodeableConcept, True, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class DeviceDeviceName(backboneelement.BackboneElement):
    """ The name of the device as given by the manufacturer.

    This represents the manufacturer's name of the device as provided by the
    device, from a UDI label, or by a person describing the Device.  This
    typically would be used when a person provides the name(s) or when the
    device represents one of the names available from DeviceDefinition.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.name = None
        """ The name that identifies the device.
        Type `str`. """

        self.type = None
        """ udi-label-name | user-friendly-name | patient-reported-name |
        manufacturer-name | model-name | other.
        Type `str`. """

        super(DeviceDeviceName, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(DeviceDeviceName, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("type", "type", DeviceNameType.str, False, None, True),
        ])
        return js


class DeviceProperty(backboneelement.BackboneElement):
    """ The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ Code that specifies the property DeviceDefinitionPropetyCode
        (Extensible).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueQuantity = None
        """ Property value as a quantity.
        List of `Quantity` items (represented as `dict` in JSON). """

        self.valueCode = None
        """ Property value as a code, e.g., NTP4 (synced to NTP).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(DeviceProperty, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(DeviceProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, True, None, False),
            ("valueCode", "valueCode", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class DeviceSpecialization(backboneelement.BackboneElement):
    """ The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.systemType = None
        """ The standard that is used to operate and communicate.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.version = None
        """ The version of the standard that is used to operate and communicate.
        Type `str`. """

        super(DeviceSpecialization, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(DeviceSpecialization, self).elementProperties()
        js.extend([
            ("systemType", "systemType", codeableconcept.CodeableConcept, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


class DeviceUdiCarrier(backboneelement.BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.

    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.deviceIdentifier = None
        """ Mandatory fixed portion of UDI.
        Type `str`. """

        self.issuer = None
        """ UDI Issuing Organization.
        Type `str`. """

        self.jurisdiction = None
        """ Regional UDI authority.
        Type `str`. """

        self.carrierAIDC = None
        """ UDI Machine Readable Barcode String.
        Type `str`. """

        self.carrierHRF = None
        """ UDI Human Readable Barcode String.
        Type `str`. """

        self.entryType = None
        """ barcode | rfid | manual +.
        Type `str`. """

        super(DeviceUdiCarrier, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(DeviceUdiCarrier, self).elementProperties()
        js.extend([
            ("deviceIdentifier", "deviceIdentifier", str, False, None, False),
            ("issuer", "issuer", str, False, None, False),
            ("jurisdiction", "jurisdiction", str, False, None, False),
            ("carrierAIDC", "carrierAIDC", str, False, None, False),
            ("carrierHRF", "carrierHRF", str, False, None, False),
            ("entryType", "entryType", UDIEntryType.str, False, None, False),
        ])
        return js


class DeviceVersion(backboneelement.BackboneElement):
    """ The actual design of the device or software version running on the device.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ The type of the device version, e.g. manufacturer, approved,
        internal.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.component = None
        """ A single component of the device version.
        Type `Identifier` (represented as `dict` in JSON). """

        self.value = None
        """ The version text.
        Type `str`. """

        super(DeviceVersion, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(DeviceVersion, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("component", "component", identifier.Identifier, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


import sys
try:
    from . import DeviceNameType
except ImportError:
    DeviceNameType = sys.modules[__package__ + '.DeviceNameType']
try:
    from . import FHIRDeviceStatus
except ImportError:
    FHIRDeviceStatus = sys.modules[__package__ + '.FHIRDeviceStatus']
try:
    from . import UDIEntryType
except ImportError:
    UDIEntryType = sys.modules[__package__ + '.UDIEntryType']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']