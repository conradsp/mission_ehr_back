#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/NamingSystem) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class NamingSystem(domainresource.DomainResource):
    """ System of unique identification.

    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """

    resource_type = "NamingSystem"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.name = None
        """ Name for this naming system (computer friendly).
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.kind = None
        """ codesystem | identifier | root.
        Type `str`. """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.responsible = None
        """ Who maintains system namespace?.
        Type `str`. """

        self.type = None
        """ e.g. driver,  provider,  patient, bank etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.description = None
        """ Natural language description of the naming system.
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for naming system (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.usage = None
        """ How/where is it used.
        Type `str`. """

        self.uniqueId = None
        """ Unique identifiers used for system.
        List of `NamingSystemUniqueId` items (represented as `dict` in JSON). """

        super(NamingSystem, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(NamingSystem, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("status", "status", PublicationStatus.str, False, None, True),
            ("kind", "kind", NamingSystemType.str, False, None, True),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("responsible", "responsible", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("usage", "usage", str, False, None, False),
            ("uniqueId", "uniqueId", NamingSystemUniqueId, True, None, True),
        ])
        return js


from . import backboneelement

class NamingSystemUniqueId(backboneelement.BackboneElement):
    """ Unique identifiers used for system.

    Indicates how the system may be identified when referenced in electronic
    exchange.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ oid | uuid | uri | other.
        Type `str`. """

        self.value = None
        """ The unique identifier.
        Type `str`. """

        self.preferred = None
        """ Is this the id that should be used for this type.
        Type `bool`. """

        self.comment = None
        """ Notes about identifier usage.
        Type `str`. """

        self.period = None
        """ When is identifier valid?.
        Type `Period` (represented as `dict` in JSON). """

        super(NamingSystemUniqueId, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(NamingSystemUniqueId, self).elementProperties()
        js.extend([
            ("type", "type", NamingSystemIdentifierType.str, False, None, True),
            ("value", "value", str, False, None, True),
            ("preferred", "preferred", bool, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


import sys
try:
    from . import NamingSystemIdentifierType
except ImportError:
    NamingSystemIdentifierType = sys.modules[__package__ + '.NamingSystemIdentifierType']
try:
    from . import NamingSystemType
except ImportError:
    NamingSystemType = sys.modules[__package__ + '.NamingSystemType']
try:
    from . import PublicationStatus
except ImportError:
    PublicationStatus = sys.modules[__package__ + '.PublicationStatus']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']