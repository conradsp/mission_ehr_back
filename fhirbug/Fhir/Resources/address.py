#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Address) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import element

class Address(element.Element):
    """ An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).

    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).  This data type may be used to convey
    addresses for use in delivering mail as well as for visiting locations
    which might not be valid for mail delivery.  There are a variety of postal
    address formats defined around the world.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.use = None
        """ home | work | temp | old | billing - purpose of this address.
        Type `str`. """

        self.type = None
        """ postal | physical | both.
        Type `str`. """

        self.text = None
        """ Text representation of the address.
        Type `str`. """

        self.line = None
        """ Street name, number, direction & P.O. Box etc..
        List of `str` items. """

        self.city = None
        """ Name of city, town etc..
        Type `str`. """

        self.district = None
        """ District name (aka county).
        Type `str`. """

        self.state = None
        """ Sub-unit of country (abbreviations ok).
        Type `str`. """

        self.postalCode = None
        """ Postal code for area.
        Type `str`. """

        self.country = None
        """ Country (e.g. can be ISO 3166 2 or 3 letter code).
        Type `str`. """

        self.period = None
        """ Time period when address was/is in use.
        Type `Period` (represented as `dict` in JSON). """

        super(Address, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Address, self).elementProperties()
        js.extend([
            ("use", "use", AddressUse.str, False, None, False),
            ("type", "type", AddressType.str, False, None, False),
            ("text", "text", str, False, None, False),
            ("line", "line", str, True, None, False),
            ("city", "city", str, False, None, False),
            ("district", "district", str, False, None, False),
            ("state", "state", str, False, None, False),
            ("postalCode", "postalCode", str, False, None, False),
            ("country", "country", str, False, None, False),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


import sys
try:
    from . import AddressType
except ImportError:
    AddressType = sys.modules[__package__ + '.AddressType']
try:
    from . import AddressUse
except ImportError:
    AddressUse = sys.modules[__package__ + '.AddressUse']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']