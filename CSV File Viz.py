import streamlit as st
import pandas as pd
import plotly.express as px

st.header("CSV File Visualization")

# @st.cache_resource()
@st.cache_data()
def load_data(file):
    return pd.read_csv(file)

file = st.file_uploader("Upload CSV File", type=["csv"])

# if file is not None:
if file:
    df = pd.read_csv(file)

    # Display DataFrame
    n_rows = st.slider("Choose Number of Rows to Display" ,min_value=5, max_value=len(df), step = 1)
    # st.write(df.sample(n_rows))
    columns = st.multiselect("Select Columns to Display", df.columns.to_list(), default=list(df.columns))
    st.write(df[ :n_rows][columns])

    # Select  a Chart Type
    tab1, tab2 = st.tabs(["Scatter Plot", "Histogram Chart"])

    # Scatter Plot
    with tab1:
        col1, col2, col3 = st.columns(3)
        numeric_columns = df.select_dtypes(include="number").columns.to_list()
        with col1:
            x_column = st.selectbox("Select Column on X-Axis", numeric_columns)
        with col2:
            y_column = st.selectbox("Select Column on Y-Axis", numeric_columns)
        with col3:
            color = st.selectbox("Select Column to be a Color", df.columns)
        fig_scatter = px.scatter(df, x=x_column, y=y_column, color=color)
        st.plotly_chart(fig_scatter)

    # Histogram Plot
    with tab2:
        hist_feature = st.selectbox("Select Feature for Histogram", numeric_columns)
        fig_hist = px.histogram(data_frame=df , x=hist_feature)
        st.plotly_chart(fig_hist)


