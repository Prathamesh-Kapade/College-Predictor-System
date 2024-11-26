# predictor/forms.py
from django import forms

class CollegePredictionForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    category = forms.ChoiceField(choices=[('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST')], required=True)
    branch = forms.ChoiceField(choices=[('Computer Science', 'Computer Science'),
                                        ('Mechanical Engineering', 'Mechanical Engineering'),
                                        ('Electrical Engineering', 'Electrical Engineering'),
                                        ('Civil Engineering', 'Civil Engineering')], required=True)
    cet_score = forms.IntegerField(required=True)
    rank = forms.IntegerField(required=True)
    subscribe = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], required=True)
    cap_round = forms.ChoiceField(choices=[(1, 'CAP Round 1'), (2, 'CAP Round 2'), (3, 'CAP Round 3')], required=True)
    