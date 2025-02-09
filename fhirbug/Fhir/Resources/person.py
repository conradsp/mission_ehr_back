#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Person) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class Person(domainresource.DomainResource):
    """ A generic person record.

    Demographics and administrative information about a person independent of a
    specific health-related context.
    """

    resource_type = "Person"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ A human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.name = None
        """ A name associated with the person.
        List of `HumanName` items (represented as `dict` in JSON). """

        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """

        self.birthDate = None
        """ The date on which the person was born.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.address = None
        """ One or more addresses for the person.
        List of `Address` items (represented as `dict` in JSON). """

        self.photo = None
        """ Image of the person.
        Type `Attachment` (represented as `dict` in JSON). """

        self.managingOrganization = None
        """ The organization that is the custodian of the person record.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.active = None
        """ This person's record is in active use.
        Type `bool`. """

        self.link = None
        """ Link to a resource that concerns the same actual person.
        List of `PersonLink` items (represented as `dict` in JSON). """

        super(Person, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Person, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("gender", "gender", AdministrativeGender.str, False, None, False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("photo", "photo", attachment.Attachment, False, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("active", "active", bool, False, None, False),
            ("link", "link", PersonLink, True, None, False),
        ])
        return js


from . import backboneelement

class PersonLink(backboneelement.BackboneElement):
    """ Link to a resource that concerns the same actual person.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.target = None
        """ The resource to which this actual person is associated.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.assurance = None
        """ level1 | level2 | level3 | level4.
        Type `str`. """

        super(PersonLink, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(PersonLink, self).elementProperties()
        js.extend([
            ("target", "target", fhirreference.FHIRReference, False, None, True),
            ("assurance", "assurance", IdentityAssuranceLevel.str, False, None, False),
        ])
        return js


import sys
try:
    from . import AdministrativeGender
except ImportError:
    AdministrativeGender = sys.modules[__package__ + '.AdministrativeGender']
try:
    from . import IdentityAssuranceLevel
except ImportError:
    IdentityAssuranceLevel = sys.modules[__package__ + '.IdentityAssuranceLevel']
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + '.humanname']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']