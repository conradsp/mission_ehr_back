#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/TestReport) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class TestReport(domainresource.DomainResource):
    """ Describes the results of a TestScript execution.

    A summary of information based on the results of executing a TestScript.
    """

    resource_type = "TestReport"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """

        self.name = None
        """ Informal name of the executed TestScript.
        Type `str`. """

        self.status = None
        """ completed | in-progress | waiting | stopped | entered-in-error.
        Type `str`. """

        self.testScript = None
        """ Reference to the  version-specific TestScript that was executed to
        produce this TestReport.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.result = None
        """ pass | fail | pending.
        Type `str`. """

        self.score = None
        """ The final score (percentage of tests passed) resulting from the
        execution of the TestScript.
        Type `float`. """

        self.tester = None
        """ Name of the tester producing this report (Organization or
        individual).
        Type `str`. """

        self.issued = None
        """ When the TestScript was executed and this TestReport was generated.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.participant = None
        """ A participant in the test execution, either the execution engine, a
        client, or a server.
        List of `TestReportParticipant` items (represented as `dict` in JSON). """

        self.setup = None
        """ The results of the series of required setup operations before the
        tests were executed.
        Type `TestReportSetup` (represented as `dict` in JSON). """

        self.test = None
        """ A test executed from the test script.
        List of `TestReportTest` items (represented as `dict` in JSON). """

        self.teardown = None
        """ The results of running the series of required clean up steps.
        Type `TestReportTeardown` (represented as `dict` in JSON). """

        super(TestReport, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestReport, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("name", "name", str, False, None, False),
            ("status", "status", TestReportStatus.str, False, None, True),
            ("testScript", "testScript", fhirreference.FHIRReference, False, None, True),
            ("result", "result", TestReportResult.str, False, None, True),
            ("score", "score", float, False, None, False),
            ("tester", "tester", str, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("participant", "participant", TestReportParticipant, True, None, False),
            ("setup", "setup", TestReportSetup, False, None, False),
            ("test", "test", TestReportTest, True, None, False),
            ("teardown", "teardown", TestReportTeardown, False, None, False),
        ])
        return js


from . import backboneelement

class TestReportParticipant(backboneelement.BackboneElement):
    """ A participant in the test execution, either the execution engine, a client,
    or a server.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ test-engine | client | server.
        Type `str`. """

        self.uri = None
        """ The uri of the participant. An absolute URL is preferred.
        Type `str`. """

        self.display = None
        """ The display name of the participant.
        Type `str`. """

        super(TestReportParticipant, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestReportParticipant, self).elementProperties()
        js.extend([
            ("type", "type", TestReportParticipantType.str, False, None, True),
            ("uri", "uri", str, False, None, True),
            ("display", "display", str, False, None, False),
        ])
        return js


class TestReportSetup(backboneelement.BackboneElement):
    """ The results of the series of required setup operations before the tests
    were executed.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.action = None
        """ A setup operation or assert that was executed.
        List of `TestReportSetupAction` items (represented as `dict` in JSON). """

        super(TestReportSetup, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestReportSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestReportSetupAction, True, None, True),
        ])
        return js


class TestReportSetupAction(backboneelement.BackboneElement):
    """ A setup operation or assert that was executed.

    Action would contain either an operation or an assertion.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.operation = None
        """ The operation to perform.
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """

        self.assert_fhir = None
        """ The assertion to perform.
        Type `TestReportSetupActionAssert` (represented as `dict` in JSON). """

        super(TestReportSetupAction, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestReportSetupAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestReportSetupActionOperation, False, None, False),
            ("assert_fhir", "assert", TestReportSetupActionAssert, False, None, False),
        ])
        return js


class TestReportSetupActionAssert(backboneelement.BackboneElement):
    """ The assertion to perform.

    The results of the assertion performed on the previous operations.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.result = None
        """ pass | skip | fail | warning | error.
        Type `str`. """

        self.message = None
        """ A message associated with the result.
        Type `str`. """

        self.detail = None
        """ A link to further details on the result.
        Type `str`. """

        super(TestReportSetupActionAssert, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestReportSetupActionAssert, self).elementProperties()
        js.extend([
            ("result", "result", TestReportActionResult.str, False, None, True),
            ("message", "message", str, False, None, False),
            ("detail", "detail", str, False, None, False),
        ])
        return js


class TestReportSetupActionOperation(backboneelement.BackboneElement):
    """ The operation to perform.

    The operation performed.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.result = None
        """ pass | skip | fail | warning | error.
        Type `str`. """

        self.message = None
        """ A message associated with the result.
        Type `str`. """

        self.detail = None
        """ A link to further details on the result.
        Type `str`. """

        super(TestReportSetupActionOperation, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestReportSetupActionOperation, self).elementProperties()
        js.extend([
            ("result", "result", TestReportActionResult.str, False, None, True),
            ("message", "message", str, False, None, False),
            ("detail", "detail", str, False, None, False),
        ])
        return js


class TestReportTeardown(backboneelement.BackboneElement):
    """ The results of running the series of required clean up steps.

    The results of the series of operations required to clean up after all the
    tests were executed (successfully or otherwise).
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.action = None
        """ One or more teardown operations performed.
        List of `TestReportTeardownAction` items (represented as `dict` in JSON). """

        super(TestReportTeardown, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestReportTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestReportTeardownAction, True, None, True),
        ])
        return js


class TestReportTeardownAction(backboneelement.BackboneElement):
    """ One or more teardown operations performed.

    The teardown action will only contain an operation.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.operation = None
        """ The teardown operation performed.
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """

        super(TestReportTeardownAction, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestReportTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestReportSetupActionOperation, False, None, True),
        ])
        return js


class TestReportTest(backboneelement.BackboneElement):
    """ A test executed from the test script.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.name = None
        """ Tracking/logging name of this test.
        Type `str`. """

        self.description = None
        """ Tracking/reporting short description of the test.
        Type `str`. """

        self.action = None
        """ A test operation or assert that was performed.
        List of `TestReportTestAction` items (represented as `dict` in JSON). """

        super(TestReportTest, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestReportTest, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("action", "action", TestReportTestAction, True, None, True),
        ])
        return js


class TestReportTestAction(backboneelement.BackboneElement):
    """ A test operation or assert that was performed.

    Action would contain either an operation or an assertion.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.operation = None
        """ The operation performed.
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """

        self.assert_fhir = None
        """ The assertion performed.
        Type `TestReportSetupActionAssert` (represented as `dict` in JSON). """

        super(TestReportTestAction, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestReportTestAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestReportSetupActionOperation, False, None, False),
            ("assert_fhir", "assert", TestReportSetupActionAssert, False, None, False),
        ])
        return js


import sys
try:
    from . import TestReportActionResult
except ImportError:
    TestReportActionResult = sys.modules[__package__ + '.TestReportActionResult']
try:
    from . import TestReportParticipantType
except ImportError:
    TestReportParticipantType = sys.modules[__package__ + '.TestReportParticipantType']
try:
    from . import TestReportResult
except ImportError:
    TestReportResult = sys.modules[__package__ + '.TestReportResult']
try:
    from . import TestReportStatus
except ImportError:
    TestReportStatus = sys.modules[__package__ + '.TestReportStatus']
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