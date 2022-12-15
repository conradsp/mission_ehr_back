#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/TestScript) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class TestScript(domainresource.DomainResource):
    """ Describes a set of tests.

    A structured set of tests against a FHIR server or client implementation to
    determine compliance against the FHIR specification.
    """

    resource_type = "TestScript"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.url = None
        """ Canonical identifier for this test script, represented as a URI
        (globally unique).
        Type `str`. """

        self.identifier = None
        """ Additional identifier for the test script.
        Type `Identifier` (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the test script.
        Type `str`. """

        self.name = None
        """ Name for this test script (computer friendly).
        Type `str`. """

        self.title = None
        """ Name for this test script (human friendly).
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
        """ Natural language description of the test script.
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for test script (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.purpose = None
        """ Why this test script is defined.
        Type `str`. """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.origin = None
        """ An abstract server representing a client or sender in a message
        exchange.
        List of `TestScriptOrigin` items (represented as `dict` in JSON). """

        self.destination = None
        """ An abstract server representing a destination or receiver in a
        message exchange.
        List of `TestScriptDestination` items (represented as `dict` in JSON). """

        self.metadata = None
        """ Required capability that is assumed to function correctly on the
        FHIR server being tested.
        Type `TestScriptMetadata` (represented as `dict` in JSON). """

        self.fixture = None
        """ Fixture in the test script - by reference (uri).
        List of `TestScriptFixture` items (represented as `dict` in JSON). """

        self.profile = None
        """ Reference of the validation profile.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.variable = None
        """ Placeholder for evaluated elements.
        List of `TestScriptVariable` items (represented as `dict` in JSON). """

        self.setup = None
        """ A series of required setup operations before tests are executed.
        Type `TestScriptSetup` (represented as `dict` in JSON). """

        self.test = None
        """ A test in this script.
        List of `TestScriptTest` items (represented as `dict` in JSON). """

        self.teardown = None
        """ A series of required clean up steps.
        Type `TestScriptTeardown` (represented as `dict` in JSON). """

        super(TestScript, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScript, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("status", "status", PublicationStatus.str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("origin", "origin", TestScriptOrigin, True, None, False),
            ("destination", "destination", TestScriptDestination, True, None, False),
            ("metadata", "metadata", TestScriptMetadata, False, None, False),
            ("fixture", "fixture", TestScriptFixture, True, None, False),
            ("profile", "profile", fhirreference.FHIRReference, True, None, False),
            ("variable", "variable", TestScriptVariable, True, None, False),
            ("setup", "setup", TestScriptSetup, False, None, False),
            ("test", "test", TestScriptTest, True, None, False),
            ("teardown", "teardown", TestScriptTeardown, False, None, False),
        ])
        return js


from . import backboneelement

class TestScriptDestination(backboneelement.BackboneElement):
    """ An abstract server representing a destination or receiver in a message
    exchange.

    An abstract server used in operations within this test script in the
    destination element.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.index = None
        """ The index of the abstract destination server starting at 1.
        Type `int`. """

        self.profile = None
        """ FHIR-Server | FHIR-SDC-FormManager | FHIR-SDC-FormReceiver | FHIR-
        SDC-FormProcessor.
        Type `Coding` (represented as `dict` in JSON). """

        super(TestScriptDestination, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptDestination, self).elementProperties()
        js.extend([
            ("index", "index", int, False, None, True),
            ("profile", "profile", coding.Coding, False, None, True),
        ])
        return js


class TestScriptFixture(backboneelement.BackboneElement):
    """ Fixture in the test script - by reference (uri).

    Fixture in the test script - by reference (uri). All fixtures are required
    for the test script to execute.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.autocreate = None
        """ Whether or not to implicitly create the fixture during setup.
        Type `bool`. """

        self.autodelete = None
        """ Whether or not to implicitly delete the fixture during teardown.
        Type `bool`. """

        self.resource = None
        """ Reference of the resource.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(TestScriptFixture, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptFixture, self).elementProperties()
        js.extend([
            ("autocreate", "autocreate", bool, False, None, True),
            ("autodelete", "autodelete", bool, False, None, True),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class TestScriptMetadata(backboneelement.BackboneElement):
    """ Required capability that is assumed to function correctly on the FHIR
    server being tested.

    The required capability must exist and are assumed to function correctly on
    the FHIR server being tested.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.link = None
        """ Links to the FHIR specification.
        List of `TestScriptMetadataLink` items (represented as `dict` in JSON). """

        self.capability = None
        """ Capabilities  that are assumed to function correctly on the FHIR
        server being tested.
        List of `TestScriptMetadataCapability` items (represented as `dict` in JSON). """

        super(TestScriptMetadata, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptMetadata, self).elementProperties()
        js.extend([
            ("link", "link", TestScriptMetadataLink, True, None, False),
            ("capability", "capability", TestScriptMetadataCapability, True, None, True),
        ])
        return js


class TestScriptMetadataCapability(backboneelement.BackboneElement):
    """ Capabilities  that are assumed to function correctly on the FHIR server
    being tested.

    Capabilities that must exist and are assumed to function correctly on the
    FHIR server being tested.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.required = None
        """ Are the capabilities required?.
        Type `bool`. """

        self.validated = None
        """ Are the capabilities validated?.
        Type `bool`. """

        self.description = None
        """ The expected capabilities of the server.
        Type `str`. """

        self.origin = None
        """ Which origin server these requirements apply to.
        List of `int` items. """

        self.destination = None
        """ Which server these requirements apply to.
        Type `int`. """

        self.link = None
        """ Links to the FHIR specification.
        List of `str` items. """

        self.capabilities = None
        """ Required Capability Statement.
        Type `str`. """

        super(TestScriptMetadataCapability, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptMetadataCapability, self).elementProperties()
        js.extend([
            ("required", "required", bool, False, None, True),
            ("validated", "validated", bool, False, None, True),
            ("description", "description", str, False, None, False),
            ("origin", "origin", int, True, None, False),
            ("destination", "destination", int, False, None, False),
            ("link", "link", str, True, None, False),
            ("capabilities", "capabilities", str, False, None, True),
        ])
        return js


class TestScriptMetadataLink(backboneelement.BackboneElement):
    """ Links to the FHIR specification.

    A link to the FHIR specification that this test is covering.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.url = None
        """ URL to the specification.
        Type `str`. """

        self.description = None
        """ Short description.
        Type `str`. """

        super(TestScriptMetadataLink, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptMetadataLink, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("description", "description", str, False, None, False),
        ])
        return js


class TestScriptOrigin(backboneelement.BackboneElement):
    """ An abstract server representing a client or sender in a message exchange.

    An abstract server used in operations within this test script in the origin
    element.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.index = None
        """ The index of the abstract origin server starting at 1.
        Type `int`. """

        self.profile = None
        """ FHIR-Client | FHIR-SDC-FormFiller.
        Type `Coding` (represented as `dict` in JSON). """

        super(TestScriptOrigin, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptOrigin, self).elementProperties()
        js.extend([
            ("index", "index", int, False, None, True),
            ("profile", "profile", coding.Coding, False, None, True),
        ])
        return js


class TestScriptSetup(backboneelement.BackboneElement):
    """ A series of required setup operations before tests are executed.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.action = None
        """ A setup operation or assert to perform.
        List of `TestScriptSetupAction` items (represented as `dict` in JSON). """

        super(TestScriptSetup, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptSetupAction, True, None, True),
        ])
        return js


class TestScriptSetupAction(backboneelement.BackboneElement):
    """ A setup operation or assert to perform.

    Action would contain either an operation or an assertion.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.operation = None
        """ The setup operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """

        self.assert_fhir = None
        """ The assertion to perform.
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """

        super(TestScriptSetupAction, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptSetupAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
            ("assert_fhir", "assert", TestScriptSetupActionAssert, False, None, False),
        ])
        return js


class TestScriptSetupActionAssert(backboneelement.BackboneElement):
    """ The assertion to perform.

    Evaluates the results of previous operations to determine if the server
    under test behaves appropriately.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.label = None
        """ Tracking/logging assertion label.
        Type `str`. """

        self.description = None
        """ Tracking/reporting assertion description.
        Type `str`. """

        self.direction = None
        """ response | request.
        Type `str`. """

        self.compareToSourceId = None
        """ Id of the source fixture to be evaluated.
        Type `str`. """

        self.compareToSourceExpression = None
        """ The FHIRPath expression to evaluate against the source fixture.
        Type `str`. """

        self.compareToSourcePath = None
        """ XPath or JSONPath expression to evaluate against the source fixture.
        Type `str`. """

        self.contentType = None
        """ Mime type to compare against the 'Content-Type' header.
        Type `str`. """

        self.expression = None
        """ The FHIRPath expression to be evaluated.
        Type `str`. """

        self.headerField = None
        """ HTTP header field name.
        Type `str`. """

        self.minimumId = None
        """ Fixture Id of minimum content resource.
        Type `str`. """

        self.navigationLinks = None
        """ Perform validation on navigation links?.
        Type `bool`. """

        self.operator = None
        """ equals | notEquals | in | notIn | greaterThan | lessThan | empty |
        notEmpty | contains | notContains | eval.
        Type `str`. """

        self.path = None
        """ XPath or JSONPath expression.
        Type `str`. """

        self.requestMethod = None
        """ delete | get | options | patch | post | put | head.
        Type `str`. """

        self.requestURL = None
        """ Request URL comparison value.
        Type `str`. """

        self.resource = None
        """ Resource type.
        Type `str`. """

        self.response = None
        """ okay | created | noContent | notModified | bad | forbidden |
        notFound | methodNotAllowed | conflict | gone | preconditionFailed
        | unprocessable.
        Type `str`. """

        self.responseCode = None
        """ HTTP response code to test.
        Type `str`. """

        self.sourceId = None
        """ Fixture Id of source expression or headerField.
        Type `str`. """

        self.validateProfileId = None
        """ Profile Id of validation profile reference.
        Type `str`. """

        self.value = None
        """ The value to compare to.
        Type `str`. """

        self.warningOnly = None
        """ Will this assert produce a warning only on error?.
        Type `bool`. """

        super(TestScriptSetupActionAssert, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptSetupActionAssert, self).elementProperties()
        js.extend([
            ("label", "label", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("direction", "direction", AssertionDirectionType.str, False, None, False),
            ("compareToSourceId", "compareToSourceId", str, False, None, False),
            ("compareToSourceExpression", "compareToSourceExpression", str, False, None, False),
            ("compareToSourcePath", "compareToSourcePath", str, False, None, False),
            ("contentType", "contentType", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("headerField", "headerField", str, False, None, False),
            ("minimumId", "minimumId", str, False, None, False),
            ("navigationLinks", "navigationLinks", bool, False, None, False),
            ("operator", "operator", AssertionOperatorType.str, False, None, False),
            ("path", "path", str, False, None, False),
            ("requestMethod", "requestMethod", TestScriptRequestMethodCode.str, False, None, False),
            ("requestURL", "requestURL", str, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("response", "response", AssertionResponseTypes.str, False, None, False),
            ("responseCode", "responseCode", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("validateProfileId", "validateProfileId", str, False, None, False),
            ("value", "value", str, False, None, False),
            ("warningOnly", "warningOnly", bool, False, None, True),
        ])
        return js


class TestScriptSetupActionOperation(backboneelement.BackboneElement):
    """ The setup operation to perform.

    The operation to perform.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ The operation code type that will be executed.
        Type `Coding` (represented as `dict` in JSON). """

        self.resource = None
        """ Resource type.
        Type `str`. """

        self.label = None
        """ Tracking/logging operation label.
        Type `str`. """

        self.description = None
        """ Tracking/reporting operation description.
        Type `str`. """

        self.accept = None
        """ Mime type to accept in the payload of the response, with charset
        etc..
        Type `str`. """

        self.contentType = None
        """ Mime type of the request payload contents, with charset etc..
        Type `str`. """

        self.destination = None
        """ Server responding to the request.
        Type `int`. """

        self.encodeRequestUrl = None
        """ Whether or not to send the request url in encoded format.
        Type `bool`. """

        self.method = None
        """ delete | get | options | patch | post | put | head.
        Type `str`. """

        self.origin = None
        """ Server initiating the request.
        Type `int`. """

        self.params = None
        """ Explicitly defined path parameters.
        Type `str`. """

        self.requestHeader = None
        """ Each operation can have one or more header elements.
        List of `TestScriptSetupActionOperationRequestHeader` items (represented as `dict` in JSON). """

        self.requestId = None
        """ Fixture Id of mapped request.
        Type `str`. """

        self.responseId = None
        """ Fixture Id of mapped response.
        Type `str`. """

        self.sourceId = None
        """ Fixture Id of body for PUT and POST requests.
        Type `str`. """

        self.targetId = None
        """ Id of fixture used for extracting the [id],  [type], and [vid] for
        GET requests.
        Type `str`. """

        self.url = None
        """ Request URL.
        Type `str`. """

        super(TestScriptSetupActionOperation, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptSetupActionOperation, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("label", "label", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("accept", "accept", str, False, None, False),
            ("contentType", "contentType", str, False, None, False),
            ("destination", "destination", int, False, None, False),
            ("encodeRequestUrl", "encodeRequestUrl", bool, False, None, True),
            ("method", "method", TestScriptRequestMethodCode.str, False, None, False),
            ("origin", "origin", int, False, None, False),
            ("params", "params", str, False, None, False),
            ("requestHeader", "requestHeader", TestScriptSetupActionOperationRequestHeader, True, None, False),
            ("requestId", "requestId", str, False, None, False),
            ("responseId", "responseId", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("targetId", "targetId", str, False, None, False),
            ("url", "url", str, False, None, False),
        ])
        return js


class TestScriptSetupActionOperationRequestHeader(backboneelement.BackboneElement):
    """ Each operation can have one or more header elements.

    Header elements would be used to set HTTP headers.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.field = None
        """ HTTP header field name.
        Type `str`. """

        self.value = None
        """ HTTP headerfield value.
        Type `str`. """

        super(TestScriptSetupActionOperationRequestHeader, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptSetupActionOperationRequestHeader, self).elementProperties()
        js.extend([
            ("field", "field", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class TestScriptTeardown(backboneelement.BackboneElement):
    """ A series of required clean up steps.

    A series of operations required to clean up after all the tests are
    executed (successfully or otherwise).
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.action = None
        """ One or more teardown operations to perform.
        List of `TestScriptTeardownAction` items (represented as `dict` in JSON). """

        super(TestScriptTeardown, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptTeardownAction, True, None, True),
        ])
        return js


class TestScriptTeardownAction(backboneelement.BackboneElement):
    """ One or more teardown operations to perform.

    The teardown action will only contain an operation.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.operation = None
        """ The teardown operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """

        super(TestScriptTeardownAction, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestScriptSetupActionOperation, False, None, True),
        ])
        return js


class TestScriptTest(backboneelement.BackboneElement):
    """ A test in this script.
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
        """ A test operation or assert to perform.
        List of `TestScriptTestAction` items (represented as `dict` in JSON). """

        super(TestScriptTest, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptTest, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("action", "action", TestScriptTestAction, True, None, True),
        ])
        return js


class TestScriptTestAction(backboneelement.BackboneElement):
    """ A test operation or assert to perform.

    Action would contain either an operation or an assertion.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.operation = None
        """ The setup operation to perform.
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """

        self.assert_fhir = None
        """ The setup assertion to perform.
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """

        super(TestScriptTestAction, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptTestAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
            ("assert_fhir", "assert", TestScriptSetupActionAssert, False, None, False),
        ])
        return js


class TestScriptVariable(backboneelement.BackboneElement):
    """ Placeholder for evaluated elements.

    Variable is set based either on element value in response body or on header
    field value in the response headers.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.name = None
        """ Descriptive name for this variable.
        Type `str`. """

        self.defaultValue = None
        """ Default, hard-coded, or user-defined value for this variable.
        Type `str`. """

        self.description = None
        """ Natural language description of the variable.
        Type `str`. """

        self.expression = None
        """ The FHIRPath expression against the fixture body.
        Type `str`. """

        self.headerField = None
        """ HTTP header field name for source.
        Type `str`. """

        self.hint = None
        """ Hint help text for default value to enter.
        Type `str`. """

        self.path = None
        """ XPath or JSONPath against the fixture body.
        Type `str`. """

        self.sourceId = None
        """ Fixture Id of source expression or headerField within this variable.
        Type `str`. """

        super(TestScriptVariable, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(TestScriptVariable, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("defaultValue", "defaultValue", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("headerField", "headerField", str, False, None, False),
            ("hint", "hint", str, False, None, False),
            ("path", "path", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
        ])
        return js


import sys
try:
    from . import AssertionDirectionType
except ImportError:
    AssertionDirectionType = sys.modules[__package__ + '.AssertionDirectionType']
try:
    from . import AssertionOperatorType
except ImportError:
    AssertionOperatorType = sys.modules[__package__ + '.AssertionOperatorType']
try:
    from . import AssertionResponseTypes
except ImportError:
    AssertionResponseTypes = sys.modules[__package__ + '.AssertionResponseTypes']
try:
    from . import PublicationStatus
except ImportError:
    PublicationStatus = sys.modules[__package__ + '.PublicationStatus']
try:
    from . import TestScriptRequestMethodCode
except ImportError:
    TestScriptRequestMethodCode = sys.modules[__package__ + '.TestScriptRequestMethodCode']
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
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']