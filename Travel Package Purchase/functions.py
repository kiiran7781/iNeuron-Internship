def predict(model, features):
    prediction = model.predict([features])
    return prediction[0]