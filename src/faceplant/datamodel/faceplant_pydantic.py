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
version = "0.2.0"


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


linkml_meta = LinkMLMeta({'default_prefix': 'faceplant',
     'default_range': 'string',
     'description': 'A LinkML data model for data recorded by the APPL automated '
                    'plant phenotyping platform: fluorescence, thermal, moisture, '
                    'RGB, 3D, and hyperspectral camera readings, plus '
                    'watering-scale and spray-treatment logs, organized as '
                    'Experiment > Tray > Plant > PhenotypingImagingRound.',
     'id': 'https://w3id.org/your-org/faceplant',
     'imports': ['linkml:types'],
     'license': 'https://creativecommons.org/licenses/by/4.0/',
     'name': 'faceplant',
     'prefixes': {'faceplant': {'prefix_prefix': 'faceplant',
                                'prefix_reference': 'https://github.com/Firstnamehannah/FacePlant-'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': 'src/faceplant/schema/faceplant.yaml',
     'title': 'FacePlant: an APPL automated plant phenotyping data model'} )

class FluorescencePhase(str, Enum):
    """
    Which part of the light/dark induction protocol a reading came from.
    """
    L1 = "L1"
    """
    Light step 1
    """
    L2 = "L2"
    """
    Light step 2
    """
    L3 = "L3"
    """
    Light step 3
    """
    L4 = "L4"
    """
    Light step 4
    """
    Lss = "Lss"
    """
    Light steady-state
    """
    D1 = "D1"
    """
    Dark recovery step 1
    """
    D2 = "D2"
    """
    Dark recovery step 2
    """
    D3 = "D3"
    """
    Dark recovery step 3
    """
    Dss = "Dss"
    """
    Dark steady-state
    """



class FacePlantSubmission(ConfiguredBaseModel):
    """
    Root container for one or more APPL phenotyping experiments.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant', 'tree_root': True})

    experiments: Optional[list[Experiment]] = Field(default=None, description="""Experiments in this submission.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FacePlantSubmission']} })


class Experiment(ConfiguredBaseModel):
    """
    A single automated phenotyping study/trial run on the APPL platform.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant',
         'slot_usage': {'experimentId': {'identifier': True,
                                         'name': 'experimentId',
                                         'required': True},
                        'trays': {'name': 'trays', 'required': True}}})

    experimentId: str = Field(default=..., description="""Unique identifier for the experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    studyName: Optional[str] = Field(default=None, description="""Name/type of the study, e.g. 'GWAS'.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })
    trays: list[Tray] = Field(default=..., description="""Trays belonging to an experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Experiment']} })


class Tray(ConfiguredBaseModel):
    """
    A physical tray/carrier holding one or more plants.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant',
         'slot_usage': {'plants': {'name': 'plants', 'required': True},
                        'trayId': {'identifier': True,
                                   'name': 'trayId',
                                   'required': True}}})

    trayId: str = Field(default=..., description="""Unique identifier for the tray.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Tray']} })
    trayInfo: Optional[str] = Field(default=None, description="""Block/grouping code for the tray.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Tray']} })
    plants: list[Plant] = Field(default=..., description="""Plants held in a tray.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Tray']} })


class Plant(ConfiguredBaseModel):
    """
    A single plant tracked through the experiment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant',
         'slot_usage': {'plantId': {'identifier': True,
                                    'name': 'plantId',
                                    'required': True}}})

    plantId: str = Field(default=..., description="""Unique plant identifier (e.g. composite of sow date, project code, and replicate number).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Plant']} })
    genotype: Optional[str] = Field(default=None, description="""Accession/clone/genotype code for the plant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Plant']} })
    position: Optional[str] = Field(default=None, description="""Position label within the tray/imaging cassette.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Plant']} })
    imagingRounds: Optional[list[PhenotypingImagingRound]] = Field(default=None, description="""APPL automated phenotyping snapshots recorded for this plant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Plant']} })


class PhenotypingImagingRound(ConfiguredBaseModel):
    """
    One full automated phenotyping snapshot of a single plant on a given date, across every connected sensor. Corresponds to one row of the APPL platform's raw export.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant',
         'slot_usage': {'roundDate': {'name': 'roundDate', 'required': True}}})

    roundDate: date = Field(default=..., description="""Date of this imaging round.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypingImagingRound']} })
    roundTime: Optional[datetime ] = Field(default=None, description="""Timestamp of this imaging round.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypingImagingRound']} })
    roundOrder: Optional[int] = Field(default=None, description="""Sequence number of this round within the experiment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypingImagingRound']} })
    imagingAngle: Optional[float] = Field(default=None, description="""Camera/turntable angle for this shot.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypingImagingRound']} })
    fluorescenceFc1: Optional[FluorescenceProtocol] = Field(default=None, description="""Full induction-kinetics fluorescence reading from the primary fluorescence camera (e.g. APPL's FC1).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypingImagingRound']} })
    fluorescenceFc2: Optional[FluorescenceSnapshot] = Field(default=None, description="""Basic-snapshot fluorescence reading from a second fluorescence camera/angle (e.g. APPL's FC2).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypingImagingRound']} })
    thermal: Optional[ThermalMeasurement] = Field(default=None, description="""Infrared/thermal camera readings for this imaging round.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypingImagingRound']} })
    moisture: Optional[MoistureMeasurement] = Field(default=None, description="""Moisture-sensing camera readings for this imaging round.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypingImagingRound']} })
    rgbReadings: Optional[list[RgbMeasurement]] = Field(default=None, description="""Visible-light camera readings for this imaging round (one per camera/angle).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypingImagingRound']} })
    structure3d: Optional[StructureMeasurement] = Field(default=None, description="""3D/stereo scanner readings for this imaging round.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypingImagingRound']} })
    swir: Optional[SwirMeasurement] = Field(default=None, description="""Short-wave infrared hyperspectral camera readings for this imaging round.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypingImagingRound']} })
    vnir: Optional[VnirMeasurement] = Field(default=None, description="""Visible + near-infrared hyperspectral camera readings for this imaging round.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypingImagingRound']} })
    scaleReadings: Optional[list[ScaleReading]] = Field(default=None, description="""Watering-station scale readings taken during this imaging round.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypingImagingRound']} })
    sprayEvent: Optional[SprayEvent] = Field(default=None, description="""Foliar treatment/spray applied during this imaging round, if any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhenotypingImagingRound']} })


class PixelStatistic(ConfiguredBaseModel):
    """
    A single derived measurement summarized across every pixel of the segmented plant in one image (an average plus distribution stats).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    statAvg: Optional[float] = Field(default=None, description="""Average value across all pixels of the segmented plant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PixelStatistic']} })
    statStddev: Optional[float] = Field(default=None, description="""Standard deviation across all pixels of the segmented plant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PixelStatistic']} })
    statMedian: Optional[float] = Field(default=None, description="""Median value across all pixels of the segmented plant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PixelStatistic']} })
    statMin: Optional[float] = Field(default=None, description="""Minimum value across all pixels of the segmented plant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PixelStatistic']} })
    statMax: Optional[float] = Field(default=None, description="""Maximum value across all pixels of the segmented plant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PixelStatistic']} })


class ColorBin(ConfiguredBaseModel):
    """
    One of the predefined color clusters an RGB camera sorts plant pixels into, used as a leaf-color / senescence proxy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    colorBinReference: Optional[str] = Field(default=None, description="""Reference color for this bin, e.g. '90,98,58'.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ColorBin']} })
    colorBinValue: Optional[float] = Field(default=None, description="""Pixel count or proportion of the plant in this color bin.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ColorBin']} })


class FluorescenceKineticsStep(ConfiguredBaseModel):
    """
    One timepoint in a light/dark chlorophyll-fluorescence induction protocol (e.g. light steps L1-L4/steady-state, dark recovery steps D1-D3/steady-state).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant',
         'slot_usage': {'fluorescencePhase': {'name': 'fluorescencePhase',
                                              'required': True}}})

    fluorescencePhase: FluorescencePhase = Field(default=..., description="""Which step of the induction protocol this reading is from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceKineticsStep']} })
    ft: Optional[float] = Field(default=None, description="""Instantaneous fluorescence at this step.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceKineticsStep']} })
    fm: Optional[float] = Field(default=None, description="""Maximum fluorescence at this step.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceKineticsStep']} })
    fo: Optional[float] = Field(default=None, description="""Minimum fluorescence at this step.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceKineticsStep']} })
    fv: Optional[float] = Field(default=None, description="""Variable fluorescence (Fm - Fo) at this step.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceKineticsStep']} })
    fq: Optional[float] = Field(default=None, description="""Fluorescence quenched by light at this step.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceKineticsStep']} })
    fvOverFm: Optional[float] = Field(default=None, description="""Quantum yield of PSII at this step.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceKineticsStep']} })
    qy: Optional[float] = Field(default=None, description="""Operating quantum yield at this step.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceKineticsStep']} })
    npq: Optional[float] = Field(default=None, description="""Non-photochemical quenching at this step.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceKineticsStep']} })
    qN: Optional[float] = Field(default=None, description="""Non-photochemical quenching coefficient at this step.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceKineticsStep']} })
    qP: Optional[float] = Field(default=None, description="""Photochemical quenching coefficient at this step.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceKineticsStep']} })
    qL: Optional[float] = Field(default=None, description="""Lake-model photochemical quenching coefficient at this step.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceKineticsStep']} })
    rfd: Optional[float] = Field(default=None, description="""Fluorescence decrease ratio (vitality index) at this step.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceKineticsStep']} })


class FluorescenceSnapshot(ConfiguredBaseModel):
    """
    Basic single-shot chlorophyll-fluorescence reading.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    fluorescenceCameraId: Optional[str] = Field(default=None, description="""Identifier of the fluorescence camera unit, e.g. 'FC1', 'FC2'.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceSnapshot']} })
    fluorescenceSize: Optional[float] = Field(default=None, description="""Segmented plant size as measured by the fluorescence camera.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceSnapshot']} })
    foBase: Optional[float] = Field(default=None, description="""Minimum fluorescence (dark-adapted).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceSnapshot']} })
    fmBase: Optional[float] = Field(default=None, description="""Maximum fluorescence (dark-adapted).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceSnapshot']} })
    fvBase: Optional[float] = Field(default=None, description="""Variable fluorescence (dark-adapted).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceSnapshot']} })
    qyMax: Optional[float] = Field(default=None, description="""Fv/Fm - dark-adapted maximum quantum yield of PSII, the most commonly used fluorescence metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceSnapshot']} })


class FluorescenceProtocol(FluorescenceSnapshot):
    """
    Full light/dark induction-kinetics fluorescence reading: a base snapshot plus a series of kinetics steps (what the primary fluorescence camera, e.g. APPL's FC1, reports).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    fp: Optional[float] = Field(default=None, description="""Peak fluorescence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceProtocol']} })
    ftLss: Optional[float] = Field(default=None, description="""Instantaneous fluorescence at light steady-state.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceProtocol']} })
    rfdLss: Optional[float] = Field(default=None, description="""Vitality/fluorescence-decrease index at light steady-state.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceProtocol']} })
    kineticsSteps: Optional[list[FluorescenceKineticsStep]] = Field(default=None, description="""The full sequence of light/dark induction-kinetics steps for one fluorescence reading.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceProtocol']} })
    fluorescenceCameraId: Optional[str] = Field(default=None, description="""Identifier of the fluorescence camera unit, e.g. 'FC1', 'FC2'.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceSnapshot']} })
    fluorescenceSize: Optional[float] = Field(default=None, description="""Segmented plant size as measured by the fluorescence camera.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceSnapshot']} })
    foBase: Optional[float] = Field(default=None, description="""Minimum fluorescence (dark-adapted).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceSnapshot']} })
    fmBase: Optional[float] = Field(default=None, description="""Maximum fluorescence (dark-adapted).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceSnapshot']} })
    fvBase: Optional[float] = Field(default=None, description="""Variable fluorescence (dark-adapted).""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceSnapshot']} })
    qyMax: Optional[float] = Field(default=None, description="""Fv/Fm - dark-adapted maximum quantum yield of PSII, the most commonly used fluorescence metric.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluorescenceSnapshot']} })


class ThermalMeasurement(ConfiguredBaseModel):
    """
    Infrared/thermal camera output for one imaging round.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    thermalTemp: Optional[PixelStatistic] = Field(default=None, description="""Primary temperature channel, summarized across the plant's pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThermalMeasurement']} })
    thermalTemp2: Optional[PixelStatistic] = Field(default=None, description="""Secondary temperature channel, summarized across the plant's pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThermalMeasurement']} })
    thermalSize: Optional[PixelStatistic] = Field(default=None, description="""Segmented plant size as measured by the thermal camera.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThermalMeasurement']} })


class MoistureMeasurement(ConfiguredBaseModel):
    """
    Moisture-sensing camera output, based on reflectance at known water-absorption wavelengths (940nm, 1450nm).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    waterContent: Optional[PixelStatistic] = Field(default=None, description="""Derived water-content index, summarized across the plant's pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MoistureMeasurement']} })
    band940nm: Optional[PixelStatistic] = Field(default=None, description="""Reflectance at 940nm (a water-absorption band), summarized across the plant's pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MoistureMeasurement']} })
    band1450nm: Optional[PixelStatistic] = Field(default=None, description="""Reflectance at 1450nm (a water-absorption band), summarized across the plant's pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MoistureMeasurement']} })


class SwirMeasurement(ConfiguredBaseModel):
    """
    Short-wave infrared hyperspectral camera output.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    swirSize: Optional[PixelStatistic] = Field(default=None, description="""Segmented plant size as measured by the SWIR camera.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SwirMeasurement']} })
    swirWater1: Optional[PixelStatistic] = Field(default=None, description="""SWIR-derived water index, summarized across the plant's pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SwirMeasurement']} })


class VnirMeasurement(ConfiguredBaseModel):
    """
    Visible + near-infrared hyperspectral camera output, reduced from the full spectrum to a set of pre-computed vegetation indices.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    vnirSize: Optional[PixelStatistic] = Field(default=None, description="""Segmented plant size as measured by the VNIR camera.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VnirMeasurement']} })
    ndvi: Optional[PixelStatistic] = Field(default=None, description="""Normalized Difference Vegetation Index (greenness/biomass), summarized across the plant's pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VnirMeasurement']} })
    ndvi2: Optional[PixelStatistic] = Field(default=None, description="""Alternate NDVI formulation, summarized across the plant's pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VnirMeasurement']} })
    pri: Optional[PixelStatistic] = Field(default=None, description="""Photochemical Reflectance Index - tracks xanthophyll-pigment changes, an early/fast indicator of light stress. Summarized across the plant's pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VnirMeasurement']} })
    psri: Optional[PixelStatistic] = Field(default=None, description="""Plant Senescence Reflectance Index, summarized across the plant's pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VnirMeasurement']} })
    sipi: Optional[PixelStatistic] = Field(default=None, description="""Structure-Insensitive Pigment Index (carotenoid:chlorophyll ratio), summarized across the plant's pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VnirMeasurement']} })
    osavi: Optional[PixelStatistic] = Field(default=None, description="""Optimized Soil-Adjusted Vegetation Index, summarized across the plant's pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VnirMeasurement']} })
    mcari1: Optional[PixelStatistic] = Field(default=None, description="""Modified Chlorophyll Absorption Ratio Index, summarized across the plant's pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VnirMeasurement']} })


class RgbMorphology(ConfiguredBaseModel):
    """
    Shape/size metrics from a visible-light camera.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    areaPx: Optional[float] = Field(default=None, description="""Segmented plant area, in pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMorphology']} })
    areaMm: Optional[float] = Field(default=None, description="""Segmented plant area, in square millimetres.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMorphology']} })
    perimeterPx: Optional[float] = Field(default=None, description="""Segmented plant perimeter, in pixels.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMorphology']} })
    perimeterMm: Optional[float] = Field(default=None, description="""Segmented plant perimeter, in millimetres.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMorphology']} })
    rgbCompactness: Optional[float] = Field(default=None, description="""Shape compactness of the segmented plant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMorphology']} })
    widthMm: Optional[float] = Field(default=None, description="""Segmented plant width, in millimetres.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMorphology']} })
    heightMm: Optional[float] = Field(default=None, description="""Segmented plant height, in millimetres.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMorphology']} })
    roundness: Optional[float] = Field(default=None, description="""Roundness of the segmented plant shape.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMorphology']} })
    roundness2: Optional[float] = Field(default=None, description="""Alternate roundness formulation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMorphology']} })
    isotropy: Optional[float] = Field(default=None, description="""Isotropy of the segmented plant shape.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMorphology']} })
    eccentricity: Optional[float] = Field(default=None, description="""Eccentricity of the segmented plant shape.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMorphology']} })
    rms: Optional[float] = Field(default=None, description="""Root-mean-square shape descriptor.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMorphology']} })
    solidity: Optional[float] = Field(default=None, description="""Solidity (area / convex-hull area) of the segmented plant shape.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMorphology']} })


class RgbMeasurement(ConfiguredBaseModel):
    """
    One RGB camera's full output (a given view/angle).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    rgbCameraId: Optional[str] = Field(default=None, description="""Identifier of the RGB camera unit/angle, e.g. 'RGB1', 'RGB2'.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMeasurement']} })
    morphology: Optional[RgbMorphology] = Field(default=None, description="""Shape/size metrics for one RGB reading.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMeasurement']} })
    colorBins: Optional[list[ColorBin]] = Field(default=None, description="""The color histogram for one RGB reading.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RgbMeasurement']} })


class StructureMeasurement(ConfiguredBaseModel):
    """
    3D/stereo scanner output describing plant architecture.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    structureArea: Optional[float] = Field(default=None, description="""Total leaf area from the 3D scanner.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StructureMeasurement']} })
    projectedArea: Optional[float] = Field(default=None, description="""Projected (canopy-view) area from the 3D scanner.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StructureMeasurement']} })
    leafInclination: Optional[float] = Field(default=None, description="""Average leaf inclination angle.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StructureMeasurement']} })
    leafAreaIndex: Optional[float] = Field(default=None, description="""Leaf area index (leaf area per unit ground area).""", json_schema_extra = { "linkml_meta": {'domain_of': ['StructureMeasurement']} })
    structureCompactness: Optional[float] = Field(default=None, description="""Compactness of the 3D plant structure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StructureMeasurement']} })
    plantHeight: Optional[float] = Field(default=None, description="""Plant height, in millimetres.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StructureMeasurement']} })
    digitalBiomass: Optional[float] = Field(default=None, description="""Volumetric biomass proxy derived from the 3D scan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StructureMeasurement']} })
    stemHeight: Optional[float] = Field(default=None, description="""Stem height, in millimetres.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StructureMeasurement']} })
    stemLength: Optional[float] = Field(default=None, description="""Stem length, in millimetres.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StructureMeasurement']} })
    branchesCount: Optional[int] = Field(default=None, description="""Number of branches detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StructureMeasurement']} })


class ScaleReading(ConfiguredBaseModel):
    """
    One load-cell weight reading from an automated watering station.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    scaleId: Optional[str] = Field(default=None, description="""Identifier of the scale/watering-station unit, e.g. 'SC1', 'SC2', 'SC3'.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ScaleReading']} })
    weight: Optional[float] = Field(default=None, description="""Plant/pot weight before watering, in grams.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ScaleReading']} })
    weightAfterWatering: Optional[float] = Field(default=None, description="""Plant/pot weight after watering, in grams.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ScaleReading']} })


class SprayEvent(ConfiguredBaseModel):
    """
    A foliar treatment/spray applied during an imaging round.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/your-org/faceplant'})

    sprayTime: Optional[datetime ] = Field(default=None, description="""Date/time the spray was applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SprayEvent']} })
    sprayLiquid: Optional[str] = Field(default=None, description="""Name/type of the sprayed substance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SprayEvent']} })
    sprayLiquidAmount: Optional[float] = Field(default=None, description="""Amount of liquid sprayed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SprayEvent']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
FacePlantSubmission.model_rebuild()
Experiment.model_rebuild()
Tray.model_rebuild()
Plant.model_rebuild()
PhenotypingImagingRound.model_rebuild()
PixelStatistic.model_rebuild()
ColorBin.model_rebuild()
FluorescenceKineticsStep.model_rebuild()
FluorescenceSnapshot.model_rebuild()
FluorescenceProtocol.model_rebuild()
ThermalMeasurement.model_rebuild()
MoistureMeasurement.model_rebuild()
SwirMeasurement.model_rebuild()
VnirMeasurement.model_rebuild()
RgbMorphology.model_rebuild()
RgbMeasurement.model_rebuild()
StructureMeasurement.model_rebuild()
ScaleReading.model_rebuild()
SprayEvent.model_rebuild()
