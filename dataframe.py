"""
This module downloads the latest National, State, and Puerto Rico Commonwealth
population totals dataset from www.census.gov and loads the data into a dataframe.
The module also provides a testing function to ensure that the download
operated correctly.
"""

import pandas as pd


def read_in_us_population(csv_location):
    """Function that reads in the us_population csv file from
    www.census.gov and checks that the import was successful by
    checking that all column names are present in the returned
    dataframe.

    Args:
        :param csv_location (str): Location of downloaded csv file on computer

    Returns:
        :return data_frame (pd.DataFrame): Validated pandas DataFrame of csv file.


    """

    data_frame = pd.read_csv(csv_location)

    expected_col_names = ['SUMLEV',
                          'REGION',
                          'DIVISION',
                          'STATE',
                          'NAME',
                          'CENSUS2010POP',
                          'ESTIMATESBASE2010',
                          'POPESTIMATE2010',
                          'POPESTIMATE2011',
                          'POPESTIMATE2012',
                          'POPESTIMATE2013',
                          'POPESTIMATE2014',
                          'POPESTIMATE2015',
                          'POPESTIMATE2016',
                          'POPESTIMATE2017',
                          'POPESTIMATE2018',
                          'NPOPCHG_2010',
                          'NPOPCHG_2011',
                          'NPOPCHG_2012',
                          'NPOPCHG_2013',
                          'NPOPCHG_2014',
                          'NPOPCHG_2015',
                          'NPOPCHG_2016',
                          'NPOPCHG_2017',
                          'NPOPCHG_2018',
                          'BIRTHS2010',
                          'BIRTHS2011',
                          'BIRTHS2012',
                          'BIRTHS2013',
                          'BIRTHS2014',
                          'BIRTHS2015',
                          'BIRTHS2016',
                          'BIRTHS2017',
                          'BIRTHS2018',
                          'DEATHS2010',
                          'DEATHS2011',
                          'DEATHS2012',
                          'DEATHS2013',
                          'DEATHS2014',
                          'DEATHS2015',
                          'DEATHS2016',
                          'DEATHS2017',
                          'DEATHS2018',
                          'NATURALINC2010',
                          'NATURALINC2011',
                          'NATURALINC2012',
                          'NATURALINC2013',
                          'NATURALINC2014',
                          'NATURALINC2015',
                          'NATURALINC2016',
                          'NATURALINC2017',
                          'NATURALINC2018',
                          'INTERNATIONALMIG2010',
                          'INTERNATIONALMIG2011',
                          'INTERNATIONALMIG2012',
                          'INTERNATIONALMIG2013',
                          'INTERNATIONALMIG2014',
                          'INTERNATIONALMIG2015',
                          'INTERNATIONALMIG2016',
                          'INTERNATIONALMIG2017',
                          'INTERNATIONALMIG2018',
                          'DOMESTICMIG2010',
                          'DOMESTICMIG2011',
                          'DOMESTICMIG2012',
                          'DOMESTICMIG2013',
                          'DOMESTICMIG2014',
                          'DOMESTICMIG2015',
                          'DOMESTICMIG2016',
                          'DOMESTICMIG2017',
                          'DOMESTICMIG2018',
                          'NETMIG2010',
                          'NETMIG2011',
                          'NETMIG2012',
                          'NETMIG2013',
                          'NETMIG2014',
                          'NETMIG2015',
                          'NETMIG2016',
                          'NETMIG2017',
                          'NETMIG2018',
                          'RESIDUAL2010',
                          'RESIDUAL2011',
                          'RESIDUAL2012',
                          'RESIDUAL2013',
                          'RESIDUAL2014',
                          'RESIDUAL2015',
                          'RESIDUAL2016',
                          'RESIDUAL2017',
                          'RESIDUAL2018',
                          'RBIRTH2011',
                          'RBIRTH2012',
                          'RBIRTH2013',
                          'RBIRTH2014',
                          'RBIRTH2015',
                          'RBIRTH2016',
                          'RBIRTH2017',
                          'RBIRTH2018',
                          'RDEATH2011',
                          'RDEATH2012',
                          'RDEATH2013',
                          'RDEATH2014',
                          'RDEATH2015',
                          'RDEATH2016',
                          'RDEATH2017',
                          'RDEATH2018',
                          'RNATURALINC2011',
                          'RNATURALINC2012',
                          'RNATURALINC2013',
                          'RNATURALINC2014',
                          'RNATURALINC2015',
                          'RNATURALINC2016',
                          'RNATURALINC2017',
                          'RNATURALINC2018',
                          'RINTERNATIONALMIG2011',
                          'RINTERNATIONALMIG2012',
                          'RINTERNATIONALMIG2013',
                          'RINTERNATIONALMIG2014',
                          'RINTERNATIONALMIG2015',
                          'RINTERNATIONALMIG2016',
                          'RINTERNATIONALMIG2017',
                          'RINTERNATIONALMIG2018',
                          'RDOMESTICMIG2011',
                          'RDOMESTICMIG2012',
                          'RDOMESTICMIG2013',
                          'RDOMESTICMIG2014',
                          'RDOMESTICMIG2015',
                          'RDOMESTICMIG2016',
                          'RDOMESTICMIG2017',
                          'RDOMESTICMIG2018',
                          'RNETMIG2011',
                          'RNETMIG2012',
                          'RNETMIG2013',
                          'RNETMIG2014',
                          'RNETMIG2015',
                          'RNETMIG2016',
                          'RNETMIG2017',
                          'RNETMIG2018']

    for col in data_frame.columns:
        if col not in expected_col_names:
            raise ValueError("Unexpected column in dataframe: ", col)

    for col in expected_col_names:
        if col not in data_frame.columns:
            raise ValueError("Expected column missing from dataframe: ", col)

    return data_frame
