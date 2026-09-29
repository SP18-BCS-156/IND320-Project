import streamlit as st

# Page configuration
st.set_page_config(
    page_title="IND-320 | Reservoir Dashboard",
    page_icon="💧",
    layout="wide"
)

# -----------------------------
# Hero Section
# -----------------------------
st.title("💧 IND-320 | Reservoir Dashboard")

st.markdown(
    """
    ### From Data to Decisions

    Explore, analyse, and visualise reservoir data through an
    interactive dashboard built with **Python, Pandas, Matplotlib, and Streamlit**.
    """
)

# -----------------------------
# Add an image
# -----------------------------
st.image(
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    caption="Exploring reservoir data through visualisation",
    use_container_width=True
)

# -----------------------------
# Project Introduction
# -----------------------------
st.markdown("## 📊 About the Project")

st.write(
    """
    This dashboard provides an interactive way to explore reservoir
    measurements over time. The data can be viewed as tables and
    visualisations, making it easier to understand patterns, changes,
    and differences between reservoir measurements.
    """
)

# -----------------------------
# Dashboard Features
# -----------------------------
st.markdown("## 🔎 Explore the Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📋 Data Overview")
    st.write(
        "Explore the imported reservoir dataset and view monthly data summaries."
    )

with col2:
    st.markdown("### 📈 Visualisation")
    st.write(
        "Create interactive plots and investigate individual variables or all measurements together."
    )

with col3:
    st.markdown("### 🧪 Project Information")
    st.write(
        "Learn more about the project, methodology, and implementation."
    )

# -----------------------------
# Project Information
# -----------------------------
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎓 Course")
    st.write("**IND-320 – Data to Decision**")

with col2:
    st.markdown("### 💻 Project")
    st.write("**Project Work – Part 1**")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption(
    "IND-320 | Data to Decision • Reservoir Data Analysis & Visualisation"
)