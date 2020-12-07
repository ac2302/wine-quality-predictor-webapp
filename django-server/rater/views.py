from django.http import HttpResponse
from django.shortcuts import render
import pickle
import sys

# predict stuff
with open('models/decision-tree-1', 'rb') as f:
    models = pickle.load(f)
    red_model = models['red']
    white_model = models['white']


def predict(color, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sufur_oxide, total_sufur_oxide, density, pH, sulphates, alcohol):
    if color == 'red':
        model = red_model
    else:
        model = white_model
    pred = model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                           chlorides, free_sufur_oxide, total_sufur_oxide, density, pH, sulphates, alcohol]])
    return pred[0]


# Create your views here.

def input_view(request):
    # return HttpResponse("Hello World")
    return render(request, 'input.html', {})


def output_view(request):
    data = request.GET
    print(data)
    try:
        result = predict(data['color'], float(data['fixed_acidity']), float(data['volatile_acidity']), float(data['citric_acid']), float(data['residual_sugar']), float(data['chlorides']), float(
            data['free_sulfur_dioxide']), float(data['total_sulfur_dioxide']), float(data['density']), float(data['pH']), float(data['sulphates']), float(data['alcohol']))
    except:
        return HttpResponse("invaid response")
    return HttpResponse(result)
