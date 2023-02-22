"""Ngspice simulation results to Pandas
"""

from pathlib import Path
import pandas as pd
from .analyses import Analyses


def to_pandas(
    results_loc: Path,
    list_analyses: list[Analyses],
    del_results_file: bool = False,
) -> list[pd.DataFrame]:
    """converts simulation results to list of Pandas dataframes
    Args:
        results_loc (Path):
        list_analyses (list[Analyses]):
        del_results_file (bool, optional): deletes results file after conversion.
                                           defaults to False.
    Returns:
        list[pd.DataFrame]:
    """
    list_df: list[pd.DataFrame] = []
    for analysis in list_analyses:
        results_filename: Path = results_loc / f"{analysis.name}.txt"
        if analysis.cmd_type == "op":
            this_df = pd.read_csv(
                results_filename, header=3, skiprows=[4], delim_whitespace=True
            )
            this_df = this_df.drop("Index", axis=1)
        else:
            this_df: pd.DataFrame = pd.read_csv(results_filename, delim_whitespace=True)
        list_df.append(this_df)

        # Want to delete raw text files after converting to Pandas?
        if del_results_file:
            results_filename.unlink()

    return list_df
