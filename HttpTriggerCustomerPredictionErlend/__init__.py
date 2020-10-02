import logging
import pickle
import azure.functions as func
import os
import sklearn


def main(req: func.HttpRequest) -> func.HttpResponse:

    klasse = req.params.get('klasse')
    alder = req.params.get('alder')
    kjonn = req.params.get('kjonn')
    min_data = [klasse, kjonn, alder]
    
    try:
        filename = 'finalized_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
    except Exception:
        logging.error("Could not load model.")
    else:
        logging.info("Model successfully loaded.")
    
    if klasse and alder and kjonn:
        prediction_raw = loaded_model.predict([min_data])[0]
        prediction_string = "Yes!" if prediction_raw == 1 else "No..."
        return func.HttpResponse(f"This HTTP triggered function executed successfully. Can I get a loan? {prediction_string}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function execution, but query parameters were not correct. Pass them in the query string a prediction response.",
             status_code=200
        )
