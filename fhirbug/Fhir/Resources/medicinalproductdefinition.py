#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/MedicinalProductDefinition) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class MedicinalProductDefinition(domainresource.DomainResource):
    """ Detailed definition of a medicinal product.

    A medicinal product, being a substance or combination of substances that is
    intended to treat, prevent or diagnose a disease, or to restore, correct or
    modify physiological functions by exerting a pharmacological, immunological
    or metabolic action. This resource is intended to define and detail such
    products and their properties, for uses other than direct patient care
    (e.g. regulatory use, or drug catalogs).
    """

    resource_type = "MedicinalProductDefinition"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Business identifier for this product. Could be an MPID.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.type = None
        """ Regulatory type, e.g. Investigational or Authorized.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.domain = None
        """ If this medicine applies to human or veterinary uses.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.version = None
        """ A business identifier relating to a specific version of the product.
        Type `str`. """

        self.status = None
        """ The status within the lifecycle of this product record.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.statusDate = None
        """ The date at which the given status became applicable.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ General description of this product.
        Type `str`. """

        self.combinedPharmaceuticalDoseForm = None
        """ The dose form for a single part product, or combined form of a
        multiple part product.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.route = None
        """ The path by which the product is taken into or makes contact with
        the body.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.indication = None
        """ Description of indication(s) for this product, used when structured
        indications are not required.
        Type `str`. """

        self.legalStatusOfSupply = None
        """ The legal status of supply of the medicinal product as classified
        by the regulator.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.additionalMonitoringIndicator = None
        """ Whether the Medicinal Product is subject to additional monitoring
        for regulatory reasons.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.specialMeasures = None
        """ Whether the Medicinal Product is subject to special measures for
        regulatory reasons.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.pediatricUseIndicator = None
        """ If authorised for use in children.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.classification = None
        """ Allows the product to be classified by various systems.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.marketingStatus = None
        """ Marketing status of the medicinal product, in contrast to marketing
        authorization.
        List of `MarketingStatus` items (represented as `dict` in JSON). """

        self.packagedMedicinalProduct = None
        """ Package type for the product.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.ingredient = None
        """ The ingredients of this medicinal product - when not detailed in
        other resources.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.impurity = None
        """ Any component of the drug product which is not the chemical entity
        defined as the drug substance, or an excipient in the drug product.
        List of `CodeableReference` items (represented as `dict` in JSON). """

        self.attachedDocument = None
        """ Additional documentation about the medicinal product.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.masterFile = None
        """ A master file for the medicinal product (e.g. Pharmacovigilance
        System Master File).
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.contact = None
        """ A product specific contact, person (in a role), or an organization.
        List of `MedicinalProductDefinitionContact` items (represented as `dict` in JSON). """

        self.clinicalTrial = None
        """ Clinical trials or studies that this product is involved in.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.code = None
        """ A code that this product is known by, within some formal
        terminology.
        List of `Coding` items (represented as `dict` in JSON). """

        self.name = None
        """ The product's name, including full name and possibly coded parts.
        List of `MedicinalProductDefinitionName` items (represented as `dict` in JSON). """

        self.crossReference = None
        """ Reference to another product, e.g. for linking authorised to
        investigational product.
        List of `MedicinalProductDefinitionCrossReference` items (represented as `dict` in JSON). """

        self.operation = None
        """ A manufacturing or administrative process for the medicinal product.
        List of `MedicinalProductDefinitionOperation` items (represented as `dict` in JSON). """

        self.characteristic = None
        """ Key product features such as "sugar free", "modified release".
        List of `MedicinalProductDefinitionCharacteristic` items (represented as `dict` in JSON). """

        super(MedicinalProductDefinition, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(MedicinalProductDefinition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("domain", "domain", codeableconcept.CodeableConcept, False, None, False),
            ("version", "version", str, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("combinedPharmaceuticalDoseForm", "combinedPharmaceuticalDoseForm", codeableconcept.CodeableConcept, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, True, None, False),
            ("indication", "indication", str, False, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, False),
            ("additionalMonitoringIndicator", "additionalMonitoringIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("specialMeasures", "specialMeasures", codeableconcept.CodeableConcept, True, None, False),
            ("pediatricUseIndicator", "pediatricUseIndicator", codeableconcept.CodeableConcept, False, None, False),
            ("classification", "classification", codeableconcept.CodeableConcept, True, None, False),
            ("marketingStatus", "marketingStatus", marketingstatus.MarketingStatus, True, None, False),
            ("packagedMedicinalProduct", "packagedMedicinalProduct", codeableconcept.CodeableConcept, True, None, False),
            ("ingredient", "ingredient", codeableconcept.CodeableConcept, True, None, False),
            ("impurity", "impurity", codeablereference.CodeableReference, True, None, False),
            ("attachedDocument", "attachedDocument", fhirreference.FHIRReference, True, None, False),
            ("masterFile", "masterFile", fhirreference.FHIRReference, True, None, False),
            ("contact", "contact", MedicinalProductDefinitionContact, True, None, False),
            ("clinicalTrial", "clinicalTrial", fhirreference.FHIRReference, True, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("name", "name", MedicinalProductDefinitionName, True, None, True),
            ("crossReference", "crossReference", MedicinalProductDefinitionCrossReference, True, None, False),
            ("operation", "operation", MedicinalProductDefinitionOperation, True, None, False),
            ("characteristic", "characteristic", MedicinalProductDefinitionCharacteristic, True, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductDefinitionCharacteristic(backboneelement.BackboneElement):
    """ Key product features such as "sugar free", "modified release".

    Allows the key product features to be recorded, such as "sugar free",
    "modified release", "parallel import".
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

        super(MedicinalProductDefinitionCharacteristic, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(MedicinalProductDefinitionCharacteristic, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
        ])
        return js


class MedicinalProductDefinitionContact(backboneelement.BackboneElement):
    """ A product specific contact, person (in a role), or an organization.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ Allows the contact to be classified, for example QPPV,
        Pharmacovigilance Enquiry Information.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.contact = None
        """ A product specific contact, person (in a role), or an organization.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(MedicinalProductDefinitionContact, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(MedicinalProductDefinitionContact, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class MedicinalProductDefinitionCrossReference(backboneelement.BackboneElement):
    """ Reference to another product, e.g. for linking authorised to
    investigational product.

    Reference to another product, e.g. for linking authorised to
    investigational product, or a virtual product.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.product = None
        """ Reference to another product, e.g. for linking authorised to
        investigational product.
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.type = None
        """ The type of relationship, for instance branded to generic or
        virtual to actual product.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(MedicinalProductDefinitionCrossReference, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(MedicinalProductDefinitionCrossReference, self).elementProperties()
        js.extend([
            ("product", "product", codeablereference.CodeableReference, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MedicinalProductDefinitionName(backboneelement.BackboneElement):
    """ The product's name, including full name and possibly coded parts.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.productName = None
        """ The full product name.
        Type `str`. """

        self.type = None
        """ Type of product name, such as rINN, BAN, Proprietary, Non-
        Proprietary.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.namePart = None
        """ Coding words or phrases of the name.
        List of `MedicinalProductDefinitionNameNamePart` items (represented as `dict` in JSON). """

        self.countryLanguage = None
        """ Country and jurisdiction where the name applies.
        List of `MedicinalProductDefinitionNameCountryLanguage` items (represented as `dict` in JSON). """

        super(MedicinalProductDefinitionName, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(MedicinalProductDefinitionName, self).elementProperties()
        js.extend([
            ("productName", "productName", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("namePart", "namePart", MedicinalProductDefinitionNameNamePart, True, None, False),
            ("countryLanguage", "countryLanguage", MedicinalProductDefinitionNameCountryLanguage, True, None, False),
        ])
        return js


class MedicinalProductDefinitionNameCountryLanguage(backboneelement.BackboneElement):
    """ Country and jurisdiction where the name applies.

    Country and jurisdiction where the name applies, and associated language.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.country = None
        """ Country code for where this name applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Jurisdiction code for where this name applies.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.language = None
        """ Language code for this name.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(MedicinalProductDefinitionNameCountryLanguage, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(MedicinalProductDefinitionNameCountryLanguage, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, False, None, True),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, False, None, False),
            ("language", "language", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class MedicinalProductDefinitionNameNamePart(backboneelement.BackboneElement):
    """ Coding words or phrases of the name.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.part = None
        """ A fragment of a product name.
        Type `str`. """

        self.type = None
        """ Identifying type for this part of the name (e.g. strength part).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(MedicinalProductDefinitionNameNamePart, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(MedicinalProductDefinitionNameNamePart, self).elementProperties()
        js.extend([
            ("part", "part", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class MedicinalProductDefinitionOperation(backboneelement.BackboneElement):
    """ A manufacturing or administrative process for the medicinal product.

    A manufacturing or administrative process or step associated with (or
    performed on) the medicinal product.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ The type of manufacturing operation e.g. manufacturing itself, re-
        packaging.
        Type `CodeableReference` (represented as `dict` in JSON). """

        self.effectiveDate = None
        """ Date range of applicability.
        Type `Period` (represented as `dict` in JSON). """

        self.organization = None
        """ The organization responsible for the particular process, e.g. the
        manufacturer or importer.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.confidentialityIndicator = None
        """ Specifies whether this process is considered proprietary or
        confidential.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(MedicinalProductDefinitionOperation, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(MedicinalProductDefinitionOperation, self).elementProperties()
        js.extend([
            ("type", "type", codeablereference.CodeableReference, False, None, False),
            ("effectiveDate", "effectiveDate", period.Period, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, True, None, False),
            ("confidentialityIndicator", "confidentialityIndicator", codeableconcept.CodeableConcept, False, None, False),
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
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']