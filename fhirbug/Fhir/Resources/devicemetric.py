#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/DeviceMetric) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class DeviceMetric(domainresource.DomainResource):
    """ Measurement, calculation or setting capability of a medical device.

    Describes a measurement, calculation or setting capability of a medical
    device.
    """

    resource_type = "DeviceMetric"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ Instance identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.type = None
        """ Identity of metric, for example Heart Rate or PEEP Setting.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.unit = None
        """ Unit of Measure for the Metric.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.source = None
        """ Describes the link to the source Device.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.parent = None
        """ Describes the link to the parent Device.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.operationalStatus = None
        """ on | off | standby | entered-in-error.
        Type `str`. """

        self.color = None
        """ black | red | green | yellow | blue | magenta | cyan | white.
        Type `str`. """

        self.category = None
        """ measurement | setting | calculation | unspecified.
        Type `str`. """

        self.measurementPeriod = None
        """ Describes the measurement repetition time.
        Type `Timing` (represented as `dict` in JSON). """

        self.calibration = None
        """ Describes the calibrations that have been performed or that are
        required to be performed.
        List of `DeviceMetricCalibration` items (represented as `dict` in JSON). """

        super(DeviceMetric, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(DeviceMetric, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("operationalStatus", "operationalStatus", DeviceMetricOperationalStatus.str, False, None, False),
            ("color", "color", DeviceMetricColor.str, False, None, False),
            ("category", "category", DeviceMetricCategory.str, False, None, True),
            ("measurementPeriod", "measurementPeriod", timing.Timing, False, None, False),
            ("calibration", "calibration", DeviceMetricCalibration, True, None, False),
        ])
        return js


from . import backboneelement

class DeviceMetricCalibration(backboneelement.BackboneElement):
    """ Describes the calibrations that have been performed or that are required to
    be performed.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ unspecified | offset | gain | two-point.
        Type `str`. """

        self.state = None
        """ not-calibrated | calibration-required | calibrated | unspecified.
        Type `str`. """

        self.time = None
        """ Describes the time last calibration has been performed.
        Type `FHIRDate` (represented as `str` in JSON). """

        super(DeviceMetricCalibration, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(DeviceMetricCalibration, self).elementProperties()
        js.extend([
            ("type", "type", DeviceMetricCalibrationType.str, False, None, False),
            ("state", "state", DeviceMetricCalibrationState.str, False, None, False),
            ("time", "time", fhirdate.FHIRDate, False, None, False),
        ])
        return js


import sys
try:
    from . import DeviceMetricCalibrationState
except ImportError:
    DeviceMetricCalibrationState = sys.modules[__package__ + '.DeviceMetricCalibrationState']
try:
    from . import DeviceMetricCalibrationType
except ImportError:
    DeviceMetricCalibrationType = sys.modules[__package__ + '.DeviceMetricCalibrationType']
try:
    from . import DeviceMetricCategory
except ImportError:
    DeviceMetricCategory = sys.modules[__package__ + '.DeviceMetricCategory']
try:
    from . import DeviceMetricColor
except ImportError:
    DeviceMetricColor = sys.modules[__package__ + '.DeviceMetricColor']
try:
    from . import DeviceMetricOperationalStatus
except ImportError:
    DeviceMetricOperationalStatus = sys.modules[__package__ + '.DeviceMetricOperationalStatus']
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
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']