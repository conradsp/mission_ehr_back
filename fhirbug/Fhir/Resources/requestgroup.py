#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/RequestGroup) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class RequestGroup(domainresource.DomainResource):
    """ A group of related requests.

    A group of related requests that can be used to capture intended activities
    that have inter-dependencies such as "give this medication after that one".
    """

    resource_type = "RequestGroup"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """

        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """

        self.basedOn = None
        """ Fulfills plan, proposal, or order.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.replaces = None
        """ Request(s) replaced by this request.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.groupIdentifier = None
        """ Composite request this is part of.
        Type `Identifier` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `str`. """

        self.intent = None
        """ proposal | plan | directive | order | original-order | reflex-order
        | filler-order | instance-order | option.
        Type `str`. """

        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """

        self.code = None
        """ What's being requested/ordered.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.subject = None
        """ Who the request group is about.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.encounter = None
        """ Created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.authoredOn = None
        """ When the request group was authored.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.author = None
        """ Device or practitioner that authored the request group.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.reasonCode = None
        """ Why the request group is needed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Why the request group is needed.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.note = None
        """ Additional notes about the response.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.action = None
        """ Proposed actions, if any.
        List of `RequestGroupAction` items (represented as `dict` in JSON). """

        super(RequestGroup, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(RequestGroup, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("status", "status", str, False, None, True),
            ("intent", "intent", str, False, None, True),
            ("priority", "priority", str, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("action", "action", RequestGroupAction, True, None, False),
        ])
        return js


from . import backboneelement

class RequestGroupAction(backboneelement.BackboneElement):
    """ Proposed actions, if any.

    The actions, if any, produced by the evaluation of the artifact.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.prefix = None
        """ User-visible prefix for the action (e.g. 1. or A.).
        Type `str`. """

        self.title = None
        """ User-visible title.
        Type `str`. """

        self.description = None
        """ Short description of the action.
        Type `str`. """

        self.textEquivalent = None
        """ Static text equivalent of the action, used if the dynamic aspects
        cannot be interpreted by the receiving system.
        Type `str`. """

        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """

        self.code = None
        """ Code representing the meaning of the action or sub-actions.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.documentation = None
        """ Supporting documentation for the intended performer of the action.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """

        self.condition = None
        """ Whether or not the action is applicable.
        List of `RequestGroupActionCondition` items (represented as `dict` in JSON). """

        self.relatedAction = None
        """ Relationship to another action.
        List of `RequestGroupActionRelatedAction` items (represented as `dict` in JSON). """

        self.timingDateTime = None
        """ When the action should take place.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.timingAge = None
        """ When the action should take place.
        Type `Age` (represented as `dict` in JSON). """

        self.timingPeriod = None
        """ When the action should take place.
        Type `Period` (represented as `dict` in JSON). """

        self.timingDuration = None
        """ When the action should take place.
        Type `Duration` (represented as `dict` in JSON). """

        self.timingRange = None
        """ When the action should take place.
        Type `Range` (represented as `dict` in JSON). """

        self.timingTiming = None
        """ When the action should take place.
        Type `Timing` (represented as `dict` in JSON). """

        self.participant = None
        """ Who should perform the action.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.type = None
        """ create | update | remove | fire-event.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.groupingBehavior = None
        """ visual-group | logical-group | sentence-group.
        Type `str`. """

        self.selectionBehavior = None
        """ any | all | all-or-none | exactly-one | at-most-one | one-or-more.
        Type `str`. """

        self.requiredBehavior = None
        """ must | could | must-unless-documented.
        Type `str`. """

        self.precheckBehavior = None
        """ yes | no.
        Type `str`. """

        self.cardinalityBehavior = None
        """ single | multiple.
        Type `str`. """

        self.resource = None
        """ The target of the action.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.action = None
        """ Sub action.
        List of `RequestGroupAction` items (represented as `dict` in JSON). """

        super(RequestGroupAction, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(RequestGroupAction, self).elementProperties()
        js.extend([
            ("prefix", "prefix", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False),
            ("condition", "condition", RequestGroupActionCondition, True, None, False),
            ("relatedAction", "relatedAction", RequestGroupActionRelatedAction, True, None, False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingAge", "timingAge", age.Age, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False),
            ("timingRange", "timingRange", range.Range, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("participant", "participant", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("groupingBehavior", "groupingBehavior", ActionGroupingBehavior.str, False, None, False),
            ("selectionBehavior", "selectionBehavior", ActionSelectionBehavior.str, False, None, False),
            ("requiredBehavior", "requiredBehavior", ActionRequiredBehavior.str, False, None, False),
            ("precheckBehavior", "precheckBehavior", ActionPrecheckBehavior.str, False, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", ActionCardinalityBehavior.str, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("action", "action", RequestGroupAction, True, None, False),
        ])
        return js


class RequestGroupActionCondition(backboneelement.BackboneElement):
    """ Whether or not the action is applicable.

    An expression that describes applicability criteria, or start/stop
    conditions for the action.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.kind = None
        """ applicability | start | stop.
        Type `str`. """

        self.expression = None
        """ Boolean-valued expression.
        Type `Expression` (represented as `dict` in JSON). """

        super(RequestGroupActionCondition, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(RequestGroupActionCondition, self).elementProperties()
        js.extend([
            ("kind", "kind", ActionConditionKind.str, False, None, True),
            ("expression", "expression", expression.Expression, False, None, False),
        ])
        return js


class RequestGroupActionRelatedAction(backboneelement.BackboneElement):
    """ Relationship to another action.

    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.actionId = None
        """ What action this is related to.
        Type `str`. """

        self.relationship = None
        """ before-start | before | before-end | concurrent-with-start |
        concurrent | concurrent-with-end | after-start | after | after-end.
        Type `str`. """

        self.offsetDuration = None
        """ Time offset for the relationship.
        Type `Duration` (represented as `dict` in JSON). """

        self.offsetRange = None
        """ Time offset for the relationship.
        Type `Range` (represented as `dict` in JSON). """

        super(RequestGroupActionRelatedAction, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(RequestGroupActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", str, False, None, True),
            ("relationship", "relationship", ActionRelationshipType.str, False, None, True),
            ("offsetDuration", "offsetDuration", duration.Duration, False, "offset", False),
            ("offsetRange", "offsetRange", range.Range, False, "offset", False),
        ])
        return js


import sys
try:
    from . import ActionCardinalityBehavior
except ImportError:
    ActionCardinalityBehavior = sys.modules[__package__ + '.ActionCardinalityBehavior']
try:
    from . import ActionConditionKind
except ImportError:
    ActionConditionKind = sys.modules[__package__ + '.ActionConditionKind']
try:
    from . import ActionGroupingBehavior
except ImportError:
    ActionGroupingBehavior = sys.modules[__package__ + '.ActionGroupingBehavior']
try:
    from . import ActionPrecheckBehavior
except ImportError:
    ActionPrecheckBehavior = sys.modules[__package__ + '.ActionPrecheckBehavior']
try:
    from . import ActionRelationshipType
except ImportError:
    ActionRelationshipType = sys.modules[__package__ + '.ActionRelationshipType']
try:
    from . import ActionRequiredBehavior
except ImportError:
    ActionRequiredBehavior = sys.modules[__package__ + '.ActionRequiredBehavior']
try:
    from . import ActionSelectionBehavior
except ImportError:
    ActionSelectionBehavior = sys.modules[__package__ + '.ActionSelectionBehavior']
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']