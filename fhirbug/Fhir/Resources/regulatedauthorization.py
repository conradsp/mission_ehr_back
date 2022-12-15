#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/RegulatedAuthorization) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class RegulatedAuthorization(domainresource.DomainResource):
    """ Regulatory approval, clearance or licencing related to a regulated product,
    treatment, facility or activity e.g. Market Authorization for a Medicinal
    Product.

    Regulatory approval, clearance or licencing related to a regulated product,
    treatment, facility or activity that is cited in a guidance, regulation,
    rule or legislative act. An example is Market Authorization relating to a
    Medicinal Product.
    """

    resource_type = "RegulatedAuthorization"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Business identifier for the authorization, typically assigned by
        the authorizing body.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.subject = None
        """ The product type, treatment, facility or activity that is being
        authorized.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.type = None
        """ Overall type of this authorization, for example drug marketing
        approval, orphan drug designation.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.description = None
        """ General textual supporting information.
        Type `str`. """

        self.region = None
        """ The territory in which the authorization has been granted.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.status = None
        """ The status that is authorised e.g. approved. Intermediate states
        can be tracked with cases and applications.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.statusDate = None
        """ The date at which the current status was assigned.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.validityPeriod = None
        """ The time period in which the regulatory approval etc. is in effect,
        e.g. a Marketing Authorization includes the date of authorization
        and/or expiration date.
        Type `Period` (represented as `dict` in JSON). """

        self.indication = None
        """ Condition for which the use of the regulated product applies.
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.intendedUse = None
        """ The intended use of the product, e.g. prevention, treatment.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.basis = None
        """ The legal/regulatory framework or reasons under which this
        authorization is granted.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.holder = None
        """ The organization that has been granted this authorization, by the
        regulator.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.regulator = None
        """ The regulatory authority or authorizing body granting the
        authorization.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.case = None
        """ The case or regulatory procedure for granting or amending a
        regulated authorization. Note: This area is subject to ongoing
        review and the workgroup is seeking implementer feedback on its use
        (see link at bottom of page).
        Type `RegulatedAuthorizationCase` (represented as `dict` in JSON). """

        super(RegulatedAuthorization, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(RegulatedAuthorization, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("region", "region", codeableconcept.CodeableConcept, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
            ("indication", "indication", codeablereference.CodeableReference, False, None, False),
            ("intendedUse", "intendedUse", codeableconcept.CodeableConcept, False, None, False),
            ("basis", "basis", codeableconcept.CodeableConcept, True, None, False),
            ("holder", "holder", fhirreference.FHIRReference, False, None, False),
            ("regulator", "regulator", fhirreference.FHIRReference, False, None, False),
            ("case", "case", RegulatedAuthorizationCase, False, None, False),
        ])
        return js


from . import backboneelement

class RegulatedAuthorizationCase(backboneelement.BackboneElement):
    """ The case or regulatory procedure for granting or amending a regulated
    authorization. Note: This area is subject to ongoing review and the
    workgroup is seeking implementer feedback on its use (see link at bottom of
    page).

    The case or regulatory procedure for granting or amending a regulated
    authorization. An authorization is granted in response to
    submissions/applications by those seeking authorization. A case is the
    administrative process that deals with the application(s) that relate to
    this and assesses them. Note: This area is subject to ongoing review and
    the workgroup is seeking implementer feedback on its use (see link at
    bottom of page).
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Identifier by which this case can be referenced.
        Type `Identifier` (represented as `dict` in JSON). """

        self.type = None
        """ The defining type of case.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.status = None
        """ The status associated with the case.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.datePeriod = None
        """ Relevant date for this case.
        Type `Period` (represented as `dict` in JSON). """

        self.dateDateTime = None
        """ Relevant date for this case.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.application = None
        """ Applications submitted to obtain a regulated authorization. Steps
        within the longer running case or procedure.
        List of `RegulatedAuthorizationCase` items (represented as `dict` in JSON). """

        super(RegulatedAuthorizationCase, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(RegulatedAuthorizationCase, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("datePeriod", "datePeriod", period.Period, False, "date", False),
            ("dateDateTime", "dateDateTime", fhirdate.FHIRDate, False, "date", False),
            ("application", "application", RegulatedAuthorizationCase, True, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import codeablereference
except ImportError:
    codeablereference = sys.modules[__package__ + '.codeablereference']
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