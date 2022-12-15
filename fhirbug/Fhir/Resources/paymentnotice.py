#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/PaymentNotice) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class PaymentNotice(domainresource.DomainResource):
    """ PaymentNotice request.

    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """

    resource_type = "PaymentNotice"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Business Identifier for the payment noctice.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        self.request = None
        """ Request reference.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.response = None
        """ Response reference.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.payment = None
        """ Payment reference.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.paymentDate = None
        """ Payment or clearing date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.payee = None
        """ Party being paid.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.recipient = None
        """ Party being notified.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.amount = None
        """ Monetary amount of the payment.
        Type `Money` (represented as `dict` in JSON). """

        self.paymentStatus = None
        """ Issued or cleared Status of the payment.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(PaymentNotice, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(PaymentNotice, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", FinancialResourceStatusCodes.str, False, None, True),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("payment", "payment", fhirreference.FHIRReference, False, None, True),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False, None, False),
            ("payee", "payee", fhirreference.FHIRReference, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, True),
            ("amount", "amount", money.Money, False, None, True),
            ("paymentStatus", "paymentStatus", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import FinancialResourceStatusCodes
except ImportError:
    FinancialResourceStatusCodes = sys.modules[__package__ + '.FinancialResourceStatusCodes']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']