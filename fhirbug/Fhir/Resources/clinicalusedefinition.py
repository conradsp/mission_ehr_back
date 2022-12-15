#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class ClinicalUseDefinition(domainresource.DomainResource):
    """ A single issue - either an indication, contraindication, interaction or an
    undesirable effect for a medicinal product, medication, device or procedure.
    """

    resource_type = "ClinicalUseDefinition"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Business identifier for this issue.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.type = None
        """ indication | contraindication | interaction | undesirable-effect |
        warning.
        Type `str`. """

        self.category = None
        """ A categorisation of the issue, primarily for dividing warnings into
        subject heading areas such as "Pregnancy", "Overdose".
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.subject = None
        """ The medication or procedure for which this is an indication.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.status = None
        """ Whether this is a current issue or one that has been retired etc.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.contraindication = None
        """ Specifics for when this is a contraindication.
        Type `ClinicalUseDefinitionContraindication` (represented as `dict` in JSON). """

        self.indication = None
        """ Specifics for when this is an indication.
        Type `ClinicalUseDefinitionIndication` (represented as `dict` in JSON). """

        self.interaction = None
        """ Specifics for when this is an interaction.
        Type `ClinicalUseDefinitionInteraction` (represented as `dict` in JSON). """

        self.population = None
        """ The population group to which this applies.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.undesirableEffect = None
        """ A possible negative outcome from the use of this treatment.
        Type `ClinicalUseDefinitionUndesirableEffect` (represented as `dict` in JSON). """

        self.warning = None
        """ Critical environmental, health or physical risks or hazards. For
        example 'Do not operate heavy machinery', 'May cause drowsiness'.
        Type `ClinicalUseDefinitionWarning` (represented as `dict` in JSON). """

        super(ClinicalUseDefinition, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(ClinicalUseDefinition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("type", "type", ClinicalUseDefinitionType.str, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("contraindication", "contraindication", ClinicalUseDefinitionContraindication, False, None, False),
            ("indication", "indication", ClinicalUseDefinitionIndication, False, None, False),
            ("interaction", "interaction", ClinicalUseDefinitionInteraction, False, None, False),
            ("population", "population", fhirreference.FHIRReference, True, None, False),
            ("undesirableEffect", "undesirableEffect", ClinicalUseDefinitionUndesirableEffect, False, None, False),
            ("warning", "warning", ClinicalUseDefinitionWarning, False, None, False),
        ])
        return js


from . import backboneelement

class ClinicalUseDefinitionContraindication(backboneelement.BackboneElement):
    """ Specifics for when this is a contraindication.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.diseaseSymptomProcedure = None
        """ The situation that is being documented as contraindicating against
        this item.
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.diseaseStatus = None
        """ The status of the disease or symptom for the contraindication.
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.comorbidity = None
        """ A comorbidity (concurrent condition) or coinfection.
        List of `CodeableReference` items (represented as `dict` in JSON). """

        self.indication = None
        """ The indication which this is a contraidication for.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.otherTherapy = None
        """ Information about use of the product in relation to other therapies
        described as part of the contraindication.
        List of `ClinicalUseDefinitionContraindicationOtherTherapy` items (represented as `dict` in JSON). """

        super(ClinicalUseDefinitionContraindication, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(ClinicalUseDefinitionContraindication, self).elementProperties()
        js.extend([
            ("diseaseSymptomProcedure", "diseaseSymptomProcedure", codeablereference.CodeableReference, False, None, False),
            ("diseaseStatus", "diseaseStatus", codeablereference.CodeableReference, False, None, False),
            ("comorbidity", "comorbidity", codeablereference.CodeableReference, True, None, False),
            ("indication", "indication", fhirreference.FHIRReference, True, None, False),
            ("otherTherapy", "otherTherapy", ClinicalUseDefinitionContraindicationOtherTherapy, True, None, False),
        ])
        return js


class ClinicalUseDefinitionContraindicationOtherTherapy(backboneelement.BackboneElement):
    """ Information about use of the product in relation to other therapies
    described as part of the contraindication.

    Information about the use of the medicinal product in relation to other
    therapies described as part of the contraindication.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.relationshipType = None
        """ The type of relationship between the product
        indication/contraindication and another therapy.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.therapy = None
        """ Reference to a specific medication as part of an indication or
        contraindication.
        Type `CodeableReference` (represented as `dict` in JSON). """

        super(ClinicalUseDefinitionContraindicationOtherTherapy, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(ClinicalUseDefinitionContraindicationOtherTherapy, self).elementProperties()
        js.extend([
            ("relationshipType", "relationshipType", codeableconcept.CodeableConcept, False, None, True),
            ("therapy", "therapy", codeablereference.CodeableReference, False, None, True),
        ])
        return js


class ClinicalUseDefinitionIndication(backboneelement.BackboneElement):
    """ Specifics for when this is an indication.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.diseaseSymptomProcedure = None
        """ The situation that is being documented as an indicaton for this
        item.
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.diseaseStatus = None
        """ The status of the disease or symptom for the indication.
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.comorbidity = None
        """ A comorbidity or coinfection as part of the indication.
        List of `CodeableReference` items (represented as `dict` in JSON). """

        self.intendedEffect = None
        """ The intended effect, aim or strategy to be achieved.
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.durationRange = None
        """ Timing or duration information.
        Type `Range` (represented as `dict` in JSON). """

        self.durationString = None
        """ Timing or duration information.
        Type `str`. """

        self.undesirableEffect = None
        """ An unwanted side effect or negative outcome of the subject of this
        resource when being used for this indication.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.otherTherapy = None
        """ The use of the medicinal product in relation to other therapies
        described as part of the indication.
        List of `ClinicalUseDefinitionContraindicationOtherTherapy` items (represented as `dict` in JSON). """

        super(ClinicalUseDefinitionIndication, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(ClinicalUseDefinitionIndication, self).elementProperties()
        js.extend([
            ("diseaseSymptomProcedure", "diseaseSymptomProcedure", codeablereference.CodeableReference, False, None, False),
            ("diseaseStatus", "diseaseStatus", codeablereference.CodeableReference, False, None, False),
            ("comorbidity", "comorbidity", codeablereference.CodeableReference, True, None, False),
            ("intendedEffect", "intendedEffect", codeablereference.CodeableReference, False, None, False),
            ("durationRange", "durationRange", range.Range, False, "duration", False),
            ("durationString", "durationString", str, False, "duration", False),
            ("undesirableEffect", "undesirableEffect", fhirreference.FHIRReference, True, None, False),
            ("otherTherapy", "otherTherapy", ClinicalUseDefinitionContraindicationOtherTherapy, True, None, False),
        ])
        return js


class ClinicalUseDefinitionInteraction(backboneelement.BackboneElement):
    """ Specifics for when this is an interaction.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.interactant = None
        """ The specific medication, food, substance or laboratory test that
        interacts.
        List of `ClinicalUseDefinitionInteractionInteractant` items (represented as `dict` in JSON). """

        self.type = None
        """ The type of the interaction e.g. drug-drug interaction, drug-lab
        test interaction.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.effect = None
        """ The effect of the interaction, for example "reduced gastric
        absorption of primary medication".
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.incidence = None
        """ The incidence of the interaction, e.g. theoretical, observed.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.management = None
        """ Actions for managing the interaction.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(ClinicalUseDefinitionInteraction, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(ClinicalUseDefinitionInteraction, self).elementProperties()
        js.extend([
            ("interactant", "interactant", ClinicalUseDefinitionInteractionInteractant, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("effect", "effect", codeablereference.CodeableReference, False, None, False),
            ("incidence", "incidence", codeableconcept.CodeableConcept, False, None, False),
            ("management", "management", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ClinicalUseDefinitionInteractionInteractant(backboneelement.BackboneElement):
    """ The specific medication, food, substance or laboratory test that interacts.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.itemReference = None
        """ The specific medication, food or laboratory test that interacts.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.itemCodeableConcept = None
        """ The specific medication, food or laboratory test that interacts.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ClinicalUseDefinitionInteractionInteractant, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(ClinicalUseDefinitionInteractionInteractant, self).elementProperties()
        js.extend([
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
        ])
        return js


class ClinicalUseDefinitionUndesirableEffect(backboneelement.BackboneElement):
    """ A possible negative outcome from the use of this treatment.

    Describe the possible undesirable effects (negative outcomes) from the use
    of the medicinal product as treatment.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.symptomConditionEffect = None
        """ The situation in which the undesirable effect may manifest.
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.classification = None
        """ High level classification of the effect.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.frequencyOfOccurrence = None
        """ How often the effect is seen.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ClinicalUseDefinitionUndesirableEffect, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(ClinicalUseDefinitionUndesirableEffect, self).elementProperties()
        js.extend([
            ("symptomConditionEffect", "symptomConditionEffect", codeablereference.CodeableReference, False, None, False),
            ("classification", "classification", codeableconcept.CodeableConcept, False, None, False),
            ("frequencyOfOccurrence", "frequencyOfOccurrence", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ClinicalUseDefinitionWarning(backboneelement.BackboneElement):
    """ Critical environmental, health or physical risks or hazards. For example
    'Do not operate heavy machinery', 'May cause drowsiness'.

    A critical piece of information about environmental, health or physical
    risks or hazards that serve as caution to the user. For example 'Do not
    operate heavy machinery', 'May cause drowsiness', or 'Get medical
    advice/attention if you feel unwell'.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ A textual definition of this warning, with formatting.
        Type `str`. """

        self.code = None
        """ A coded or unformatted textual definition of this warning.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ClinicalUseDefinitionWarning, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(ClinicalUseDefinitionWarning, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import ClinicalUseDefinitionType
except ImportError:
    ClinicalUseDefinitionType = sys.modules[__package__ + '.ClinicalUseDefinitionType']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import codeablereference
except ImportError:
    codeablereference = sys.modules[__package__ + '.codeablereference']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']