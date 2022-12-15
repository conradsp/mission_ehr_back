#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/PackagedProductDefinition) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class PackagedProductDefinition(domainresource.DomainResource):
    """ A medically related item or items, in a container or package.
    """

    resource_type = "PackagedProductDefinition"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ A unique identifier for this package as whole.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.name = None
        """ A name for this package. Typically as listed in a drug formulary,
        catalogue, inventory etc.
        Type `str`. """

        self.type = None
        """ A high level category e.g. medicinal product, raw material,
        shipping container etc.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.packageFor = None
        """ The product that this is a pack for.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.status = None
        """ The status within the lifecycle of this item. High level - not
        intended to duplicate details elsewhere e.g. legal status, or
        authorization/marketing status.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.statusDate = None
        """ The date at which the given status became applicable.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.containedItemQuantity = None
        """ A total of the complete count of contained items of a particular
        type/form, independent of sub-packaging or organization. This can
        be considered as the pack size.
        List of `Quantity` items (represented as `dict` in JSON). """

        self.description = None
        """ Textual description. Note that this is not the name of the package
        or product.
        Type `str`. """

        self.legalStatusOfSupply = None
        """ The legal status of supply of the packaged item as classified by
        the regulator.
        List of `PackagedProductDefinitionLegalStatusOfSupply` items (represented as `dict` in JSON). """

        self.marketingStatus = None
        """ Allows specifying that an item is on the market for sale, or that
        it is not available, and the dates and locations associated.
        List of `MarketingStatus` items (represented as `dict` in JSON). """

        self.characteristic = None
        """ Allows the key features to be recorded, such as "hospital pack",
        "nurse prescribable".
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.copackagedIndicator = None
        """ If the drug product is supplied with another item such as a diluent
        or adjuvant.
        Type `bool`. """

        self.manufacturer = None
        """ Manufacturer of this package type (multiple means these are all
        possible manufacturers).
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.package = None
        """ A packaging item, as a container for medically related items,
        possibly with other packaging items within, or a packaging
        component, such as bottle cap.
        Type `PackagedProductDefinitionPackage` (represented as `dict` in JSON). """

        super(PackagedProductDefinition, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(PackagedProductDefinition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("packageFor", "packageFor", fhirreference.FHIRReference, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("containedItemQuantity", "containedItemQuantity", quantity.Quantity, True, None, False),
            ("description", "description", str, False, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", PackagedProductDefinitionLegalStatusOfSupply, True, None, False),
            ("marketingStatus", "marketingStatus", marketingstatus.MarketingStatus, True, None, False),
            ("characteristic", "characteristic", codeableconcept.CodeableConcept, True, None, False),
            ("copackagedIndicator", "copackagedIndicator", bool, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("package", "package", PackagedProductDefinitionPackage, False, None, False),
        ])
        return js


from . import backboneelement

class PackagedProductDefinitionLegalStatusOfSupply(backboneelement.BackboneElement):
    """ The legal status of supply of the packaged item as classified by the
    regulator.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ The actual status of supply. In what situation this package type
        may be supplied for use.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ The place where the legal status of supply applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(PackagedProductDefinitionLegalStatusOfSupply, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(PackagedProductDefinitionLegalStatusOfSupply, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class PackagedProductDefinitionPackage(backboneelement.BackboneElement):
    """ A packaging item, as a container for medically related items, possibly with
    other packaging items within, or a packaging component, such as bottle cap.

    A packaging item, as a container for medically related items, possibly with
    other packaging items within, or a packaging component, such as bottle cap
    (which is not a device or a medication manufactured item).
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ An identifier that is specific to this particular part of the
        packaging. Including possibly a Data Carrier Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.type = None
        """ The physical type of the container of the items.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.quantity = None
        """ The quantity of this level of packaging in the package that
        contains it (with the outermost level being 1).
        Type `int`. """

        self.material = None
        """ Material type of the package item.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.alternateMaterial = None
        """ A possible alternate material for this part of the packaging, that
        is allowed to be used instead of the usual material.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.shelfLifeStorage = None
        """ Shelf Life and storage information.
        List of `PackagedProductDefinitionPackageShelfLifeStorage` items (represented as `dict` in JSON). """

        self.manufacturer = None
        """ Manufacturer of this package Item (multiple means these are all
        possible manufacturers).
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.property = None
        """ General characteristics of this item.
        List of `PackagedProductDefinitionPackageProperty` items (represented as `dict` in JSON). """

        self.containedItem = None
        """ The item(s) within the packaging.
        List of `PackagedProductDefinitionPackageContainedItem` items (represented as `dict` in JSON). """

        self.package = None
        """ Allows containers (and parts of containers) within containers,
        still a single packaged product.
        List of `PackagedProductDefinitionPackage` items (represented as `dict` in JSON). """

        super(PackagedProductDefinitionPackage, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(PackagedProductDefinitionPackage, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("quantity", "quantity", int, False, None, False),
            ("material", "material", codeableconcept.CodeableConcept, True, None, False),
            ("alternateMaterial", "alternateMaterial", codeableconcept.CodeableConcept, True, None, False),
            ("shelfLifeStorage", "shelfLifeStorage", PackagedProductDefinitionPackageShelfLifeStorage, True, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("property", "property", PackagedProductDefinitionPackageProperty, True, None, False),
            ("containedItem", "containedItem", PackagedProductDefinitionPackageContainedItem, True, None, False),
            ("package", "package", PackagedProductDefinitionPackage, True, None, False),
        ])
        return js


class PackagedProductDefinitionPackageContainedItem(backboneelement.BackboneElement):
    """ The item(s) within the packaging.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.item = None
        """ The actual item(s) of medication, as manufactured, or a device, or
        other medically related item (food, biologicals, raw materials,
        medical fluids, gases etc.), as contained in the package.
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.amount = None
        """ The number of this type of item within this packaging.
        Type `Quantity` (represented as `dict` in JSON). """

        super(PackagedProductDefinitionPackageContainedItem, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(PackagedProductDefinitionPackageContainedItem, self).elementProperties()
        js.extend([
            ("item", "item", codeablereference.CodeableReference, False, None, True),
            ("amount", "amount", quantity.Quantity, False, None, False),
        ])
        return js


class PackagedProductDefinitionPackageProperty(backboneelement.BackboneElement):
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

        super(PackagedProductDefinitionPackageProperty, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(PackagedProductDefinitionPackageProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
        ])
        return js


class PackagedProductDefinitionPackageShelfLifeStorage(backboneelement.BackboneElement):
    """ Shelf Life and storage information.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ This describes the shelf life, taking into account various
        scenarios such as shelf life of the packaged Medicinal Product
        itself, shelf life after transformation where necessary and shelf
        life after the first opening of a bottle, etc. The shelf life type
        shall be specified using an appropriate controlled vocabulary The
        controlled term and the controlled term identifier shall be
        specified.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.periodDuration = None
        """ The shelf life time period can be specified using a numerical value
        for the period of time and its unit of time measurement The unit of
        measurement shall be specified in accordance with ISO 11240 and the
        resulting terminology The symbol and the symbol identifier shall be
        used.
        Type `Duration` (represented as `dict` in JSON). """

        self.periodString = None
        """ The shelf life time period can be specified using a numerical value
        for the period of time and its unit of time measurement The unit of
        measurement shall be specified in accordance with ISO 11240 and the
        resulting terminology The symbol and the symbol identifier shall be
        used.
        Type `str`. """

        self.specialPrecautionsForStorage = None
        """ Special precautions for storage, if any, can be specified using an
        appropriate controlled vocabulary. The controlled term and the
        controlled term identifier shall be specified.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(PackagedProductDefinitionPackageShelfLifeStorage, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(PackagedProductDefinitionPackageShelfLifeStorage, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("periodDuration", "periodDuration", duration.Duration, False, "period", False),
            ("periodString", "periodString", str, False, "period", False),
            ("specialPrecautionsForStorage", "specialPrecautionsForStorage", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


import sys
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
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
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
    from . import marketingstatus
except ImportError:
    marketingstatus = sys.modules[__package__ + '.marketingstatus']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']