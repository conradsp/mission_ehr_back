#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Distance) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import quantity

class Distance(quantity.Quantity):
    """ A length - a value with a unit that is a physical distance.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        super(Distance, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

