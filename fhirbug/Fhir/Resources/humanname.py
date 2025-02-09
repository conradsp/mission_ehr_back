#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/HumanName) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import element

class HumanName(element.Element):
    """ Name of a human - parts and usage.

    A human's name with the ability to identify parts and usage.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.use = None
        """ usual | official | temp | nickname | anonymous | old | maiden.
        Type `str`. """

        self.text = None
        """ Text representation of the full name.
        Type `str`. """

        self.family = None
        """ Family name (often called 'Surname').
        Type `str`. """

        self.given = None
        """ Given names (not always 'first'). Includes middle names.
        List of `str` items. """

        self.prefix = None
        """ Parts that come before the name.
        List of `str` items. """

        self.suffix = None
        """ Parts that come after the name.
        List of `str` items. """

        self.period = None
        """ Time period when name was/is in use.
        Type `Period` (represented as `dict` in JSON). """

        super(HumanName, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(HumanName, self).elementProperties()
        js.extend([
            ("use", "use", NameUse.str, False, None, False),
            ("text", "text", str, False, None, False),
            ("family", "family", str, False, None, False),
            ("given", "given", str, True, None, False),
            ("prefix", "prefix", str, True, None, False),
            ("suffix", "suffix", str, True, None, False),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


import sys
try:
    from . import NameUse
except ImportError:
    NameUse = sys.modules[__package__ + '.NameUse']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']