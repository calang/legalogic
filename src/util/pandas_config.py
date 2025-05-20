#!/usr/bin/env python

"""
Utility functions for configuring pandas display options.
"""
import pandas as pd

def configure_pandas_display() -> None:
    """
    Configure pandas to display DataFrames with increased width and length limits.
    
    Sets the following display options:
    - max_colwidth: 100 characters
    - display.width: 300 characters
    - display.max_rows: 100 rows
    - display.max_columns: 100 columns
    """
    pd.set_option('max_colwidth', 100)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_rows', 100)
    pd.set_option('display.max_columns', 100)
