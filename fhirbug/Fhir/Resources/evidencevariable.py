#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/EvidenceVariable) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class EvidenceVariable(domainresource.DomainResource):
    """ A definition of an exposure, outcome, or other variable.

    The EvidenceVariable resource describes an element that knowledge
    (Evidence) is about.
    """

    resource_type = "EvidenceVariable"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.url = None
        """ Canonical identifier for this evidence variable, represented as a
        URI (globally unique).
        Type `str`. """

        self.identifier = None
        """ Additional identifier for the evidence variable.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the evidence variable.
        Type `str`. """

        self.name = None
        """ Name for this evidence variable (computer friendly).
        Type `str`. """

        self.title = None
        """ Name for this evidence variable (human friendly).
        Type `str`. """

        self.shortTitle = None
        """ Title for use in informal contexts.
        Type `str`. """

        self.subtitle = None
        """ Subordinate title of the EvidenceVariable.
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Natural language description of the evidence variable.
        Type `str`. """

        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

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

        self.relatedArtifact = None
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """

        self.actual = None
        """ Actual or conceptual.
        Type `bool`. """

        self.characteristicCombination = None
        """ intersection | union.
        Type `str`. """

        self.characteristic = None
        """ What defines the members of the evidence element.
        List of `EvidenceVariableCharacteristic` items (represented as `dict` in JSON). """

        self.handling = None
        """ continuous | dichotomous | ordinal | polychotomous.
        Type `str`. """

        self.category = None
        """ A grouping for ordinal or polychotomous variables.
        List of `EvidenceVariableCategory` items (represented as `dict` in JSON). """

        super(EvidenceVariable, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceVariable, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("shortTitle", "shortTitle", str, False, None, False),
            ("subtitle", "subtitle", str, False, None, False),
            ("status", "status", PublicationStatus.str, False, None, True),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("actual", "actual", bool, False, None, False),
            ("characteristicCombination", "characteristicCombination", CharacteristicCombination.str, False, None, False),
            ("characteristic", "characteristic", EvidenceVariableCharacteristic, True, None, False),
            ("handling", "handling", EvidenceVariableHandling.str, False, None, False),
            ("category", "category", EvidenceVariableCategory, True, None, False),
        ])
        return js


from . import backboneelement

class EvidenceVariableCategory(backboneelement.BackboneElement):
    """ A grouping for ordinal or polychotomous variables.

    A grouping (or set of values) described along with other groupings to
    specify the set of groupings allowed for the variable.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.name = None
        """ Description of the grouping.
        Type `str`. """

        self.valueCodeableConcept = None
        """ Definition of the grouping.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueQuantity = None
        """ Definition of the grouping.
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueRange = None
        """ Definition of the grouping.
        Type `Range` (represented as `dict` in JSON). """

        super(EvidenceVariableCategory, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceVariableCategory, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
        ])
        return js


class EvidenceVariableCharacteristic(backboneelement.BackboneElement):
    """ What defines the members of the evidence element.

    A characteristic that defines the members of the evidence element. Multiple
    characteristics are applied with "and" semantics.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Natural language description of the characteristic.
        Type `str`. """

        self.definitionReference = None
        """ What code or expression defines members?.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.definitionCanonical = None
        """ What code or expression defines members?.
        Type `str`. """

        self.definitionCodeableConcept = None
        """ What code or expression defines members?.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.definitionExpression = None
        """ What code or expression defines members?.
        Type `Expression` (represented as `dict` in JSON). """

        self.method = None
        """ Method used for describing characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.device = None
        """ Device used for determining characteristic.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.exclude = None
        """ Whether the characteristic includes or excludes members.
        Type `bool`. """

        self.timeFromStart = None
        """ Observation time from study start.
        Type `EvidenceVariableCharacteristicTimeFromStart` (represented as `dict` in JSON). """

        self.groupMeasure = None
        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
        Type `str`. """

        super(EvidenceVariableCharacteristic, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceVariableCharacteristic, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("definitionReference", "definitionReference", fhirreference.FHIRReference, False, "definition", True),
            ("definitionCanonical", "definitionCanonical", str, False, "definition", True),
            ("definitionCodeableConcept", "definitionCodeableConcept", codeableconcept.CodeableConcept, False, "definition", True),
            ("definitionExpression", "definitionExpression", expression.Expression, False, "definition", True),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("exclude", "exclude", bool, False, None, False),
            ("timeFromStart", "timeFromStart", EvidenceVariableCharacteristicTimeFromStart, False, None, False),
            ("groupMeasure", "groupMeasure", GroupMeasure.str, False, None, False),
        ])
        return js


class EvidenceVariableCharacteristicTimeFromStart(backboneelement.BackboneElement):
    """ Observation time from study start.

    Indicates duration, period, or point of observation from the participant's
    study entry.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Human readable description.
        Type `str`. """

        self.quantity = None
        """ Used to express the observation at a defined amount of time after
        the study start.
        Type `Quantity` (represented as `dict` in JSON). """

        self.range = None
        """ Used to express the observation within a period after the study
        start.
        Type `Range` (represented as `dict` in JSON). """

        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """

        super(EvidenceVariableCharacteristicTimeFromStart, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceVariableCharacteristicTimeFromStart, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("range", "range", range.Range, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
        ])
        return js


import sys
try:
    from . import CharacteristicCombination
except ImportError:
    CharacteristicCombination = sys.modules[__package__ + '.CharacteristicCombination']
try:
    from . import EvidenceVariableHandling
except ImportError:
    EvidenceVariableHandling = sys.modules[__package__ + '.EvidenceVariableHandling']
try:
    from . import GroupMeasure
except ImportError:
    GroupMeasure = sys.modules[__package__ + '.GroupMeasure']
try:
    from . import PublicationStatus
except ImportError:
    PublicationStatus = sys.modules[__package__ + '.PublicationStatus']
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
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']
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