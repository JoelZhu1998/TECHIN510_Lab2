import streamlit as st
import pandas as pd
import altair as alt

# Load the dataset
@st.cache
def load_data():
    url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv"
    data = pd.read_csv(url)
    return data

iris_data = load_data()

# Title and introduction
st.title("Iris Flower Data Analysis")
st.write("""
This app provides an analysis of the Iris Flower Dataset. The dataset includes measurements for various attributes of three iris species: Iris setosa, Iris virginica, and Iris versicolor. Use the widgets to filter the data and explore different visualizations.
""")

# Filters
species_selection = st.selectbox("Select Species", options=["All"] + list(iris_data['species'].unique()))
petal_length_min, petal_length_max = st.slider("Petal Length Range", float(iris_data['petal_length'].min()), float(iris_data['petal_length'].max()), (float(iris_data['petal_length'].min()), float(iris_data['petal_length'].max())))
sepal_width_min, sepal_width_max = st.slider("Sepal Width Range", float(iris_data['sepal_width'].min()), float(iris_data['sepal_width'].max()), (float(iris_data['sepal_width'].min()), float(iris_data['sepal_width'].max())))

# Filtering data based on selection
if species_selection != "All":
    iris_data = iris_data[iris_data['species'] == species_selection]
filtered_data = iris_data[(iris_data['petal_length'] >= petal_length_min) & (iris_data['petal_length'] <= petal_length_max) &
                          (iris_data['sepal_width'] >= sepal_width_min) & (iris_data['sepal_width'] <= sepal_width_max)]

# Display filtered data
st.write(filtered_data)

# Visualization with Altair
chart = alt.Chart(filtered_data).mark_circle(size=60).encode(
    x='sepal_length',
    y='sepal_width',
    color='species',
    tooltip=['sepal_length', 'sepal_width', 'species']
).interactive()

st.altair_chart(chart, use_container_width=True)
