#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/CatalogEntry) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class CatalogEntry(domainresource.DomainResource):
    """ An entry in a catalog.

    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """

    resource_type = "CatalogEntry"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Unique identifier of the catalog item.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.type = None
        """ The type of item - medication, device, service, protocol or other.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.orderable = None
        """ Whether the entry represents an orderable item.
        Type `bool`. """

        self.referencedItem = None
        """ The item that is being defined.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.additionalIdentifier = None
        """ Any additional identifier(s) for the catalog item, in the same
        granularity or concept.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.classification = None
        """ Classification (category or class) of the item entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.validityPeriod = None
        """ The time period in which this catalog entry is expected to be
        active.
        Type `Period` (represented as `dict` in JSON). """

        self.validTo = None
        """ The date until which this catalog entry is expected to be active.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.lastUpdated = None
        """ When was this catalog last updated.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.additionalCharacteristic = None
        """ Additional characteristics of the catalog entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.additionalClassification = None
        """ Additional classification of the catalog entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.relatedEntry = None
        """ An item that this catalog entry is related to.
        List of `CatalogEntryRelatedEntry` items (represented as `dict` in JSON). """

        super(CatalogEntry, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CatalogEntry, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("orderable", "orderable", bool, False, None, True),
            ("referencedItem", "referencedItem", fhirreference.FHIRReference, False, None, True),
            ("additionalIdentifier", "additionalIdentifier", identifier.Identifier, True, None, False),
            ("classification", "classification", codeableconcept.CodeableConcept, True, None, False),
            ("status", "status", PublicationStatus.str, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
            ("validTo", "validTo", fhirdate.FHIRDate, False, None, False),
            ("lastUpdated", "lastUpdated", fhirdate.FHIRDate, False, None, False),
            ("additionalCharacteristic", "additionalCharacteristic", codeableconcept.CodeableConcept, True, None, False),
            ("additionalClassification", "additionalClassification", codeableconcept.CodeableConcept, True, None, False),
            ("relatedEntry", "relatedEntry", CatalogEntryRelatedEntry, True, None, False),
        ])
        return js


from . import backboneelement

class CatalogEntryRelatedEntry(backboneelement.BackboneElement):
    """ An item that this catalog entry is related to.

    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.relationtype = None
        """ triggers | is-replaced-by.
        Type `str`. """

        self.item = None
        """ The reference to the related item.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(CatalogEntryRelatedEntry, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CatalogEntryRelatedEntry, self).elementProperties()
        js.extend([
            ("relationtype", "relationtype", CatalogEntryRelationType.str, False, None, True),
            ("item", "item", fhirreference.FHIRReference, False, None, True),
        ])
        return js


import sys
try:
    from . import CatalogEntryRelationType
except ImportError:
    CatalogEntryRelationType = sys.modules[__package__ + '.CatalogEntryRelationType']
try:
    from . import PublicationStatus
except ImportError:
    PublicationStatus = sys.modules[__package__ + '.PublicationStatus']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']