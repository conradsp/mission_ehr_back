#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/AdministrableProductDefinition) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class AdministrableProductDefinition(domainresource.DomainResource):
    """ A medicinal product in the final form, suitable for administration - after
    any mixing of multiple components.

    A medicinal product in the final form which is suitable for administering
    to a patient (after any mixing of multiple components, dissolution etc. has
    been performed).
    """

    resource_type = "AdministrableProductDefinition"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ An identifier for the administrable product.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.formOf = None
        """ References a product from which one or more of the constituent
        parts of that product can be prepared and used as described by this
        administrable product.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.administrableDoseForm = None
        """ The dose form of the final product after necessary reconstitution
        or processing.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.unitOfPresentation = None
        """ The presentation type in which this item is given to a patient.
        e.g. for a spray - 'puff'.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.producedFrom = None
        """ Indicates the specific manufactured items that are part of the
        'formOf' product that are used in the preparation of this specific
        administrable form.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.ingredient = None
        """ The ingredients of this administrable medicinal product. This is
        only needed if the ingredients are not specified either using
        ManufacturedItemDefiniton, or using by incoming references from the
        Ingredient resource.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.device = None
        """ A device that is integral to the medicinal product, in effect being
        considered as an "ingredient" of the medicinal product.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.property = None
        """ Characteristics e.g. a product's onset of action.
        List of `AdministrableProductDefinitionProperty` items (represented as `dict` in JSON). """

        self.routeOfAdministration = None
        """ The path by which the product is taken into or makes contact with
        the body.
        List of `AdministrableProductDefinitionRouteOfAdministration` items (represented as `dict` in JSON). """

        super(AdministrableProductDefinition, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(AdministrableProductDefinition, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", PublicationStatus.str, False, None, True),
            ("formOf", "formOf", fhirreference.FHIRReference, True, None, False),
            ("administrableDoseForm", "administrableDoseForm", codeableconcept.CodeableConcept, False, None, False),
            ("unitOfPresentation", "unitOfPresentation", codeableconcept.CodeableConcept, False, None, False),
            ("producedFrom", "producedFrom", fhirreference.FHIRReference, True, None, False),
            ("ingredient", "ingredient", codeableconcept.CodeableConcept, True, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("property", "property", AdministrableProductDefinitionProperty, True, None, False),
            ("routeOfAdministration", "routeOfAdministration", AdministrableProductDefinitionRouteOfAdministration, True, None, True),
        ])
        return js


from . import backboneelement

class AdministrableProductDefinitionProperty(backboneelement.BackboneElement):
    """ Characteristics e.g. a product's onset of action.
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

        self.status = None
        """ The status of characteristic e.g. assigned or pending.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(AdministrableProductDefinitionProperty, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(AdministrableProductDefinitionProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class AdministrableProductDefinitionRouteOfAdministration(backboneelement.BackboneElement):
    """ The path by which the product is taken into or makes contact with the body.

    The path by which the product is taken into or makes contact with the body.
    In some regions this is referred to as the licenced or approved route.
    RouteOfAdministration cannot be used when the 'formOf' product already uses
    MedicinalProductDefinition.route (and vice versa).
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Coded expression for the route.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.firstDose = None
        """ The first dose (dose quantity) administered can be specified for
        the product.
        Type `Quantity` (represented as `dict` in JSON). """

        self.maxSingleDose = None
        """ The maximum single dose that can be administered.
        Type `Quantity` (represented as `dict` in JSON). """

        self.maxDosePerDay = None
        """ The maximum dose quantity to be administered in any one 24-h period.
        Type `Quantity` (represented as `dict` in JSON). """

        self.maxDosePerTreatmentPeriod = None
        """ The maximum dose per treatment period that can be administered.
        Type `Ratio` (represented as `dict` in JSON). """

        self.maxTreatmentPeriod = None
        """ The maximum treatment period during which the product can be
        administered.
        Type `Duration` (represented as `dict` in JSON). """

        self.targetSpecies = None
        """ A species for which this route applies.
        List of `AdministrableProductDefinitionRouteOfAdministrationTargetSpecies` items (represented as `dict` in JSON). """

        super(AdministrableProductDefinitionRouteOfAdministration, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(AdministrableProductDefinitionRouteOfAdministration, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("firstDose", "firstDose", quantity.Quantity, False, None, False),
            ("maxSingleDose", "maxSingleDose", quantity.Quantity, False, None, False),
            ("maxDosePerDay", "maxDosePerDay", quantity.Quantity, False, None, False),
            ("maxDosePerTreatmentPeriod", "maxDosePerTreatmentPeriod", ratio.Ratio, False, None, False),
            ("maxTreatmentPeriod", "maxTreatmentPeriod", duration.Duration, False, None, False),
            ("targetSpecies", "targetSpecies", AdministrableProductDefinitionRouteOfAdministrationTargetSpecies, True, None, False),
        ])
        return js


class AdministrableProductDefinitionRouteOfAdministrationTargetSpecies(backboneelement.BackboneElement):
    """ A species for which this route applies.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Coded expression for the species.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.withdrawalPeriod = None
        """ A species specific time during which consumption of animal product
        is not appropriate.
        List of `AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod` items (represented as `dict` in JSON). """

        super(AdministrableProductDefinitionRouteOfAdministrationTargetSpecies, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(AdministrableProductDefinitionRouteOfAdministrationTargetSpecies, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("withdrawalPeriod", "withdrawalPeriod", AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod, True, None, False),
        ])
        return js


class AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod(backboneelement.BackboneElement):
    """ A species specific time during which consumption of animal product is not
    appropriate.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.tissue = None
        """ The type of tissue for which the withdrawal period applies, e.g.
        meat, milk.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.value = None
        """ A value for the time.
        Type `Quantity` (represented as `dict` in JSON). """

        self.supportingInformation = None
        """ Extra information about the withdrawal period.
        Type `str`. """

        super(AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod, self).elementProperties()
        js.extend([
            ("tissue", "tissue", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", quantity.Quantity, False, None, True),
            ("supportingInformation", "supportingInformation", str, False, None, False),
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']