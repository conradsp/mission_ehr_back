#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Account) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class Account(domainresource.DomainResource):
    """ Tracks balance, charges, for patient or cost center.

    A financial tool for tracking value accrued for a particular purpose.  In
    the healthcare field, used to track charges for a patient, cost centers,
    etc.
    """

    resource_type = "Account"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Account number.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.status = None
        """ active | inactive | entered-in-error | on-hold | unknown.
        Type `str`. """

        self.type = None
        """ E.g. patient, expense, depreciation.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.name = None
        """ Human-readable label.
        Type `str`. """

        self.subject = None
        """ The entity that caused the expenses.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.servicePeriod = None
        """ Transaction window.
        Type `Period` (represented as `dict` in JSON). """

        self.coverage = None
        """ The party(s) that are responsible for covering the payment of this
        account, and what order should they be applied to the account.
        List of `AccountCoverage` items (represented as `dict` in JSON). """

        self.owner = None
        """ Entity managing the Account.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.description = None
        """ Explanation of purpose/use.
        Type `str`. """

        self.guarantor = None
        """ The parties ultimately responsible for balancing the Account.
        List of `AccountGuarantor` items (represented as `dict` in JSON). """

        self.partOf = None
        """ Reference to a parent Account.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(Account, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Account, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", AccountStatus.str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("name", "name", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("servicePeriod", "servicePeriod", period.Period, False, None, False),
            ("coverage", "coverage", AccountCoverage, True, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("description", "description", str, False, None, False),
            ("guarantor", "guarantor", AccountGuarantor, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class AccountCoverage(backboneelement.BackboneElement):
    """ The party(s) that are responsible for covering the payment of this account,
    and what order should they be applied to the account.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.coverage = None
        """ The party(s), such as insurances, that may contribute to the
        payment of this account.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.priority = None
        """ The priority of the coverage in the context of this account.
        Type `int`. """

        super(AccountCoverage, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(AccountCoverage, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("priority", "priority", int, False, None, False),
        ])
        return js


class AccountGuarantor(backboneelement.BackboneElement):
    """ The parties ultimately responsible for balancing the Account.

    The parties responsible for balancing the account if other payment options
    fall short.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.party = None
        """ Responsible entity.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.onHold = None
        """ Credit or other hold applied.
        Type `bool`. """

        self.period = None
        """ Guarantee account during.
        Type `Period` (represented as `dict` in JSON). """

        super(AccountGuarantor, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(AccountGuarantor, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, True),
            ("onHold", "onHold", bool, False, None, False),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


import sys
try:
    from . import AccountStatus
except ImportError:
    AccountStatus = sys.modules[__package__ + '.AccountStatus']
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