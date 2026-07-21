from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "0.1.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'source': {'tag': 'source',
                                'value': 'Derived from the MIAPPE LinkML schema '
                                         '(https://github.com/lakehouse-code/datamodel/blob/main/miappe.yaml), '
                                         'itself generated from '
                                         'MIAPPE_Checklist_Data_Model.tsv in the '
                                         'MIAPPE/MIAPPE GitHub repository.'},
                     'source_version': {'tag': 'source_version',
                                        'value': 'MIAPPE 1.2'}},
     'default_prefix': 'faceplant',
     'default_range': 'string',
     'description': 'A LinkML data model for plant phenotypic data, based on the '
                    'Minimum Information About a Plant Phenotyping Experiment '
                    '(MIAPPE v1.2) checklist. Slot names follow the original '
                    'MIAPPE codenames for traceability.\n',
     'id': 'https://w3id.org/your-org/faceplant',
     'imports': ['linkml:types'],
     'license': 'https://creativecommons.org/licenses/by/4.0/',
     'name': 'faceplant',
     'prefixes': {'CO': {'prefix_prefix': 'CO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/CO_'},
                  'CO_322': {'prefix_prefix': 'CO_322',
                             'prefix_reference': 'https://cropontology.org/rdf/CO_322:'},
                  'CO_715': {'prefix_prefix': 'CO_715',
                             'prefix_reference': 'http://purl.obolibrary.org/obo/CO_715_'},
                  'DOI': {'prefix_prefix': 'DOI',
                          'prefix_reference': 'http://identifiers.org/doi/'},
                  'EO': {'prefix_prefix': 'EO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/EO_'},
                  'NCBITaxon': {'prefix_prefix': 'NCBITaxon',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/NCBITaxon_'},
                  'ORCID': {'prefix_prefix': 'ORCID',
                            'prefix_reference': 'http://identifiers.org/orcid/'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'PO': {'prefix_prefix': 'PO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/PO_'},
                  'TO': {'prefix_prefix': 'TO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/TO_'},
                  'faceplant': {'prefix_prefix': 'faceplant',
                                'prefix_reference': 'https://w3id.org/your-org/faceplant/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'miappe': {'prefix_prefix': 'miappe',
                             'prefix_reference': 'https://w3id.org/miappe/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'source_file': 'src/faceplant/schema/faceplant.yaml',
     'title': 'FacePlant: a plant phenotypic data model',
     'types': {'iso8601DateTime': {'description': 'ISO 8601 date or date-time, '
                                                  'with optional timezone.',
                                   'from_schema': 'https://w3id.org/your-org/faceplant',
                                   'name': 'iso8601DateTime',
                                   'pattern': '^\\d{4}-\\d{2}-\\d{2}([Tt '
                                              '][0-9:.+-]+(Z|[+-][0-9]{2}:[0-9]{2})?)?$',
                                   'typeof': 'string'},
               'keyValueList': {'description': 'Key-value pair list encoded as '
                                               'text, usually separated by commas '
                                               'or semicolons.',
                                'from_schema': 'https://w3id.org/your-org/faceplant',
                                'name': 'keyValueList',
                                'typeof': 'string'},
               'measurementWithUnit': {'description': 'Numeric value followed by a '
                                                      'unit abbreviation, as used '
                                                      'in the MIAPPE checklist.',
                                       'from_schema': 'https://w3id.org/your-org/faceplant',
                                       'name': 'measurementWithUnit',
                                       'typeof': 'string'}}} )


class MIAPPESubmission(ConfiguredBaseModel):
    """
    A complete MIAPPE submission containing exactly one investigation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant', 'tree_root': True})

    investigation: Investigation = Field(default=..., description="""The single investigation represented by a MIAPPE submission.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MIAPPESubmission']} })


class Investigation(ConfiguredBaseModel):
    """
    Investigations are research programmes with defined aims. They can exist at various scales, including a grant-funded programme, a publication, or a single experiment.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant',
         'slot_usage': {'persons': {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                                           'value': '1+ '
                                                                                    'per '
                                                                                    'investigation'}},
                                    'name': 'persons',
                                    'required': True},
                        'studies': {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                                           'value': '1+ '
                                                                                    'per '
                                                                                    'investigation'}},
                                    'name': 'studies',
                                    'required': True}}})

    investigationId: Optional[str] = Field(default=None, description="""Identifier comprising the unique name of the institution/database hosting the submission and the accession number of the investigation there.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Unique identifier'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Investigation unique ID'}},
         'domain_of': ['Investigation']} })
    investigationTitle: str = Field(default=..., description="""Human-readable string summarising the investigation.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text (short)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Investigation title'}},
         'domain_of': ['Investigation']} })
    investigationDescription: Optional[str] = Field(default=None, description="""Human-readable text describing the investigation in more detail.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Investigation description'}},
         'domain_of': ['Investigation']} })
    submissionDate: Optional[str] = Field(default=None, description="""Date of submission of the dataset being described to a host repository.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Date/Time (ISO 8601, optional '
                                                    'time zone)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Submission date'}},
         'domain_of': ['Investigation']} })
    publicReleaseDate: Optional[str] = Field(default=None, description="""Date of first public release of the dataset being described.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Date/Time (ISO 8601, optional '
                                                    'time zone)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Public release date'}},
         'domain_of': ['Investigation']} })
    license: Optional[str] = Field(default=None, description="""License for reuse of the data associated with this investigation.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Unique identifier'},
                         'miappe_label': {'tag': 'miappe_label', 'value': 'License'}},
         'domain_of': ['Investigation']} })
    miappeVersion: str = Field(default=..., description="""The version of MIAPPE used.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Version number'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'MIAPPE version'}},
         'domain_of': ['Investigation']} })
    associatedPublication: Optional[list[str]] = Field(default=None, description="""Identifier for a literature publication where the investigation is described.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+'},
                         'miappe_format': {'tag': 'miappe_format', 'value': 'DOI'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Associated publication'}},
         'domain_of': ['Investigation']} })
    persons: list[Person] = Field(default=..., description="""People associated with an investigation or study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1+ per investigation'}},
         'domain_of': ['Investigation', 'Study']} })
    studies: list[Study] = Field(default=..., description="""Studies belonging to an investigation.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1+ per investigation'}},
         'domain_of': ['Investigation']} })


class Study(ConfiguredBaseModel):
    """
    A study or experiment comprises a series of assays or measurements of one or more types, undertaken to answer a particular biological question.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant',
         'slot_usage': {'biologicalMaterials': {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                                                       'value': '1+ '
                                                                                                'per '
                                                                                                'study'}},
                                                'name': 'biologicalMaterials',
                                                'required': True},
                        'observationUnits': {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                                                    'value': '1+ '
                                                                                             'per '
                                                                                             'study'}},
                                             'name': 'observationUnits',
                                             'required': True},
                        'observedVariables': {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                                                     'value': '1+ '
                                                                                              'per '
                                                                                              'study'}},
                                              'name': 'observedVariables',
                                              'required': True},
                        'persons': {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                                           'value': '0+ '
                                                                                    'per '
                                                                                    'study'}},
                                    'name': 'persons',
                                    'required': False}}})

    studyId: Optional[str] = Field(default=None, description="""Unique identifier comprising the name or identifier for the institution or database hosting the study data and the identifier of the study there.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Unique identifier'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Study unique ID'}},
         'domain_of': ['Study']} })
    studyTitle: str = Field(default=..., description="""Human-readable name summarising the study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text (short)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Study title'}},
         'domain_of': ['Study']} })
    studyDescription: Optional[str] = Field(default=None, description="""Human-readable text describing the study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Study description'}},
         'domain_of': ['Study']} })
    studyStartDate: str = Field(default=..., description="""Date and, if relevant, time when the experiment started.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Date/Time (ISO 8601, optional '
                                                    'time zone)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Start date of study'}},
         'domain_of': ['Study']} })
    studyEndDate: Optional[str] = Field(default=None, description="""Date and, if relevant, time when the experiment ended.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Date/Time (ISO 8601, optional '
                                                    'time zone)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'End date of study'}},
         'domain_of': ['Study']} })
    contactInst: str = Field(default=..., description="""Name and address of the institution responsible for the study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text (short)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Contact institution'}},
         'domain_of': ['Study']} })
    locationCountry: str = Field(default=..., description="""Country where the experiment took place, either as a full name or preferably as a 2-letter ISO 3166 country code.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Country name or 2-letter code '
                                                    '(ISO 3166)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Geographic location (country)'}},
         'domain_of': ['Study']} })
    siteName: str = Field(default=..., description="""Name of the natural site, experimental field, greenhouse, phenotyping facility, or other site where the experiment took place.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text (short)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Experimental site name'}},
         'domain_of': ['Study']} })
    locationLatitude: Optional[Decimal] = Field(default=None, description="""Latitude of the experimental site in decimal degrees.""", ge=-90, le=90, json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1 (1 if longitude is '
                                                         'provided)'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Degrees in decimal format (ISO '
                                                    '6709)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Geographic location (latitude)'}},
         'domain_of': ['Study']} })
    locationLongitude: Optional[Decimal] = Field(default=None, description="""Longitude of the experimental site in decimal degrees.""", ge=-180, le=180, json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1 (1 if latitude is '
                                                         'provided)'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Degrees in decimal format (ISO '
                                                    '6709)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Geographic location (longitude)'}},
         'domain_of': ['Study']} })
    locationAltitude: Optional[str] = Field(default=None, description="""Altitude of the experimental site, provided in metres.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Numeric + unit abbreviation'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Geographic location (altitude)'}},
         'domain_of': ['Study']} })
    expeDesignDesc: str = Field(default=..., description="""Short description of the experimental design, possibly including statistical design.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Description of the experimental '
                                                   'design'}},
         'domain_of': ['Study']} })
    expeDesignType: Optional[str] = Field(default=None, description="""Type of experimental design of the study, preferably as a Crop Ontology accession.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Crop Ontology term'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Type of experimental design'}},
         'domain_of': ['Study']} })
    obsUnitLevelHierarchy: Optional[str] = Field(default=None, description="""Hierarchy of the different levels of repetition.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Formatted text (level>level)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Observation unit level hierarchy'}},
         'domain_of': ['Study']} })
    obsUnitDesc: str = Field(default=..., description="""General description of the observation units in the study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Observation unit description'}},
         'domain_of': ['Study']} })
    growthFacilityDesc: str = Field(default=..., description="""Short description of the facility in which the study was carried out.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text (short)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Description of growth facility'}},
         'domain_of': ['Study']} })
    growthFacilityType: Optional[str] = Field(default=None, description="""Type of growth facility, preferably as a Crop Ontology accession.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Crop Ontology term'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Type of growth facility'}},
         'domain_of': ['Study']} })
    culturalPractice: Optional[str] = Field(default=None, description="""General description of the cultural practices of the study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Cultural practices'}},
         'domain_of': ['Study']} })
    expeDesignMap: Optional[list[str]] = Field(default=None, description="""Representation of the experimental design as a URL or file name.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'URL or file name'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Map of experimental design'}},
         'domain_of': ['Study']} })
    persons: Optional[list[Person]] = Field(default=None, description="""People associated with an investigation or study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+ per study'}},
         'domain_of': ['Investigation', 'Study']} })
    dataFiles: Optional[list[DataFile]] = Field(default=None, description="""Data files associated with a study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+ per study'}},
         'domain_of': ['Study']} })
    biologicalMaterials: list[BiologicalMaterial] = Field(default=..., description="""Biological materials associated with a study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1+ per study'}},
         'domain_of': ['Study']} })
    environment: Optional[Environment] = Field(default=None, description="""Constant environmental parameters for a study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1 per study'}},
         'domain_of': ['Study']} })
    experimentalFactors: Optional[list[ExperimentalFactor]] = Field(default=None, description="""Experimental factors associated with a study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+ per study'}},
         'domain_of': ['Study']} })
    events: Optional[list[Event]] = Field(default=None, description="""Events associated with a study or observation unit.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+ per study or observation '
                                                         'unit'}},
         'domain_of': ['Study', 'ObservationUnit']} })
    observationUnits: list[ObservationUnit] = Field(default=..., description="""Observation units associated with a study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1+ per study'}},
         'domain_of': ['Study']} })
    observedVariables: list[ObservedVariable] = Field(default=..., description="""Observed variables associated with a study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1+ per study'}},
         'domain_of': ['Study']} })


class Person(ConfiguredBaseModel):
    """
    A human involved in the investigation or specifically in one of its studies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    personName: str = Field(default=..., description="""The person's name, either full name or as used in scientific publications.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format', 'value': 'Name'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Person name'}},
         'domain_of': ['Person']} })
    personEmail: Optional[str] = Field(default=None, description="""The electronic mail address of the person.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'email address'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Person email'}},
         'domain_of': ['Person']} })
    personId: Optional[str] = Field(default=None, description="""Identifier for the data submitter or person. ORCID identifiers are recommended.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Unique identifier'},
                         'miappe_label': {'tag': 'miappe_label', 'value': 'Person ID'}},
         'domain_of': ['Person']} })
    personRole: list[str] = Field(default=..., description="""Type of contribution of the person to the investigation.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1+'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text (short)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Person role'}},
         'domain_of': ['Person']} })
    personAffiliation: list[str] = Field(default=..., description="""The institution the person belongs to.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1+'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text (short)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Person affiliation'}},
         'domain_of': ['Person']} })

    @field_validator('personEmail')
    def pattern_personEmail(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid personEmail format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid personEmail format: {v}"
            raise ValueError(err_msg)
        return v


class DataFile(ConfiguredBaseModel):
    """
    A file or digital object holding observation data recorded during one or more assays of the study, typically in tabular form.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    dataFileLink: str = Field(default=..., description="""Link to the data file or identifier of a data file submitted with the MIAPPE submission.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'URL or file name'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Data file link'}},
         'domain_of': ['DataFile']} })
    dataFileDesc: str = Field(default=..., description="""Description of the data file format.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text (short)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Data file description'}},
         'domain_of': ['DataFile']} })
    dataFileVersion: Optional[str] = Field(default=None, description="""Version of the dataset or actual data.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Software version number'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Data file version'}},
         'domain_of': ['DataFile']} })


class BiologicalMaterial(ConfiguredBaseModel):
    """
    The biological material being studied, such as plants grown from a seed bag or plants grown in a particular field.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    biologicalMaterialId: str = Field(default=..., description="""Code used to identify the biological material in the data file. It should be unique within the investigation.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Unique identifier'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Biological material ID'}},
         'domain_of': ['BiologicalMaterial']} })
    biologicalMaterialExtId: Optional[list[str]] = Field(default=None, description="""One or more external identifiers for the biological material.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Semicolon-separated list of '
                                                    'unique identifiers'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Biological material external ID'}},
         'domain_of': ['BiologicalMaterial']} })
    organism: str = Field(default=..., description="""Identifier for the organism at species level. NCBI Taxon ID is recommended.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Unique identifier'},
                         'miappe_label': {'tag': 'miappe_label', 'value': 'Organism'}},
         'domain_of': ['BiologicalMaterial']} })
    genus: Optional[str] = Field(default=None, description="""Genus name for the organism under study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Genus name'},
                         'miappe_label': {'tag': 'miappe_label', 'value': 'Genus'}},
         'domain_of': ['BiologicalMaterial']} })
    species: Optional[str] = Field(default=None, description="""Species name or specific epithet for the organism under study.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Species name'},
                         'miappe_label': {'tag': 'miappe_label', 'value': 'Species'}},
         'domain_of': ['BiologicalMaterial']} })
    infraspecificName: Optional[str] = Field(default=None, description="""Name of any subtaxa level, including variety, crossing name, cultivar, or line.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Key-value pair list or '
                                                    'MCPD-compliant format'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Infraspecific name'}},
         'domain_of': ['BiologicalMaterial']} })
    biologicalMaterialLatitude: Optional[Decimal] = Field(default=None, description="""Latitude of the studied biological material.""", ge=-90, le=90, json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1 (1 if longitude is '
                                                         'provided)'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Degrees in decimal format (ISO '
                                                    '6709)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Biological material latitude'}},
         'domain_of': ['BiologicalMaterial']} })
    biologicalMaterialLongitude: Optional[Decimal] = Field(default=None, description="""Longitude of the studied biological material.""", ge=-180, le=180, json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1 (1 if latitude is '
                                                         'provided)'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Degrees in decimal format (ISO '
                                                    '6709)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Biological material longitude'}},
         'domain_of': ['BiologicalMaterial']} })
    biologicalMaterialAltitude: Optional[str] = Field(default=None, description="""Altitude of the studied biological material, provided in meters.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Numeric + unit abbreviation'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Biological material altitude'}},
         'domain_of': ['BiologicalMaterial']} })
    biologicalMaterialCoordUncertainty: Optional[str] = Field(default=None, description="""Circular uncertainty of the coordinates, preferably provided in meters.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format', 'value': 'Numeric'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Biological material coordinates '
                                                   'uncertainty'}},
         'domain_of': ['BiologicalMaterial']} })
    biologicalMaterialPreprocessing: Optional[list[str]] = Field(default=None, description="""Description of any process or treatment applied uniformly to the biological material before the study itself.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Plant Environment Ontology and/or '
                                                    'free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Biological material '
                                                   'preprocessing'}},
         'domain_of': ['BiologicalMaterial']} })
    materialSourceId: Optional[str] = Field(default=None, description="""Identifier for the source of the biological material, commonly called germplasm, accession, genotype, or variety.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Unique identifier'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Material source ID (Holding '
                                                   'institute/stock centre, '
                                                   'accession)'}},
         'domain_of': ['BiologicalMaterial']} })
    materialSourceDoi: Optional[str] = Field(default=None, description="""Digital Object Identifier of the material source.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format', 'value': 'DOI'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Material source DOI'}},
         'domain_of': ['BiologicalMaterial']} })
    materialSourceAccNumber: Optional[str] = Field(default=None, description="""Unique identifier for accessions within a genebank or laboratory.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Unique identifier'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Material source accession number'}},
         'domain_of': ['BiologicalMaterial']} })
    materialSourceAccName: Optional[str] = Field(default=None, description="""Genebank accession registered name, other designation, or variety name.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text (short)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Material source accession name'}},
         'domain_of': ['BiologicalMaterial']} })
    materialSourceInstCode: Optional[str] = Field(default=None, description="""FAO WIEWS code of the institute where the accession is maintained.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Unique identifier'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Material source institute code'}},
         'domain_of': ['BiologicalMaterial']} })
    materialSourceInstName: Optional[str] = Field(default=None, description="""Name of the material source institute.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Institute name'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Material source institute name'}},
         'domain_of': ['BiologicalMaterial']} })
    materialSourceOtherIds: Optional[str] = Field(default=None, description="""Other identifiers known to exist in other collections for this material source.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Key:Value pairs'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Material source other '
                                                   'identifiers'}},
         'domain_of': ['BiologicalMaterial']} })
    materialSourceLatitude: Optional[Decimal] = Field(default=None, description="""Latitude of the material source.""", ge=-90, le=90, json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1 (1 if longitude is '
                                                         'provided)'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Degrees in decimal format (ISO '
                                                    '6709)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Material source latitude'}},
         'domain_of': ['BiologicalMaterial']} })
    materialSourceLongitude: Optional[Decimal] = Field(default=None, description="""Longitude of the material source.""", ge=-180, le=180, json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1 (1 if latitude is '
                                                         'provided)'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Degrees in decimal format (ISO '
                                                    '6709)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Material source longitude'}},
         'domain_of': ['BiologicalMaterial']} })
    materialSourceAltitude: Optional[str] = Field(default=None, description="""Altitude of the material source, provided in metres.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Numeric + unit abbreviation'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Material source altitude'}},
         'domain_of': ['BiologicalMaterial']} })
    materialSourceCoordUncertainty: Optional[str] = Field(default=None, description="""Circular uncertainty of the coordinates, provided in meters.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Numeric + unit abbreviation'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Material source coordinates '
                                                   'uncertainty'}},
         'domain_of': ['BiologicalMaterial']} })
    materialSourceDesc: Optional[str] = Field(default=None, description="""Description of the material source.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Material source description'}},
         'domain_of': ['BiologicalMaterial']} })


class Environment(ConfiguredBaseModel):
    """
    Environmental parameters that were kept constant throughout the study and did not change between observation units or assays.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    environmentParameters: list[EnvironmentParameter] = Field(default=..., description="""Constant environmental parameter values for a study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Environment']} })


class EnvironmentParameter(ConfiguredBaseModel):
    """
    A constant environmental parameter and its value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    envParam: str = Field(default=..., description="""Name of an environment parameter constant within the experiment.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1+'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Environment parameter'}},
         'domain_of': ['EnvironmentParameter']} })
    envParamValue: str = Field(default=..., description="""Value of the environment parameter constant within the experiment.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1 per parameter'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Environment parameter value'}},
         'domain_of': ['EnvironmentParameter']} })


class ExperimentalFactor(ConfiguredBaseModel):
    """
    A condition that varies between observation units and whose impact on the biological material is the object of a study.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    expeFactorType: str = Field(default=..., description="""Name or acronym of the experimental factor.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Experimental Factor type'}},
         'domain_of': ['ExperimentalFactor']} })
    expeFactorDesc: Optional[str] = Field(default=None, description="""Free text description of the experimental factor, including relevant treatment planning and protocol details.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Experimental Factor description'}},
         'domain_of': ['ExperimentalFactor']} })
    expeFactorValues: list[str] = Field(default=..., description="""List of possible values for the experimental factor.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '2+ per factor'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Experimental Factor values'}},
         'domain_of': ['ExperimentalFactor']} })


class Event(ConfiguredBaseModel):
    """
    A discrete occurrence at a particular time in the experiment, natural or unnatural, such as planting, rain, fertilizing, or watering.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    eventType: str = Field(default=..., description="""Short name of the event.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text (short)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Event type'}},
         'domain_of': ['Event']} })
    eventAccNumber: Optional[str] = Field(default=None, description="""Accession number of the event type in a suitable controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Crop Ontology term'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Event accession number'}},
         'domain_of': ['Event']} })
    eventDesc: Optional[str] = Field(default=None, description="""Description of the event, including amount applied and possibly duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Event description'}},
         'domain_of': ['Event']} })
    eventDate: list[str] = Field(default=..., description="""Date and time of the event.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1+'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Date/Time (ISO 8601, optional '
                                                    'time zone)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Event date'}},
         'domain_of': ['Event']} })


class ObservationUnit(ConfiguredBaseModel):
    """
    Objects that are subject to instances of observation and measurement. Observation units may comprise plants, their environment, or pure environmental observation units.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant',
         'slot_usage': {'externalId': {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                                              'value': '0+'},
                                                       'miappe_label': {'tag': 'miappe_label',
                                                                        'value': 'Observation '
                                                                                 'unit '
                                                                                 'external '
                                                                                 'ID'}},
                                       'description': 'Identifier for the observation '
                                                      'unit in a persistent '
                                                      'repository, comprising the '
                                                      'repository name and observation '
                                                      'unit identifier.\n',
                                       'name': 'externalId'}}})

    obsUnitId: str = Field(default=..., description="""Identifier used to identify the observation unit in data files containing values observed or measured on that unit.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Unique identifier'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Observation unit ID'}},
         'domain_of': ['ObservationUnit']} })
    obsUnitType: str = Field(default=..., description="""Type of observation unit in textual form, usually study, block, sub-block, plot, sub-plot, pot, or plant.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Observation unit type'}},
         'domain_of': ['ObservationUnit']} })
    externalId: Optional[list[str]] = Field(default=None, description="""Identifier for the observation unit in a persistent repository, comprising the repository name and observation unit identifier.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Observation unit external ID'}},
         'domain_of': ['ObservationUnit', 'Sample']} })
    spatialDistribution: Optional[list[str]] = Field(default=None, description="""Type and value of a spatial coordinate or level of observation as a key-value pair.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Formatted text (Key:value)'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Spatial distribution'}},
         'domain_of': ['ObservationUnit']} })
    obsUnitFactorValue: Optional[list[str]] = Field(default=None, description="""List of values for each factor applied to the observation unit.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Observation Unit factor value'}},
         'domain_of': ['ObservationUnit']} })
    biologicalMaterialRefs: Optional[list[str]] = Field(default=None, description="""References from an observation unit to biological material identifiers defined in the study-level biologicalMaterials list.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+ per observation unit'}},
         'domain_of': ['ObservationUnit']} })
    events: Optional[list[Event]] = Field(default=None, description="""Events associated with a study or observation unit.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+ per study or observation '
                                                         'unit'}},
         'domain_of': ['Study', 'ObservationUnit']} })
    samples: Optional[list[Sample]] = Field(default=None, description="""Samples associated with an observation unit.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+ per observation unit'}},
         'domain_of': ['ObservationUnit']} })


class Sample(ConfiguredBaseModel):
    """
    A portion of plant tissue harvested, non-harvested, or extracted from an observation unit for sub-plant observations and/or molecular studies.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant',
         'slot_usage': {'externalId': {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                                              'value': '0+'},
                                                       'miappe_label': {'tag': 'miappe_label',
                                                                        'value': 'Sample '
                                                                                 'external '
                                                                                 'ID'}},
                                       'description': 'Identifier for the sample in a '
                                                      'persistent repository, '
                                                      'comprising the repository name '
                                                      'and sample accession number.\n',
                                       'name': 'externalId'}}})

    sampleId: str = Field(default=..., description="""Unique identifier for the sample.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Unique identifier'},
                         'miappe_label': {'tag': 'miappe_label', 'value': 'Sample ID'}},
         'domain_of': ['Sample']} })
    developmentStage: Optional[str] = Field(default=None, description="""Stage in the life of a plant structure during which the sample was taken, preferably as a Plant Ontology or BBCH accession.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Plant Ontology term or BBCH scale '
                                                    'term'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Plant structure development '
                                                   'stage'}},
         'domain_of': ['Sample']} })
    anatomicalEntity: str = Field(default=..., description="""Plant part or product from which the sample was taken, preferably as a Plant Ontology accession.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Plant Ontology term'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Plant anatomical entity'}},
         'domain_of': ['Sample']} })
    sampleDesc: Optional[str] = Field(default=None, description="""Information not captured by other sample fields, including quantification, sample treatments, and processing.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Sample description'}},
         'domain_of': ['Sample']} })
    collectionDate: str = Field(default=..., description="""Date and time when the sample was collected or harvested.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Date/Time'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Collection date'}},
         'domain_of': ['Sample']} })
    externalId: Optional[list[str]] = Field(default=None, description="""Identifier for the sample in a persistent repository, comprising the repository name and sample accession number.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Sample external ID'}},
         'domain_of': ['ObservationUnit', 'Sample']} })


class ObservedVariable(ConfiguredBaseModel):
    """
    Description of how a measurement has been made, usually a trait associated with a method and a unit or scale of measurement.

    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    variableId: str = Field(default=..., description="""Code used to identify the variable in the data file. It must be unique within a given investigation.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Unique identifier'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Variable ID'}},
         'domain_of': ['ObservedVariable']} })
    variableName: Optional[str] = Field(default=None, description="""Name of the variable.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Variable name'}},
         'domain_of': ['ObservedVariable']} })
    variableAccNumber: Optional[str] = Field(default=None, description="""Accession number of the variable in the Crop Ontology.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Crop Ontology term'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Variable accession number'}},
         'domain_of': ['ObservedVariable']} })
    traitName: str = Field(default=..., description="""Name of the plant or environmental trait under observation.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label', 'value': 'Trait'}},
         'domain_of': ['ObservedVariable']} })
    traitEntity: Optional[str] = Field(default=None, description="""Entity on which the trait has been measured.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Trait Entity'}},
         'domain_of': ['ObservedVariable']} })
    traitEntityAccessionNumber: Optional[str] = Field(default=None, description="""Accession number of the trait entity in a suitable controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Ontology term'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Trait Entity Accession number'}},
         'domain_of': ['ObservedVariable']} })
    traitCharacteristic: Optional[str] = Field(default=None, description="""Characteristic measured, such as size, volume, surface, or sugar concentration.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Trait Characteristic'}},
         'domain_of': ['ObservedVariable']} })
    traitCharacteristicAccessionNumber: Optional[str] = Field(default=None, description="""Accession number of the trait characteristic in a suitable controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Ontology term'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Trait Characteristic Accession '
                                                   'number'}},
         'domain_of': ['ObservedVariable']} })
    traitAccNumber: Optional[str] = Field(default=None, description="""Accession number of the trait in a suitable controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Ontology term'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Trait accession number'}},
         'domain_of': ['ObservedVariable']} })
    methodName: str = Field(default=..., description="""Name of the method of observation.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label', 'value': 'Method'}},
         'domain_of': ['ObservedVariable']} })
    methodAccNumber: Optional[str] = Field(default=None, description="""Accession number of the method in a suitable controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Ontology term'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Method accession number'}},
         'domain_of': ['ObservedVariable']} })
    methodDesc: Optional[str] = Field(default=None, description="""Textual description of the method, which may extend an externally defined method with specific parameters.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Method description'}},
         'domain_of': ['ObservedVariable']} })
    methodRef: Optional[str] = Field(default=None, description="""URI or DOI of a reference describing the method.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'URI or DOI'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Reference associated to the '
                                                   'method'}},
         'domain_of': ['ObservedVariable']} })
    scaleName: str = Field(default=..., description="""Name of the scale associated with the variable.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Unique identifier'},
                         'miappe_label': {'tag': 'miappe_label', 'value': 'Scale'}},
         'domain_of': ['ObservedVariable']} })
    scaleAccNumber: Optional[str] = Field(default=None, description="""Accession number of the scale in a suitable controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0-1'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Crop Ontology term'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Scale accession number'}},
         'domain_of': ['ObservedVariable']} })
    timeScale: Optional[list[str]] = Field(default=None, description="""Scale or unit of time with which observations of this type were recorded in the data file, for time series studies.
""", json_schema_extra = { "linkml_meta": {'annotations': {'miappe_cardinality': {'tag': 'miappe_cardinality',
                                                'value': '0+'},
                         'miappe_format': {'tag': 'miappe_format',
                                           'value': 'Free text'},
                         'miappe_label': {'tag': 'miappe_label',
                                          'value': 'Time scale'}},
         'domain_of': ['ObservedVariable']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
MIAPPESubmission.model_rebuild()
Investigation.model_rebuild()
Study.model_rebuild()
Person.model_rebuild()
DataFile.model_rebuild()
BiologicalMaterial.model_rebuild()
Environment.model_rebuild()
EnvironmentParameter.model_rebuild()
ExperimentalFactor.model_rebuild()
Event.model_rebuild()
ObservationUnit.model_rebuild()
Sample.model_rebuild()
ObservedVariable.model_rebuild()
