#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/RatioRange) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import element

class RatioRange(element.Element):
    """ Range of ratio values.

    A range of ratios expressed as a low and high numerator and a denominator.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.lowNumerator = None
        """ Low Numerator limit.
        Type `Quantity` (represented as `dict` in JSON). """

        self.highNumerator = None
        """ High Numerator limit.
        Type `Quantity` (represented as `dict` in JSON). """

        self.denominator = None
        """ Denominator value.
        Type `Quantity` (represented as `dict` in JSON). """

        super(RatioRange, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(RatioRange, self).elementProperties()
        js.extend([
            ("lowNumerator", "lowNumerator", quantity.Quantity, False, None, False),
            ("highNumerator", "highNumerator", quantity.Quantity, False, None, False),
            ("denominator", "denominator", quantity.Quantity, False, None, False),
        ])
        return js


import sys
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']