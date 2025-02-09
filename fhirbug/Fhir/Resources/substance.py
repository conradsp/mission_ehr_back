#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Substance) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class Substance(domainresource.DomainResource):
    """ A homogeneous material with a definite composition.
    """

    resource_type = "Substance"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.status = None
        """ active | inactive | entered-in-error.
        Type `str`. """

        self.category = None
        """ What class/type of substance this is.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.code = None
        """ What substance this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.description = None
        """ Textual description of the substance, comments.
        Type `str`. """

        self.instance = None
        """ If this describes a specific package/container of the substance.
        List of `SubstanceInstance` items (represented as `dict` in JSON). """

        self.ingredient = None
        """ Composition information about the substance.
        List of `SubstanceIngredient` items (represented as `dict` in JSON). """

        super(Substance, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Substance, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", FHIRSubstanceStatus.str, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("description", "description", str, False, None, False),
            ("instance", "instance", SubstanceInstance, True, None, False),
            ("ingredient", "ingredient", SubstanceIngredient, True, None, False),
        ])
        return js


from . import backboneelement

class SubstanceIngredient(backboneelement.BackboneElement):
    """ Composition information about the substance.

    A substance can be composed of other substances.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.quantity = None
        """ Optional amount (concentration).
        Type `Ratio` (represented as `dict` in JSON). """

        self.substanceCodeableConcept = None
        """ A component of the substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.substanceReference = None
        """ A component of the substance.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(SubstanceIngredient, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceIngredient, self).elementProperties()
        js.extend([
            ("quantity", "quantity", ratio.Ratio, False, None, False),
            ("substanceCodeableConcept", "substanceCodeableConcept", codeableconcept.CodeableConcept, False, "substance", True),
            ("substanceReference", "substanceReference", fhirreference.FHIRReference, False, "substance", True),
        ])
        return js


class SubstanceInstance(backboneelement.BackboneElement):
    """ If this describes a specific package/container of the substance.

    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Identifier of the package/container.
        Type `Identifier` (represented as `dict` in JSON). """

        self.expiry = None
        """ When no longer valid to use.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.quantity = None
        """ Amount of substance in the package.
        Type `Quantity` (represented as `dict` in JSON). """

        super(SubstanceInstance, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceInstance, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("expiry", "expiry", fhirdate.FHIRDate, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
        ])
        return js


import sys
try:
    from . import FHIRSubstanceStatus
except ImportError:
    FHIRSubstanceStatus = sys.modules[__package__ + '.FHIRSubstanceStatus']
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']