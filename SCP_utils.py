import pandas as pd
import numpy as np
import streamlit as st
from ECHO_modules.geographies import region_field, states


def fix_county_names( in_counties ):
    '''
    ECHO_EXPORTER has counties listed both as ALAMEDA and ALAMEDA COUNTY, seemingly
    for every county.  We drop the 'COUNTY' so they only get listed once.

    Parameters
    ----------
    in_counties : list of county names (str)

    Returns
    -------
    list
        The list of counties without duplicates
    '''

    counties = []
    for county in in_counties:
        if (county.endswith( ' COUNTY' )):
            county = county[:-7]
        counties.append( county.strip() )
    counties = np.unique( counties )
    return counties


def show_program_widget():
    '''
    Create and return a dropdown list of types of regions

    Parameters
    ----------
   
    Returns
    -------
    widget
        The dropdown widget with the list of regions
    '''

    programs = ['CAA', 'CWA', 'RCRA']

    return st.sidebar.selectbox(
        'Choose the program:',
        programs
    )

def show_region_type_widget( region_types=None, default_value='County' ):
    '''
    Create and return a dropdown list of types of regions

    Parameters
    ----------
    region_types : list of region types to show (str)
   
    Returns
    -------
    widget
        The dropdown widget with the list of regions
    '''

    if ( region_types == None ):
        region_types = region_field.keys()

    return st.sidebar.selectbox(
        'Choose the type of region:',
        region_types
    )

def show_state_widget():
    '''
    Create and return a dropdown list of types of states

    Returns
    -------
    widget
        The dropdown widget with the list of states
    '''

    return st.sidebar.selectbox(
        'Choose a state:',
        states
    )

def show_county_widget( state ):
    '''
    Create and return a dropdown list of counties in the state

    Parameters
    ----------
    state : the previously chosen state
   
    Returns
    -------
    widget
        The dropdown widget with the list of regions
    '''

    url = "https://raw.githubusercontent.com/edgi-govdata-archiving/"
    url += "ECHO_modules/packaging/data/state_counties.csv"
    df = pd.read_csv( url )
    counties = df[df['FAC_STATE'] == state]['FAC_COUNTY']
    counties = fix_county_names(counties)

    return st.sidebar.selectbox(
        'Choose a county:',
        counties
    )

def show_zip_widget():
    return st.sidebar.text_input('Enter a zip code:', value="")

def show_watershed_widget():
    return st.sidebar.text_input('Enter a zip code:', value="")