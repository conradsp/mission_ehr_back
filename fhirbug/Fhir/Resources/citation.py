#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.3.0 (http://hl7.org/fhir/StructureDefinition/Citation) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class Citation(domainresource.DomainResource):
    """ A description of identification, location, or contributorship of a
    publication (article or artifact).

    The Citation Resource enables reference to any knowledge artifact for
    purposes of identification and attribution. The Citation Resource supports
    existing reference structures and developing publication practices such as
    versioning, expressing complex contributorship roles, and referencing
    computable resources.
    """

    resource_type = "Citation"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.url = None
        """ Canonical identifier for this citation, represented as a globally
        unique URI.
        Type `str`. """

        self.identifier = None
        """ Identifier for the Citation resource itself.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the citation.
        Type `str`. """

        self.name = None
        """ Name for this citation (computer friendly).
        Type `str`. """

        self.title = None
        """ Name for this citation (human friendly).
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
        """ The publisher of the Citation, not the publisher of the article or
        artifact being cited.
        Type `str`. """

        self.contact = None
        """ Contact details for the publisher of the Citation Resource.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.description = None
        """ Natural language description of the citation.
        Type `str`. """

        self.useContext = None
        """ The context that the Citation Resource content is intended to
        support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for citation (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.purpose = None
        """ Why this citation is defined.
        Type `str`. """

        self.copyright = None
        """ Use and/or publishing restrictions for the Citation, not for the
        cited artifact.
        Type `str`. """

        self.approvalDate = None
        """ When the citation was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.lastReviewDate = None
        """ When the citation was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.effectivePeriod = None
        """ When the citation is expected to be used.
        Type `Period` (represented as `dict` in JSON). """

        self.author = None
        """ Who authored the Citation.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.editor = None
        """ Who edited the Citation.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.reviewer = None
        """ Who reviewed the Citation.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.endorser = None
        """ Who endorsed the Citation.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.summary = None
        """ A human-readable display of the citation.
        List of `CitationSummary` items (represented as `dict` in JSON). """

        self.classification = None
        """ The assignment to an organizing scheme.
        List of `CitationClassification` items (represented as `dict` in JSON). """

        self.note = None
        """ Used for general notes and annotations not coded elsewhere.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.currentState = None
        """ The status of the citation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.statusDate = None
        """ An effective date or period for a status of the citation.
        List of `CitationStatusDate` items (represented as `dict` in JSON). """

        self.relatesTo = None
        """ Artifact related to the Citation Resource.
        List of `CitationRelatesTo` items (represented as `dict` in JSON). """

        self.citedArtifact = None
        """ The article or artifact being described.
        Type `CitationCitedArtifact` (represented as `dict` in JSON). """

        super(Citation, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(Citation, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("name", "name", str, False, None, False),
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
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("summary", "summary", CitationSummary, True, None, False),
            ("classification", "classification", CitationClassification, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("currentState", "currentState", codeableconcept.CodeableConcept, True, None, False),
            ("statusDate", "statusDate", CitationStatusDate, True, None, False),
            ("relatesTo", "relatesTo", CitationRelatesTo, True, None, False),
            ("citedArtifact", "citedArtifact", CitationCitedArtifact, False, None, False),
        ])
        return js


from . import backboneelement

class CitationCitedArtifact(backboneelement.BackboneElement):
    """ The article or artifact being described.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ May include DOI, PMID, PMCID, etc..
        List of `Identifier` items (represented as `dict` in JSON). """

        self.relatedIdentifier = None
        """ May include trial registry identifiers.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.dateAccessed = None
        """ When the cited artifact was accessed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.version = None
        """ The defined version of the cited artifact.
        Type `CitationCitedArtifactVersion` (represented as `dict` in JSON). """

        self.currentState = None
        """ The status of the cited artifact.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.statusDate = None
        """ An effective date or period for a status of the cited artifact.
        List of `CitationCitedArtifactStatusDate` items (represented as `dict` in JSON). """

        self.title = None
        """ The title details of the article or artifact.
        List of `CitationCitedArtifactTitle` items (represented as `dict` in JSON). """

        self.abstract = None
        """ Summary of the article or artifact.
        List of `CitationCitedArtifactAbstract` items (represented as `dict` in JSON). """

        self.part = None
        """ The component of the article or artifact.
        Type `CitationCitedArtifactPart` (represented as `dict` in JSON). """

        self.relatesTo = None
        """ The artifact related to the cited artifact.
        List of `CitationCitedArtifactRelatesTo` items (represented as `dict` in JSON). """

        self.publicationForm = None
        """ If multiple, used to represent alternative forms of the article
        that are not separate citations.
        List of `CitationCitedArtifactPublicationForm` items (represented as `dict` in JSON). """

        self.webLocation = None
        """ Used for any URL for the article or artifact cited.
        List of `CitationCitedArtifactWebLocation` items (represented as `dict` in JSON). """

        self.classification = None
        """ The assignment to an organizing scheme.
        List of `CitationCitedArtifactClassification` items (represented as `dict` in JSON). """

        self.contributorship = None
        """ Attribution of authors and other contributors.
        Type `CitationCitedArtifactContributorship` (represented as `dict` in JSON). """

        self.note = None
        """ Any additional information or content for the article or artifact.
        List of `Annotation` items (represented as `dict` in JSON). """

        super(CitationCitedArtifact, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifact, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("relatedIdentifier", "relatedIdentifier", identifier.Identifier, True, None, False),
            ("dateAccessed", "dateAccessed", fhirdate.FHIRDate, False, None, False),
            ("version", "version", CitationCitedArtifactVersion, False, None, False),
            ("currentState", "currentState", codeableconcept.CodeableConcept, True, None, False),
            ("statusDate", "statusDate", CitationCitedArtifactStatusDate, True, None, False),
            ("title", "title", CitationCitedArtifactTitle, True, None, False),
            ("abstract", "abstract", CitationCitedArtifactAbstract, True, None, False),
            ("part", "part", CitationCitedArtifactPart, False, None, False),
            ("relatesTo", "relatesTo", CitationCitedArtifactRelatesTo, True, None, False),
            ("publicationForm", "publicationForm", CitationCitedArtifactPublicationForm, True, None, False),
            ("webLocation", "webLocation", CitationCitedArtifactWebLocation, True, None, False),
            ("classification", "classification", CitationCitedArtifactClassification, True, None, False),
            ("contributorship", "contributorship", CitationCitedArtifactContributorship, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
        ])
        return js


class CitationCitedArtifactAbstract(backboneelement.BackboneElement):
    """ Summary of the article or artifact.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ The kind of abstract.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.language = None
        """ Used to express the specific language.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.text = None
        """ Abstract content.
        Type `str`. """

        self.copyright = None
        """ Copyright notice for the abstract.
        Type `str`. """

        super(CitationCitedArtifactAbstract, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactAbstract, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("language", "language", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, True),
            ("copyright", "copyright", str, False, None, False),
        ])
        return js


class CitationCitedArtifactClassification(backboneelement.BackboneElement):
    """ The assignment to an organizing scheme.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ The kind of classifier (e.g. publication type, keyword).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.classifier = None
        """ The specific classification value.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.whoClassified = None
        """ Provenance and copyright of classification.
        Type `CitationCitedArtifactClassificationWhoClassified` (represented as `dict` in JSON). """

        super(CitationCitedArtifactClassification, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactClassification, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("classifier", "classifier", codeableconcept.CodeableConcept, True, None, False),
            ("whoClassified", "whoClassified", CitationCitedArtifactClassificationWhoClassified, False, None, False),
        ])
        return js


class CitationCitedArtifactClassificationWhoClassified(backboneelement.BackboneElement):
    """ Provenance and copyright of classification.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.person = None
        """ Person who created the classification.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.organization = None
        """ Organization who created the classification.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.publisher = None
        """ The publisher of the classification, not the publisher of the
        article or artifact being cited.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.classifierCopyright = None
        """ Rights management statement for the classification.
        Type `str`. """

        self.freeToShare = None
        """ Acceptable to re-use the classification.
        Type `bool`. """

        super(CitationCitedArtifactClassificationWhoClassified, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactClassificationWhoClassified, self).elementProperties()
        js.extend([
            ("person", "person", fhirreference.FHIRReference, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("publisher", "publisher", fhirreference.FHIRReference, False, None, False),
            ("classifierCopyright", "classifierCopyright", str, False, None, False),
            ("freeToShare", "freeToShare", bool, False, None, False),
        ])
        return js


class CitationCitedArtifactContributorship(backboneelement.BackboneElement):
    """ Attribution of authors and other contributors.

    This element is used to list authors and other contributors, their contact
    information, specific contributions, and summary statements.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.complete = None
        """ Indicates if the list includes all authors and/or contributors.
        Type `bool`. """

        self.entry = None
        """ An individual entity named in the list.
        List of `CitationCitedArtifactContributorshipEntry` items (represented as `dict` in JSON). """

        self.summary = None
        """ Used to record a display of the author/contributor list without
        separate coding for each list member.
        List of `CitationCitedArtifactContributorshipSummary` items (represented as `dict` in JSON). """

        super(CitationCitedArtifactContributorship, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactContributorship, self).elementProperties()
        js.extend([
            ("complete", "complete", bool, False, None, False),
            ("entry", "entry", CitationCitedArtifactContributorshipEntry, True, None, False),
            ("summary", "summary", CitationCitedArtifactContributorshipSummary, True, None, False),
        ])
        return js


class CitationCitedArtifactContributorshipEntry(backboneelement.BackboneElement):
    """ An individual entity named in the list.

    An individual entity named in the author list or contributor list.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.name = None
        """ A name associated with the person.
        Type `HumanName` (represented as `dict` in JSON). """

        self.initials = None
        """ Initials for forename.
        Type `str`. """

        self.collectiveName = None
        """ Used for collective or corporate name as an author.
        Type `str`. """

        self.identifier = None
        """ Author identifier, eg ORCID.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.affiliationInfo = None
        """ Organizational affiliation.
        List of `CitationCitedArtifactContributorshipEntryAffiliationInfo` items (represented as `dict` in JSON). """

        self.address = None
        """ Physical mailing address.
        List of `Address` items (represented as `dict` in JSON). """

        self.telecom = None
        """ Email or telephone contact methods for the author or contributor.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        self.contributionType = None
        """ The specific contribution.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.role = None
        """ The role of the contributor (e.g. author, editor, reviewer).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.contributionInstance = None
        """ Contributions with accounting for time or number.
        List of `CitationCitedArtifactContributorshipEntryContributionInstance` items (represented as `dict` in JSON). """

        self.correspondingContact = None
        """ Indication of which contributor is the corresponding contributor
        for the role.
        Type `bool`. """

        self.listOrder = None
        """ Used to code order of authors.
        Type `int`. """

        super(CitationCitedArtifactContributorshipEntry, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactContributorshipEntry, self).elementProperties()
        js.extend([
            ("name", "name", humanname.HumanName, False, None, False),
            ("initials", "initials", str, False, None, False),
            ("collectiveName", "collectiveName", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("affiliationInfo", "affiliationInfo", CitationCitedArtifactContributorshipEntryAffiliationInfo, True, None, False),
            ("address", "address", address.Address, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("contributionType", "contributionType", codeableconcept.CodeableConcept, True, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("contributionInstance", "contributionInstance", CitationCitedArtifactContributorshipEntryContributionInstance, True, None, False),
            ("correspondingContact", "correspondingContact", bool, False, None, False),
            ("listOrder", "listOrder", int, False, None, False),
        ])
        return js


class CitationCitedArtifactContributorshipEntryAffiliationInfo(backboneelement.BackboneElement):
    """ Organizational affiliation.

    Organization affiliated with the entity.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.affiliation = None
        """ Display for the organization.
        Type `str`. """

        self.role = None
        """ Role within the organization, such as professional title.
        Type `str`. """

        self.identifier = None
        """ Identifier for the organization.
        List of `Identifier` items (represented as `dict` in JSON). """

        super(CitationCitedArtifactContributorshipEntryAffiliationInfo, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactContributorshipEntryAffiliationInfo, self).elementProperties()
        js.extend([
            ("affiliation", "affiliation", str, False, None, False),
            ("role", "role", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
        ])
        return js


class CitationCitedArtifactContributorshipEntryContributionInstance(backboneelement.BackboneElement):
    """ Contributions with accounting for time or number.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ The specific contribution.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.time = None
        """ The time that the contribution was made.
        Type `FHIRDate` (represented as `str` in JSON). """

        super(CitationCitedArtifactContributorshipEntryContributionInstance, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactContributorshipEntryContributionInstance, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("time", "time", fhirdate.FHIRDate, False, None, False),
        ])
        return js


class CitationCitedArtifactContributorshipSummary(backboneelement.BackboneElement):
    """ Used to record a display of the author/contributor list without separate
    coding for each list member.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ Either authorList or contributorshipStatement.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.style = None
        """ The format for the display string.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.source = None
        """ Used to code the producer or rule for creating the display string.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.value = None
        """ The display string for the author list, contributor list, or
        contributorship statement.
        Type `str`. """

        super(CitationCitedArtifactContributorshipSummary, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactContributorshipSummary, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("style", "style", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


class CitationCitedArtifactPart(backboneelement.BackboneElement):
    """ The component of the article or artifact.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ The kind of component.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.value = None
        """ The specification of the component.
        Type `str`. """

        self.baseCitation = None
        """ The citation for the full article or artifact.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(CitationCitedArtifactPart, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactPart, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", str, False, None, False),
            ("baseCitation", "baseCitation", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class CitationCitedArtifactPublicationForm(backboneelement.BackboneElement):
    """ If multiple, used to represent alternative forms of the article that are
    not separate citations.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.publishedIn = None
        """ The collection the cited article or artifact is published in.
        Type `CitationCitedArtifactPublicationFormPublishedIn` (represented as `dict` in JSON). """

        self.periodicRelease = None
        """ The specific issue in which the cited article resides.
        Type `CitationCitedArtifactPublicationFormPeriodicRelease` (represented as `dict` in JSON). """

        self.articleDate = None
        """ The date the article was added to the database, or the date the
        article was released.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.lastRevisionDate = None
        """ The date the article was last revised or updated in the database.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.language = None
        """ Language in which this form of the article is published.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.accessionNumber = None
        """ Entry number or identifier for inclusion in a database.
        Type `str`. """

        self.pageString = None
        """ Used for full display of pagination.
        Type `str`. """

        self.firstPage = None
        """ Used for isolated representation of first page.
        Type `str`. """

        self.lastPage = None
        """ Used for isolated representation of last page.
        Type `str`. """

        self.pageCount = None
        """ Number of pages or screens.
        Type `str`. """

        self.copyright = None
        """ Copyright notice for the full article or artifact.
        Type `str`. """

        super(CitationCitedArtifactPublicationForm, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactPublicationForm, self).elementProperties()
        js.extend([
            ("publishedIn", "publishedIn", CitationCitedArtifactPublicationFormPublishedIn, False, None, False),
            ("periodicRelease", "periodicRelease", CitationCitedArtifactPublicationFormPeriodicRelease, False, None, False),
            ("articleDate", "articleDate", fhirdate.FHIRDate, False, None, False),
            ("lastRevisionDate", "lastRevisionDate", fhirdate.FHIRDate, False, None, False),
            ("language", "language", codeableconcept.CodeableConcept, True, None, False),
            ("accessionNumber", "accessionNumber", str, False, None, False),
            ("pageString", "pageString", str, False, None, False),
            ("firstPage", "firstPage", str, False, None, False),
            ("lastPage", "lastPage", str, False, None, False),
            ("pageCount", "pageCount", str, False, None, False),
            ("copyright", "copyright", str, False, None, False),
        ])
        return js


class CitationCitedArtifactPublicationFormPeriodicRelease(backboneelement.BackboneElement):
    """ The specific issue in which the cited article resides.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.citedMedium = None
        """ Internet or Print.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.volume = None
        """ Volume number of journal in which the article is published.
        Type `str`. """

        self.issue = None
        """ Issue, part or supplement of journal in which the article is
        published.
        Type `str`. """

        self.dateOfPublication = None
        """ Defining the date on which the issue of the journal was published.
        Type `CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublication` (represented as `dict` in JSON). """

        super(CitationCitedArtifactPublicationFormPeriodicRelease, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactPublicationFormPeriodicRelease, self).elementProperties()
        js.extend([
            ("citedMedium", "citedMedium", codeableconcept.CodeableConcept, False, None, False),
            ("volume", "volume", str, False, None, False),
            ("issue", "issue", str, False, None, False),
            ("dateOfPublication", "dateOfPublication", CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublication, False, None, False),
        ])
        return js


class CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublication(backboneelement.BackboneElement):
    """ Defining the date on which the issue of the journal was published.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.date = None
        """ Date on which the issue of the journal was published.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.year = None
        """ Year on which the issue of the journal was published.
        Type `str`. """

        self.month = None
        """ Month on which the issue of the journal was published.
        Type `str`. """

        self.day = None
        """ Day on which the issue of the journal was published.
        Type `str`. """

        self.season = None
        """ Season on which the issue of the journal was published.
        Type `str`. """

        self.text = None
        """ Text representation of the date of which the issue of the journal
        was published.
        Type `str`. """

        super(CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublication, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublication, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("year", "year", str, False, None, False),
            ("month", "month", str, False, None, False),
            ("day", "day", str, False, None, False),
            ("season", "season", str, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


class CitationCitedArtifactPublicationFormPublishedIn(backboneelement.BackboneElement):
    """ The collection the cited article or artifact is published in.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ Kind of container (e.g. Periodical, database, or book).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.identifier = None
        """ Journal identifiers include ISSN, ISO Abbreviation and NLMuniqueID;
        Book identifiers include ISBN.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.title = None
        """ Name of the database or title of the book or journal.
        Type `str`. """

        self.publisher = None
        """ Name of the publisher.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.publisherLocation = None
        """ Geographic location of the publisher.
        Type `str`. """

        super(CitationCitedArtifactPublicationFormPublishedIn, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactPublicationFormPublishedIn, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("title", "title", str, False, None, False),
            ("publisher", "publisher", fhirreference.FHIRReference, False, None, False),
            ("publisherLocation", "publisherLocation", str, False, None, False),
        ])
        return js


class CitationCitedArtifactRelatesTo(backboneelement.BackboneElement):
    """ The artifact related to the cited artifact.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.relationshipType = None
        """ How the cited artifact relates to the target artifact.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.targetClassifier = None
        """ The clasification of the related artifact.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.targetUri = None
        """ The article or artifact that the cited artifact is related to.
        Type `str`. """

        self.targetIdentifier = None
        """ The article or artifact that the cited artifact is related to.
        Type `Identifier` (represented as `dict` in JSON). """

        self.targetReference = None
        """ The article or artifact that the cited artifact is related to.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.targetAttachment = None
        """ The article or artifact that the cited artifact is related to.
        Type `Attachment` (represented as `dict` in JSON). """

        super(CitationCitedArtifactRelatesTo, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactRelatesTo, self).elementProperties()
        js.extend([
            ("relationshipType", "relationshipType", codeableconcept.CodeableConcept, False, None, True),
            ("targetClassifier", "targetClassifier", codeableconcept.CodeableConcept, True, None, False),
            ("targetUri", "targetUri", str, False, "target", True),
            ("targetIdentifier", "targetIdentifier", identifier.Identifier, False, "target", True),
            ("targetReference", "targetReference", fhirreference.FHIRReference, False, "target", True),
            ("targetAttachment", "targetAttachment", attachment.Attachment, False, "target", True),
        ])
        return js


class CitationCitedArtifactStatusDate(backboneelement.BackboneElement):
    """ An effective date or period for a status of the cited artifact.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.activity = None
        """ Classification of the status.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.actual = None
        """ Either occurred or expected.
        Type `bool`. """

        self.period = None
        """ When the status started and/or ended.
        Type `Period` (represented as `dict` in JSON). """

        super(CitationCitedArtifactStatusDate, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactStatusDate, self).elementProperties()
        js.extend([
            ("activity", "activity", codeableconcept.CodeableConcept, False, None, True),
            ("actual", "actual", bool, False, None, False),
            ("period", "period", period.Period, False, None, True),
        ])
        return js


class CitationCitedArtifactTitle(backboneelement.BackboneElement):
    """ The title details of the article or artifact.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ The kind of title.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.language = None
        """ Used to express the specific language.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.text = None
        """ The title of the article or artifact.
        Type `str`. """

        super(CitationCitedArtifactTitle, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactTitle, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("language", "language", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, True),
        ])
        return js


class CitationCitedArtifactVersion(backboneelement.BackboneElement):
    """ The defined version of the cited artifact.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.value = None
        """ The version number or other version identifier.
        Type `str`. """

        self.baseCitation = None
        """ Citation for the main version of the cited artifact.
        Type `FHIRReference` (represented as `dict` in JSON). """

        super(CitationCitedArtifactVersion, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactVersion, self).elementProperties()
        js.extend([
            ("value", "value", str, False, None, True),
            ("baseCitation", "baseCitation", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class CitationCitedArtifactWebLocation(backboneelement.BackboneElement):
    """ Used for any URL for the article or artifact cited.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ Code the reason for different URLs, e.g. abstract and full-text.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.url = None
        """ The specific URL.
        Type `str`. """

        super(CitationCitedArtifactWebLocation, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationCitedArtifactWebLocation, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("url", "url", str, False, None, False),
        ])
        return js


class CitationClassification(backboneelement.BackboneElement):
    """ The assignment to an organizing scheme.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.type = None
        """ The kind of classifier (e.g. publication type, keyword).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.classifier = None
        """ The specific classification value.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(CitationClassification, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationClassification, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("classifier", "classifier", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class CitationRelatesTo(backboneelement.BackboneElement):
    """ Artifact related to the Citation Resource.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.relationshipType = None
        """ How the Citation resource relates to the target artifact.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.targetClassifier = None
        """ The clasification of the related artifact.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.targetUri = None
        """ The article or artifact that the Citation Resource is related to.
        Type `str`. """

        self.targetIdentifier = None
        """ The article or artifact that the Citation Resource is related to.
        Type `Identifier` (represented as `dict` in JSON). """

        self.targetReference = None
        """ The article or artifact that the Citation Resource is related to.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.targetAttachment = None
        """ The article or artifact that the Citation Resource is related to.
        Type `Attachment` (represented as `dict` in JSON). """

        super(CitationRelatesTo, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationRelatesTo, self).elementProperties()
        js.extend([
            ("relationshipType", "relationshipType", codeableconcept.CodeableConcept, False, None, True),
            ("targetClassifier", "targetClassifier", codeableconcept.CodeableConcept, True, None, False),
            ("targetUri", "targetUri", str, False, "target", True),
            ("targetIdentifier", "targetIdentifier", identifier.Identifier, False, "target", True),
            ("targetReference", "targetReference", fhirreference.FHIRReference, False, "target", True),
            ("targetAttachment", "targetAttachment", attachment.Attachment, False, "target", True),
        ])
        return js


class CitationStatusDate(backboneelement.BackboneElement):
    """ An effective date or period for a status of the citation.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.activity = None
        """ Classification of the status.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.actual = None
        """ Either occurred or expected.
        Type `bool`. """

        self.period = None
        """ When the status started and/or ended.
        Type `Period` (represented as `dict` in JSON). """

        super(CitationStatusDate, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationStatusDate, self).elementProperties()
        js.extend([
            ("activity", "activity", codeableconcept.CodeableConcept, False, None, True),
            ("actual", "actual", bool, False, None, False),
            ("period", "period", period.Period, False, None, True),
        ])
        return js


class CitationSummary(backboneelement.BackboneElement):
    """ A human-readable display of the citation.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.style = None
        """ Format for display of the citation.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.text = None
        """ The human-readable display of the citation.
        Type `str`. """

        super(CitationSummary, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(CitationSummary, self).elementProperties()
        js.extend([
            ("style", "style", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, True),
        ])
        return js


import sys
try:
    from . import PublicationStatus
except ImportError:
    PublicationStatus = sys.modules[__package__ + '.PublicationStatus']
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + '.humanname']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']