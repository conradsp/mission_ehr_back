#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/RiskEvidenceSynthesis) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class RiskEvidenceSynthesis(domainresource.DomainResource):
    """ A quantified estimate of risk based on a body of evidence.

    The RiskEvidenceSynthesis resource describes the likelihood of an outcome
    in a population plus exposure state where the risk estimate is derived from
    a combination of research studies.
    """

    resource_type = "RiskEvidenceSynthesis"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.url = None
        """ Canonical identifier for this risk evidence synthesis, represented
        as a URI (globally unique).
        Type `str`. """

        self.identifier = None
        """ Additional identifier for the risk evidence synthesis.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the risk evidence synthesis.
        Type `str`. """

        self.name = None
        """ Name for this risk evidence synthesis (computer friendly).
        Type `str`. """

        self.title = None
        """ Name for this risk evidence synthesis (human friendly).
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
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

        self.description = None
        """ Natural language description of the risk evidence synthesis.
        Type `str`. """

        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for risk evidence synthesis (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.approvalDate = None
        """ When the risk evidence synthesis was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.lastReviewDate = None
        """ When the risk evidence synthesis was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.effectivePeriod = None
        """ When the risk evidence synthesis is expected to be used.
        Type `Period` (represented as `dict` in JSON). """

        self.topic = None
        """ The category of the EffectEvidenceSynthesis, such as Education,
        Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """

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

        self.synthesisType = None
        """ Type of synthesis.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.studyType = None
        """ Type of study.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.population = None
        """ What population?.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.exposure = None
        """ What exposure?.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.outcome = None
        """ What outcome?.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.sampleSize = None
        """ What sample size was involved?.
        Type `RiskEvidenceSynthesisSampleSize` (represented as `dict` in JSON). """

        self.riskEstimate = None
        """ What was the estimated risk.
        Type `RiskEvidenceSynthesisRiskEstimate` (represented as `dict` in JSON). """

        self.certainty = None
        """ How certain is the risk.
        List of `RiskEvidenceSynthesisCertainty` items (represented as `dict` in JSON). """

        super(RiskEvidenceSynthesis, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesis, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("status", "status", PublicationStatus.str, False, None, True),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("synthesisType", "synthesisType", codeableconcept.CodeableConcept, False, None, False),
            ("studyType", "studyType", codeableconcept.CodeableConcept, False, None, False),
            ("population", "population", fhirreference.FHIRReference, False, None, True),
            ("exposure", "exposure", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", fhirreference.FHIRReference, False, None, True),
            ("sampleSize", "sampleSize", RiskEvidenceSynthesisSampleSize, False, None, False),
            ("riskEstimate", "riskEstimate", RiskEvidenceSynthesisRiskEstimate, False, None, False),
            ("certainty", "certainty", RiskEvidenceSynthesisCertainty, True, None, False),
        ])
        return js


from . import backboneelement

class RiskEvidenceSynthesisCertainty(backboneelement.BackboneElement):
    """ How certain is the risk.

    A description of the certainty of the risk estimate.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.rating = None
        """ Certainty rating.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.certaintySubcomponent = None
        """ A component that contributes to the overall certainty.
        List of `RiskEvidenceSynthesisCertaintyCertaintySubcomponent` items (represented as `dict` in JSON). """

        super(RiskEvidenceSynthesisCertainty, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisCertainty, self).elementProperties()
        js.extend([
            ("rating", "rating", codeableconcept.CodeableConcept, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("certaintySubcomponent", "certaintySubcomponent", RiskEvidenceSynthesisCertaintyCertaintySubcomponent, True, None, False),
        ])
        return js


class RiskEvidenceSynthesisCertaintyCertaintySubcomponent(backboneelement.BackboneElement):
    """ A component that contributes to the overall certainty.

    A description of a component of the overall certainty.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ Type of subcomponent of certainty rating.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.rating = None
        """ Subcomponent certainty rating.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """

        super(RiskEvidenceSynthesisCertaintyCertaintySubcomponent, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisCertaintyCertaintySubcomponent, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("rating", "rating", codeableconcept.CodeableConcept, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
        ])
        return js


class RiskEvidenceSynthesisRiskEstimate(backboneelement.BackboneElement):
    """ What was the estimated risk.

    The estimated risk of the outcome.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Description of risk estimate.
        Type `str`. """

        self.type = None
        """ Type of risk estimate.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.value = None
        """ Point estimate.
        Type `float`. """

        self.unitOfMeasure = None
        """ What unit is the outcome described in?.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.denominatorCount = None
        """ Sample size for group measured.
        Type `int`. """

        self.numeratorCount = None
        """ Number with the outcome.
        Type `int`. """

        self.precisionEstimate = None
        """ How precise the estimate is.
        List of `RiskEvidenceSynthesisRiskEstimatePrecisionEstimate` items (represented as `dict` in JSON). """

        super(RiskEvidenceSynthesisRiskEstimate, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisRiskEstimate, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
            ("unitOfMeasure", "unitOfMeasure", codeableconcept.CodeableConcept, False, None, False),
            ("denominatorCount", "denominatorCount", int, False, None, False),
            ("numeratorCount", "numeratorCount", int, False, None, False),
            ("precisionEstimate", "precisionEstimate", RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, True, None, False),
        ])
        return js


class RiskEvidenceSynthesisRiskEstimatePrecisionEstimate(backboneelement.BackboneElement):
    """ How precise the estimate is.

    A description of the precision of the estimate for the effect.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ Type of precision estimate.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.level = None
        """ Level of confidence interval.
        Type `float`. """

        self.from_fhir = None
        """ Lower bound.
        Type `float`. """

        self.to = None
        """ Upper bound.
        Type `float`. """

        super(RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("level", "level", float, False, None, False),
            ("from_fhir", "from", float, False, None, False),
            ("to", "to", float, False, None, False),
        ])
        return js


class RiskEvidenceSynthesisSampleSize(backboneelement.BackboneElement):
    """ What sample size was involved?.

    A description of the size of the sample involved in the synthesis.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Description of sample size.
        Type `str`. """

        self.numberOfStudies = None
        """ How many studies?.
        Type `int`. """

        self.numberOfParticipants = None
        """ How many participants?.
        Type `int`. """

        super(RiskEvidenceSynthesisSampleSize, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisSampleSize, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("numberOfStudies", "numberOfStudies", int, False, None, False),
            ("numberOfParticipants", "numberOfParticipants", int, False, None, False),
        ])
        return js


import sys
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']