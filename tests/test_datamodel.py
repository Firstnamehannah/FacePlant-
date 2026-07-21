import pytest
from pydantic import ValidationError
from faceplant.datamodel.faceplant_pydantic import (
    MIAPPESubmission,
    Investigation,
    Study,
    Person,
    BiologicalMaterial,
    ObservationUnit,
    ObservedVariable,
)


# ---------- Person ----------

def test_person_requires_name_role_affiliation():
    with pytest.raises(ValidationError):
        Person()


def test_person_valid_instantiation():
    obj = Person(
        personName="Ada Lovelace",
        personRole=["principal investigator"],
        personAffiliation=["Example University"],
    )
    assert obj.personName == "Ada Lovelace"
    assert obj.personEmail is None
    assert obj.personId is None


def test_person_roundtrip():
    obj = Person(
        personName="Ada Lovelace",
        personRole=["principal investigator"],
        personAffiliation=["Example University"],
        personEmail="ada@example.com",
    )
    data = obj.model_dump()
    obj2 = Person(**data)
    assert obj == obj2


# ---------- BiologicalMaterial ----------

def test_biological_material_requires_id_and_organism():
    with pytest.raises(ValidationError):
        BiologicalMaterial()


def test_biological_material_valid():
    obj = BiologicalMaterial(biologicalMaterialId="BM001", organism="NCBITaxon:4081")
    assert obj.biologicalMaterialId == "BM001"


# ---------- ObservationUnit ----------

def test_observation_unit_requires_id_and_type():
    with pytest.raises(ValidationError):
        ObservationUnit()


def test_observation_unit_valid():
    obj = ObservationUnit(obsUnitId="OU001", obsUnitType="plant")
    assert obj.obsUnitType == "plant"


# ---------- ObservedVariable ----------

def test_observed_variable_requires_core_fields():
    with pytest.raises(ValidationError):
        ObservedVariable()


def test_observed_variable_valid():
    obj = ObservedVariable(
        variableId="VAR001",
        traitName="Plant height",
        methodName="Ruler measurement",
        scaleName="centimeter",
    )
    assert obj.traitName == "Plant height"


# ---------- Study ----------

def test_study_requires_nested_lists_and_core_fields():
    with pytest.raises(ValidationError):
        Study()


def test_study_valid_instantiation():
    study = Study(
        studyTitle="Test study",
        studyStartDate="2024-01-01",
        contactInst="Example Institute",
        locationCountry="US",
        siteName="Test Site",
        expeDesignDesc="Randomized complete block design",
        obsUnitDesc="Individual plants",
        growthFacilityDesc="Greenhouse",
        biologicalMaterials=[
            BiologicalMaterial(biologicalMaterialId="BM001", organism="NCBITaxon:4081")
        ],
        observationUnits=[ObservationUnit(obsUnitId="OU001", obsUnitType="plant")],
        observedVariables=[
            ObservedVariable(
                variableId="VAR001",
                traitName="Plant height",
                methodName="Ruler measurement",
                scaleName="centimeter",
            )
        ],
    )
    assert study.studyTitle == "Test study"


# ---------- Investigation / full submission ----------

def test_investigation_requires_persons_and_studies():
    with pytest.raises(ValidationError):
        Investigation(investigationTitle="Test", miappeVersion="1.2")


def test_full_submission_roundtrip():
    person = Person(
        personName="Ada Lovelace",
        personRole=["principal investigator"],
        personAffiliation=["Example University"],
    )
    study = Study(
        studyTitle="Test study",
        studyStartDate="2024-01-01",
        contactInst="Example Institute",
        locationCountry="US",
        siteName="Test Site",
        expeDesignDesc="Randomized complete block design",
        obsUnitDesc="Individual plants",
        growthFacilityDesc="Greenhouse",
        biologicalMaterials=[
            BiologicalMaterial(biologicalMaterialId="BM001", organism="NCBITaxon:4081")
        ],
        observationUnits=[ObservationUnit(obsUnitId="OU001", obsUnitType="plant")],
        observedVariables=[
            ObservedVariable(
                variableId="VAR001",
                traitName="Plant height",
                methodName="Ruler measurement",
                scaleName="centimeter",
            )
        ],
    )
    investigation = Investigation(
        investigationTitle="Test investigation",
        miappeVersion="1.2",
        persons=[person],
        studies=[study],
    )
    submission = MIAPPESubmission(investigation=investigation)

    data = submission.model_dump()
    submission2 = MIAPPESubmission(**data)
    assert submission == submission2