#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/DocumentReference) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class DocumentReference(domainresource.DomainResource):
    """ A reference to a document.

    A reference to a document of any kind for any purpose. Provides metadata
    about the document so that the document can be discovered and managed. The
    scope of a document is any seralized object with a mime-type, so includes
    formal patient centric documents (CDA), cliical notes, scanned paper, and
    non-patient specific documents like policy text.
    """

    resource_type = "DocumentReference"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.masterIdentifier = None
        """ Master Version Specific Identifier.
        Type `Identifier` (represented as `dict` in JSON). """

        self.identifier = None
        """ Other identifiers for the document.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.status = None
        """ current | superseded | entered-in-error.
        Type `str`. """

        self.docStatus = None
        """ preliminary | final | amended | entered-in-error.
        Type `str`. """

        self.type = None
        """ Kind of document (LOINC if possible).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.category = None
        """ Categorization of document.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.subject = None
        """ Who/what is the subject of the document.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.date = None
        """ When this document reference was created.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.author = None
        """ Who and/or what authored the document.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.authenticator = None
        """ Who/what authenticated the document.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.custodian = None
        """ Organization which maintains the document.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.relatesTo = None
        """ Relationships to other documents.
        List of `DocumentReferenceRelatesTo` items (represented as `dict` in JSON). """

        self.description = None
        """ Human-readable description.
        Type `str`. """

        self.securityLabel = None
        """ Document security-tags.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.content = None
        """ Document referenced.
        List of `DocumentReferenceContent` items (represented as `dict` in JSON). """

        self.context = None
        """ Clinical context of document.
        Type `DocumentReferenceContext` (represented as `dict` in JSON). """

        super(DocumentReference, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(DocumentReference, self).elementProperties()
        js.extend([
            ("masterIdentifier", "masterIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", DocumentReferenceStatus.str, False, None, True),
            ("docStatus", "docStatus", CompositionStatus.str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("author", "author", fhirreference.FHIRReference, True, None, False),
            ("authenticator", "authenticator", fhirreference.FHIRReference, False, None, False),
            ("custodian", "custodian", fhirreference.FHIRReference, False, None, False),
            ("relatesTo", "relatesTo", DocumentReferenceRelatesTo, True, None, False),
            ("description", "description", str, False, None, False),
            ("securityLabel", "securityLabel", codeableconcept.CodeableConcept, True, None, False),
            ("content", "content", DocumentReferenceContent, True, None, True),
            ("context", "context", DocumentReferenceContext, False, None, False),
        ])
        return js


from . import backboneelement

class DocumentReferenceContent(backboneelement.BackboneElement):
    """ Document referenced.

    The document and format referenced. There may be multiple content element
    repetitions, each with a different format.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.attachment = None
        """ Where to access the document.
        Type `Attachment` (represented as `dict` in JSON). """

        self.format = None
        """ Format/content rules for the document.
        Type `Coding` (represented as `dict` in JSON). """

        super(DocumentReferenceContent, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(DocumentReferenceContent, self).elementProperties()
        js.extend([
            ("attachment", "attachment", attachment.Attachment, False, None, True),
            ("format", "format", coding.Coding, False, None, False),
        ])
        return js


class DocumentReferenceContext(backboneelement.BackboneElement):
    """ Clinical context of document.

    The clinical context in which the document was prepared.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.encounter = None
        """ Context of the document  content.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.event = None
        """ Main clinical acts documented.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.period = None
        """ Time of service that is being documented.
        Type `Period` (represented as `dict` in JSON). """

        self.facilityType = None
        """ Kind of facility where patient was seen.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.practiceSetting = None
        """ Additional details about where the content was created (e.g.
        clinical specialty).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.sourcePatientInfo = None
        """ Patient demographics from source.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.related = None
        """ Related identifiers or resources.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        super(DocumentReferenceContext, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(DocumentReferenceContext, self).elementProperties()
        js.extend([
            ("encounter", "encounter", fhirreference.FHIRReference, True, None, False),
            ("event", "event", codeableconcept.CodeableConcept, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("facilityType", "facilityType", codeableconcept.CodeableConcept, False, None, False),
            ("practiceSetting", "practiceSetting", codeableconcept.CodeableConcept, False, None, False),
            ("sourcePatientInfo", "sourcePatientInfo", fhirreference.FHIRReference, False, None, False),
            ("related", "related", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class DocumentReferenceRelatesTo(backboneelement.BackboneElement):
    """ Relationships to other documents.

    Relationships that this document has with other document references that
    already exist.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ replaces | transforms | signs | appends.
        Type `str`. """

        self.target = None
        """ Target of the relationship.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(DocumentReferenceRelatesTo, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(DocumentReferenceRelatesTo, self).elementProperties()
        js.extend([
            ("code", "code", DocumentRelationshipType.str, False, None, True),
            ("target", "target", fhirreference.FHIRReference, False, None, True),
        ])
        return js


import sys
try:
    from . import CompositionStatus
except ImportError:
    CompositionStatus = sys.modules[__package__ + '.CompositionStatus']
try:
    from . import DocumentReferenceStatus
except ImportError:
    DocumentReferenceStatus = sys.modules[__package__ + '.DocumentReferenceStatus']
try:
    from . import DocumentRelationshipType
except ImportError:
    DocumentRelationshipType = sys.modules[__package__ + '.DocumentRelationshipType']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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