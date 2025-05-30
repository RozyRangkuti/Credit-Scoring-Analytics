# loads the library and all objects needed to run the prediction process.
import joblib

model = joblib.load("model/rdf_model.joblib")
result_target = joblib.load("model/encoder_target.joblib")

# Create a function named prediction() to run the prediction process.
def prediction(data):
    """Making prediction

    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data

    Returns:
        str: Prediction result (Good, Standard, or Poor)
    """
    result = model.predict(data)
    final_result = result_target.inverse_transform(result)[0]
    return final_result