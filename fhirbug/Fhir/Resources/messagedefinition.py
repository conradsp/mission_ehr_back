#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/MessageDefinition) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class MessageDefinition(domainresource.DomainResource):
    """ A resource that defines a type of message that can be exchanged between
    systems.

    Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.
    """

    resource_type = "MessageDefinition"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.url = None
        """ Business Identifier for a given MessageDefinition.
        Type `str`. """

        self.identifier = None
        """ Primary key for the message definition on a given server.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the message definition.
        Type `str`. """

        self.name = None
        """ Name for this message definition (computer friendly).
        Type `str`. """

        self.title = None
        """ Name for this message definition (human friendly).
        Type `str`. """

        self.replaces = None
        """ Takes the place of.
        List of `str` items. """

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
        """ Natural language description of the message definition.
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for message definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.purpose = None
        """ Why this message definition is defined.
        Type `str`. """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.base = None
        """ Definition this one is based on.
        Type `str`. """

        self.parent = None
        """ Protocol/workflow this is part of.
        List of `str` items. """

        self.eventCoding = None
        """ Event code  or link to the EventDefinition.
        Type `Coding` (represented as `dict` in JSON). """

        self.eventUri = None
        """ Event code  or link to the EventDefinition.
        Type `str`. """

        self.category = None
        """ consequence | currency | notification.
        Type `str`. """

        self.focus = None
        """ Resource(s) that are the subject of the event.
        List of `MessageDefinitionFocus` items (represented as `dict` in JSON). """

        self.responseRequired = None
        """ always | on-error | never | on-success.
        Type `str`. """

        self.allowedResponse = None
        """ Responses to this message.
        List of `MessageDefinitionAllowedResponse` items (represented as `dict` in JSON). """

        self.graph = None
        """ Canonical reference to a GraphDefinition.
        List of `str` items. """

        super(MessageDefinition, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(MessageDefinition, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("replaces", "replaces", str, True, None, False),
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
            ("base", "base", str, False, None, False),
            ("parent", "parent", str, True, None, False),
            ("eventCoding", "eventCoding", coding.Coding, False, "event", True),
            ("eventUri", "eventUri", str, False, "event", True),
            ("category", "category", MessageSignificanceCategory.str, False, None, False),
            ("focus", "focus", MessageDefinitionFocus, True, None, False),
            ("responseRequired", "responseRequired", MessageheaderResponseRequest.str, False, None, False),
            ("allowedResponse", "allowedResponse", MessageDefinitionAllowedResponse, True, None, False),
            ("graph", "graph", str, True, None, False),
        ])
        return js


from . import backboneelement

class MessageDefinitionAllowedResponse(backboneelement.BackboneElement):
    """ Responses to this message.

    Indicates what types of messages may be sent as an application-level
    response to this message.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.message = None
        """ Reference to allowed message definition response.
        Type `str`. """

        self.situation = None
        """ When should this response be used.
        Type `str`. """

        super(MessageDefinitionAllowedResponse, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(MessageDefinitionAllowedResponse, self).elementProperties()
        js.extend([
            ("message", "message", str, False, None, True),
            ("situation", "situation", str, False, None, False),
        ])
        return js


class MessageDefinitionFocus(backboneelement.BackboneElement):
    """ Resource(s) that are the subject of the event.

    Identifies the resource (or resources) that are being addressed by the
    event.  For example, the Encounter for an admit message or two Account
    records for a merge.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Type of resource.
        Type `str`. """

        self.profile = None
        """ Profile that must be adhered to by focus.
        Type `str`. """

        self.min = None
        """ Minimum number of focuses of this type.
        Type `int`. """

        self.max = None
        """ Maximum number of focuses of this type.
        Type `str`. """

        super(MessageDefinitionFocus, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(MessageDefinitionFocus, self).elementProperties()
        js.extend([
            ("code", "code", ResourceType.str, False, None, True),
            ("profile", "profile", str, False, None, False),
            ("min", "min", int, False, None, True),
            ("max", "max", str, False, None, False),
        ])
        return js


import sys
try:
    from . import MessageSignificanceCategory
except ImportError:
    MessageSignificanceCategory = sys.modules[__package__ + '.MessageSignificanceCategory']
try:
    from . import MessageheaderResponseRequest
except ImportError:
    MessageheaderResponseRequest = sys.modules[__package__ + '.MessageheaderResponseRequest']
try:
    from . import PublicationStatus
except ImportError:
    PublicationStatus = sys.modules[__package__ + '.PublicationStatus']
try:
    from . import ResourceType
except ImportError:
    ResourceType = sys.modules[__package__ + '.ResourceType']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']