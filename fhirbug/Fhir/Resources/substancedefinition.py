#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/SubstanceDefinition) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class SubstanceDefinition(domainresource.DomainResource):
    """ The detailed description of a substance, typically at a level beyond what
    is used for prescribing.
    """

    resource_type = "SubstanceDefinition"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Identifier by which this substance is known.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.version = None
        """ A business level version identifier of the substance.
        Type `str`. """

        self.status = None
        """ Status of substance within the catalogue e.g. active, retired.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.classification = None
        """ A categorization, high level e.g. polymer or nucleic acid, or food,
        chemical, biological, or lower e.g. polymer linear or branch chain,
        or type of impurity.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.domain = None
        """ If the substance applies to human or veterinary use.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.grade = None
        """ The quality standard, established benchmark, to which substance
        complies (e.g. USP/NF, BP).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.description = None
        """ Textual description of the substance.
        Type `str`. """

        self.informationSource = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.note = None
        """ Textual comment about the substance's catalogue or registry record.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.manufacturer = None
        """ The entity that creates, makes, produces or fabricates the
        substance.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.supplier = None
        """ An entity that is the source for the substance. It may be different
        from the manufacturer.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.moiety = None
        """ Moiety, for structural modifications.
        List of `SubstanceDefinitionMoiety` items (represented as `dict` in JSON). """

        self.property = None
        """ General specifications for this substance.
        List of `SubstanceDefinitionProperty` items (represented as `dict` in JSON). """

        self.molecularWeight = None
        """ The molecular weight or weight range.
        List of `SubstanceDefinitionMolecularWeight` items (represented as `dict` in JSON). """

        self.structure = None
        """ Structural information.
        Type `SubstanceDefinitionStructure` (represented as `dict` in JSON). """

        self.code = None
        """ Codes associated with the substance.
        List of `SubstanceDefinitionstr` items (represented as `dict` in JSON). """

        self.name = None
        """ Names applicable to this substance.
        List of `SubstanceDefinitionName` items (represented as `dict` in JSON). """

        self.relationship = None
        """ A link between this substance and another.
        List of `SubstanceDefinitionRelationship` items (represented as `dict` in JSON). """

        self.sourceMaterial = None
        """ Material or taxonomic/anatomical source.
        Type `SubstanceDefinitionSourceMaterial` (represented as `dict` in JSON). """

        super(SubstanceDefinition, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceDefinition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("classification", "classification", codeableconcept.CodeableConcept, True, None, False),
            ("domain", "domain", codeableconcept.CodeableConcept, False, None, False),
            ("grade", "grade", codeableconcept.CodeableConcept, True, None, False),
            ("description", "description", str, False, None, False),
            ("informationSource", "informationSource", fhirreference.FHIRReference, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("supplier", "supplier", fhirreference.FHIRReference, True, None, False),
            ("moiety", "moiety", SubstanceDefinitionMoiety, True, None, False),
            ("property", "property", SubstanceDefinitionProperty, True, None, False),
            ("molecularWeight", "molecularWeight", SubstanceDefinitionMolecularWeight, True, None, False),
            ("structure", "structure", SubstanceDefinitionStructure, False, None, False),
            ("code", "code", SubstanceDefinitionstr, True, None, False),
            ("name", "name", SubstanceDefinitionName, True, None, False),
            ("relationship", "relationship", SubstanceDefinitionRelationship, True, None, False),
            ("sourceMaterial", "sourceMaterial", SubstanceDefinitionSourceMaterial, False, None, False),
        ])
        return js


from . import backboneelement

class SubstanceDefinitionMoiety(backboneelement.BackboneElement):
    """ Moiety, for structural modifications.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.role = None
        """ Role that the moiety is playing.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.identifier = None
        """ Identifier by which this moiety substance is known.
        Type `Identifier` (represented as `dict` in JSON). """

        self.name = None
        """ Textual name for this moiety substance.
        Type `str`. """

        self.stereochemistry = None
        """ Stereochemistry type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.opticalActivity = None
        """ Optical activity type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.molecularFormula = None
        """ Molecular formula for this moiety (e.g. with the Hill system).
        Type `str`. """

        self.amountQuantity = None
        """ Quantitative value for this moiety.
        Type `Quantity` (represented as `dict` in JSON). """

        self.amountString = None
        """ Quantitative value for this moiety.
        Type `str`. """

        self.measurementType = None
        """ The measurement type of the quantitative value.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(SubstanceDefinitionMoiety, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceDefinitionMoiety, self).elementProperties()
        js.extend([
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("name", "name", str, False, None, False),
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("measurementType", "measurementType", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceDefinitionMolecularWeight(backboneelement.BackboneElement):
    """ The molecular weight or weight range.

    The molecular weight or weight range (for proteins, polymers or nucleic
    acids).
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.method = None
        """ The method by which the weight was determined.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.type = None
        """ Type of molecular weight e.g. exact, average, weight average.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.amount = None
        """ Used to capture quantitative values for a variety of elements.
        Type `Quantity` (represented as `dict` in JSON). """

        super(SubstanceDefinitionMolecularWeight, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceDefinitionMolecularWeight, self).elementProperties()
        js.extend([
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("amount", "amount", quantity.Quantity, False, None, True),
        ])
        return js


class SubstanceDefinitionName(backboneelement.BackboneElement):
    """ Names applicable to this substance.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.name = None
        """ The actual name.
        Type `str`. """

        self.type = None
        """ Name type e.g. 'systematic',  'scientific, 'brand'.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.status = None
        """ The status of the name e.g. 'current', 'proposed'.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.preferred = None
        """ If this is the preferred name for this substance.
        Type `bool`. """

        self.language = None
        """ Human language that the name is written in.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.domain = None
        """ The use context of this name e.g. as an active ingredient or as a
        food colour additive.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ The jurisdiction where this name applies.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.synonym = None
        """ A synonym of this particular name, by which the substance is also
        known.
        List of `SubstanceDefinitionName` items (represented as `dict` in JSON). """

        self.translation = None
        """ A translation for this name into another human language.
        List of `SubstanceDefinitionName` items (represented as `dict` in JSON). """

        self.official = None
        """ Details of the official nature of this name.
        List of `SubstanceDefinitionNameOfficial` items (represented as `dict` in JSON). """

        self.source = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        super(SubstanceDefinitionName, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceDefinitionName, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("language", "language", codeableconcept.CodeableConcept, True, None, False),
            ("domain", "domain", codeableconcept.CodeableConcept, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("synonym", "synonym", SubstanceDefinitionName, True, None, False),
            ("translation", "translation", SubstanceDefinitionName, True, None, False),
            ("official", "official", SubstanceDefinitionNameOfficial, True, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class SubstanceDefinitionNameOfficial(backboneelement.BackboneElement):
    """ Details of the official nature of this name.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.authority = None
        """ Which authority uses this official name.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.status = None
        """ The status of the official name, for example 'draft', 'active'.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.date = None
        """ Date of official name change.
        Type `FHIRDate` (represented as `str` in JSON). """

        super(SubstanceDefinitionNameOfficial, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceDefinitionNameOfficial, self).elementProperties()
        js.extend([
            ("authority", "authority", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
        ])
        return js


class SubstanceDefinitionProperty(backboneelement.BackboneElement):
    """ General specifications for this substance.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ A code expressing the type of property.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueCodeableConcept = None
        """ A value for the property.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueQuantity = None
        """ A value for the property.
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueDate = None
        """ A value for the property.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueBoolean = None
        """ A value for the property.
        Type `bool`. """

        self.valueAttachment = None
        """ A value for the property.
        Type `Attachment` (represented as `dict` in JSON). """

        super(SubstanceDefinitionProperty, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceDefinitionProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
        ])
        return js


class SubstanceDefinitionRelationship(backboneelement.BackboneElement):
    """ A link between this substance and another.

    A link between this substance and another, with details of the
    relationship.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.substanceDefinitionReference = None
        """ A pointer to another substance, as a resource or a representational
        code.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.substanceDefinitionCodeableConcept = None
        """ A pointer to another substance, as a resource or a representational
        code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.type = None
        """ For example "salt to parent", "active moiety".
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.isDefining = None
        """ For example where an enzyme strongly bonds with a particular
        substance, this is a defining relationship for that enzyme, out of
        several possible relationships.
        Type `bool`. """

        self.amountQuantity = None
        """ A numeric factor for the relationship, e.g. that a substance salt
        has some percentage of active substance in relation to some other.
        Type `Quantity` (represented as `dict` in JSON). """

        self.amountRatio = None
        """ A numeric factor for the relationship, e.g. that a substance salt
        has some percentage of active substance in relation to some other.
        Type `Ratio` (represented as `dict` in JSON). """

        self.amountString = None
        """ A numeric factor for the relationship, e.g. that a substance salt
        has some percentage of active substance in relation to some other.
        Type `str`. """

        self.ratioHighLimitAmount = None
        """ For use when the numeric has an uncertain range.
        Type `Ratio` (represented as `dict` in JSON). """

        self.comparator = None
        """ An operator for the amount, for example "average", "approximately",
        "less than".
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.source = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        super(SubstanceDefinitionRelationship, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceDefinitionRelationship, self).elementProperties()
        js.extend([
            ("substanceDefinitionReference", "substanceDefinitionReference", fhirreference.FHIRReference, False, "substanceDefinition", False),
            ("substanceDefinitionCodeableConcept", "substanceDefinitionCodeableConcept", codeableconcept.CodeableConcept, False, "substanceDefinition", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("isDefining", "isDefining", bool, False, None, False),
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountRatio", "amountRatio", ratio.Ratio, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("ratioHighLimitAmount", "ratioHighLimitAmount", ratio.Ratio, False, None, False),
            ("comparator", "comparator", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class SubstanceDefinitionSourceMaterial(backboneelement.BackboneElement):
    """ Material or taxonomic/anatomical source.

    Material or taxonomic/anatomical source for the substance.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ Classification of the origin of the raw material. e.g. cat hair is
        an Animal source type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.genus = None
        """ The genus of an organism e.g. the Latin epithet of the plant/animal
        scientific name.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.species = None
        """ The species of an organism e.g. the Latin epithet of the species of
        the plant/animal.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.part = None
        """ An anatomical origin of the source material within an organism.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.countryOfOrigin = None
        """ The country or countries where the material is harvested.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(SubstanceDefinitionSourceMaterial, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceDefinitionSourceMaterial, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("genus", "genus", codeableconcept.CodeableConcept, False, None, False),
            ("species", "species", codeableconcept.CodeableConcept, False, None, False),
            ("part", "part", codeableconcept.CodeableConcept, False, None, False),
            ("countryOfOrigin", "countryOfOrigin", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class SubstanceDefinitionStructure(backboneelement.BackboneElement):
    """ Structural information.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.stereochemistry = None
        """ Stereochemistry type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.opticalActivity = None
        """ Optical activity type.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.molecularFormula = None
        """ Molecular formula (e.g. using the Hill system).
        Type `str`. """

        self.molecularFormulaByMoiety = None
        """ Specified per moiety according to the Hill system.
        Type `str`. """

        self.molecularWeight = None
        """ The molecular weight or weight range.
        Type `SubstanceDefinitionMolecularWeight` (represented as `dict` in JSON). """

        self.technique = None
        """ The method used to find the structure e.g. X-ray, NMR.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.sourceDocument = None
        """ Source of information for the structure.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.representation = None
        """ A depiction of the structure or characterization of the substance.
        List of `SubstanceDefinitionStructureRepresentation` items (represented as `dict` in JSON). """

        super(SubstanceDefinitionStructure, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceDefinitionStructure, self).elementProperties()
        js.extend([
            ("stereochemistry", "stereochemistry", codeableconcept.CodeableConcept, False, None, False),
            ("opticalActivity", "opticalActivity", codeableconcept.CodeableConcept, False, None, False),
            ("molecularFormula", "molecularFormula", str, False, None, False),
            ("molecularFormulaByMoiety", "molecularFormulaByMoiety", str, False, None, False),
            ("molecularWeight", "molecularWeight", SubstanceDefinitionMolecularWeight, False, None, False),
            ("technique", "technique", codeableconcept.CodeableConcept, True, None, False),
            ("sourceDocument", "sourceDocument", fhirreference.FHIRReference, True, None, False),
            ("representation", "representation", SubstanceDefinitionStructureRepresentation, True, None, False),
        ])
        return js


class SubstanceDefinitionStructureRepresentation(backboneelement.BackboneElement):
    """ A depiction of the structure or characterization of the substance.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ The kind of structural representation (e.g. full, partial).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.representation = None
        """ The structural representation or characterization as a text string
        in a standard format.
        Type `str`. """

        self.format = None
        """ The format of the representation e.g. InChI, SMILES, MOLFILE (note:
        not the physical file format).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.document = None
        """ An attachment with the structural representation e.g. a structure
        graphic or AnIML file.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(SubstanceDefinitionStructureRepresentation, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceDefinitionStructureRepresentation, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("representation", "representation", str, False, None, False),
            ("format", "format", codeableconcept.CodeableConcept, False, None, False),
            ("document", "document", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class SubstanceDefinitionstr(backboneelement.BackboneElement):
    """ Codes associated with the substance.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ The specific code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.status = None
        """ Status of the code assignment, for example 'provisional',
        'approved'.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.statusDate = None
        """ The date at which the code status was changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.note = None
        """ Any comment can be provided in this field.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.source = None
        """ Supporting literature.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        super(SubstanceDefinitionstr, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceDefinitionstr, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
        ])
        return js


import sys
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