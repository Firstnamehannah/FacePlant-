# Auto generated from faceplant.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-07-21T14:26:42
# Schema: faceplant
#
# id: https://w3id.org/your-org/faceplant
# description: A LinkML data model for plant phenotypic data, based on the Minimum Information About a Plant Phenotyping Experiment (MIAPPE v1.2) checklist. Slot names follow the original MIAPPE codenames for traceability.
#
# license: https://creativecommons.org/licenses/by/4.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Decimal, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Decimal, URIorCURIE

metamodel_version = "1.11.0"
version = "0.1.0"

# Namespaces
CO = CurieNamespace('CO', 'http://purl.obolibrary.org/obo/CO_')
CO_322 = CurieNamespace('CO_322', 'https://cropontology.org/rdf/CO_322:')
CO_715 = CurieNamespace('CO_715', 'http://purl.obolibrary.org/obo/CO_715_')
DOI = CurieNamespace('DOI', 'http://identifiers.org/doi/')
EO = CurieNamespace('EO', 'http://purl.obolibrary.org/obo/EO_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
ORCID = CurieNamespace('ORCID', 'http://identifiers.org/orcid/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PO = CurieNamespace('PO', 'http://purl.obolibrary.org/obo/PO_')
TO = CurieNamespace('TO', 'http://purl.obolibrary.org/obo/TO_')
FACEPLANT = CurieNamespace('faceplant', 'https://github.com/Firstnamehannah/FacePlant-')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MIAPPE = CurieNamespace('miappe', 'https://w3id.org/miappe/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = FACEPLANT


# Types
class Iso8601DateTime(String):
    """ ISO 8601 date or date-time, with optional timezone. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "iso8601DateTime"
    type_model_uri = FACEPLANT.Iso8601DateTime


class MeasurementWithUnit(String):
    """ Numeric value followed by a unit abbreviation, as used in the MIAPPE checklist. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "measurementWithUnit"
    type_model_uri = FACEPLANT.MeasurementWithUnit


class KeyValueList(String):
    """ Key-value pair list encoded as text, usually separated by commas or semicolons. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "keyValueList"
    type_model_uri = FACEPLANT.KeyValueList


# Class references
class BiologicalMaterialBiologicalMaterialId(extended_str):
    pass


class ObservationUnitObsUnitId(extended_str):
    pass


class SampleSampleId(extended_str):
    pass


class ObservedVariableVariableId(extended_str):
    pass


@dataclass(repr=False)
class MIAPPESubmission(YAMLRoot):
    """
    A complete MIAPPE submission containing exactly one investigation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FACEPLANT["MIAPPESubmission"]
    class_class_curie: ClassVar[str] = "faceplant:MIAPPESubmission"
    class_name: ClassVar[str] = "MIAPPESubmission"
    class_model_uri: ClassVar[URIRef] = FACEPLANT.MIAPPESubmission

    investigation: Union[dict, "Investigation"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.investigation):
            self.MissingRequiredField("investigation")
        if not isinstance(self.investigation, Investigation):
            self.investigation = Investigation(**as_dict(self.investigation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Investigation(YAMLRoot):
    """
    Investigations are research programmes with defined aims. They can exist at various scales, including a
    grant-funded programme, a publication, or a single experiment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FACEPLANT["Investigation"]
    class_class_curie: ClassVar[str] = "faceplant:Investigation"
    class_name: ClassVar[str] = "Investigation"
    class_model_uri: ClassVar[URIRef] = FACEPLANT.Investigation

    investigationTitle: str = None
    miappeVersion: str = None
    persons: Union[Union[dict, "Person"], list[Union[dict, "Person"]]] = None
    studies: Union[Union[dict, "Study"], list[Union[dict, "Study"]]] = None
    investigationId: Optional[Union[str, URIorCURIE]] = None
    investigationDescription: Optional[str] = None
    submissionDate: Optional[Union[str, Iso8601DateTime]] = None
    publicReleaseDate: Optional[Union[str, Iso8601DateTime]] = None
    license: Optional[str] = None
    associatedPublication: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.investigationTitle):
            self.MissingRequiredField("investigationTitle")
        if not isinstance(self.investigationTitle, str):
            self.investigationTitle = str(self.investigationTitle)

        if self._is_empty(self.miappeVersion):
            self.MissingRequiredField("miappeVersion")
        if not isinstance(self.miappeVersion, str):
            self.miappeVersion = str(self.miappeVersion)

        if self._is_empty(self.persons):
            self.MissingRequiredField("persons")
        self._normalize_inlined_as_list(slot_name="persons", slot_type=Person, key_name="personName", keyed=False)

        if self._is_empty(self.studies):
            self.MissingRequiredField("studies")
        self._normalize_inlined_as_list(slot_name="studies", slot_type=Study, key_name="studyTitle", keyed=False)

        if self.investigationId is not None and not isinstance(self.investigationId, URIorCURIE):
            self.investigationId = URIorCURIE(self.investigationId)

        if self.investigationDescription is not None and not isinstance(self.investigationDescription, str):
            self.investigationDescription = str(self.investigationDescription)

        if self.submissionDate is not None and not isinstance(self.submissionDate, Iso8601DateTime):
            self.submissionDate = Iso8601DateTime(self.submissionDate)

        if self.publicReleaseDate is not None and not isinstance(self.publicReleaseDate, Iso8601DateTime):
            self.publicReleaseDate = Iso8601DateTime(self.publicReleaseDate)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if not isinstance(self.associatedPublication, list):
            self.associatedPublication = [self.associatedPublication] if self.associatedPublication is not None else []
        self.associatedPublication = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.associatedPublication]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(YAMLRoot):
    """
    A study or experiment comprises a series of assays or measurements of one or more types, undertaken to answer a
    particular biological question.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FACEPLANT["Study"]
    class_class_curie: ClassVar[str] = "faceplant:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = FACEPLANT.Study

    studyTitle: str = None
    studyStartDate: Union[str, Iso8601DateTime] = None
    contactInst: str = None
    locationCountry: str = None
    siteName: str = None
    expeDesignDesc: str = None
    obsUnitDesc: str = None
    growthFacilityDesc: str = None
    biologicalMaterials: Union[dict[Union[str, BiologicalMaterialBiologicalMaterialId], Union[dict, "BiologicalMaterial"]], list[Union[dict, "BiologicalMaterial"]]] = empty_dict()
    observationUnits: Union[dict[Union[str, ObservationUnitObsUnitId], Union[dict, "ObservationUnit"]], list[Union[dict, "ObservationUnit"]]] = empty_dict()
    observedVariables: Union[dict[Union[str, ObservedVariableVariableId], Union[dict, "ObservedVariable"]], list[Union[dict, "ObservedVariable"]]] = empty_dict()
    studyId: Optional[Union[str, URIorCURIE]] = None
    studyDescription: Optional[str] = None
    studyEndDate: Optional[Union[str, Iso8601DateTime]] = None
    locationLatitude: Optional[Decimal] = None
    locationLongitude: Optional[Decimal] = None
    locationAltitude: Optional[Union[str, MeasurementWithUnit]] = None
    expeDesignType: Optional[Union[str, URIorCURIE]] = None
    obsUnitLevelHierarchy: Optional[str] = None
    growthFacilityType: Optional[Union[str, URIorCURIE]] = None
    culturalPractice: Optional[str] = None
    expeDesignMap: Optional[Union[str, list[str]]] = empty_list()
    persons: Optional[Union[Union[dict, "Person"], list[Union[dict, "Person"]]]] = empty_list()
    dataFiles: Optional[Union[Union[dict, "DataFile"], list[Union[dict, "DataFile"]]]] = empty_list()
    environment: Optional[Union[dict, "Environment"]] = None
    experimentalFactors: Optional[Union[Union[dict, "ExperimentalFactor"], list[Union[dict, "ExperimentalFactor"]]]] = empty_list()
    events: Optional[Union[Union[dict, "Event"], list[Union[dict, "Event"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.studyTitle):
            self.MissingRequiredField("studyTitle")
        if not isinstance(self.studyTitle, str):
            self.studyTitle = str(self.studyTitle)

        if self._is_empty(self.studyStartDate):
            self.MissingRequiredField("studyStartDate")
        if not isinstance(self.studyStartDate, Iso8601DateTime):
            self.studyStartDate = Iso8601DateTime(self.studyStartDate)

        if self._is_empty(self.contactInst):
            self.MissingRequiredField("contactInst")
        if not isinstance(self.contactInst, str):
            self.contactInst = str(self.contactInst)

        if self._is_empty(self.locationCountry):
            self.MissingRequiredField("locationCountry")
        if not isinstance(self.locationCountry, str):
            self.locationCountry = str(self.locationCountry)

        if self._is_empty(self.siteName):
            self.MissingRequiredField("siteName")
        if not isinstance(self.siteName, str):
            self.siteName = str(self.siteName)

        if self._is_empty(self.expeDesignDesc):
            self.MissingRequiredField("expeDesignDesc")
        if not isinstance(self.expeDesignDesc, str):
            self.expeDesignDesc = str(self.expeDesignDesc)

        if self._is_empty(self.obsUnitDesc):
            self.MissingRequiredField("obsUnitDesc")
        if not isinstance(self.obsUnitDesc, str):
            self.obsUnitDesc = str(self.obsUnitDesc)

        if self._is_empty(self.growthFacilityDesc):
            self.MissingRequiredField("growthFacilityDesc")
        if not isinstance(self.growthFacilityDesc, str):
            self.growthFacilityDesc = str(self.growthFacilityDesc)

        if self._is_empty(self.biologicalMaterials):
            self.MissingRequiredField("biologicalMaterials")
        self._normalize_inlined_as_list(slot_name="biologicalMaterials", slot_type=BiologicalMaterial, key_name="biologicalMaterialId", keyed=True)

        if self._is_empty(self.observationUnits):
            self.MissingRequiredField("observationUnits")
        self._normalize_inlined_as_list(slot_name="observationUnits", slot_type=ObservationUnit, key_name="obsUnitId", keyed=True)

        if self._is_empty(self.observedVariables):
            self.MissingRequiredField("observedVariables")
        self._normalize_inlined_as_list(slot_name="observedVariables", slot_type=ObservedVariable, key_name="variableId", keyed=True)

        if self.studyId is not None and not isinstance(self.studyId, URIorCURIE):
            self.studyId = URIorCURIE(self.studyId)

        if self.studyDescription is not None and not isinstance(self.studyDescription, str):
            self.studyDescription = str(self.studyDescription)

        if self.studyEndDate is not None and not isinstance(self.studyEndDate, Iso8601DateTime):
            self.studyEndDate = Iso8601DateTime(self.studyEndDate)

        if self.locationLatitude is not None and not isinstance(self.locationLatitude, Decimal):
            self.locationLatitude = Decimal(self.locationLatitude)

        if self.locationLongitude is not None and not isinstance(self.locationLongitude, Decimal):
            self.locationLongitude = Decimal(self.locationLongitude)

        if self.locationAltitude is not None and not isinstance(self.locationAltitude, MeasurementWithUnit):
            self.locationAltitude = MeasurementWithUnit(self.locationAltitude)

        if self.expeDesignType is not None and not isinstance(self.expeDesignType, URIorCURIE):
            self.expeDesignType = URIorCURIE(self.expeDesignType)

        if self.obsUnitLevelHierarchy is not None and not isinstance(self.obsUnitLevelHierarchy, str):
            self.obsUnitLevelHierarchy = str(self.obsUnitLevelHierarchy)

        if self.growthFacilityType is not None and not isinstance(self.growthFacilityType, URIorCURIE):
            self.growthFacilityType = URIorCURIE(self.growthFacilityType)

        if self.culturalPractice is not None and not isinstance(self.culturalPractice, str):
            self.culturalPractice = str(self.culturalPractice)

        if not isinstance(self.expeDesignMap, list):
            self.expeDesignMap = [self.expeDesignMap] if self.expeDesignMap is not None else []
        self.expeDesignMap = [v if isinstance(v, str) else str(v) for v in self.expeDesignMap]

        self._normalize_inlined_as_list(slot_name="persons", slot_type=Person, key_name="personName", keyed=False)

        self._normalize_inlined_as_list(slot_name="dataFiles", slot_type=DataFile, key_name="dataFileLink", keyed=False)

        if self.environment is not None and not isinstance(self.environment, Environment):
            self.environment = Environment(**as_dict(self.environment))

        self._normalize_inlined_as_list(slot_name="experimentalFactors", slot_type=ExperimentalFactor, key_name="expeFactorType", keyed=False)

        self._normalize_inlined_as_list(slot_name="events", slot_type=Event, key_name="eventType", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(YAMLRoot):
    """
    A human involved in the investigation or specifically in one of its studies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FACEPLANT["Person"]
    class_class_curie: ClassVar[str] = "faceplant:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = FACEPLANT.Person

    personName: str = None
    personRole: Union[str, list[str]] = None
    personAffiliation: Union[str, list[str]] = None
    personEmail: Optional[str] = None
    personId: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.personName):
            self.MissingRequiredField("personName")
        if not isinstance(self.personName, str):
            self.personName = str(self.personName)

        if self._is_empty(self.personRole):
            self.MissingRequiredField("personRole")
        if not isinstance(self.personRole, list):
            self.personRole = [self.personRole] if self.personRole is not None else []
        self.personRole = [v if isinstance(v, str) else str(v) for v in self.personRole]

        if self._is_empty(self.personAffiliation):
            self.MissingRequiredField("personAffiliation")
        if not isinstance(self.personAffiliation, list):
            self.personAffiliation = [self.personAffiliation] if self.personAffiliation is not None else []
        self.personAffiliation = [v if isinstance(v, str) else str(v) for v in self.personAffiliation]

        if self.personEmail is not None and not isinstance(self.personEmail, str):
            self.personEmail = str(self.personEmail)

        if self.personId is not None and not isinstance(self.personId, URIorCURIE):
            self.personId = URIorCURIE(self.personId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataFile(YAMLRoot):
    """
    A file or digital object holding observation data recorded during one or more assays of the study, typically in
    tabular form.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FACEPLANT["DataFile"]
    class_class_curie: ClassVar[str] = "faceplant:DataFile"
    class_name: ClassVar[str] = "DataFile"
    class_model_uri: ClassVar[URIRef] = FACEPLANT.DataFile

    dataFileLink: str = None
    dataFileDesc: str = None
    dataFileVersion: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.dataFileLink):
            self.MissingRequiredField("dataFileLink")
        if not isinstance(self.dataFileLink, str):
            self.dataFileLink = str(self.dataFileLink)

        if self._is_empty(self.dataFileDesc):
            self.MissingRequiredField("dataFileDesc")
        if not isinstance(self.dataFileDesc, str):
            self.dataFileDesc = str(self.dataFileDesc)

        if self.dataFileVersion is not None and not isinstance(self.dataFileVersion, str):
            self.dataFileVersion = str(self.dataFileVersion)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalMaterial(YAMLRoot):
    """
    The biological material being studied, such as plants grown from a seed bag or plants grown in a particular field.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FACEPLANT["BiologicalMaterial"]
    class_class_curie: ClassVar[str] = "faceplant:BiologicalMaterial"
    class_name: ClassVar[str] = "BiologicalMaterial"
    class_model_uri: ClassVar[URIRef] = FACEPLANT.BiologicalMaterial

    biologicalMaterialId: Union[str, BiologicalMaterialBiologicalMaterialId] = None
    organism: Union[str, URIorCURIE] = None
    biologicalMaterialExtId: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    genus: Optional[str] = None
    species: Optional[str] = None
    infraspecificName: Optional[Union[str, KeyValueList]] = None
    biologicalMaterialLatitude: Optional[Decimal] = None
    biologicalMaterialLongitude: Optional[Decimal] = None
    biologicalMaterialAltitude: Optional[Union[str, MeasurementWithUnit]] = None
    biologicalMaterialCoordUncertainty: Optional[Union[str, MeasurementWithUnit]] = None
    biologicalMaterialPreprocessing: Optional[Union[str, list[str]]] = empty_list()
    materialSourceId: Optional[str] = None
    materialSourceDoi: Optional[Union[str, URIorCURIE]] = None
    materialSourceAccNumber: Optional[str] = None
    materialSourceAccName: Optional[str] = None
    materialSourceInstCode: Optional[str] = None
    materialSourceInstName: Optional[str] = None
    materialSourceOtherIds: Optional[Union[str, KeyValueList]] = None
    materialSourceLatitude: Optional[Decimal] = None
    materialSourceLongitude: Optional[Decimal] = None
    materialSourceAltitude: Optional[Union[str, MeasurementWithUnit]] = None
    materialSourceCoordUncertainty: Optional[Union[str, MeasurementWithUnit]] = None
    materialSourceDesc: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.biologicalMaterialId):
            self.MissingRequiredField("biologicalMaterialId")
        if not isinstance(self.biologicalMaterialId, BiologicalMaterialBiologicalMaterialId):
            self.biologicalMaterialId = BiologicalMaterialBiologicalMaterialId(self.biologicalMaterialId)

        if self._is_empty(self.organism):
            self.MissingRequiredField("organism")
        if not isinstance(self.organism, URIorCURIE):
            self.organism = URIorCURIE(self.organism)

        if not isinstance(self.biologicalMaterialExtId, list):
            self.biologicalMaterialExtId = [self.biologicalMaterialExtId] if self.biologicalMaterialExtId is not None else []
        self.biologicalMaterialExtId = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.biologicalMaterialExtId]

        if self.genus is not None and not isinstance(self.genus, str):
            self.genus = str(self.genus)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if self.infraspecificName is not None and not isinstance(self.infraspecificName, KeyValueList):
            self.infraspecificName = KeyValueList(self.infraspecificName)

        if self.biologicalMaterialLatitude is not None and not isinstance(self.biologicalMaterialLatitude, Decimal):
            self.biologicalMaterialLatitude = Decimal(self.biologicalMaterialLatitude)

        if self.biologicalMaterialLongitude is not None and not isinstance(self.biologicalMaterialLongitude, Decimal):
            self.biologicalMaterialLongitude = Decimal(self.biologicalMaterialLongitude)

        if self.biologicalMaterialAltitude is not None and not isinstance(self.biologicalMaterialAltitude, MeasurementWithUnit):
            self.biologicalMaterialAltitude = MeasurementWithUnit(self.biologicalMaterialAltitude)

        if self.biologicalMaterialCoordUncertainty is not None and not isinstance(self.biologicalMaterialCoordUncertainty, MeasurementWithUnit):
            self.biologicalMaterialCoordUncertainty = MeasurementWithUnit(self.biologicalMaterialCoordUncertainty)

        if not isinstance(self.biologicalMaterialPreprocessing, list):
            self.biologicalMaterialPreprocessing = [self.biologicalMaterialPreprocessing] if self.biologicalMaterialPreprocessing is not None else []
        self.biologicalMaterialPreprocessing = [v if isinstance(v, str) else str(v) for v in self.biologicalMaterialPreprocessing]

        if self.materialSourceId is not None and not isinstance(self.materialSourceId, str):
            self.materialSourceId = str(self.materialSourceId)

        if self.materialSourceDoi is not None and not isinstance(self.materialSourceDoi, URIorCURIE):
            self.materialSourceDoi = URIorCURIE(self.materialSourceDoi)

        if self.materialSourceAccNumber is not None and not isinstance(self.materialSourceAccNumber, str):
            self.materialSourceAccNumber = str(self.materialSourceAccNumber)

        if self.materialSourceAccName is not None and not isinstance(self.materialSourceAccName, str):
            self.materialSourceAccName = str(self.materialSourceAccName)

        if self.materialSourceInstCode is not None and not isinstance(self.materialSourceInstCode, str):
            self.materialSourceInstCode = str(self.materialSourceInstCode)

        if self.materialSourceInstName is not None and not isinstance(self.materialSourceInstName, str):
            self.materialSourceInstName = str(self.materialSourceInstName)

        if self.materialSourceOtherIds is not None and not isinstance(self.materialSourceOtherIds, KeyValueList):
            self.materialSourceOtherIds = KeyValueList(self.materialSourceOtherIds)

        if self.materialSourceLatitude is not None and not isinstance(self.materialSourceLatitude, Decimal):
            self.materialSourceLatitude = Decimal(self.materialSourceLatitude)

        if self.materialSourceLongitude is not None and not isinstance(self.materialSourceLongitude, Decimal):
            self.materialSourceLongitude = Decimal(self.materialSourceLongitude)

        if self.materialSourceAltitude is not None and not isinstance(self.materialSourceAltitude, MeasurementWithUnit):
            self.materialSourceAltitude = MeasurementWithUnit(self.materialSourceAltitude)

        if self.materialSourceCoordUncertainty is not None and not isinstance(self.materialSourceCoordUncertainty, MeasurementWithUnit):
            self.materialSourceCoordUncertainty = MeasurementWithUnit(self.materialSourceCoordUncertainty)

        if self.materialSourceDesc is not None and not isinstance(self.materialSourceDesc, str):
            self.materialSourceDesc = str(self.materialSourceDesc)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Environment(YAMLRoot):
    """
    Environmental parameters that were kept constant throughout the study and did not change between observation units
    or assays.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FACEPLANT["Environment"]
    class_class_curie: ClassVar[str] = "faceplant:Environment"
    class_name: ClassVar[str] = "Environment"
    class_model_uri: ClassVar[URIRef] = FACEPLANT.Environment

    environmentParameters: Union[Union[dict, "EnvironmentParameter"], list[Union[dict, "EnvironmentParameter"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.environmentParameters):
            self.MissingRequiredField("environmentParameters")
        self._normalize_inlined_as_list(slot_name="environmentParameters", slot_type=EnvironmentParameter, key_name="envParam", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentParameter(YAMLRoot):
    """
    A constant environmental parameter and its value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FACEPLANT["EnvironmentParameter"]
    class_class_curie: ClassVar[str] = "faceplant:EnvironmentParameter"
    class_name: ClassVar[str] = "EnvironmentParameter"
    class_model_uri: ClassVar[URIRef] = FACEPLANT.EnvironmentParameter

    envParam: str = None
    envParamValue: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.envParam):
            self.MissingRequiredField("envParam")
        if not isinstance(self.envParam, str):
            self.envParam = str(self.envParam)

        if self._is_empty(self.envParamValue):
            self.MissingRequiredField("envParamValue")
        if not isinstance(self.envParamValue, str):
            self.envParamValue = str(self.envParamValue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentalFactor(YAMLRoot):
    """
    A condition that varies between observation units and whose impact on the biological material is the object of a
    study.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FACEPLANT["ExperimentalFactor"]
    class_class_curie: ClassVar[str] = "faceplant:ExperimentalFactor"
    class_name: ClassVar[str] = "ExperimentalFactor"
    class_model_uri: ClassVar[URIRef] = FACEPLANT.ExperimentalFactor

    expeFactorType: str = None
    expeFactorValues: Union[str, list[str]] = None
    expeFactorDesc: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.expeFactorType):
            self.MissingRequiredField("expeFactorType")
        if not isinstance(self.expeFactorType, str):
            self.expeFactorType = str(self.expeFactorType)

        if self._is_empty(self.expeFactorValues):
            self.MissingRequiredField("expeFactorValues")
        if not isinstance(self.expeFactorValues, list):
            self.expeFactorValues = [self.expeFactorValues] if self.expeFactorValues is not None else []
        self.expeFactorValues = [v if isinstance(v, str) else str(v) for v in self.expeFactorValues]

        if self.expeFactorDesc is not None and not isinstance(self.expeFactorDesc, str):
            self.expeFactorDesc = str(self.expeFactorDesc)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Event(YAMLRoot):
    """
    A discrete occurrence at a particular time in the experiment, natural or unnatural, such as planting, rain,
    fertilizing, or watering.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FACEPLANT["Event"]
    class_class_curie: ClassVar[str] = "faceplant:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = FACEPLANT.Event

    eventType: str = None
    eventDate: Union[Union[str, Iso8601DateTime], list[Union[str, Iso8601DateTime]]] = None
    eventAccNumber: Optional[Union[str, URIorCURIE]] = None
    eventDesc: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.eventType):
            self.MissingRequiredField("eventType")
        if not isinstance(self.eventType, str):
            self.eventType = str(self.eventType)

        if self._is_empty(self.eventDate):
            self.MissingRequiredField("eventDate")
        if not isinstance(self.eventDate, list):
            self.eventDate = [self.eventDate] if self.eventDate is not None else []
        self.eventDate = [v if isinstance(v, Iso8601DateTime) else Iso8601DateTime(v) for v in self.eventDate]

        if self.eventAccNumber is not None and not isinstance(self.eventAccNumber, URIorCURIE):
            self.eventAccNumber = URIorCURIE(self.eventAccNumber)

        if self.eventDesc is not None and not isinstance(self.eventDesc, str):
            self.eventDesc = str(self.eventDesc)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObservationUnit(YAMLRoot):
    """
    Objects that are subject to instances of observation and measurement. Observation units may comprise plants, their
    environment, or pure environmental observation units.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FACEPLANT["ObservationUnit"]
    class_class_curie: ClassVar[str] = "faceplant:ObservationUnit"
    class_name: ClassVar[str] = "ObservationUnit"
    class_model_uri: ClassVar[URIRef] = FACEPLANT.ObservationUnit

    obsUnitId: Union[str, ObservationUnitObsUnitId] = None
    obsUnitType: str = None
    externalId: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    spatialDistribution: Optional[Union[Union[str, KeyValueList], list[Union[str, KeyValueList]]]] = empty_list()
    obsUnitFactorValue: Optional[Union[str, list[str]]] = empty_list()
    biologicalMaterialRefs: Optional[Union[str, list[str]]] = empty_list()
    events: Optional[Union[Union[dict, Event], list[Union[dict, Event]]]] = empty_list()
    samples: Optional[Union[dict[Union[str, SampleSampleId], Union[dict, "Sample"]], list[Union[dict, "Sample"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.obsUnitId):
            self.MissingRequiredField("obsUnitId")
        if not isinstance(self.obsUnitId, ObservationUnitObsUnitId):
            self.obsUnitId = ObservationUnitObsUnitId(self.obsUnitId)

        if self._is_empty(self.obsUnitType):
            self.MissingRequiredField("obsUnitType")
        if not isinstance(self.obsUnitType, str):
            self.obsUnitType = str(self.obsUnitType)

        if not isinstance(self.externalId, list):
            self.externalId = [self.externalId] if self.externalId is not None else []
        self.externalId = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.externalId]

        if not isinstance(self.spatialDistribution, list):
            self.spatialDistribution = [self.spatialDistribution] if self.spatialDistribution is not None else []
        self.spatialDistribution = [v if isinstance(v, KeyValueList) else KeyValueList(v) for v in self.spatialDistribution]

        if not isinstance(self.obsUnitFactorValue, list):
            self.obsUnitFactorValue = [self.obsUnitFactorValue] if self.obsUnitFactorValue is not None else []
        self.obsUnitFactorValue = [v if isinstance(v, str) else str(v) for v in self.obsUnitFactorValue]

        if not isinstance(self.biologicalMaterialRefs, list):
            self.biologicalMaterialRefs = [self.biologicalMaterialRefs] if self.biologicalMaterialRefs is not None else []
        self.biologicalMaterialRefs = [v if isinstance(v, str) else str(v) for v in self.biologicalMaterialRefs]

        self._normalize_inlined_as_list(slot_name="events", slot_type=Event, key_name="eventType", keyed=False)

        self._normalize_inlined_as_list(slot_name="samples", slot_type=Sample, key_name="sampleId", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(YAMLRoot):
    """
    A portion of plant tissue harvested, non-harvested, or extracted from an observation unit for sub-plant
    observations and/or molecular studies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FACEPLANT["Sample"]
    class_class_curie: ClassVar[str] = "faceplant:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = FACEPLANT.Sample

    sampleId: Union[str, SampleSampleId] = None
    anatomicalEntity: Union[str, URIorCURIE] = None
    collectionDate: Union[str, Iso8601DateTime] = None
    developmentStage: Optional[Union[str, URIorCURIE]] = None
    sampleDesc: Optional[str] = None
    externalId: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sampleId):
            self.MissingRequiredField("sampleId")
        if not isinstance(self.sampleId, SampleSampleId):
            self.sampleId = SampleSampleId(self.sampleId)

        if self._is_empty(self.anatomicalEntity):
            self.MissingRequiredField("anatomicalEntity")
        if not isinstance(self.anatomicalEntity, URIorCURIE):
            self.anatomicalEntity = URIorCURIE(self.anatomicalEntity)

        if self._is_empty(self.collectionDate):
            self.MissingRequiredField("collectionDate")
        if not isinstance(self.collectionDate, Iso8601DateTime):
            self.collectionDate = Iso8601DateTime(self.collectionDate)

        if self.developmentStage is not None and not isinstance(self.developmentStage, URIorCURIE):
            self.developmentStage = URIorCURIE(self.developmentStage)

        if self.sampleDesc is not None and not isinstance(self.sampleDesc, str):
            self.sampleDesc = str(self.sampleDesc)

        if not isinstance(self.externalId, list):
            self.externalId = [self.externalId] if self.externalId is not None else []
        self.externalId = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.externalId]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObservedVariable(YAMLRoot):
    """
    Description of how a measurement has been made, usually a trait associated with a method and a unit or scale of
    measurement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FACEPLANT["ObservedVariable"]
    class_class_curie: ClassVar[str] = "faceplant:ObservedVariable"
    class_name: ClassVar[str] = "ObservedVariable"
    class_model_uri: ClassVar[URIRef] = FACEPLANT.ObservedVariable

    variableId: Union[str, ObservedVariableVariableId] = None
    traitName: str = None
    methodName: str = None
    scaleName: str = None
    variableName: Optional[str] = None
    variableAccNumber: Optional[Union[str, URIorCURIE]] = None
    traitEntity: Optional[str] = None
    traitEntityAccessionNumber: Optional[Union[str, URIorCURIE]] = None
    traitCharacteristic: Optional[str] = None
    traitCharacteristicAccessionNumber: Optional[Union[str, URIorCURIE]] = None
    traitAccNumber: Optional[Union[str, URIorCURIE]] = None
    methodAccNumber: Optional[Union[str, URIorCURIE]] = None
    methodDesc: Optional[str] = None
    methodRef: Optional[Union[str, URIorCURIE]] = None
    scaleAccNumber: Optional[Union[str, URIorCURIE]] = None
    timeScale: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.variableId):
            self.MissingRequiredField("variableId")
        if not isinstance(self.variableId, ObservedVariableVariableId):
            self.variableId = ObservedVariableVariableId(self.variableId)

        if self._is_empty(self.traitName):
            self.MissingRequiredField("traitName")
        if not isinstance(self.traitName, str):
            self.traitName = str(self.traitName)

        if self._is_empty(self.methodName):
            self.MissingRequiredField("methodName")
        if not isinstance(self.methodName, str):
            self.methodName = str(self.methodName)

        if self._is_empty(self.scaleName):
            self.MissingRequiredField("scaleName")
        if not isinstance(self.scaleName, str):
            self.scaleName = str(self.scaleName)

        if self.variableName is not None and not isinstance(self.variableName, str):
            self.variableName = str(self.variableName)

        if self.variableAccNumber is not None and not isinstance(self.variableAccNumber, URIorCURIE):
            self.variableAccNumber = URIorCURIE(self.variableAccNumber)

        if self.traitEntity is not None and not isinstance(self.traitEntity, str):
            self.traitEntity = str(self.traitEntity)

        if self.traitEntityAccessionNumber is not None and not isinstance(self.traitEntityAccessionNumber, URIorCURIE):
            self.traitEntityAccessionNumber = URIorCURIE(self.traitEntityAccessionNumber)

        if self.traitCharacteristic is not None and not isinstance(self.traitCharacteristic, str):
            self.traitCharacteristic = str(self.traitCharacteristic)

        if self.traitCharacteristicAccessionNumber is not None and not isinstance(self.traitCharacteristicAccessionNumber, URIorCURIE):
            self.traitCharacteristicAccessionNumber = URIorCURIE(self.traitCharacteristicAccessionNumber)

        if self.traitAccNumber is not None and not isinstance(self.traitAccNumber, URIorCURIE):
            self.traitAccNumber = URIorCURIE(self.traitAccNumber)

        if self.methodAccNumber is not None and not isinstance(self.methodAccNumber, URIorCURIE):
            self.methodAccNumber = URIorCURIE(self.methodAccNumber)

        if self.methodDesc is not None and not isinstance(self.methodDesc, str):
            self.methodDesc = str(self.methodDesc)

        if self.methodRef is not None and not isinstance(self.methodRef, URIorCURIE):
            self.methodRef = URIorCURIE(self.methodRef)

        if self.scaleAccNumber is not None and not isinstance(self.scaleAccNumber, URIorCURIE):
            self.scaleAccNumber = URIorCURIE(self.scaleAccNumber)

        if not isinstance(self.timeScale, list):
            self.timeScale = [self.timeScale] if self.timeScale is not None else []
        self.timeScale = [v if isinstance(v, str) else str(v) for v in self.timeScale]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.investigation = Slot(uri=FACEPLANT.investigation, name="investigation", curie=FACEPLANT.curie('investigation'),
                   model_uri=FACEPLANT.investigation, domain=None, range=Union[dict, Investigation])

slots.studies = Slot(uri=FACEPLANT.studies, name="studies", curie=FACEPLANT.curie('studies'),
                   model_uri=FACEPLANT.studies, domain=None, range=Optional[Union[Union[dict, Study], list[Union[dict, Study]]]])

slots.persons = Slot(uri=FACEPLANT.persons, name="persons", curie=FACEPLANT.curie('persons'),
                   model_uri=FACEPLANT.persons, domain=None, range=Optional[Union[Union[dict, Person], list[Union[dict, Person]]]])

slots.dataFiles = Slot(uri=FACEPLANT.dataFiles, name="dataFiles", curie=FACEPLANT.curie('dataFiles'),
                   model_uri=FACEPLANT.dataFiles, domain=None, range=Optional[Union[Union[dict, DataFile], list[Union[dict, DataFile]]]])

slots.biologicalMaterials = Slot(uri=FACEPLANT.biologicalMaterials, name="biologicalMaterials", curie=FACEPLANT.curie('biologicalMaterials'),
                   model_uri=FACEPLANT.biologicalMaterials, domain=None, range=Optional[Union[dict[Union[str, BiologicalMaterialBiologicalMaterialId], Union[dict, BiologicalMaterial]], list[Union[dict, BiologicalMaterial]]]])

slots.biologicalMaterialRefs = Slot(uri=FACEPLANT.biologicalMaterialRefs, name="biologicalMaterialRefs", curie=FACEPLANT.curie('biologicalMaterialRefs'),
                   model_uri=FACEPLANT.biologicalMaterialRefs, domain=None, range=Optional[Union[str, list[str]]])

slots.environment = Slot(uri=FACEPLANT.environment, name="environment", curie=FACEPLANT.curie('environment'),
                   model_uri=FACEPLANT.environment, domain=None, range=Optional[Union[dict, Environment]])

slots.environmentParameters = Slot(uri=FACEPLANT.environmentParameters, name="environmentParameters", curie=FACEPLANT.curie('environmentParameters'),
                   model_uri=FACEPLANT.environmentParameters, domain=None, range=Union[Union[dict, EnvironmentParameter], list[Union[dict, EnvironmentParameter]]])

slots.experimentalFactors = Slot(uri=FACEPLANT.experimentalFactors, name="experimentalFactors", curie=FACEPLANT.curie('experimentalFactors'),
                   model_uri=FACEPLANT.experimentalFactors, domain=None, range=Optional[Union[Union[dict, ExperimentalFactor], list[Union[dict, ExperimentalFactor]]]])

slots.events = Slot(uri=FACEPLANT.events, name="events", curie=FACEPLANT.curie('events'),
                   model_uri=FACEPLANT.events, domain=None, range=Optional[Union[Union[dict, Event], list[Union[dict, Event]]]])

slots.observationUnits = Slot(uri=FACEPLANT.observationUnits, name="observationUnits", curie=FACEPLANT.curie('observationUnits'),
                   model_uri=FACEPLANT.observationUnits, domain=None, range=Optional[Union[dict[Union[str, ObservationUnitObsUnitId], Union[dict, ObservationUnit]], list[Union[dict, ObservationUnit]]]])

slots.samples = Slot(uri=FACEPLANT.samples, name="samples", curie=FACEPLANT.curie('samples'),
                   model_uri=FACEPLANT.samples, domain=None, range=Optional[Union[dict[Union[str, SampleSampleId], Union[dict, Sample]], list[Union[dict, Sample]]]])

slots.observedVariables = Slot(uri=FACEPLANT.observedVariables, name="observedVariables", curie=FACEPLANT.curie('observedVariables'),
                   model_uri=FACEPLANT.observedVariables, domain=None, range=Optional[Union[dict[Union[str, ObservedVariableVariableId], Union[dict, ObservedVariable]], list[Union[dict, ObservedVariable]]]])

slots.investigationId = Slot(uri=FACEPLANT.investigationId, name="investigationId", curie=FACEPLANT.curie('investigationId'),
                   model_uri=FACEPLANT.investigationId, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.investigationTitle = Slot(uri=FACEPLANT.investigationTitle, name="investigationTitle", curie=FACEPLANT.curie('investigationTitle'),
                   model_uri=FACEPLANT.investigationTitle, domain=None, range=str)

slots.investigationDescription = Slot(uri=FACEPLANT.investigationDescription, name="investigationDescription", curie=FACEPLANT.curie('investigationDescription'),
                   model_uri=FACEPLANT.investigationDescription, domain=None, range=Optional[str])

slots.submissionDate = Slot(uri=FACEPLANT.submissionDate, name="submissionDate", curie=FACEPLANT.curie('submissionDate'),
                   model_uri=FACEPLANT.submissionDate, domain=None, range=Optional[Union[str, Iso8601DateTime]])

slots.publicReleaseDate = Slot(uri=FACEPLANT.publicReleaseDate, name="publicReleaseDate", curie=FACEPLANT.curie('publicReleaseDate'),
                   model_uri=FACEPLANT.publicReleaseDate, domain=None, range=Optional[Union[str, Iso8601DateTime]])

slots.license = Slot(uri=FACEPLANT.license, name="license", curie=FACEPLANT.curie('license'),
                   model_uri=FACEPLANT.license, domain=None, range=Optional[str])

slots.miappeVersion = Slot(uri=FACEPLANT.miappeVersion, name="miappeVersion", curie=FACEPLANT.curie('miappeVersion'),
                   model_uri=FACEPLANT.miappeVersion, domain=None, range=str)

slots.associatedPublication = Slot(uri=FACEPLANT.associatedPublication, name="associatedPublication", curie=FACEPLANT.curie('associatedPublication'),
                   model_uri=FACEPLANT.associatedPublication, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.studyId = Slot(uri=FACEPLANT.studyId, name="studyId", curie=FACEPLANT.curie('studyId'),
                   model_uri=FACEPLANT.studyId, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.studyTitle = Slot(uri=FACEPLANT.studyTitle, name="studyTitle", curie=FACEPLANT.curie('studyTitle'),
                   model_uri=FACEPLANT.studyTitle, domain=None, range=str)

slots.studyDescription = Slot(uri=FACEPLANT.studyDescription, name="studyDescription", curie=FACEPLANT.curie('studyDescription'),
                   model_uri=FACEPLANT.studyDescription, domain=None, range=Optional[str])

slots.studyStartDate = Slot(uri=FACEPLANT.studyStartDate, name="studyStartDate", curie=FACEPLANT.curie('studyStartDate'),
                   model_uri=FACEPLANT.studyStartDate, domain=None, range=Union[str, Iso8601DateTime])

slots.studyEndDate = Slot(uri=FACEPLANT.studyEndDate, name="studyEndDate", curie=FACEPLANT.curie('studyEndDate'),
                   model_uri=FACEPLANT.studyEndDate, domain=None, range=Optional[Union[str, Iso8601DateTime]])

slots.contactInst = Slot(uri=FACEPLANT.contactInst, name="contactInst", curie=FACEPLANT.curie('contactInst'),
                   model_uri=FACEPLANT.contactInst, domain=None, range=str)

slots.locationCountry = Slot(uri=FACEPLANT.locationCountry, name="locationCountry", curie=FACEPLANT.curie('locationCountry'),
                   model_uri=FACEPLANT.locationCountry, domain=None, range=str)

slots.siteName = Slot(uri=FACEPLANT.siteName, name="siteName", curie=FACEPLANT.curie('siteName'),
                   model_uri=FACEPLANT.siteName, domain=None, range=str)

slots.locationLatitude = Slot(uri=FACEPLANT.locationLatitude, name="locationLatitude", curie=FACEPLANT.curie('locationLatitude'),
                   model_uri=FACEPLANT.locationLatitude, domain=None, range=Optional[Decimal])

slots.locationLongitude = Slot(uri=FACEPLANT.locationLongitude, name="locationLongitude", curie=FACEPLANT.curie('locationLongitude'),
                   model_uri=FACEPLANT.locationLongitude, domain=None, range=Optional[Decimal])

slots.locationAltitude = Slot(uri=FACEPLANT.locationAltitude, name="locationAltitude", curie=FACEPLANT.curie('locationAltitude'),
                   model_uri=FACEPLANT.locationAltitude, domain=None, range=Optional[Union[str, MeasurementWithUnit]])

slots.expeDesignDesc = Slot(uri=FACEPLANT.expeDesignDesc, name="expeDesignDesc", curie=FACEPLANT.curie('expeDesignDesc'),
                   model_uri=FACEPLANT.expeDesignDesc, domain=None, range=str)

slots.expeDesignType = Slot(uri=FACEPLANT.expeDesignType, name="expeDesignType", curie=FACEPLANT.curie('expeDesignType'),
                   model_uri=FACEPLANT.expeDesignType, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.obsUnitLevelHierarchy = Slot(uri=FACEPLANT.obsUnitLevelHierarchy, name="obsUnitLevelHierarchy", curie=FACEPLANT.curie('obsUnitLevelHierarchy'),
                   model_uri=FACEPLANT.obsUnitLevelHierarchy, domain=None, range=Optional[str])

slots.obsUnitDesc = Slot(uri=FACEPLANT.obsUnitDesc, name="obsUnitDesc", curie=FACEPLANT.curie('obsUnitDesc'),
                   model_uri=FACEPLANT.obsUnitDesc, domain=None, range=str)

slots.growthFacilityDesc = Slot(uri=FACEPLANT.growthFacilityDesc, name="growthFacilityDesc", curie=FACEPLANT.curie('growthFacilityDesc'),
                   model_uri=FACEPLANT.growthFacilityDesc, domain=None, range=str)

slots.growthFacilityType = Slot(uri=FACEPLANT.growthFacilityType, name="growthFacilityType", curie=FACEPLANT.curie('growthFacilityType'),
                   model_uri=FACEPLANT.growthFacilityType, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.culturalPractice = Slot(uri=FACEPLANT.culturalPractice, name="culturalPractice", curie=FACEPLANT.curie('culturalPractice'),
                   model_uri=FACEPLANT.culturalPractice, domain=None, range=Optional[str])

slots.expeDesignMap = Slot(uri=FACEPLANT.expeDesignMap, name="expeDesignMap", curie=FACEPLANT.curie('expeDesignMap'),
                   model_uri=FACEPLANT.expeDesignMap, domain=None, range=Optional[Union[str, list[str]]])

slots.personName = Slot(uri=FACEPLANT.personName, name="personName", curie=FACEPLANT.curie('personName'),
                   model_uri=FACEPLANT.personName, domain=None, range=str)

slots.personEmail = Slot(uri=FACEPLANT.personEmail, name="personEmail", curie=FACEPLANT.curie('personEmail'),
                   model_uri=FACEPLANT.personEmail, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.personId = Slot(uri=FACEPLANT.personId, name="personId", curie=FACEPLANT.curie('personId'),
                   model_uri=FACEPLANT.personId, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.personRole = Slot(uri=FACEPLANT.personRole, name="personRole", curie=FACEPLANT.curie('personRole'),
                   model_uri=FACEPLANT.personRole, domain=None, range=Union[str, list[str]])

slots.personAffiliation = Slot(uri=FACEPLANT.personAffiliation, name="personAffiliation", curie=FACEPLANT.curie('personAffiliation'),
                   model_uri=FACEPLANT.personAffiliation, domain=None, range=Union[str, list[str]])

slots.dataFileLink = Slot(uri=FACEPLANT.dataFileLink, name="dataFileLink", curie=FACEPLANT.curie('dataFileLink'),
                   model_uri=FACEPLANT.dataFileLink, domain=None, range=str)

slots.dataFileDesc = Slot(uri=FACEPLANT.dataFileDesc, name="dataFileDesc", curie=FACEPLANT.curie('dataFileDesc'),
                   model_uri=FACEPLANT.dataFileDesc, domain=None, range=str)

slots.dataFileVersion = Slot(uri=FACEPLANT.dataFileVersion, name="dataFileVersion", curie=FACEPLANT.curie('dataFileVersion'),
                   model_uri=FACEPLANT.dataFileVersion, domain=None, range=Optional[str])

slots.biologicalMaterialId = Slot(uri=FACEPLANT.biologicalMaterialId, name="biologicalMaterialId", curie=FACEPLANT.curie('biologicalMaterialId'),
                   model_uri=FACEPLANT.biologicalMaterialId, domain=None, range=URIRef)

slots.biologicalMaterialExtId = Slot(uri=FACEPLANT.biologicalMaterialExtId, name="biologicalMaterialExtId", curie=FACEPLANT.curie('biologicalMaterialExtId'),
                   model_uri=FACEPLANT.biologicalMaterialExtId, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.organism = Slot(uri=FACEPLANT.organism, name="organism", curie=FACEPLANT.curie('organism'),
                   model_uri=FACEPLANT.organism, domain=None, range=Union[str, URIorCURIE])

slots.genus = Slot(uri=FACEPLANT.genus, name="genus", curie=FACEPLANT.curie('genus'),
                   model_uri=FACEPLANT.genus, domain=None, range=Optional[str])

slots.species = Slot(uri=FACEPLANT.species, name="species", curie=FACEPLANT.curie('species'),
                   model_uri=FACEPLANT.species, domain=None, range=Optional[str])

slots.infraspecificName = Slot(uri=FACEPLANT.infraspecificName, name="infraspecificName", curie=FACEPLANT.curie('infraspecificName'),
                   model_uri=FACEPLANT.infraspecificName, domain=None, range=Optional[Union[str, KeyValueList]])

slots.biologicalMaterialLatitude = Slot(uri=FACEPLANT.biologicalMaterialLatitude, name="biologicalMaterialLatitude", curie=FACEPLANT.curie('biologicalMaterialLatitude'),
                   model_uri=FACEPLANT.biologicalMaterialLatitude, domain=None, range=Optional[Decimal])

slots.biologicalMaterialLongitude = Slot(uri=FACEPLANT.biologicalMaterialLongitude, name="biologicalMaterialLongitude", curie=FACEPLANT.curie('biologicalMaterialLongitude'),
                   model_uri=FACEPLANT.biologicalMaterialLongitude, domain=None, range=Optional[Decimal])

slots.biologicalMaterialAltitude = Slot(uri=FACEPLANT.biologicalMaterialAltitude, name="biologicalMaterialAltitude", curie=FACEPLANT.curie('biologicalMaterialAltitude'),
                   model_uri=FACEPLANT.biologicalMaterialAltitude, domain=None, range=Optional[Union[str, MeasurementWithUnit]])

slots.biologicalMaterialCoordUncertainty = Slot(uri=FACEPLANT.biologicalMaterialCoordUncertainty, name="biologicalMaterialCoordUncertainty", curie=FACEPLANT.curie('biologicalMaterialCoordUncertainty'),
                   model_uri=FACEPLANT.biologicalMaterialCoordUncertainty, domain=None, range=Optional[Union[str, MeasurementWithUnit]])

slots.biologicalMaterialPreprocessing = Slot(uri=FACEPLANT.biologicalMaterialPreprocessing, name="biologicalMaterialPreprocessing", curie=FACEPLANT.curie('biologicalMaterialPreprocessing'),
                   model_uri=FACEPLANT.biologicalMaterialPreprocessing, domain=None, range=Optional[Union[str, list[str]]])

slots.materialSourceId = Slot(uri=FACEPLANT.materialSourceId, name="materialSourceId", curie=FACEPLANT.curie('materialSourceId'),
                   model_uri=FACEPLANT.materialSourceId, domain=None, range=Optional[str])

slots.materialSourceDoi = Slot(uri=FACEPLANT.materialSourceDoi, name="materialSourceDoi", curie=FACEPLANT.curie('materialSourceDoi'),
                   model_uri=FACEPLANT.materialSourceDoi, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.materialSourceAccNumber = Slot(uri=FACEPLANT.materialSourceAccNumber, name="materialSourceAccNumber", curie=FACEPLANT.curie('materialSourceAccNumber'),
                   model_uri=FACEPLANT.materialSourceAccNumber, domain=None, range=Optional[str])

slots.materialSourceAccName = Slot(uri=FACEPLANT.materialSourceAccName, name="materialSourceAccName", curie=FACEPLANT.curie('materialSourceAccName'),
                   model_uri=FACEPLANT.materialSourceAccName, domain=None, range=Optional[str])

slots.materialSourceInstCode = Slot(uri=FACEPLANT.materialSourceInstCode, name="materialSourceInstCode", curie=FACEPLANT.curie('materialSourceInstCode'),
                   model_uri=FACEPLANT.materialSourceInstCode, domain=None, range=Optional[str])

slots.materialSourceInstName = Slot(uri=FACEPLANT.materialSourceInstName, name="materialSourceInstName", curie=FACEPLANT.curie('materialSourceInstName'),
                   model_uri=FACEPLANT.materialSourceInstName, domain=None, range=Optional[str])

slots.materialSourceOtherIds = Slot(uri=FACEPLANT.materialSourceOtherIds, name="materialSourceOtherIds", curie=FACEPLANT.curie('materialSourceOtherIds'),
                   model_uri=FACEPLANT.materialSourceOtherIds, domain=None, range=Optional[Union[str, KeyValueList]])

slots.materialSourceLatitude = Slot(uri=FACEPLANT.materialSourceLatitude, name="materialSourceLatitude", curie=FACEPLANT.curie('materialSourceLatitude'),
                   model_uri=FACEPLANT.materialSourceLatitude, domain=None, range=Optional[Decimal])

slots.materialSourceLongitude = Slot(uri=FACEPLANT.materialSourceLongitude, name="materialSourceLongitude", curie=FACEPLANT.curie('materialSourceLongitude'),
                   model_uri=FACEPLANT.materialSourceLongitude, domain=None, range=Optional[Decimal])

slots.materialSourceAltitude = Slot(uri=FACEPLANT.materialSourceAltitude, name="materialSourceAltitude", curie=FACEPLANT.curie('materialSourceAltitude'),
                   model_uri=FACEPLANT.materialSourceAltitude, domain=None, range=Optional[Union[str, MeasurementWithUnit]])

slots.materialSourceCoordUncertainty = Slot(uri=FACEPLANT.materialSourceCoordUncertainty, name="materialSourceCoordUncertainty", curie=FACEPLANT.curie('materialSourceCoordUncertainty'),
                   model_uri=FACEPLANT.materialSourceCoordUncertainty, domain=None, range=Optional[Union[str, MeasurementWithUnit]])

slots.materialSourceDesc = Slot(uri=FACEPLANT.materialSourceDesc, name="materialSourceDesc", curie=FACEPLANT.curie('materialSourceDesc'),
                   model_uri=FACEPLANT.materialSourceDesc, domain=None, range=Optional[str])

slots.envParam = Slot(uri=FACEPLANT.envParam, name="envParam", curie=FACEPLANT.curie('envParam'),
                   model_uri=FACEPLANT.envParam, domain=None, range=str)

slots.envParamValue = Slot(uri=FACEPLANT.envParamValue, name="envParamValue", curie=FACEPLANT.curie('envParamValue'),
                   model_uri=FACEPLANT.envParamValue, domain=None, range=str)

slots.expeFactorType = Slot(uri=FACEPLANT.expeFactorType, name="expeFactorType", curie=FACEPLANT.curie('expeFactorType'),
                   model_uri=FACEPLANT.expeFactorType, domain=None, range=str)

slots.expeFactorDesc = Slot(uri=FACEPLANT.expeFactorDesc, name="expeFactorDesc", curie=FACEPLANT.curie('expeFactorDesc'),
                   model_uri=FACEPLANT.expeFactorDesc, domain=None, range=Optional[str])

slots.expeFactorValues = Slot(uri=FACEPLANT.expeFactorValues, name="expeFactorValues", curie=FACEPLANT.curie('expeFactorValues'),
                   model_uri=FACEPLANT.expeFactorValues, domain=None, range=Union[str, list[str]])

slots.eventType = Slot(uri=FACEPLANT.eventType, name="eventType", curie=FACEPLANT.curie('eventType'),
                   model_uri=FACEPLANT.eventType, domain=None, range=str)

slots.eventAccNumber = Slot(uri=FACEPLANT.eventAccNumber, name="eventAccNumber", curie=FACEPLANT.curie('eventAccNumber'),
                   model_uri=FACEPLANT.eventAccNumber, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.eventDesc = Slot(uri=FACEPLANT.eventDesc, name="eventDesc", curie=FACEPLANT.curie('eventDesc'),
                   model_uri=FACEPLANT.eventDesc, domain=None, range=Optional[str])

slots.eventDate = Slot(uri=FACEPLANT.eventDate, name="eventDate", curie=FACEPLANT.curie('eventDate'),
                   model_uri=FACEPLANT.eventDate, domain=None, range=Union[Union[str, Iso8601DateTime], list[Union[str, Iso8601DateTime]]])

slots.obsUnitId = Slot(uri=FACEPLANT.obsUnitId, name="obsUnitId", curie=FACEPLANT.curie('obsUnitId'),
                   model_uri=FACEPLANT.obsUnitId, domain=None, range=URIRef)

slots.obsUnitType = Slot(uri=FACEPLANT.obsUnitType, name="obsUnitType", curie=FACEPLANT.curie('obsUnitType'),
                   model_uri=FACEPLANT.obsUnitType, domain=None, range=str)

slots.externalId = Slot(uri=FACEPLANT.externalId, name="externalId", curie=FACEPLANT.curie('externalId'),
                   model_uri=FACEPLANT.externalId, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.spatialDistribution = Slot(uri=FACEPLANT.spatialDistribution, name="spatialDistribution", curie=FACEPLANT.curie('spatialDistribution'),
                   model_uri=FACEPLANT.spatialDistribution, domain=None, range=Optional[Union[Union[str, KeyValueList], list[Union[str, KeyValueList]]]])

slots.obsUnitFactorValue = Slot(uri=FACEPLANT.obsUnitFactorValue, name="obsUnitFactorValue", curie=FACEPLANT.curie('obsUnitFactorValue'),
                   model_uri=FACEPLANT.obsUnitFactorValue, domain=None, range=Optional[Union[str, list[str]]])

slots.sampleId = Slot(uri=FACEPLANT.sampleId, name="sampleId", curie=FACEPLANT.curie('sampleId'),
                   model_uri=FACEPLANT.sampleId, domain=None, range=URIRef)

slots.developmentStage = Slot(uri=FACEPLANT.developmentStage, name="developmentStage", curie=FACEPLANT.curie('developmentStage'),
                   model_uri=FACEPLANT.developmentStage, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.anatomicalEntity = Slot(uri=FACEPLANT.anatomicalEntity, name="anatomicalEntity", curie=FACEPLANT.curie('anatomicalEntity'),
                   model_uri=FACEPLANT.anatomicalEntity, domain=None, range=Union[str, URIorCURIE])

slots.sampleDesc = Slot(uri=FACEPLANT.sampleDesc, name="sampleDesc", curie=FACEPLANT.curie('sampleDesc'),
                   model_uri=FACEPLANT.sampleDesc, domain=None, range=Optional[str])

slots.collectionDate = Slot(uri=FACEPLANT.collectionDate, name="collectionDate", curie=FACEPLANT.curie('collectionDate'),
                   model_uri=FACEPLANT.collectionDate, domain=None, range=Union[str, Iso8601DateTime])

slots.variableId = Slot(uri=FACEPLANT.variableId, name="variableId", curie=FACEPLANT.curie('variableId'),
                   model_uri=FACEPLANT.variableId, domain=None, range=URIRef)

slots.variableName = Slot(uri=FACEPLANT.variableName, name="variableName", curie=FACEPLANT.curie('variableName'),
                   model_uri=FACEPLANT.variableName, domain=None, range=Optional[str])

slots.variableAccNumber = Slot(uri=FACEPLANT.variableAccNumber, name="variableAccNumber", curie=FACEPLANT.curie('variableAccNumber'),
                   model_uri=FACEPLANT.variableAccNumber, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.traitName = Slot(uri=FACEPLANT.traitName, name="traitName", curie=FACEPLANT.curie('traitName'),
                   model_uri=FACEPLANT.traitName, domain=None, range=str)

slots.traitEntity = Slot(uri=FACEPLANT.traitEntity, name="traitEntity", curie=FACEPLANT.curie('traitEntity'),
                   model_uri=FACEPLANT.traitEntity, domain=None, range=Optional[str])

slots.traitEntityAccessionNumber = Slot(uri=FACEPLANT.traitEntityAccessionNumber, name="traitEntityAccessionNumber", curie=FACEPLANT.curie('traitEntityAccessionNumber'),
                   model_uri=FACEPLANT.traitEntityAccessionNumber, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.traitCharacteristic = Slot(uri=FACEPLANT.traitCharacteristic, name="traitCharacteristic", curie=FACEPLANT.curie('traitCharacteristic'),
                   model_uri=FACEPLANT.traitCharacteristic, domain=None, range=Optional[str])

slots.traitCharacteristicAccessionNumber = Slot(uri=FACEPLANT.traitCharacteristicAccessionNumber, name="traitCharacteristicAccessionNumber", curie=FACEPLANT.curie('traitCharacteristicAccessionNumber'),
                   model_uri=FACEPLANT.traitCharacteristicAccessionNumber, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.traitAccNumber = Slot(uri=FACEPLANT.traitAccNumber, name="traitAccNumber", curie=FACEPLANT.curie('traitAccNumber'),
                   model_uri=FACEPLANT.traitAccNumber, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.methodName = Slot(uri=FACEPLANT.methodName, name="methodName", curie=FACEPLANT.curie('methodName'),
                   model_uri=FACEPLANT.methodName, domain=None, range=str)

slots.methodAccNumber = Slot(uri=FACEPLANT.methodAccNumber, name="methodAccNumber", curie=FACEPLANT.curie('methodAccNumber'),
                   model_uri=FACEPLANT.methodAccNumber, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.methodDesc = Slot(uri=FACEPLANT.methodDesc, name="methodDesc", curie=FACEPLANT.curie('methodDesc'),
                   model_uri=FACEPLANT.methodDesc, domain=None, range=Optional[str])

slots.methodRef = Slot(uri=FACEPLANT.methodRef, name="methodRef", curie=FACEPLANT.curie('methodRef'),
                   model_uri=FACEPLANT.methodRef, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.scaleName = Slot(uri=FACEPLANT.scaleName, name="scaleName", curie=FACEPLANT.curie('scaleName'),
                   model_uri=FACEPLANT.scaleName, domain=None, range=str)

slots.scaleAccNumber = Slot(uri=FACEPLANT.scaleAccNumber, name="scaleAccNumber", curie=FACEPLANT.curie('scaleAccNumber'),
                   model_uri=FACEPLANT.scaleAccNumber, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.timeScale = Slot(uri=FACEPLANT.timeScale, name="timeScale", curie=FACEPLANT.curie('timeScale'),
                   model_uri=FACEPLANT.timeScale, domain=None, range=Optional[Union[str, list[str]]])

slots.Investigation_persons = Slot(uri=FACEPLANT.persons, name="Investigation_persons", curie=FACEPLANT.curie('persons'),
                   model_uri=FACEPLANT.Investigation_persons, domain=Investigation, range=Union[Union[dict, "Person"], list[Union[dict, "Person"]]])

slots.Investigation_studies = Slot(uri=FACEPLANT.studies, name="Investigation_studies", curie=FACEPLANT.curie('studies'),
                   model_uri=FACEPLANT.Investigation_studies, domain=Investigation, range=Union[Union[dict, "Study"], list[Union[dict, "Study"]]])

slots.Study_persons = Slot(uri=FACEPLANT.persons, name="Study_persons", curie=FACEPLANT.curie('persons'),
                   model_uri=FACEPLANT.Study_persons, domain=Study, range=Optional[Union[Union[dict, "Person"], list[Union[dict, "Person"]]]])

slots.Study_biologicalMaterials = Slot(uri=FACEPLANT.biologicalMaterials, name="Study_biologicalMaterials", curie=FACEPLANT.curie('biologicalMaterials'),
                   model_uri=FACEPLANT.Study_biologicalMaterials, domain=Study, range=Union[dict[Union[str, BiologicalMaterialBiologicalMaterialId], Union[dict, "BiologicalMaterial"]], list[Union[dict, "BiologicalMaterial"]]])

slots.Study_observationUnits = Slot(uri=FACEPLANT.observationUnits, name="Study_observationUnits", curie=FACEPLANT.curie('observationUnits'),
                   model_uri=FACEPLANT.Study_observationUnits, domain=Study, range=Union[dict[Union[str, ObservationUnitObsUnitId], Union[dict, "ObservationUnit"]], list[Union[dict, "ObservationUnit"]]])

slots.Study_observedVariables = Slot(uri=FACEPLANT.observedVariables, name="Study_observedVariables", curie=FACEPLANT.curie('observedVariables'),
                   model_uri=FACEPLANT.Study_observedVariables, domain=Study, range=Union[dict[Union[str, ObservedVariableVariableId], Union[dict, "ObservedVariable"]], list[Union[dict, "ObservedVariable"]]])

slots.ObservationUnit_externalId = Slot(uri=FACEPLANT.externalId, name="ObservationUnit_externalId", curie=FACEPLANT.curie('externalId'),
                   model_uri=FACEPLANT.ObservationUnit_externalId, domain=ObservationUnit, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.Sample_externalId = Slot(uri=FACEPLANT.externalId, name="Sample_externalId", curie=FACEPLANT.curie('externalId'),
                   model_uri=FACEPLANT.Sample_externalId, domain=Sample, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])
