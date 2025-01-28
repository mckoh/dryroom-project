"""

"""


import streamlit as st
from matplotlib import pyplot as plt
from pandas import read_csv
from scipy.signal import find_peaks


# Set page config
st.set_page_config(
    page_title="BMW Peak Detector",
    page_icon="✴️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Print page header
st.sidebar.markdown("# Sensor Selection")
st.sidebar.markdown("Please use the controls below to select which sensor you are interested in and what locations you would like to display.")

# Data content for sensor display
data = read_csv("data/preprocessed_data.csv")
data.dropna(inplace=True)

######################################

s_type = data.sensor_type.unique()
s_select = st.sidebar.selectbox("Errection Location", s_type)
_data = data.loc[data["sensor_type"]==s_select]

e_loc = _data["errection_location"].unique()
e_select = st.sidebar.selectbox("Errection Location", e_loc)
__data = _data.loc[_data["errection_location"]==e_select]

i_loc = __data["installation_location"].unique()
i_select = st.sidebar.selectbox("Instalation Location", i_loc)
___data = __data.loc[__data["installation_location"]==i_select]

smoothing_select = st.sidebar.slider("Smoothing strength", 1, 1000, 1, 10)
prominance_factor = st.sidebar.slider("Peak prominance", 1, 5, 1, 1)

# Peak detection
x = ___data.measured_value.rolling(smoothing_select).mean().fillna(0).values
minimum = min(x)
maximum = max(x)
peaks, _ = find_peaks(x, prominence=(maximum-minimum)/prominance_factor)


figure_global, ax_global = plt.subplots()
ax_global.plot(x, "-", color="k")
ax_global.plot(peaks, x[peaks], "x", color="red")
ax_global.set_xlabel("time")
ax_global.set_ylabel(f"Value of {s_select}")
ax_global.set_title(f"{s_select} at globally")
st.pyplot(figure_global)
