import streamlit as st

st.title("IND-320 Project - Reservoir")

st.write(
    """
    Reservoir is an  application developed
    as part of project of the IND320 – Data to Decision course.

    The project explores Norwegian reservoir data using Python, Pandas,
    Matplotlib, Streamlit, and GitHub.
    """
)


st.header("Project Objective")

st.write(
    """
    The purpose of this project is to make reservoir data easier to
    explore and understand through interactive visualisation and filtering.

    The application allows users to inspect the dataset, compare reservoir
    measurements, and explore changes over time.
    """
)


st.header("Tasks")

st.markdown(
    """
    - Import reservoir data from CSV
    - Change Norwegian variables to English labels
    - Show reservoir measurements in tabular form
    - Display first-month data series using Streamlit line-chart columns
    - Select individual reservoir variables using a drop-down menu
    - Filter observations by month range
    - Visualise national reservoir measurements over time
    - Compare multiple reservoir variables using Min-Max normalisation
    - Handle constant variables during normalisation
    - Cache data loading for improved application performance
    """
)


st.header("Dataset")

st.write(
    """
    The application uses the reservoirs.csv dataset provided for the
    IND320 project.

    The dataset contains reservoir observations from different geographical
    areas, including fill level, storage capacity, stored energy,
    previous-week fill level, and changes in fill level.

    The Reservoir Data page displays the imported dataset and first-month
    measurements from the available geographical areas.

    The Reservoir Visualisation page uses national reservoir observations
    to explore changes over time.
    """
)


st.header("Application Pages")

st.markdown(
    """
    This Project currently contains four pages:

    1. **Home** – introduction to the project
    2. **Data Representation** – imported dataset and first-month data series
    3. **Visualisation** – interactive time-series exploration
    4. **Project Information** – project overview and documentation
    """
)


st.header("Project Access")

st.markdown(
    "[View ReservoirScope on GitHub](https://github.com/SP18-BCS-156/IND320-Project)"
)

st.header("Live Application")

st.markdown(
    "[Open Project](https://ind320-project.streamlit.app/)"
)