#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/ParameterDefinition) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import element

class ParameterDefinition(element.Element):
    """ Definition of a parameter to a module.

    The parameters to the module. This collection specifies both the input and
    output parameters. Input parameters are provided by the caller as part of
    the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.name = None
        """ Name used to access the parameter value.
        Type `str`. """

        self.use = None
        """ in | out.
        Type `str`. """

        self.min = None
        """ Minimum cardinality.
        Type `int`. """

        self.max = None
        """ Maximum cardinality (a number of *).
        Type `str`. """

        self.documentation = None
        """ A brief description of the parameter.
        Type `str`. """

        self.type = None
        """ What type of value.
        Type `str`. """

        self.profile = None
        """ What profile the value is expected to be.
        Type `str`. """

        super(ParameterDefinition, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(ParameterDefinition, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("use", "use", OperationParameterUse.str, False, None, True),
            ("min", "min", int, False, None, False),
            ("max", "max", str, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("profile", "profile", str, False, None, False),
        ])
        return js


import sys
try:
    from . import OperationParameterUse
except ImportError:
    OperationParameterUse = sys.modules[__package__ + '.OperationParameterUse']