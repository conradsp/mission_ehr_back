#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Evidence) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class Evidence(domainresource.DomainResource):
    """ Single evidence bit.

    The Evidence Resource provides a machine-interpretable expression of an
    evidence concept including the evidence variables (eg population,
    exposures/interventions, comparators, outcomes, measured variables,
    confounding variables), the statistics, and the certainty of this evidence.
    """

    resource_type = "Evidence"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.url = None
        """ Canonical identifier for this evidence, represented as a globally
        unique URI.
        Type `str`. """

        self.identifier = None
        """ Additional identifier for the summary.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of this summary.
        Type `str`. """

        self.title = None
        """ Name for this summary (human friendly).
        Type `str`. """

        self.citeAsReference = None
        """ Citation for this evidence.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.citeAsMarkdown = None
        """ Citation for this evidence.
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.approvalDate = None
        """ When the summary was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.lastReviewDate = None
        """ When the summary was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """

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
        """ Link or citation to artifact associated with the summary.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """

        self.description = None
        """ Description of the particular summary.
        Type `str`. """

        self.assertion = None
        """ Declarative description of the Evidence.
        Type `str`. """

        self.note = None
        """ Footnotes and/or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.variableDefinition = None
        """ Evidence variable such as population, exposure, or outcome.
        List of `EvidenceVariableDefinition` items (represented as `dict` in JSON). """

        self.synthesisType = None
        """ The method to combine studies.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.studyType = None
        """ The type of study that produced this evidence.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.statistic = None
        """ Values and parameters for a single statistic.
        List of `EvidenceStatistic` items (represented as `dict` in JSON). """

        self.certainty = None
        """ Certainty or quality of the evidence.
        List of `EvidenceCertainty` items (represented as `dict` in JSON). """

        super(Evidence, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Evidence, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("citeAsReference", "citeAsReference", fhirreference.FHIRReference, False, "citeAs", False),
            ("citeAsMarkdown", "citeAsMarkdown", str, False, "citeAs", False),
            ("status", "status", PublicationStatus.str, False, None, True),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("description", "description", str, False, None, False),
            ("assertion", "assertion", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("variableDefinition", "variableDefinition", EvidenceVariableDefinition, True, None, True),
            ("synthesisType", "synthesisType", codeableconcept.CodeableConcept, False, None, False),
            ("studyType", "studyType", codeableconcept.CodeableConcept, False, None, False),
            ("statistic", "statistic", EvidenceStatistic, True, None, False),
            ("certainty", "certainty", EvidenceCertainty, True, None, False),
        ])
        return js


from . import backboneelement

class EvidenceCertainty(backboneelement.BackboneElement):
    """ Certainty or quality of the evidence.

    Assessment of certainty, confidence in the estimates, or quality of the
    evidence.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Textual description of certainty.
        Type `str`. """

        self.note = None
        """ Footnotes and/or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.type = None
        """ Aspect of certainty being rated.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.rating = None
        """ Assessment or judgement of the aspect.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.rater = None
        """ Individual or group who did the rating.
        Type `str`. """

        self.subcomponent = None
        """ A domain or subdomain of certainty.
        List of `EvidenceCertainty` items (represented as `dict` in JSON). """

        super(EvidenceCertainty, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceCertainty, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("rating", "rating", codeableconcept.CodeableConcept, False, None, False),
            ("rater", "rater", str, False, None, False),
            ("subcomponent", "subcomponent", EvidenceCertainty, True, None, False),
        ])
        return js


class EvidenceStatistic(backboneelement.BackboneElement):
    """ Values and parameters for a single statistic.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Description of content.
        Type `str`. """

        self.note = None
        """ Footnotes and/or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.statisticType = None
        """ Type of statistic, eg relative risk.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.category = None
        """ Associated category for categorical variable.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.quantity = None
        """ Statistic value.
        Type `Quantity` (represented as `dict` in JSON). """

        self.numberOfEvents = None
        """ The number of events associated with the statistic.
        Type `int`. """

        self.numberAffected = None
        """ The number of participants affected.
        Type `int`. """

        self.sampleSize = None
        """ Number of samples in the statistic.
        Type `EvidenceStatisticSampleSize` (represented as `dict` in JSON). """

        self.attributeEstimate = None
        """ An attribute of the Statistic.
        List of `EvidenceStatisticAttributeEstimate` items (represented as `dict` in JSON). """

        self.modelCharacteristic = None
        """ An aspect of the statistical model.
        List of `EvidenceStatisticModelCharacteristic` items (represented as `dict` in JSON). """

        super(EvidenceStatistic, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceStatistic, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("statisticType", "statisticType", codeableconcept.CodeableConcept, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("numberOfEvents", "numberOfEvents", int, False, None, False),
            ("numberAffected", "numberAffected", int, False, None, False),
            ("sampleSize", "sampleSize", EvidenceStatisticSampleSize, False, None, False),
            ("attributeEstimate", "attributeEstimate", EvidenceStatisticAttributeEstimate, True, None, False),
            ("modelCharacteristic", "modelCharacteristic", EvidenceStatisticModelCharacteristic, True, None, False),
        ])
        return js


class EvidenceStatisticAttributeEstimate(backboneelement.BackboneElement):
    """ An attribute of the Statistic.

    A statistical attribute of the statistic such as a measure of
    heterogeneity.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Textual description of the attribute estimate.
        Type `str`. """

        self.note = None
        """ Footnote or explanatory note about the estimate.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.type = None
        """ The type of attribute estimate, eg confidence interval or p value.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.quantity = None
        """ The singular quantity of the attribute estimate, for attribute
        estimates represented as single values; also used to report unit of
        measure.
        Type `Quantity` (represented as `dict` in JSON). """

        self.level = None
        """ Level of confidence interval, eg 0.95 for 95% confidence interval.
        Type `float`. """

        self.range = None
        """ Lower and upper bound values of the attribute estimate.
        Type `Range` (represented as `dict` in JSON). """

        self.attributeEstimate = None
        """ A nested attribute estimate; which is the attribute estimate of an
        attribute estimate.
        List of `EvidenceStatisticAttributeEstimate` items (represented as `dict` in JSON). """

        super(EvidenceStatisticAttributeEstimate, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceStatisticAttributeEstimate, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("level", "level", float, False, None, False),
            ("range", "range", range.Range, False, None, False),
            ("attributeEstimate", "attributeEstimate", EvidenceStatisticAttributeEstimate, True, None, False),
        ])
        return js


class EvidenceStatisticModelCharacteristic(backboneelement.BackboneElement):
    """ An aspect of the statistical model.

    A component of the method to generate the statistic.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Model specification.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.value = None
        """ Numerical value to complete model specification.
        Type `Quantity` (represented as `dict` in JSON). """

        self.variable = None
        """ A variable adjusted for in the adjusted analysis.
        List of `EvidenceStatisticModelCharacteristicVariable` items (represented as `dict` in JSON). """

        self.attributeEstimate = None
        """ An attribute of the statistic used as a model characteristic.
        List of `EvidenceStatisticAttributeEstimate` items (represented as `dict` in JSON). """

        super(EvidenceStatisticModelCharacteristic, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceStatisticModelCharacteristic, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", quantity.Quantity, False, None, False),
            ("variable", "variable", EvidenceStatisticModelCharacteristicVariable, True, None, False),
            ("attributeEstimate", "attributeEstimate", EvidenceStatisticAttributeEstimate, True, None, False),
        ])
        return js


class EvidenceStatisticModelCharacteristicVariable(backboneelement.BackboneElement):
    """ A variable adjusted for in the adjusted analysis.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.variableDefinition = None
        """ Description of the variable.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.handling = None
        """ continuous | dichotomous | ordinal | polychotomous.
        Type `str`. """

        self.valueCategory = None
        """ Description for grouping of ordinal or polychotomous variables.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.valueQuantity = None
        """ Discrete value for grouping of ordinal or polychotomous variables.
        List of `Quantity` items (represented as `dict` in JSON). """

        self.valueRange = None
        """ Range of values for grouping of ordinal or polychotomous variables.
        List of `Range` items (represented as `dict` in JSON). """

        super(EvidenceStatisticModelCharacteristicVariable, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceStatisticModelCharacteristicVariable, self).elementProperties()
        js.extend([
            ("variableDefinition", "variableDefinition", fhirreference.FHIRReference, False, None, True),
            ("handling", "handling", EvidenceVariableHandling.str, False, None, False),
            ("valueCategory", "valueCategory", codeableconcept.CodeableConcept, True, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, True, None, False),
            ("valueRange", "valueRange", range.Range, True, None, False),
        ])
        return js


class EvidenceStatisticSampleSize(backboneelement.BackboneElement):
    """ Number of samples in the statistic.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Textual description of sample size for statistic.
        Type `str`. """

        self.note = None
        """ Footnote or explanatory note about the sample size.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.numberOfStudies = None
        """ Number of contributing studies.
        Type `int`. """

        self.numberOfParticipants = None
        """ Cumulative number of participants.
        Type `int`. """

        self.knownDataCount = None
        """ Number of participants with known results for measured variables.
        Type `int`. """

        super(EvidenceStatisticSampleSize, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceStatisticSampleSize, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("numberOfStudies", "numberOfStudies", int, False, None, False),
            ("numberOfParticipants", "numberOfParticipants", int, False, None, False),
            ("knownDataCount", "knownDataCount", int, False, None, False),
        ])
        return js


class EvidenceVariableDefinition(backboneelement.BackboneElement):
    """ Evidence variable such as population, exposure, or outcome.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ A text description or summary of the variable.
        Type `str`. """

        self.note = None
        """ Footnotes and/or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.variableRole = None
        """ population | subpopulation | exposure | referenceExposure |
        measuredVariable | confounder.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.observed = None
        """ Definition of the actual variable related to the statistic(s).
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.intended = None
        """ Definition of the intended variable related to the Evidence.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.directnessMatch = None
        """ low | moderate | high | exact.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(EvidenceVariableDefinition, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EvidenceVariableDefinition, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("variableRole", "variableRole", codeableconcept.CodeableConcept, False, None, True),
            ("observed", "observed", fhirreference.FHIRReference, False, None, False),
            ("intended", "intended", fhirreference.FHIRReference, False, None, False),
            ("directnessMatch", "directnessMatch", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import EvidenceVariableHandling
except ImportError:
    EvidenceVariableHandling = sys.modules[__package__ + '.EvidenceVariableHandling']
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