"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.6
"""

import pandas as pd


def _is_true(x: pd.Series) -> pd.Series:
    return x == "t"


def _parse_percentage(x: pd.Series) -> pd.Series:
    return x.str.replace("%", "").astype(float)


def _parse_money(x: pd.Series) -> pd.Series:
    return x.str.replace("$", "").str.replace(",", "").astype(float)


def preprocess_companies(df: pd.DataFrame) -> pd.DataFrame:
    comp_df = df.assign(
        iata_approved=lambda df_: _is_true(df_.iata_approved),
        company_rating=lambda df_: _parse_percentage(df_.company_rating),
    )
    return comp_df


def preprocess_shuttles(df: pd.DataFrame) -> pd.DataFrame:
    shuttles_df = df.assign(
        d_check_complete=lambda df_: _is_true(df_.d_check_complete),
        moon_clearance_complete=lambda df_: _is_true(df_.moon_clearance_complete),
        price=lambda df_: _parse_money(df_.price),
    )

    return shuttles_df
