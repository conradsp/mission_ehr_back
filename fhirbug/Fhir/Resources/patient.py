#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Patient) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class Patient(domainresource.DomainResource):
    """ Information about an individual or animal receiving health care services.

    Demographics and other administrative information about an individual or
    animal receiving care or other health-related services.
    """

    resource_type = "Patient"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ An identifier for this patient.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.active = None
        """ Whether this patient's record is in active use.
        Type `bool`. """

        self.name = None
        """ A name associated with the patient.
        List of `HumanName` items (represented as `dict` in JSON). """

        self.telecom = None
        """ A contact detail for the individual.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """

        self.birthDate = None
        """ The date of birth for the individual.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.deceasedBoolean = None
        """ Indicates if the individual is deceased or not.
        Type `bool`. """

        self.deceasedDateTime = None
        """ Indicates if the individual is deceased or not.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.address = None
        """ An address for the individual.
        List of `Address` items (represented as `dict` in JSON). """

        self.maritalStatus = None
        """ Marital (civil) status of a patient.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.multipleBirthBoolean = None
        """ Whether patient is part of a multiple birth.
        Type `bool`. """

        self.multipleBirthInteger = None
        """ Whether patient is part of a multiple birth.
        Type `int`. """

        self.photo = None
        """ Image of the patient.
        List of `Attachment` items (represented as `dict` in JSON). """

        self.contact = None
        """ A contact party (e.g. guardian, partner, friend) for the patient.
        List of `PatientContact` items (represented as `dict` in JSON). """

        self.communication = None
        """ A language which may be used to communicate with the patient about
        his or her health.
        List of `PatientCommunication` items (represented as `dict` in JSON). """

        self.generalPractitioner = None
        """ Patient's nominated primary care provider.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.managingOrganization = None
        """ Organization that is the custodian of the patient record.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.link = None
        """ Link to another patient resource that concerns the same actual
        person.
        List of `PatientLink` items (represented as `dict` in JSON). """

        super(Patient, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Patient, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("active", "active", bool, False, None, False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("gender", "gender", AdministrativeGender.str, False, None, False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False),
            ("deceasedDateTime", "deceasedDateTime", fhirdate.FHIRDate, False, "deceased", False),
            ("address", "address", address.Address, True, None, False),
            ("maritalStatus", "maritalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("multipleBirthBoolean", "multipleBirthBoolean", bool, False, "multipleBirth", False),
            ("multipleBirthInteger", "multipleBirthInteger", int, False, "multipleBirth", False),
            ("photo", "photo", attachment.Attachment, True, None, False),
            ("contact", "contact", PatientContact, True, None, False),
            ("communication", "communication", PatientCommunication, True, None, False),
            ("generalPractitioner", "generalPractitioner", fhirreference.FHIRReference, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("link", "link", PatientLink, True, None, False),
        ])
        return js


from . import backboneelement

class PatientCommunication(backboneelement.BackboneElement):
    """ A language which may be used to communicate with the patient about his or
    her health.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.language = None
        """ The language which can be used to communicate with the patient
        about his or her health.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.preferred = None
        """ Language preference indicator.
        Type `bool`. """

        super(PatientCommunication, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(PatientCommunication, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, True),
            ("preferred", "preferred", bool, False, None, False),
        ])
        return js


class PatientContact(backboneelement.BackboneElement):
    """ A contact party (e.g. guardian, partner, friend) for the patient.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.relationship = None
        """ The kind of relationship.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.name = None
        """ A name associated with the contact person.
        Type `HumanName` (represented as `dict` in JSON). """

        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        self.address = None
        """ Address for the contact person.
        Type `Address` (represented as `dict` in JSON). """

        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """

        self.organization = None
        """ Organization that is associated with the contact.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.period = None
        """ The period during which this contact person or organization is
        valid to be contacted relating to this patient.
        Type `Period` (represented as `dict` in JSON). """

        super(PatientContact, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(PatientContact, self).elementProperties()
        js.extend([
            ("relationship", "relationship", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("address", "address", address.Address, False, None, False),
            ("gender", "gender", AdministrativeGender.str, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


class PatientLink(backboneelement.BackboneElement):
    """ Link to another patient resource that concerns the same actual person.

    Link to another patient resource that concerns the same actual patient.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.other = None
        """ The other patient or related person resource that the link refers
        to.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.type = None
        """ replaced-by | replaces | refer | seealso.
        Type `str`. """

        super(PatientLink, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(PatientLink, self).elementProperties()
        js.extend([
            ("other", "other", fhirreference.FHIRReference, False, None, True),
            ("type", "type", LinkType.str, False, None, True),
        ])
        return js


import sys
try:
    from . import AdministrativeGender
except ImportError:
    AdministrativeGender = sys.modules[__package__ + '.AdministrativeGender']
try:
    from . import LinkType
except ImportError:
    LinkType = sys.modules[__package__ + '.LinkType']
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']