#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/EnrollmentRequest) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class EnrollmentRequest(domainresource.DomainResource):
    """ Enroll in coverage.

    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """

    resource_type = "EnrollmentRequest"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.insurer = None
        """ Target.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.candidate = None
        """ The subject to be enrolled.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(EnrollmentRequest, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(EnrollmentRequest, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", FinancialResourceStatusCodes.str, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("candidate", "candidate", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import FinancialResourceStatusCodes
except ImportError:
    FinancialResourceStatusCodes = sys.modules[__package__ + '.FinancialResourceStatusCodes']
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