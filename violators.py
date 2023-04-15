import streamlit as st

import altair as alt
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from ECHO_modules.utilities import get_active_facilities, \
    get_top_violators, chart_top_violators
class Violators():
    def demand_supply_cruve(self , data=None):
        """Graph demand and supply curve
        inputs
        --------------------------------
        Data is a {price:[] , 'Demand':[1,2,3....] , 'Supply':[1,2,3,....] } per unit

        """
        data =  data if data != None else {'price':list(range(0,201,10)) ,'Demand':list(range(0,401,20))[::-1] , 'Supply':list(range(0,401,20))}
        fig, ax = plt.subplots() #solved by add this line
        ax = sns.lineplot(data=pd.DataFrame(data), x="Demand", y="price")
        return fig

    def show_top_violators(self, program, region_type, state, region):
        if region_type == 'County':
            regions_selected = (region,)
            df_active = get_active_facilities(state, 'County', regions_selected)
            if df_active is None:
                st.write('This region has no active facilities.')
            else:
                if program == 'CAA':
                    df_violators = get_top_violators(df_active, 'AIR_FLAG',
                                                     'CAA_3YR_COMPL_QTRS_HISTORY', 'CAA_FORMAL_ACTION_COUNT', 20)
                    if df_violators.shape[0] == 0:
                        st.write('There are no violators found for this region.')
                    else:
                        self.__chart_violators(df_violators, state, regions_selected, 'CAA')

                if program == 'CWA':
                    df_violators = get_top_violators(df_active, 'NPDES_FLAG',
                                                     'CWA_13QTRS_COMPL_HISTORY', 'CWA_FORMAL_ACTION_COUNT', 20)
                    if df_violators.shape[0] == 0:
                        st.write('There are no violators found for this region.')
                    else:
                        if df_violators.shape[0] == 0:
                            st.write('There are no violators found for this region.')
                        else:
                            self.__chart_violators(df_violators, state, regions_selected, 'CAA')

                if program == 'RCRA':
                    df_violators = get_top_violators(df_active, 'RCRA_FLAG',
                                                     'RCRA_3YR_COMPL_QTRS_HISTORY', 'RCRA_FORMAL_ACTION_COUNT', 20)
                    if df_violators.shape[0] == 0:
                        st.write('There are no violators found for this region.')
                    else:
                        if df_violators.shape[0] == 0:
                            st.write('There are no violators found for this region.')
                        else:
                            self.__chart_violators(df_violators, state, regions_selected, 'CAA')
    def __chart_violators(self, data, state, regions, program):
        # Convert wide-form data to long-form
        # See: https://altair-viz.github.io/user_guide/data.html#long-form-vs-wide-form-data
        # chart_data = pd.melt(data.reset_index(), id_vars=["REGISTRY_ID"])

        # Horizontal stacked bar chart
        chart = (
            alt.Chart(data)
            .mark_bar()
            .encode(
                y="FAC_NAME",
                x="noncomp_count"
            )
        )

        st.altair_chart(chart, use_container_width=True)