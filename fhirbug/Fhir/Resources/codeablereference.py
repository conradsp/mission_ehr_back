#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/CodeableReference) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import element

class CodeableReference(element.Element):
    """ Reference to a resource or a concept.

    A reference to a resource (by instance), or instead, a reference to a
    concept defined in a terminology or ontology (by class).
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.concept = None
        """ Reference to a concept (by class).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.reference = None
        """ Reference to a resource (by instance).
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(CodeableReference, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CodeableReference, self).elementProperties()
        js.extend([
            ("concept", "concept", codeableconcept.CodeableConcept, False, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']