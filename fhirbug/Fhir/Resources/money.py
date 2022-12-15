#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Money) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import element

class Money(element.Element):
    """ An amount of economic utility in some recognized currency.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.value = None
        """ Numerical value (with implicit precision).
        Type `float`. """

        self.currency = None
        """ ISO 4217 Currency Code.
        Type `str`. """

        super(Money, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Money, self).elementProperties()
        js.extend([
            ("value", "value", float, False, None, False),
            ("currency", "currency", str, False, None, False),
        ])
        return js

