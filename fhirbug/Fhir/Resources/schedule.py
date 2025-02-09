#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Schedule) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class Schedule(domainresource.DomainResource):
    """ A container for slots of time that may be available for booking
    appointments.
    """

    resource_type = "Schedule"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.active = None
        """ Whether this schedule is in active use.
        Type `bool`. """

        self.serviceCategory = None
        """ High-level category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.serviceType = None
        """ Specific service.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.specialty = None
        """ Type of specialty needed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.actor = None
        """ Resource(s) that availability information is being provided for.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.planningHorizon = None
        """ Period of time covered by schedule.
        Type `Period` (represented as `dict` in JSON). """

        self.comment = None
        """ Comments on availability.
        Type `str`. """

        super(Schedule, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Schedule, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("active", "active", bool, False, None, False),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, True, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("actor", "actor", fhirreference.FHIRReference, True, None, True),
            ("planningHorizon", "planningHorizon", period.Period, False, None, False),
            ("comment", "comment", str, False, None, False),
        ])
        return js


import sys
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