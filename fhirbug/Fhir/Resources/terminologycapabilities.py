#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class TerminologyCapabilities(domainresource.DomainResource):
    """ A statement of system capabilities.

    A TerminologyCapabilities resource documents a set of capabilities
    (behaviors) of a FHIR Terminology Server that may be used as a statement of
    actual server functionality or a statement of required or desired server
    implementation.
    """

    resource_type = "TerminologyCapabilities"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.url = None
        """ Canonical identifier for this terminology capabilities, represented
        as a URI (globally unique).
        Type `str`. """

        self.version = None
        """ Business version of the terminology capabilities.
        Type `str`. """

        self.name = None
        """ Name for this terminology capabilities (computer friendly).
        Type `str`. """

        self.title = None
        """ Name for this terminology capabilities (human friendly).
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
        """ Natural language description of the terminology capabilities.
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for terminology capabilities (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.purpose = None
        """ Why this terminology capabilities is defined.
        Type `str`. """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.kind = None
        """ instance | capability | requirements.
        Type `str`. """

        self.software = None
        """ Software that is covered by this terminology capability statement.
        Type `TerminologyCapabilitiesSoftware` (represented as `dict` in JSON). """

        self.implementation = None
        """ If this describes a specific instance.
        Type `TerminologyCapabilitiesImplementation` (represented as `dict` in JSON). """

        self.lockedDate = None
        """ Whether lockedDate is supported.
        Type `bool`. """

        self.codeSystem = None
        """ A code system supported by the server.
        List of `TerminologyCapabilitiesCodeSystem` items (represented as `dict` in JSON). """

        self.expansion = None
        """ Information about the [ValueSet/$expand](valueset-operation-
        expand.html) operation.
        Type `TerminologyCapabilitiesExpansion` (represented as `dict` in JSON). """

        self.codeSearch = None
        """ explicit | all.
        Type `str`. """

        self.validateCode = None
        """ Information about the [ValueSet/$validate-code](valueset-operation-
        validate-code.html) operation.
        Type `TerminologyCapabilitiesValidateCode` (represented as `dict` in JSON). """

        self.translation = None
        """ Information about the [ConceptMap/$translate](conceptmap-operation-
        translate.html) operation.
        Type `TerminologyCapabilitiesTranslation` (represented as `dict` in JSON). """

        self.closure = None
        """ Information about the [ConceptMap/$closure](conceptmap-operation-
        closure.html) operation.
        Type `TerminologyCapabilitiesClosure` (represented as `dict` in JSON). """

        super(TerminologyCapabilities, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TerminologyCapabilities, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("status", "status", PublicationStatus.str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("kind", "kind", CapabilityStatementKind.str, False, None, True),
            ("software", "software", TerminologyCapabilitiesSoftware, False, None, False),
            ("implementation", "implementation", TerminologyCapabilitiesImplementation, False, None, False),
            ("lockedDate", "lockedDate", bool, False, None, False),
            ("codeSystem", "codeSystem", TerminologyCapabilitiesCodeSystem, True, None, False),
            ("expansion", "expansion", TerminologyCapabilitiesExpansion, False, None, False),
            ("codeSearch", "codeSearch", CodeSearchSupport.str, False, None, False),
            ("validateCode", "validateCode", TerminologyCapabilitiesValidateCode, False, None, False),
            ("translation", "translation", TerminologyCapabilitiesTranslation, False, None, False),
            ("closure", "closure", TerminologyCapabilitiesClosure, False, None, False),
        ])
        return js


from . import backboneelement

class TerminologyCapabilitiesClosure(backboneelement.BackboneElement):
    """ Information about the [ConceptMap/$closure](conceptmap-operation-
    closure.html) operation.

    Whether the $closure operation is supported.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.translation = None
        """ If cross-system closure is supported.
        Type `bool`. """

        super(TerminologyCapabilitiesClosure, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesClosure, self).elementProperties()
        js.extend([
            ("translation", "translation", bool, False, None, False),
        ])
        return js


class TerminologyCapabilitiesCodeSystem(backboneelement.BackboneElement):
    """ A code system supported by the server.

    Identifies a code system that is supported by the server. If there is a no
    code system URL, then this declares the general assumptions a client can
    make about support for any CodeSystem resource.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.uri = None
        """ URI for the Code System.
        Type `str`. """

        self.version = None
        """ Version of Code System supported.
        List of `TerminologyCapabilitiesCodeSystemVersion` items (represented as `dict` in JSON). """

        self.subsumption = None
        """ Whether subsumption is supported.
        Type `bool`. """

        super(TerminologyCapabilitiesCodeSystem, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystem, self).elementProperties()
        js.extend([
            ("uri", "uri", str, False, None, False),
            ("version", "version", TerminologyCapabilitiesCodeSystemVersion, True, None, False),
            ("subsumption", "subsumption", bool, False, None, False),
        ])
        return js


class TerminologyCapabilitiesCodeSystemVersion(backboneelement.BackboneElement):
    """ Version of Code System supported.

    For the code system, a list of versions that are supported by the server.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Version identifier for this version.
        Type `str`. """

        self.isDefault = None
        """ If this is the default version for this code system.
        Type `bool`. """

        self.compositional = None
        """ If compositional grammar is supported.
        Type `bool`. """

        self.language = None
        """ Language Displays supported.
        List of `str` items. """

        self.filter = None
        """ Filter Properties supported.
        List of `TerminologyCapabilitiesCodeSystemVersionFilter` items (represented as `dict` in JSON). """

        self.property = None
        """ Properties supported for $lookup.
        List of `str` items. """

        super(TerminologyCapabilitiesCodeSystemVersion, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystemVersion, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("isDefault", "isDefault", bool, False, None, False),
            ("compositional", "compositional", bool, False, None, False),
            ("language", "language", str, True, None, False),
            ("filter", "filter", TerminologyCapabilitiesCodeSystemVersionFilter, True, None, False),
            ("property", "property", str, True, None, False),
        ])
        return js


class TerminologyCapabilitiesCodeSystemVersionFilter(backboneelement.BackboneElement):
    """ Filter Properties supported.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Code of the property supported.
        Type `str`. """

        self.op = None
        """ Operations supported for the property.
        List of `str` items. """

        super(TerminologyCapabilitiesCodeSystemVersionFilter, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystemVersionFilter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("op", "op", str, True, None, True),
        ])
        return js


class TerminologyCapabilitiesExpansion(backboneelement.BackboneElement):
    """ Information about the [ValueSet/$expand](valueset-operation-expand.html)
    operation.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.hierarchical = None
        """ Whether the server can return nested value sets.
        Type `bool`. """

        self.paging = None
        """ Whether the server supports paging on expansion.
        Type `bool`. """

        self.incomplete = None
        """ Allow request for incomplete expansions?.
        Type `bool`. """

        self.parameter = None
        """ Supported expansion parameter.
        List of `TerminologyCapabilitiesExpansionParameter` items (represented as `dict` in JSON). """

        self.textFilter = None
        """ Documentation about text searching works.
        Type `str`. """

        super(TerminologyCapabilitiesExpansion, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesExpansion, self).elementProperties()
        js.extend([
            ("hierarchical", "hierarchical", bool, False, None, False),
            ("paging", "paging", bool, False, None, False),
            ("incomplete", "incomplete", bool, False, None, False),
            ("parameter", "parameter", TerminologyCapabilitiesExpansionParameter, True, None, False),
            ("textFilter", "textFilter", str, False, None, False),
        ])
        return js


class TerminologyCapabilitiesExpansionParameter(backboneelement.BackboneElement):
    """ Supported expansion parameter.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.name = None
        """ Expansion Parameter name.
        Type `str`. """

        self.documentation = None
        """ Description of support for parameter.
        Type `str`. """

        super(TerminologyCapabilitiesExpansionParameter, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesExpansionParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


class TerminologyCapabilitiesImplementation(backboneelement.BackboneElement):
    """ If this describes a specific instance.

    Identifies a specific implementation instance that is described by the
    terminology capability statement - i.e. a particular installation, rather
    than the capabilities of a software program.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Describes this specific instance.
        Type `str`. """

        self.url = None
        """ Base URL for the implementation.
        Type `str`. """

        super(TerminologyCapabilitiesImplementation, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesImplementation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js


class TerminologyCapabilitiesSoftware(backboneelement.BackboneElement):
    """ Software that is covered by this terminology capability statement.

    Software that is covered by this terminology capability statement.  It is
    used when the statement describes the capabilities of a particular software
    version, independent of an installation.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.name = None
        """ A name the software is known by.
        Type `str`. """

        self.version = None
        """ Version covered by this statement.
        Type `str`. """

        super(TerminologyCapabilitiesSoftware, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesSoftware, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


class TerminologyCapabilitiesTranslation(backboneelement.BackboneElement):
    """ Information about the [ConceptMap/$translate](conceptmap-operation-
    translate.html) operation.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.needsMap = None
        """ Whether the client must identify the map.
        Type `bool`. """

        super(TerminologyCapabilitiesTranslation, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesTranslation, self).elementProperties()
        js.extend([
            ("needsMap", "needsMap", bool, False, None, True),
        ])
        return js


class TerminologyCapabilitiesValidateCode(backboneelement.BackboneElement):
    """ Information about the [ValueSet/$validate-code](valueset-operation-
    validate-code.html) operation.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.translations = None
        """ Whether translations are validated.
        Type `bool`. """

        super(TerminologyCapabilitiesValidateCode, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TerminologyCapabilitiesValidateCode, self).elementProperties()
        js.extend([
            ("translations", "translations", bool, False, None, True),
        ])
        return js


import sys
try:
    from . import CapabilityStatementKind
except ImportError:
    CapabilityStatementKind = sys.modules[__package__ + '.CapabilityStatementKind']
try:
    from . import CodeSearchSupport
except ImportError:
    CodeSearchSupport = sys.modules[__package__ + '.CodeSearchSupport']
try:
    from . import PublicationStatus
except ImportError:
    PublicationStatus = sys.modules[__package__ + '.PublicationStatus']
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