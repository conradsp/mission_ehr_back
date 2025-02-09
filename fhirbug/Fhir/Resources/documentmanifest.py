#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/DocumentManifest) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class DocumentManifest(domainresource.DomainResource):
    """ A list that defines a set of documents.

    A collection of documents compiled for a purpose together with metadata
    that applies to the collection.
    """

    resource_type = "DocumentManifest"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.masterIdentifier = None
        """ Unique Identifier for the set of documents.
        Type `Identifier` (represented as `dict` in JSON). """

        self.identifier = None
        """ Other identifiers for the manifest.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.status = None
        """ current | superseded | entered-in-error.
        Type `str`. """

        self.type = None
        """ Kind of document set.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.subject = None
        """ The subject of the set of documents.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.created = None
        """ When this document manifest created.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.author = None
        """ Who and/or what authored the DocumentManifest.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.recipient = None
        """ Intended to get notified about this set of documents.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.source = None
        """ The source system/application/software.
        Type `str`. """

        self.description = None
        """ Human-readable description (title).
        Type `str`. """

        self.content = None
        """ Items in manifest.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.related = None
        """ Related things.
        List of `DocumentManifestRelated` items (represented as `dict` in JSON). """

        super(DocumentManifest, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(DocumentManifest, self).elementProperties()
        js.extend([
            ("masterIdentifier", "masterIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", DocumentReferenceStatus.str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("author", "author", fhirreference.FHIRReference, True, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("source", "source", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("content", "content", fhirreference.FHIRReference, True, None, True),
            ("related", "related", DocumentManifestRelated, True, None, False),
        ])
        return js


from . import backboneelement

class DocumentManifestRelated(backboneelement.BackboneElement):
    """ Related things.

    Related identifiers or resources associated with the DocumentManifest.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Identifiers of things that are related.
        Type `Identifier` (represented as `dict` in JSON). """

        self.ref = None
        """ Related Resource.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(DocumentManifestRelated, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(DocumentManifestRelated, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("ref", "ref", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import DocumentReferenceStatus
except ImportError:
    DocumentReferenceStatus = sys.modules[__package__ + '.DocumentReferenceStatus']
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