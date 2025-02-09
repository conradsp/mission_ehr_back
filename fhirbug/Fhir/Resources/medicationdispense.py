#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/MedicationDispense) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class MedicationDispense(domainresource.DomainResource):
    """ Dispensing a medication to a named patient.

    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """

    resource_type = "MedicationDispense"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.partOf = None
        """ Event that dispense is part of.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.status = None
        """ preparation | in-progress | cancelled | on-hold | completed |
        entered-in-error | stopped | declined | unknown.
        Type `str`. """

        self.statusReasonCodeableConcept = None
        """ Why a dispense was not performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.statusReasonReference = None
        """ Why a dispense was not performed.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.category = None
        """ Type of medication dispense.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.medicationCodeableConcept = None
        """ What medication was supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.medicationReference = None
        """ What medication was supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.subject = None
        """ Who the dispense is for.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.context = None
        """ Encounter / Episode associated with event.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.supportingInformation = None
        """ Information that supports the dispensing of the medication.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.performer = None
        """ Who performed event.
        List of `MedicationDispensePerformer` items (represented as `dict` in JSON). """

        self.location = None
        """ Where the dispense occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.authorizingPrescription = None
        """ Medication order that authorizes the dispense.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.type = None
        """ Trial fill, partial fill, emergency fill, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.quantity = None
        """ Amount dispensed.
        Type `Quantity` (represented as `dict` in JSON). """

        self.daysSupply = None
        """ Amount of medication expressed as a timing amount.
        Type `Quantity` (represented as `dict` in JSON). """

        self.whenPrepared = None
        """ When product was packaged and reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.whenHandedOver = None
        """ When product was given out.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.destination = None
        """ Where the medication was sent.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.receiver = None
        """ Who collected the medication.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.note = None
        """ Information about the dispense.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.dosageInstruction = None
        """ How the medication is to be used by the patient or administered by
        the caregiver.
        List of `Dosage` items (represented as `dict` in JSON). """

        self.substitution = None
        """ Whether a substitution was performed on the dispense.
        Type `MedicationDispenseSubstitution` (represented as `dict` in JSON). """

        self.detectedIssue = None
        """ Clinical issue with action.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.eventHistory = None
        """ A list of relevant lifecycle events.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        super(MedicationDispense, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(MedicationDispense, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("status", "status", MedicationDispenseStatusCodes.str, False, None, True),
            ("statusReasonCodeableConcept", "statusReasonCodeableConcept", codeableconcept.CodeableConcept, False, "statusReason", False),
            ("statusReasonReference", "statusReasonReference", fhirreference.FHIRReference, False, "statusReason", False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
            ("performer", "performer", MedicationDispensePerformer, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("authorizingPrescription", "authorizingPrescription", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("daysSupply", "daysSupply", quantity.Quantity, False, None, False),
            ("whenPrepared", "whenPrepared", fhirdate.FHIRDate, False, None, False),
            ("whenHandedOver", "whenHandedOver", fhirdate.FHIRDate, False, None, False),
            ("destination", "destination", fhirreference.FHIRReference, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("dosageInstruction", "dosageInstruction", dosage.Dosage, True, None, False),
            ("substitution", "substitution", MedicationDispenseSubstitution, False, None, False),
            ("detectedIssue", "detectedIssue", fhirreference.FHIRReference, True, None, False),
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class MedicationDispensePerformer(backboneelement.BackboneElement):
    """ Who performed event.

    Indicates who or what performed the event.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.function = None
        """ Who performed the dispense and what they did.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.actor = None
        """ Individual who was performing.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(MedicationDispensePerformer, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(MedicationDispensePerformer, self).elementProperties()
        js.extend([
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    """ Whether a substitution was performed on the dispense.

    Indicates whether or not substitution was made as part of the dispense.  In
    some cases, substitution will be expected but does not happen, in other
    cases substitution is not expected but does happen.  This block explains
    what substitution did or did not happen and why.  If nothing is specified,
    substitution was not done.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.wasSubstituted = None
        """ Whether a substitution was or was not performed on the dispense.
        Type `bool`. """

        self.type = None
        """ Code signifying whether a different drug was dispensed from what
        was prescribed.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.reason = None
        """ Why was substitution made.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.responsibleParty = None
        """ Who is responsible for the substitution.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        super(MedicationDispenseSubstitution, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(MedicationDispenseSubstitution, self).elementProperties()
        js.extend([
            ("wasSubstituted", "wasSubstituted", bool, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("responsibleParty", "responsibleParty", fhirreference.FHIRReference, True, None, False),
        ])
        return js


import sys
try:
    from . import MedicationDispenseStatusCodes
except ImportError:
    MedicationDispenseStatusCodes = sys.modules[__package__ + '.MedicationDispenseStatusCodes']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + '.dosage']
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