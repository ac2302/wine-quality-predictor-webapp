import pickle
import sys

with open('model', 'rb') as f:
    models = pickle.load(f)
    red_model = models['red']
    white_model = models['white']

def predict(color, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sufur_oxide, total_sufur_oxide, density, pH, sulphates, alcohol):
    if wine_color == 'red':
        model = red_model
    else:
        model = white_model
    pred = model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sufur_oxide, total_sufur_oxide, density, pH, sulphates, alcohol]])
    return pred[0]

if __name__ == "__main__":
    wine_color = input("color of wine (red or white): ")
    if wine_color.lower() not in ['red', 'white']:
        print('invalid input')
        sys.exit()

    fixed_acidity = float(input("fixed acidity: "))
    volatile_acidity = float(input("volatile acidity: "))
    citric_acid = float(input("citric acid: "))
    residual_sugar = float(input("residual sugar: "))
    chlorides = float(input("chlorides: "))
    free_sufur_oxide = float(input("free sulfur oxide: "))
    total_sufur_oxide = float(input("total sulfur oxide: "))
    density = float(input("density: "))
    pH = float(input("pH: "))
    sulphates = float(input("sulphates: "))
    alcohol = float(input("alcohol: "))
    
    score = predict(wine_color, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sufur_oxide, total_sufur_oxide, density, pH, sulphates, alcohol)
    print(f"the wine gets {round(score)}/10")