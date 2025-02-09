#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstanceNucleicAcid) on 2022-12-14.
#  2022, SMART Health IT.
##


from . import domainresource

class SubstanceNucleicAcid(domainresource.DomainResource):
    """ Nucleic acids are defined by three distinct elements: the base, sugar and
    linkage. Individual substance/moiety IDs will be created for each of these
    elements. The nucleotide sequence will be always entered in the 5’-3’
    direction.
    """

    resource_type = "SubstanceNucleicAcid"

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.sequenceType = None
        """ The type of the sequence shall be specified based on a controlled
        vocabulary.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.numberOfSubunits = None
        """ The number of linear sequences of nucleotides linked through
        phosphodiester bonds shall be described. Subunits would be strands
        of nucleic acids that are tightly associated typically through
        Watson-Crick base pairing. NOTE: If not specified in the reference
        source, the assumption is that there is 1 subunit.
        Type `int`. """

        self.areaOfHybridisation = None
        """ The area of hybridisation shall be described if applicable for
        double stranded RNA or DNA. The number associated with the subunit
        followed by the number associated to the residue shall be specified
        in increasing order. The underscore “” shall be used as separator
        as follows: “Subunitnumber Residue”.
        Type `str`. """

        self.oligoNucleotideType = None
        """ (TBC).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.subunit = None
        """ Subunits are listed in order of decreasing length; sequences of the
        same length will be ordered by molecular weight; subunits that have
        identical sequences will be repeated multiple times.
        List of `SubstanceNucleicAcidSubunit` items (represented as `dict` in JSON). """

        super(SubstanceNucleicAcid, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceNucleicAcid, self).elementProperties()
        js.extend([
            ("sequenceType", "sequenceType", codeableconcept.CodeableConcept, False, None, False),
            ("numberOfSubunits", "numberOfSubunits", int, False, None, False),
            ("areaOfHybridisation", "areaOfHybridisation", str, False, None, False),
            ("oligoNucleotideType", "oligoNucleotideType", codeableconcept.CodeableConcept, False, None, False),
            ("subunit", "subunit", SubstanceNucleicAcidSubunit, True, None, False),
        ])
        return js


from . import backboneelement

class SubstanceNucleicAcidSubunit(backboneelement.BackboneElement):
    """ Subunits are listed in order of decreasing length; sequences of the same
    length will be ordered by molecular weight; subunits that have identical
    sequences will be repeated multiple times.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.subunit = None
        """ Index of linear sequences of nucleic acids in order of decreasing
        length. Sequences of the same length will be ordered by molecular
        weight. Subunits that have identical sequences will be repeated and
        have sequential subscripts.
        Type `int`. """

        self.sequence = None
        """ Actual nucleotide sequence notation from 5' to 3' end using
        standard single letter codes. In addition to the base sequence,
        sugar and type of phosphate or non-phosphate linkage should also be
        captured.
        Type `str`. """

        self.length = None
        """ The length of the sequence shall be captured.
        Type `int`. """

        self.sequenceAttachment = None
        """ (TBC).
        Type `Attachment` (represented as `dict` in JSON). """

        self.fivePrime = None
        """ The nucleotide present at the 5’ terminal shall be specified based
        on a controlled vocabulary. Since the sequence is represented from
        the 5' to the 3' end, the 5’ prime nucleotide is the letter at the
        first position in the sequence. A separate representation would be
        redundant.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.threePrime = None
        """ The nucleotide present at the 3’ terminal shall be specified based
        on a controlled vocabulary. Since the sequence is represented from
        the 5' to the 3' end, the 5’ prime nucleotide is the letter at the
        last position in the sequence. A separate representation would be
        redundant.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.linkage = None
        """ The linkages between sugar residues will also be captured.
        List of `SubstanceNucleicAcidSubunitLinkage` items (represented as `dict` in JSON). """

        self.sugar = None
        """ 5.3.6.8.1 Sugar ID (Mandatory).
        List of `SubstanceNucleicAcidSubunitSugar` items (represented as `dict` in JSON). """

        super(SubstanceNucleicAcidSubunit, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceNucleicAcidSubunit, self).elementProperties()
        js.extend([
            ("subunit", "subunit", int, False, None, False),
            ("sequence", "sequence", str, False, None, False),
            ("length", "length", int, False, None, False),
            ("sequenceAttachment", "sequenceAttachment", attachment.Attachment, False, None, False),
            ("fivePrime", "fivePrime", codeableconcept.CodeableConcept, False, None, False),
            ("threePrime", "threePrime", codeableconcept.CodeableConcept, False, None, False),
            ("linkage", "linkage", SubstanceNucleicAcidSubunitLinkage, True, None, False),
            ("sugar", "sugar", SubstanceNucleicAcidSubunitSugar, True, None, False),
        ])
        return js


class SubstanceNucleicAcidSubunitLinkage(backboneelement.BackboneElement):
    """ The linkages between sugar residues will also be captured.
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.connectivity = None
        """ The entity that links the sugar residues together should also be
        captured for nearly all naturally occurring nucleic acid the
        linkage is a phosphate group. For many synthetic oligonucleotides
        phosphorothioate linkages are often seen. Linkage connectivity is
        assumed to be 3’-5’. If the linkage is either 3’-3’ or 5’-5’ this
        should be specified.
        Type `str`. """

        self.identifier = None
        """ Each linkage will be registered as a fragment and have an ID.
        Type `Identifier` (represented as `dict` in JSON). """

        self.name = None
        """ Each linkage will be registered as a fragment and have at least one
        name. A single name shall be assigned to each linkage.
        Type `str`. """

        self.residueSite = None
        """ Residues shall be captured as described in 5.3.6.8.3.
        Type `str`. """

        super(SubstanceNucleicAcidSubunitLinkage, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceNucleicAcidSubunitLinkage, self).elementProperties()
        js.extend([
            ("connectivity", "connectivity", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("name", "name", str, False, None, False),
            ("residueSite", "residueSite", str, False, None, False),
        ])
        return js


class SubstanceNucleicAcidSubunitSugar(backboneelement.BackboneElement):
    """ 5.3.6.8.1 Sugar ID (Mandatory).
    """

    def __init__(self, jsondict=None, strict=True, **kwargs):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.identifier = None
        """ The Substance ID of the sugar or sugar-like component that make up
        the nucleotide.
        Type `Identifier` (represented as `dict` in JSON). """

        self.name = None
        """ The name of the sugar or sugar-like component that make up the
        nucleotide.
        Type `str`. """

        self.residueSite = None
        """ The residues that contain a given sugar will be captured. The order
        of given residues will be captured in the 5‘-3‘direction consistent
        with the base sequences listed above.
        Type `str`. """

        super(SubstanceNucleicAcidSubunitSugar, self).__init__(jsondict=jsondict, strict=strict, **kwargs)

    def elementProperties(self):
        js = super(SubstanceNucleicAcidSubunitSugar, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("name", "name", str, False, None, False),
            ("residueSite", "residueSite", str, False, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']