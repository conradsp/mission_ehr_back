#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Narrative) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import element

class Narrative(element.Element):
    """ Human-readable summary of the resource (essential clinical and business
    information).

    A human-readable summary of the resource conveying the essential clinical
    and business information for the resource.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.status = None
        """ generated | extensions | additional | empty.
        Type `str`. """

        self.div = None
        """ Limited xhtml content.
        Type `str`. """

        super(Narrative, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Narrative, self).elementProperties()
        js.extend([
            ("status", "status", NarrativeStatus.str, False, None, True),
            ("div", "div", str, False, None, True),
        ])
        return js


import sys
try:
    from . import NarrativeStatus
except ImportError:
    NarrativeStatus = sys.modules[__package__ + '.NarrativeStatus']