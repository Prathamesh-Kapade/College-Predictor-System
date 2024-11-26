# predictor/services.py


import pandas as pd
import joblib

# Path to the trained model file
MODEL_PATH = 'college_prediction_model_with_cap_round.pkl'

# Load the trained model
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")


def predict_colleges(seat_type, branch, cet_score, rank, cap_round):
    """
    Predicts colleges based on user inputs and CAP round.

    Args:
        seat_type (str): The category of the user (e.g., OPEN, SC, OBC).
        branch (str): The branch of engineering.
        cet_score (float): CET score of the user.
        rank (int): Rank of the user.
        cap_round (int): CAP round number (1, 2, or 3).

    Returns:
        list of tuples: [(college_name, probability), ...]
    """
    try:
        # Prepare user input data
        input_data = {
            'seat_type': [seat_type],
            'branch': [branch],
            'min': [cet_score],
            'Min Rank': [rank],
            'cap_round': [cap_round]
        }
        input_df = pd.DataFrame(input_data)

        # One-hot encode the input data
        input_encoded = pd.get_dummies(input_df, columns=['seat_type', 'branch'])

        # Ensure all required columns are present
        for col in model.feature_names_in_:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[model.feature_names_in_]

        # Predict probabilities for all colleges
        predicted_probabilities = model.predict_proba(input_encoded)

        # Create a DataFrame for probabilities
        college_names = model.classes_
        probability_df = pd.DataFrame(predicted_probabilities, columns=college_names)

        # Get the top 4 colleges based on probabilities
        top_colleges = probability_df.iloc[0].nlargest(4)

        return [(college, prob) for college, prob in top_colleges.items()]

    except Exception as e:
        print(f"Error during prediction: {e}")
        return []









# import joblib
# import pandas as pd

# # Load the trained model
# MODEL_PATH = 'D:\\PROJECT\\KNN\\college_prediction_model.pkl' 
# model = joblib.load(MODEL_PATH)

# def predict_college(seat_type, branch, min_score, min_rank):

#     input_data = {
#         'seat_type': [seat_type],
#         'branch': [branch],
#         'min': [min_score],
#         'Min Rank': [min_rank]
#     }

#     input_df = pd.DataFrame(input_data)

#     input_encoded = pd.get_dummies(input_df, columns=['seat_type', 'branch'])


#     for col in model.feature_names_in_:
#         if col not in input_encoded.columns:
#             input_encoded[col] = 0
#     input_encoded = input_encoded[model.feature_names_in_]

#     predicted_probabilities = model.predict_proba(input_encoded)


#     college_names = model.classes_
#     probability_df = pd.DataFrame(predicted_probabilities, columns=college_names)

#     top_colleges = probability_df.iloc[0].nlargest(4)

#     return top_colleges.to_dict()
