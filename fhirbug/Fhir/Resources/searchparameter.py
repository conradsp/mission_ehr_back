#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/SearchParameter) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class SearchParameter(domainresource.DomainResource):
    """ Search parameter for a resource.

    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """

    resource_type = "SearchParameter"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.url = None
        """ Canonical identifier for this search parameter, represented as a
        URI (globally unique).
        Type `str`. """

        self.version = None
        """ Business version of the search parameter.
        Type `str`. """

        self.name = None
        """ Name for this search parameter (computer friendly).
        Type `str`. """

        self.derivedFrom = None
        """ Original definition for the search parameter.
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.description = None
        """ Natural language description of the search parameter.
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for search parameter (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.purpose = None
        """ Why this search parameter is defined.
        Type `str`. """

        self.code = None
        """ Code used in URL.
        Type `str`. """

        self.base = None
        """ The resource type(s) this search parameter applies to.
        List of `str` items. """

        self.type = None
        """ number | date | string | token | reference | composite | quantity |
        uri | special.
        Type `str`. """

        self.expression = None
        """ FHIRPath expression that extracts the values.
        Type `str`. """

        self.xpath = None
        """ XPath that extracts the values.
        Type `str`. """

        self.xpathUsage = None
        """ normal | phonetic | nearby | distance | other.
        Type `str`. """

        self.target = None
        """ Types of resource (if a resource reference).
        List of `str` items. """

        self.multipleOr = None
        """ Allow multiple values per parameter (or).
        Type `bool`. """

        self.multipleAnd = None
        """ Allow multiple parameters (and).
        Type `bool`. """

        self.comparator = None
        """ eq | ne | gt | lt | ge | le | sa | eb | ap.
        List of `str` items. """

        self.modifier = None
        """ missing | exact | contains | not | text | in | not-in | below |
        above | type | identifier | ofType.
        List of `str` items. """

        self.chain = None
        """ Chained names supported.
        List of `str` items. """

        self.component = None
        """ For Composite resources to define the parts.
        List of `SearchParameterComponent` items (represented as `dict` in JSON). """

        super(SearchParameter, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SearchParameter, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("derivedFrom", "derivedFrom", str, False, None, False),
            ("status", "status", PublicationStatus.str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("description", "description", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("code", "code", str, False, None, True),
            ("base", "base", ResourceType.str, True, None, True),
            ("type", "type", SearchParamType.str, False, None, True),
            ("expression", "expression", str, False, None, False),
            ("xpath", "xpath", str, False, None, False),
            ("xpathUsage", "xpathUsage", XPathUsageType.str, False, None, False),
            ("target", "target", ResourceType.str, True, None, False),
            ("multipleOr", "multipleOr", bool, False, None, False),
            ("multipleAnd", "multipleAnd", bool, False, None, False),
            ("comparator", "comparator", SearchComparator.str, True, None, False),
            ("modifier", "modifier", SearchModifierCode.str, True, None, False),
            ("chain", "chain", str, True, None, False),
            ("component", "component", SearchParameterComponent, True, None, False),
        ])
        return js


from . import backboneelement

class SearchParameterComponent(backboneelement.BackboneElement):
    """ For Composite resources to define the parts.

    Used to define the parts of a composite search parameter.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.definition = None
        """ Defines how the part works.
        Type `str`. """

        self.expression = None
        """ Subexpression relative to main expression.
        Type `str`. """

        super(SearchParameterComponent, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SearchParameterComponent, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, True),
            ("expression", "expression", str, False, None, True),
        ])
        return js


import sys
try:
    from . import PublicationStatus
except ImportError:
    PublicationStatus = sys.modules[__package__ + '.PublicationStatus']
try:
    from . import ResourceType
except ImportError:
    ResourceType = sys.modules[__package__ + '.ResourceType']
try:
    from . import SearchComparator
except ImportError:
    SearchComparator = sys.modules[__package__ + '.SearchComparator']
try:
    from . import SearchModifierCode
except ImportError:
    SearchModifierCode = sys.modules[__package__ + '.SearchModifierCode']
try:
    from . import SearchParamType
except ImportError:
    SearchParamType = sys.modules[__package__ + '.SearchParamType']
try:
    from . import XPathUsageType
except ImportError:
    XPathUsageType = sys.modules[__package__ + '.XPathUsageType']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']