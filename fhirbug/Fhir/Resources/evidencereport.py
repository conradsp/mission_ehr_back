#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/EvidenceReport) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class EvidenceReport(domainresource.DomainResource):
    """ A EvidenceReport.

    The EvidenceReport Resource is a specialized container for a collection of
    resources and codable concepts, adapted to support compositions of
    Evidence, EvidenceVariable, and Citation resources and related concepts.
    """

    resource_type = "EvidenceReport"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.url = None
        """ Canonical identifier for this EvidenceReport, represented as a
        globally unique URI.
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.identifier = None
        """ Unique identifier for the evidence report.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.relatedIdentifier = None
        """ Identifiers for articles that may relate to more than one evidence
        report.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.citeAsReference = None
        """ Citation for this report.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.citeAsMarkdown = None
        """ Citation for this report.
        Type `str`. """

        self.type = None
        """ Kind of report.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.note = None
        """ Used for footnotes and annotations.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.relatedArtifact = None
        """ Link, description or reference to artifact associated with the
        report.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """

        self.subject = None
        """ Focus of the report.
        Type `EvidenceReportSubject` (represented as `dict` in JSON). """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.author = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.editor = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.reviewer = None
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.endorser = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.relatesTo = None
        """ Relationships to other compositions/documents.
        List of `EvidenceReportRelatesTo` items (represented as `dict` in JSON). """

        self.section = None
        """ Composition is broken into sections.
        List of `EvidenceReportSection` items (represented as `dict` in JSON). """

        super(EvidenceReport, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceReport, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("status", "status", PublicationStatus.str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("relatedIdentifier", "relatedIdentifier", identifier.Identifier, True, None, False),
            ("citeAsReference", "citeAsReference", fhirreference.FHIRReference, False, "citeAs", False),
            ("citeAsMarkdown", "citeAsMarkdown", str, False, "citeAs", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("subject", "subject", EvidenceReportSubject, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("relatesTo", "relatesTo", EvidenceReportRelatesTo, True, None, False),
            ("section", "section", EvidenceReportSection, True, None, False),
        ])
        return js


from . import backboneelement

class EvidenceReportRelatesTo(backboneelement.BackboneElement):
    """ Relationships to other compositions/documents.

    Relationships that this composition has with other compositions or
    documents that already exist.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ replaces | amends | appends | transforms | replacedWith |
        amendedWith | appendedWith | transformedWith.
        Type `str`. """

        self.targetIdentifier = None
        """ Target of the relationship.
        Type `Identifier` (represented as `dict` in JSON). """

        self.targetReference = None
        """ Target of the relationship.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(EvidenceReportRelatesTo, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceReportRelatesTo, self).elementProperties()
        js.extend([
            ("code", "code", ReportRelationshipType.str, False, None, True),
            ("targetIdentifier", "targetIdentifier", identifier.Identifier, False, "target", True),
            ("targetReference", "targetReference", fhirreference.FHIRReference, False, "target", True),
        ])
        return js


class EvidenceReportSection(backboneelement.BackboneElement):
    """ Composition is broken into sections.

    The root of the sections that make up the composition.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.title = None
        """ Label for section (e.g. for ToC).
        Type `str`. """

        self.focus = None
        """ Classification of section (recommended).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.focusReference = None
        """ Classification of section by Resource.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.author = None
        """ Who and/or what authored the section.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.text = None
        """ Text summary of the section, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """

        self.mode = None
        """ working | snapshot | changes.
        Type `str`. """

        self.orderedBy = None
        """ Order of section entries.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.entryClassifier = None
        """ Extensible classifiers as content.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.entryReference = None
        """ Reference to resources as content.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.entryQuantity = None
        """ Quantity as content.
        List of `Quantity` items (represented as `dict` in JSON). """

        self.emptyReason = None
        """ Why the section is empty.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.section = None
        """ Nested Section.
        List of `EvidenceReportSection` items (represented as `dict` in JSON). """

        super(EvidenceReportSection, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceReportSection, self).elementProperties()
        js.extend([
            ("title", "title", str, False, None, False),
            ("focus", "focus", codeableconcept.CodeableConcept, False, None, False),
            ("focusReference", "focusReference", fhirreference.FHIRReference, False, None, False),
            ("author", "author", fhirreference.FHIRReference, True, None, False),
            ("text", "text", narrative.Narrative, False, None, False),
            ("mode", "mode", ListMode.str, False, None, False),
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, False, None, False),
            ("entryClassifier", "entryClassifier", codeableconcept.CodeableConcept, True, None, False),
            ("entryReference", "entryReference", fhirreference.FHIRReference, True, None, False),
            ("entryQuantity", "entryQuantity", quantity.Quantity, True, None, False),
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, False, None, False),
            ("section", "section", EvidenceReportSection, True, None, False),
        ])
        return js


class EvidenceReportSubject(backboneelement.BackboneElement):
    """ Focus of the report.

    Specifies the subject or focus of the report. Answers "What is this report
    about?".
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.characteristic = None
        """ Characteristic.
        List of `EvidenceReportSubjectCharacteristic` items (represented as `dict` in JSON). """

        self.note = None
        """ Footnotes and/or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """

        super(EvidenceReportSubject, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceReportSubject, self).elementProperties()
        js.extend([
            ("characteristic", "characteristic", EvidenceReportSubjectCharacteristic, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
        ])
        return js


class EvidenceReportSubjectCharacteristic(backboneelement.BackboneElement):
    """ Characteristic.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Characteristic code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueReference = None
        """ Characteristic value.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.valueCodeableConcept = None
        """ Characteristic value.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueBoolean = None
        """ Characteristic value.
        Type `bool`. """

        self.valueQuantity = None
        """ Characteristic value.
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueRange = None
        """ Characteristic value.
        Type `Range` (represented as `dict` in JSON). """

        self.exclude = None
        """ Is used to express not the characteristic.
        Type `bool`. """

        self.period = None
        """ Timeframe for the characteristic.
        Type `Period` (represented as `dict` in JSON). """

        super(EvidenceReportSubjectCharacteristic, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceReportSubjectCharacteristic, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("exclude", "exclude", bool, False, None, False),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


import sys
try:
    from . import ListMode
except ImportError:
    ListMode = sys.modules[__package__ + '.ListMode']
try:
    from . import PublicationStatus
except ImportError:
    PublicationStatus = sys.modules[__package__ + '.PublicationStatus']
try:
    from . import ReportRelationshipType
except ImportError:
    ReportRelationshipType = sys.modules[__package__ + '.ReportRelationshipType']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import narrative
except ImportError:
    narrative = sys.modules[__package__ + '.narrative']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']