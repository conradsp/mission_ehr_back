#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Period) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import element

class Period(element.Element):
    """ Time range defined by start and end date/time.

    A time period defined by a start and end date and optionally time.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.start = None
        """ Starting time with inclusive boundary.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.end = None
        """ End time with inclusive boundary, if not ongoing.
        Type `FHIRDate` (represented as `str` in JSON). """

        super(Period, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Period, self).elementProperties()
        js.extend([
            ("start", "start", fhirdate.FHIRDate, False, None, False),
            ("end", "end", fhirdate.FHIRDate, False, None, False),
        ])
        return js


import sys
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']