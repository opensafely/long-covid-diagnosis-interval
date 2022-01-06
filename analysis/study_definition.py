from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA
from codelists import *

start_date = "2019-12-01"
end_date = "2021-11-30"

study = StudyDefinition(
    default_expectations={
        "date": {"earliest": start_date, "latest": end_date},
        "rate": "uniform",
        "incidence": 0.5,
    },
    index_date="2019-12-01",
    population=patients.satisfying(
        "has_covid AND has_long_covid",
        has_covid=patients.with_these_clinical_events(covid_codes, between=[start_date, end_date],),
        has_long_covid=patients.with_these_clinical_events(long_covid_codes, between=[start_date, end_date],),
    ),

    covid_date=patients.with_these_clinical_events(
        covid_codes,
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
        return_expectations={"rate": "uniform", "incidence": 1.0, "date": {"earliest": start_date, "latest": end_date}},
    ),

    long_covid_date=patients.with_these_clinical_events(
        long_covid_codes,
        between=["covid_date", end_date],
        returning="date",
        date_format="YYYY-MM-DD",
        find_first_match_in_period=True,
        return_expectations={"rate": "uniform", "incidence": 1.0, "date": {"earliest": start_date, "latest": end_date}},
    ),

    age=patients.age_as_of(
        "covid_date", 
        return_expectations={"rate" : "universal", "int" : {"distribution" : "population_ages"}},
    ),

    sex=patients.sex(
        return_expectations={"rate": "universal", "category": {"ratios": {"M": 0.5, "F": 0.5}}},
    ),
)