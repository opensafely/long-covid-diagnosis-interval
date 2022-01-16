from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA
from codelists import *

start_date = "2019-12-01"
end_date = "2022-01-15"

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
        between=[start_date, end_date],
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

    ethnicity=patients.with_these_clinical_events(
        ethnicity_codes,
        returning="category",
        find_last_match_in_period=True,
        on_or_before="index_date",
        return_expectations={"category": {"ratios": {"1": 0.80, "2": 0.05, "3": 0.05, "4": 0.05, "5": 0.05}}, "incidence": 1.0},
    ),

    imd=patients.categorised_as(
        {
            "0": "DEFAULT",
            "1": """index_of_multiple_deprivation >=1 AND index_of_multiple_deprivation < 32844*1/5""",
            "2": """index_of_multiple_deprivation >= 32844*1/5 AND index_of_multiple_deprivation < 32844*2/5""",
            "3": """index_of_multiple_deprivation >= 32844*2/5 AND index_of_multiple_deprivation < 32844*3/5""",
            "4": """index_of_multiple_deprivation >= 32844*3/5 AND index_of_multiple_deprivation < 32844*4/5""",
            "5": """index_of_multiple_deprivation >= 32844*4/5 AND index_of_multiple_deprivation < 32844""",
        },
        index_of_multiple_deprivation=patients.address_as_of(
            "index_date",
            returning="index_of_multiple_deprivation",
            round_to_nearest=100,
        ),
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "0": 0.05,
                    "1": 0.19,
                    "2": 0.19,
                    "3": 0.19,
                    "4": 0.19,
                    "5": 0.19,
                }
            },
        },
    ),

    region=patients.registered_practice_as_of(
        "index_date",
        returning="nuts1_region_name",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "North East": 0.1,
                    "North West": 0.1,
                    "Yorkshire and The Humber": 0.1,
                    "East Midlands": 0.1,
                    "West Midlands": 0.1,
                    "East": 0.1,
                    "London": 0.2,
                    "South East": 0.1,
                    "South West": 0.1,
                },
            },
        },
    ),
)