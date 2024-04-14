# Prototype - Karnataka-Police-Hackathon-Police_Rescue

TEAM : Police Rescue

DATASET : Download dataset and  paste the csv file on predictive_crime folder!!
      link : https://drive.google.com/drive/folders/1d3zbqzQ2gSerwuYQ3zMgys2-nTEPOIy_?usp=sharing

## Requirements
To run this prototype, you must have the following libraries installed on your PC:
- Streamlit
- Matplotlib.pyplot
- Godesic
- KMeans
- Numpy
- Pandas
- Pickle

## Installation
Make sure you have all the required libraries installed on your system. You can install them using pip:

```bash
pip install streamlit matplotlib godesic KMeans numpy pandas pickle
```

## Running the Models
To run the models, navigate to the `model` folder in your command prompt (cmd) and execute the following commands:

1. **Cluster Model**:
```bash
streamlit run "write full path\model\model.py"
```

2. **ARIMA Model**:
```bash
streamlit run "write full path\model\arima\arima.py"
```

3. **Accused Behavior Model**:
```bash
streamlit run "write full path\model\accused behaiver\model.py"
```

4. **Predictive Model**:
```bash
streamlit run "write full path\model\preditive.py"
```

## Accessing the Models
After running each model, you will get a local network URL. Replace the placeholder "runing network url" with the provided URL in the respective HTML files:

1. **clustered_crime.html**: 
Replace `"runing network url"` with `"http://192.168.1.40:8501"`

2. **future_crime_predicted.html**: 
Replace `"runing network url"` with `"http://192.168.1.40:8502"`

3. **behaviroal_prediction.html**: 
Replace `"runing network url"` with `"http://192.168.1.40:8503"`

4. **prediction_for_cases.html**: 
Replace `"runing network url"` with `"http://192.168.1.40:8504"`

## Usage
Once all models are running and URLs are replaced, you can access the prototype by opening the respective HTML files in a web browser.

Now you can explore the prototype! If you have any questions or feedback, feel free to reach out.
