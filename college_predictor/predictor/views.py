# predictor/views.py
# predictor/views.py

from django.shortcuts import render
from .services import predict_colleges


def home(request):
    return render(request, 'home.html')


def result(request):
    if request.method == 'POST':
        try:
            # Retrieve input data from the form
            name = request.POST.get('name', '')
            seat_type = request.POST.get('category', '').upper()  # Convert to uppercase for consistency
            branch = request.POST.get('branch', '')
            cet_score = float(request.POST.get('cet_score', 0))
            rank = int(request.POST.get('rank', 0))
            cap_round = int(request.POST.get('cap_round', 1))  # Default to CAP round 1 if not provided

            # Call prediction service
            predicted_colleges = predict_colleges(seat_type, branch, cet_score, rank, cap_round)

            # Render results
            return render(request, 'result.html', {
                'name': name,
                'cap_round': cap_round,
                'predicted_colleges': predicted_colleges
            })

        except ValueError as e:
            # Handle input conversion errors
            return render(request, 'error.html', {'error': f"Invalid input: {e}"})

        except Exception as e:
            # Handle other exceptions
            return render(request, 'error.html', {'error': f"An error occurred: {e}"})

    return render(request, 'home.html')


def about(request):
    return render(request,"about.html")










# import pandas as pd
# import numpy as np
# import joblib
# from django.shortcuts import render
# from .forms import CollegePredictionForm
# from .services import predict_college

# def home(request):
#     return render(request, 'home.html')


# def result(request):
#     # Load the trained model
#     model_filename = 'college_prediction_model.pkl' 
#     model = joblib.load(model_filename)

#     data = pd.read_csv('C:\\Users\\Prathamesh\\Documents\\MHTCET_RANK.csv')
#     data_cleaned = data.drop(columns=['score_type', 'max', 'Max Rank'])

#     name = request.POST.get('name', '') 
#     category = request.POST.get('category', '')
#     branch = request.POST.get('branch', '')
#     cet_score = float(request.POST.get('cet_score', 0))  
#     rank = int(request.POST.get('rank', 0))  

#     input_data = {
#         'seat_type': [category], 
#         'branch': [branch],
#         'min': [cet_score],  
#         'Min Rank': [rank]
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

#     predicted_colleges = [(college, probability) for college, probability in top_colleges.items()]

#     return render(request, 'result.html', {
#         'name': name,
#         'predicted_colleges': predicted_colleges
#     })



