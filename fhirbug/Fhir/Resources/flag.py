#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Flag) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class Flag(domainresource.DomainResource):
    """ Key information to flag to healthcare providers.

    Prospective warnings of potential issues when providing care to the
    patient.
    """

    resource_type = "Flag"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.status = None
        """ active | inactive | entered-in-error.
        Type `str`. """

        self.category = None
        """ Clinical, administrative, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.code = None
        """ Coded or textual message to display to user.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.subject = None
        """ Who/What is flag about?.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.period = None
        """ Time period when flag is active.
        Type `Period` (represented as `dict` in JSON). """

        self.encounter = None
        """ Alert relevant during encounter.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.author = None
        """ Flag creator.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(Flag, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Flag, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", FlagStatus.str, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import FlagStatus
except ImportError:
    FlagStatus = sys.modules[__package__ + '.FlagStatus']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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