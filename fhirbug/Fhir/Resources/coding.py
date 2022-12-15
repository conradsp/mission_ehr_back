#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Coding) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import element

class Coding(element.Element):
    """ A reference to a code defined by a terminology system.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.system = None
        """ Identity of the terminology system.
        Type `str`. """

        self.version = None
        """ Version of the system - if relevant.
        Type `str`. """

        self.code = None
        """ Symbol in syntax defined by the system.
        Type `str`. """

        self.display = None
        """ Representation defined by the system.
        Type `str`. """

        self.userSelected = None
        """ If this coding was chosen directly by the user.
        Type `bool`. """

        super(Coding, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Coding, self).elementProperties()
        js.extend([
            ("system", "system", str, False, None, False),
            ("version", "version", str, False, None, False),
            ("code", "code", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("userSelected", "userSelected", bool, False, None, False),
        ])
        return js

