#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Ingredient) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class Ingredient(domainresource.DomainResource):
    """ An ingredient of a manufactured item or pharmaceutical product.
    """

    resource_type = "Ingredient"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ An identifier or code by which the ingredient can be referenced.
        Type `Identifier` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.for_fhir = None
        """ The product which this ingredient is a constituent part of.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.role = None
        """ Purpose of the ingredient within the product, e.g. active, inactive.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.function = None
        """ Precise action within the drug product, e.g. antioxidant,
        alkalizing agent.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.allergenicIndicator = None
        """ If the ingredient is a known or suspected allergen.
        Type `bool`. """

        self.manufacturer = None
        """ An organization that manufactures this ingredient.
        List of `IngredientManufacturer` items (represented as `dict` in JSON). """

        self.substance = None
        """ The substance that comprises this ingredient.
        Type `IngredientSubstance` (represented as `dict` in JSON). """

        super(Ingredient, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Ingredient, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("status", "status", PublicationStatus.str, False, None, True),
            ("for_fhir", "for", fhirreference.FHIRReference, True, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, True, None, False),
            ("allergenicIndicator", "allergenicIndicator", bool, False, None, False),
            ("manufacturer", "manufacturer", IngredientManufacturer, True, None, False),
            ("substance", "substance", IngredientSubstance, False, None, True),
        ])
        return js


from . import backboneelement

class IngredientManufacturer(backboneelement.BackboneElement):
    """ An organization that manufactures this ingredient.

    The organization(s) that manufacture this ingredient. Can be used to
    indicate:         1) Organizations we are aware of that manufacture this
    ingredient         2) Specific Manufacturer(s) currently being used
    3) Set of organisations allowed to manufacture this ingredient for this
    product         Users must be clear on the application of context relevant
    to their use case.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.role = None
        """ allowed | possible | actual.
        Type `str`. """

        self.manufacturer = None
        """ An organization that manufactures this ingredient.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(IngredientManufacturer, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(IngredientManufacturer, self).elementProperties()
        js.extend([
            ("role", "role", IngredientManufacturerRole.str, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class IngredientSubstance(backboneelement.BackboneElement):
    """ The substance that comprises this ingredient.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ A code or full resource that represents the ingredient substance.
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.strength = None
        """ The quantity of substance, per presentation, or per volume or mass,
        and type of quantity.
        List of `IngredientSubstanceStrength` items (represented as `dict` in JSON). """

        super(IngredientSubstance, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(IngredientSubstance, self).elementProperties()
        js.extend([
            ("code", "code", codeablereference.CodeableReference, False, None, True),
            ("strength", "strength", IngredientSubstanceStrength, True, None, False),
        ])
        return js


class IngredientSubstanceStrength(backboneelement.BackboneElement):
    """ The quantity of substance, per presentation, or per volume or mass, and
    type of quantity.

    The quantity of substance in the unit of presentation, or in the volume (or
    mass) of the single pharmaceutical product or manufactured item. The
    allowed repetitions do not represent different strengths, but are different
    representations - mathematically equivalent - of a single strength.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.presentationRatio = None
        """ The quantity of substance in the unit of presentation.
        Type `Ratio` (represented as `dict` in JSON). """

        self.presentationRatioRange = None
        """ The quantity of substance in the unit of presentation.
        Type `RatioRange` (represented as `dict` in JSON). """

        self.textPresentation = None
        """ Text of either the whole presentation strength or a part of it
        (rest being in Strength.presentation as a ratio).
        Type `str`. """

        self.concentrationRatio = None
        """ The strength per unitary volume (or mass).
        Type `Ratio` (represented as `dict` in JSON). """

        self.concentrationRatioRange = None
        """ The strength per unitary volume (or mass).
        Type `RatioRange` (represented as `dict` in JSON). """

        self.textConcentration = None
        """ Text of either the whole concentration strength or a part of it
        (rest being in Strength.concentration as a ratio).
        Type `str`. """

        self.measurementPoint = None
        """ When strength is measured at a particular point or distance.
        Type `str`. """

        self.country = None
        """ Where the strength range applies.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.referenceStrength = None
        """ Strength expressed in terms of a reference substance.
        List of `IngredientSubstanceStrengthReferenceStrength` items (represented as `dict` in JSON). """

        super(IngredientSubstanceStrength, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(IngredientSubstanceStrength, self).elementProperties()
        js.extend([
            ("presentationRatio", "presentationRatio", ratio.Ratio, False, "presentation", False),
            ("presentationRatioRange", "presentationRatioRange", ratiorange.RatioRange, False, "presentation", False),
            ("textPresentation", "textPresentation", str, False, None, False),
            ("concentrationRatio", "concentrationRatio", ratio.Ratio, False, "concentration", False),
            ("concentrationRatioRange", "concentrationRatioRange", ratiorange.RatioRange, False, "concentration", False),
            ("textConcentration", "textConcentration", str, False, None, False),
            ("measurementPoint", "measurementPoint", str, False, None, False),
            ("country", "country", codeableconcept.CodeableConcept, True, None, False),
            ("referenceStrength", "referenceStrength", IngredientSubstanceStrengthReferenceStrength, True, None, False),
        ])
        return js


class IngredientSubstanceStrengthReferenceStrength(backboneelement.BackboneElement):
    """ Strength expressed in terms of a reference substance.

    Strength expressed in terms of a reference substance. For when the
    ingredient strength is additionally expressed as equivalent to the strength
    of some other closely related substance (e.g. salt vs. base). Reference
    strength represents the strength (quantitative composition) of the active
    moiety of the active substance. There are situations when the active
    substance and active moiety are different, therefore both a strength and a
    reference strength are needed.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.substance = None
        """ Relevant reference substance.
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.strengthRatio = None
        """ Strength expressed in terms of a reference substance.
        Type `Ratio` (represented as `dict` in JSON). """

        self.strengthRatioRange = None
        """ Strength expressed in terms of a reference substance.
        Type `RatioRange` (represented as `dict` in JSON). """

        self.measurementPoint = None
        """ When strength is measured at a particular point or distance.
        Type `str`. """

        self.country = None
        """ Where the strength range applies.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(IngredientSubstanceStrengthReferenceStrength, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(IngredientSubstanceStrengthReferenceStrength, self).elementProperties()
        js.extend([
            ("substance", "substance", codeablereference.CodeableReference, False, None, False),
            ("strengthRatio", "strengthRatio", ratio.Ratio, False, "strength", True),
            ("strengthRatioRange", "strengthRatioRange", ratiorange.RatioRange, False, "strength", True),
            ("measurementPoint", "measurementPoint", str, False, None, False),
            ("country", "country", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


import sys
try:
    from . import IngredientManufacturerRole
except ImportError:
    IngredientManufacturerRole = sys.modules[__package__ + '.IngredientManufacturerRole']
try:
    from . import PublicationStatus
except ImportError:
    PublicationStatus = sys.modules[__package__ + '.PublicationStatus']
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
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import ratiorange
except ImportError:
    ratiorange = sys.modules[__package__ + '.ratiorange']