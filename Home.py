"""

"""


import streamlit as st
from matplotlib import pyplot as plt
from pandas import read_csv, concat

BOXPLOT_SIZE = (8,2)


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

st.markdown("# BMW Cloud Dashboard")
st.markdown("Willkommen im Cloud Dashboard. Bitte verwenden sie die Navigation auf der linken Seite, um zwischen den Seiten dieses Dashboards zu navigieren.")

data = read_csv("data/preprocessed_data.csv")
df = concat([
    data[["sensor_type", "measured_value"]].groupby(["sensor_type"]).min().set_axis(["Min Value"], axis=1),
    data[["sensor_type", "measured_value"]].groupby(["sensor_type"]).mean().set_axis(["Mean Value"], axis=1),
    data[["sensor_type", "measured_value"]].groupby(["sensor_type"]).median().set_axis(["Median Value"], axis=1),
    data[["sensor_type", "measured_value"]].groupby(["sensor_type"]).max().set_axis(["Max Value"], axis=1)
], axis=1)

st.dataframe(df)