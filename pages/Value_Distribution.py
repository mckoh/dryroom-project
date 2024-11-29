"""

"""


import streamlit as st
from matplotlib import pyplot as plt
from pandas import read_csv


# Set page config
st.set_page_config(
    page_title="BMW Dashboard",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Print page header
st.sidebar.markdown("# Sensor Selection")
st.sidebar.markdown("Please use the controls below to select which sensor you are interested in and what locations you would like to display.")

col1, col2 = st.columns(2)

# Data content for sensor display
data = read_csv("data/preprocessed_data.csv")

s_type = data.sensor_type.unique()
s_select = st.sidebar.selectbox("Errection Location", s_type)
_data = data.loc[data["sensor_type"]==s_select]

e_loc = _data["errection_location"].unique()
e_select = st.sidebar.selectbox("Errection Location", e_loc)
__data = _data.loc[_data["errection_location"]==e_select]

i_loc = __data["installation_location"].unique()
i_select = st.sidebar.selectbox("Instalation Location", i_loc)
___data = __data.loc[__data["installation_location"]==i_select]

with col1:

    st.markdown("# Global Situation")

    figure_global, ax_global = plt.subplots()
    ax_global.hist(_data.measured_value, color="k")
    ax_global.set_ylabel("Frequency")
    ax_global.set_xlabel(f"Range of {s_select}")
    ax_global.set_title(f"{s_select} at globally")
    st.pyplot(figure_global)

    figure_box_global, ax_box_global = plt.subplots(figsize=(8,2))
    ax_box_global.boxplot(_data.measured_value, vert=False)
    ax_box_global.set_title(f"Distribution of {s_select} at {e_select}/{i_select}")
    ax_box_global.set_xlabel(f"Range of {s_select}")
    ax_box_global.set_yticks([])
    ax_box_global.set_ylabel(f"{s_select}")
    st.pyplot(figure_box_global)

with col2:

    st.markdown(f"# Situation at {e_select}/{i_select}")

    figure_detail, ax_detail = plt.subplots()
    ax_detail.hist(___data.measured_value, color="orange")
    ax_detail.set_ylabel("Frequency")
    ax_detail.set_xlabel(f"Range of {s_select}")
    ax_detail.set_title(f"{s_select} at globally")
    st.pyplot(figure_detail)

    figure_box_global, ax_box_global = plt.subplots(figsize=(8,2))
    ax_box_global.boxplot(___data.measured_value, vert=False)
    ax_box_global.set_title(f"Distribution of {s_select} globally")
    ax_box_global.set_xlabel(f"Range of {s_select}")
    ax_box_global.set_yticks([])
    ax_box_global.set_ylabel(f"{s_select}")
    st.pyplot(figure_box_global)