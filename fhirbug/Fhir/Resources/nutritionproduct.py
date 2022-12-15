#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/NutritionProduct) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class NutritionProduct(domainresource.DomainResource):
    """ A product used for nutritional purposes.

    A food or fluid product that is consumed by patients.
    """

    resource_type = "NutritionProduct"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.status = None
        """ active | inactive | entered-in-error.
        Type `str`. """

        self.category = None
        """ A category or class of the nutrition product (halal, kosher, gluten
        free, vegan, etc).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.code = None
        """ A code designating a specific type of nutritional product.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.manufacturer = None
        """ Manufacturer, representative or officially responsible for the
        product.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.nutrient = None
        """ The product's nutritional information expressed by the nutrients.
        List of `NutritionProductNutrient` items (represented as `dict` in JSON). """

        self.ingredient = None
        """ Ingredients contained in this product.
        List of `NutritionProductIngredient` items (represented as `dict` in JSON). """

        self.knownAllergen = None
        """ Known or suspected allergens that are a part of this product.
        List of `CodeableReference` items (represented as `dict` in JSON). """

        self.productCharacteristic = None
        """ Specifies descriptive properties of the nutrition product.
        List of `NutritionProductProductCharacteristic` items (represented as `dict` in JSON). """

        self.instance = None
        """ One or several physical instances or occurrences of the nutrition
        product.
        Type `NutritionProductInstance` (represented as `dict` in JSON). """

        self.note = None
        """ Comments made about the product.
        List of `Annotation` items (represented as `dict` in JSON). """

        super(NutritionProduct, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(NutritionProduct, self).elementProperties()
        js.extend([
            ("status", "status", NutritionProductStatus.str, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("nutrient", "nutrient", NutritionProductNutrient, True, None, False),
            ("ingredient", "ingredient", NutritionProductIngredient, True, None, False),
            ("knownAllergen", "knownAllergen", codeablereference.CodeableReference, True, None, False),
            ("productCharacteristic", "productCharacteristic", NutritionProductProductCharacteristic, True, None, False),
            ("instance", "instance", NutritionProductInstance, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
        ])
        return js


from . import backboneelement

class NutritionProductIngredient(backboneelement.BackboneElement):
    """ Ingredients contained in this product.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.item = None
        """ The ingredient contained in the product.
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.amount = None
        """ The amount of ingredient that is in the product.
        List of `Ratio` items (represented as `dict` in JSON). """

        super(NutritionProductIngredient, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(NutritionProductIngredient, self).elementProperties()
        js.extend([
            ("item", "item", codeablereference.CodeableReference, False, None, True),
            ("amount", "amount", ratio.Ratio, True, None, False),
        ])
        return js


class NutritionProductInstance(backboneelement.BackboneElement):
    """ One or several physical instances or occurrences of the nutrition product.

    Conveys instance-level information about this product item. One or several
    physical, countable instances or occurrences of the product.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.quantity = None
        """ The amount of items or instances.
        Type `Quantity` (represented as `dict` in JSON). """

        self.identifier = None
        """ The identifier for the physical instance, typically a serial number.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.lotNumber = None
        """ The identification of the batch or lot of the product.
        Type `str`. """

        self.expiry = None
        """ The expiry date or date and time for the product.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.useBy = None
        """ The date until which the product is expected to be good for
        consumption.
        Type `FHIRDate` (represented as `str` in JSON). """

        super(NutritionProductInstance, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(NutritionProductInstance, self).elementProperties()
        js.extend([
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("expiry", "expiry", fhirdate.FHIRDate, False, None, False),
            ("useBy", "useBy", fhirdate.FHIRDate, False, None, False),
        ])
        return js


class NutritionProductNutrient(backboneelement.BackboneElement):
    """ The product's nutritional information expressed by the nutrients.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.item = None
        """ The (relevant) nutrients in the product.
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.amount = None
        """ The amount of nutrient expressed in one or more units: X per pack /
        per serving / per dose.
        List of `Ratio` items (represented as `dict` in JSON). """

        super(NutritionProductNutrient, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(NutritionProductNutrient, self).elementProperties()
        js.extend([
            ("item", "item", codeablereference.CodeableReference, False, None, False),
            ("amount", "amount", ratio.Ratio, True, None, False),
        ])
        return js


class NutritionProductProductCharacteristic(backboneelement.BackboneElement):
    """ Specifies descriptive properties of the nutrition product.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ Code specifying the type of characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueCodeableConcept = None
        """ The value of the characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueString = None
        """ The value of the characteristic.
        Type `str`. """

        self.valueQuantity = None
        """ The value of the characteristic.
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueBase64Binary = None
        """ The value of the characteristic.
        Type `str`. """

        self.valueAttachment = None
        """ The value of the characteristic.
        Type `Attachment` (represented as `dict` in JSON). """

        self.valueBoolean = None
        """ The value of the characteristic.
        Type `bool`. """

        super(NutritionProductProductCharacteristic, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(NutritionProductProductCharacteristic, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
        ])
        return js


import sys
try:
    from . import NutritionProductStatus
except ImportError:
    NutritionProductStatus = sys.modules[__package__ + '.NutritionProductStatus']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']