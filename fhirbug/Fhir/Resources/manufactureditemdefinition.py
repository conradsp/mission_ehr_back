#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/ManufacturedItemDefinition) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class ManufacturedItemDefinition(domainresource.DomainResource):
    """ The definition and characteristics of a medicinal manufactured item, such
    as a tablet or capsule, as contained in a packaged medicinal product.
    """

    resource_type = "ManufacturedItemDefinition"

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
        """ draft | active | retired | unknown.
        Type `str`. """

        self.manufacturedDoseForm = None
        """ Dose form as manufactured (before any necessary transformation).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.unitOfPresentation = None
        """ The “real world” units in which the quantity of the item is
        described.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.manufacturer = None
        """ Manufacturer of the item (Note that this should be named
        "manufacturer" but it currently causes technical issues).
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.ingredient = None
        """ The ingredients of this manufactured item. Only needed if these are
        not specified by incoming references from the Ingredient resource.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.property = None
        """ General characteristics of this item.
        List of `ManufacturedItemDefinitionProperty` items (represented as `dict` in JSON). """

        super(ManufacturedItemDefinition, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(ManufacturedItemDefinition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", PublicationStatus.str, False, None, True),
            ("manufacturedDoseForm", "manufacturedDoseForm", codeableconcept.CodeableConcept, False, None, True),
            ("unitOfPresentation", "unitOfPresentation", codeableconcept.CodeableConcept, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("ingredient", "ingredient", codeableconcept.CodeableConcept, True, None, False),
            ("property", "property", ManufacturedItemDefinitionProperty, True, None, False),
        ])
        return js


from . import backboneelement

class ManufacturedItemDefinitionProperty(backboneelement.BackboneElement):
    """ General characteristics of this item.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ A code expressing the type of characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueCodeableConcept = None
        """ A value for the characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueQuantity = None
        """ A value for the characteristic.
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueDate = None
        """ A value for the characteristic.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueBoolean = None
        """ A value for the characteristic.
        Type `bool`. """

        self.valueAttachment = None
        """ A value for the characteristic.
        Type `Attachment` (represented as `dict` in JSON). """

        super(ManufacturedItemDefinitionProperty, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(ManufacturedItemDefinitionProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
        ])
        return js


import sys
try:
    from . import PublicationStatus
except ImportError:
    PublicationStatus = sys.modules[__package__ + '.PublicationStatus']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
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