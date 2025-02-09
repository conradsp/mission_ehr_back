#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/GuidanceResponse) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class GuidanceResponse(domainresource.DomainResource):
    """ The formal response to a guidance request.

    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """

    resource_type = "GuidanceResponse"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.requestIdentifier = None
        """ The identifier of the request associated with this response, if any.
        Type `Identifier` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.moduleUri = None
        """ What guidance was requested.
        Type `str`. """

        self.moduleCanonical = None
        """ What guidance was requested.
        Type `str`. """

        self.moduleCodeableConcept = None
        """ What guidance was requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.status = None
        """ success | data-requested | data-required | in-progress | failure |
        entered-in-error.
        Type `str`. """

        self.subject = None
        """ Patient the request was performed for.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.encounter = None
        """ Encounter during which the response was returned.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.occurrenceDateTime = None
        """ When the guidance response was processed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.performer = None
        """ Device returning the guidance.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.reasonCode = None
        """ Why guidance is needed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Why guidance is needed.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.note = None
        """ Additional notes about the response.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.evaluationMessage = None
        """ Messages resulting from the evaluation of the artifact or artifacts.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.outputParameters = None
        """ The output parameters of the evaluation, if any.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.result = None
        """ Proposed actions, if any.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.dataRequirement = None
        """ Additional required data.
        List of `DataRequirement` items (represented as `dict` in JSON). """

        super(GuidanceResponse, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(GuidanceResponse, self).elementProperties()
        js.extend([
            ("requestIdentifier", "requestIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("moduleUri", "moduleUri", str, False, "module", True),
            ("moduleCanonical", "moduleCanonical", str, False, "module", True),
            ("moduleCodeableConcept", "moduleCodeableConcept", codeableconcept.CodeableConcept, False, "module", True),
            ("status", "status", GuidanceResponseStatus.str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("evaluationMessage", "evaluationMessage", fhirreference.FHIRReference, True, None, False),
            ("outputParameters", "outputParameters", fhirreference.FHIRReference, False, None, False),
            ("result", "result", fhirreference.FHIRReference, False, None, False),
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
        ])
        return js


import sys
try:
    from . import GuidanceResponseStatus
except ImportError:
    GuidanceResponseStatus = sys.modules[__package__ + '.GuidanceResponseStatus']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
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