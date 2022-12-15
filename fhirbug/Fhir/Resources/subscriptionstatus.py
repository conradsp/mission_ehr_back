#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/SubscriptionStatus) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class SubscriptionStatus(domainresource.DomainResource):
    """ Status information about a Subscription provided during event notification.

    The SubscriptionStatus resource describes the state of a Subscription
    during notifications.
    """

    resource_type = "SubscriptionStatus"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.status = None
        """ requested | active | error | off | entered-in-error.
        Type `str`. """

        self.type = None
        """ handshake | heartbeat | event-notification | query-status | query-
        event.
        Type `str`. """

        self.eventsSinceSubscriptionStart = None
        """ Events since the Subscription was created.
        Type `str`. """

        self.notificationEvent = None
        """ Detailed information about any events relevant to this notification.
        List of `SubscriptionStatusNotificationEvent` items (represented as `dict` in JSON). """

        self.subscription = None
        """ Reference to the Subscription responsible for this notification.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.topic = None
        """ Reference to the SubscriptionTopic this notification relates to.
        Type `str`. """

        self.error = None
        """ List of errors on the subscription.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(SubscriptionStatus, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubscriptionStatus, self).elementProperties()
        js.extend([
            ("status", "status", SubscriptionStatus.str, False, None, False),
            ("type", "type", SubscriptionNotificationType.str, False, None, True),
            ("eventsSinceSubscriptionStart", "eventsSinceSubscriptionStart", str, False, None, False),
            ("notificationEvent", "notificationEvent", SubscriptionStatusNotificationEvent, True, None, False),
            ("subscription", "subscription", fhirreference.FHIRReference, False, None, True),
            ("topic", "topic", str, False, None, False),
            ("error", "error", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class SubscriptionStatusNotificationEvent(backboneelement.BackboneElement):
    """ Detailed information about any events relevant to this notification.

    Detailed information about events relevant to this subscription
    notification.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.eventNumber = None
        """ Event number.
        Type `str`. """

        self.timestamp = None
        """ The instant this event occurred.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.focus = None
        """ The focus of this event.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.additionalContext = None
        """ Additional context for this event.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        super(SubscriptionStatusNotificationEvent, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubscriptionStatusNotificationEvent, self).elementProperties()
        js.extend([
            ("eventNumber", "eventNumber", str, False, None, True),
            ("timestamp", "timestamp", fhirdate.FHIRDate, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, False, None, False),
            ("additionalContext", "additionalContext", fhirreference.FHIRReference, True, None, False),
        ])
        return js


import sys
try:
    from . import SubscriptionNotificationType
except ImportError:
    SubscriptionNotificationType = sys.modules[__package__ + '.SubscriptionNotificationType']
try:
    from . import SubscriptionStatus
except ImportError:
    SubscriptionStatus = sys.modules[__package__ + '.SubscriptionStatus']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']