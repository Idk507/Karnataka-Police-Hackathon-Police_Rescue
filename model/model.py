import streamlit as st
import pandas as pd
import numpy as np
from geopy.distance import geodesic
from sklearn.cluster import KMeans

# Load the dataset
@st.cache_data
def load_data():
    file_path = r"C:\Users\hp\Desktop\project\predictive crime\preprocessed_df1.csv"  # Update with your file path
    return pd.read_csv(file_path, low_memory=False)

# Function to calculate distance between two coordinates
def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).km

# Function to generate deployment plan
def generate_deployment_plan(df, centroids):
    deployment_plan = {}
    for cluster in centroids.keys():
        cluster_data = df[df['Cluster'] == cluster]
        number_of_incidents = len(cluster_data)
        suggestions = ""
        if number_of_incidents == 0:
            suggestions = "Increase police presence and conduct thorough investigations to prevent future incidents."
        elif number_of_incidents <= 10:
            suggestions = "Continue monitoring the area and conduct periodic patrols to maintain security."
        else:
            suggestions = "<span style='color:red;font-weight:bold'>Intensify surveillance efforts</span> and consider implementing community policing strategies."

        deployment_plan[cluster] = {
            'cluster_centroid': centroids[cluster],
            'number_of_incidents': number_of_incidents,
            'suggestions': suggestions
        }
    return deployment_plan

# Function to predict the number of incidents based on input latitude and longitude
def predict_incidents(input_latitude, input_longitude, df, centroids):
    offense_location = (input_latitude, input_longitude)
    closest_centroid = min(centroids.keys(), key=lambda x: calculate_distance(offense_location, (centroids[x]['Latitude'], centroids[x]['Longitude'])))
    return closest_centroid

# Streamlit app
def main():
    st.title("Crime Deployment Plan")

    # Load the data
    df = load_data()

    # Preprocessing
    df = df[(df['Latitude'] != 0.0) & (df['Longitude'] != 0.0)]

    # Clustering
    features = ['Latitude', 'Longitude']
    X = df[features]
    X = (X - X.mean()) / X.std()
    kmeans = KMeans(n_clusters=5, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

    # Define the latitude and longitude of the cluster centroids
    centroids = {
        1: {'Latitude': -0.26350117329990513, 'Longitude': 0.20905869782346226},
        2: {'Latitude': 5.807340212426832, 'Longitude': -5.187200322116295},
        3: {'Latitude': -1.2370956602478118, 'Longitude': -5.921660553559399},
        4: {'Latitude': -0.2676250405697857, 'Longitude': 59.52073073890124},
        5: {'Latitude': 0.023547431083855475, 'Longitude': 0.09870306054587759}
    }

    # User input for latitude and longitude
    st.header("Input Latitude and Longitude")
    input_latitude = st.number_input("Latitude", value=0.0)
    input_longitude = st.number_input("Longitude", value=0.0)

    # Button to trigger the calculation
    if st.button("Predict and Generate Suggestions"):
        # Predict the cluster and get suggestions
        cluster_prediction = predict_incidents(input_latitude, input_longitude, df, centroids)
        deployment_plan = generate_deployment_plan(df, centroids)
        suggestions = deployment_plan[cluster_prediction]['suggestions']

        # Calculate the number of incidents based on input value
        offense_location = (input_latitude, input_longitude)
        closest_centroid_data = df[df['Cluster'] == cluster_prediction]
        number_of_incidents = len(closest_centroid_data)
        
        # Display suggestions and number of incidents
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Suggestions")
            st.markdown(suggestions, unsafe_allow_html=True)
        with col2:
            st.subheader("Number of Incidents")
            st.write(number_of_incidents)

if __name__ == "__main__":
    main()
