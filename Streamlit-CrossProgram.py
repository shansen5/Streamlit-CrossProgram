"""
# Cross Program 
Here's our first attempt at using data to create a table:
"""

from violators import Violators
import streamlit as st
import pandas as pd
import numpy as np
import math
from ECHO_modules.get_data import get_echo_data

from SCP_utils import show_region_type_widget, show_state_widget, \
    show_county_widget, show_zip_widget, show_watershed_widget, \
    show_program_widget

st.title('Cross Program Data')

violators = Violators()
st.pyplot(violators.demand_supply_cruve())

"st.session_state object", st.session_state

if "region_type" not in st.session_state:
    st.session_state.region_type = "None"
if "state" not in st.session_state:
    st.session_state.state = "None"
    st.session_state.county = "None"
if "program" not in st.session_state:
    st.session_state.program = "None"


st.session_state.program = show_program_widget()

st.session_state.region_type = show_region_type_widget()
st.write(st.session_state.region_type)

if st.session_state.region_type != "None":
    if st.session_state.region_type == "Zip Code": 
        st.session_state.state = "None"
        st.session_state.zip = show_zip_widget()
    elif st.session_state.region_type == "Watershed":
        st.session_state.state = "None"
        st.session_state.watershed = show_watershed_widget()
    else:
        st.session_state.state = show_state_widget()
        st.write(st.session_state.state)
        if st.session_state.region_type == "County":
            st.session_state.county = show_county_widget(st.session_state.state)
            st.write(st.session_state.county)
            if st.session_state.county != "None":
                violators.show_top_violators(region_type='County',
                                             state=st.session_state.state,
                                             region=st.session_state.county)


# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
st.line_chart(dataframe)

map_data = pd.DataFrame(
    np.random.randn(20, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

x = st.slider('x')  # 👈 this is a widget
str = "The square root of {} is".format(x)
st.write(str, math.sqrt(x))
