#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/ContactPoint) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import element

class ContactPoint(element.Element):
    """ Details of a Technology mediated contact point (phone, fax, email, etc.).

    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.system = None
        """ phone | fax | email | pager | url | sms | other.
        Type `str`. """

        self.value = None
        """ The actual contact point details.
        Type `str`. """

        self.use = None
        """ home | work | temp | old | mobile - purpose of this contact point.
        Type `str`. """

        self.rank = None
        """ Specify preferred order of use (1 = highest).
        Type `int`. """

        self.period = None
        """ Time period when the contact point was/is in use.
        Type `Period` (represented as `dict` in JSON). """

        super(ContactPoint, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(ContactPoint, self).elementProperties()
        js.extend([
            ("system", "system", ContactPointSystem.str, False, None, False),
            ("value", "value", str, False, None, False),
            ("use", "use", ContactPointUse.str, False, None, False),
            ("rank", "rank", int, False, None, False),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


import sys
try:
    from . import ContactPointSystem
except ImportError:
    ContactPointSystem = sys.modules[__package__ + '.ContactPointSystem']
try:
    from . import ContactPointUse
except ImportError:
    ContactPointUse = sys.modules[__package__ + '.ContactPointUse']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']