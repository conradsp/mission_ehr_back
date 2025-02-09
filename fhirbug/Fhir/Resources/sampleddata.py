#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/SampledData) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import element

class SampledData(element.Element):
    """ A series of measurements taken by a device.

    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.origin = None
        """ Zero value and units.
        Type `Quantity` (represented as `dict` in JSON). """

        self.period = None
        """ Number of milliseconds between samples.
        Type `float`. """

        self.factor = None
        """ Multiply data by this before adding to origin.
        Type `float`. """

        self.lowerLimit = None
        """ Lower limit of detection.
        Type `float`. """

        self.upperLimit = None
        """ Upper limit of detection.
        Type `float`. """

        self.dimensions = None
        """ Number of sample points at each time point.
        Type `int`. """

        self.data = None
        """ Decimal values with spaces, or "E" | "U" | "L".
        Type `str`. """

        super(SampledData, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SampledData, self).elementProperties()
        js.extend([
            ("origin", "origin", quantity.Quantity, False, None, True),
            ("period", "period", float, False, None, True),
            ("factor", "factor", float, False, None, False),
            ("lowerLimit", "lowerLimit", float, False, None, False),
            ("upperLimit", "upperLimit", float, False, None, False),
            ("dimensions", "dimensions", int, False, None, True),
            ("data", "data", str, False, None, False),
        ])
        return js


import sys
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']