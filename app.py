import pandas as pd
import gradio as gr
import pycaret

# load sample dataset
from pycaret.datasets import get_data
data = get_data('iris')

#Setup 
from pycaret.classification import *
s = setup(data, target = 'species', session_id = 123)

#compare_models()
model=compare_models(sort = 'Accuracy', n_select = 1)
compare_model_results = pull()



def predict(selected_model, sepal_length, sepal_width, petal_length, petal_width):
    df = pd.DataFrame.from_dict({
        'sepal_length': [sepal_length], 
        'sepal_width': [sepal_width],
        'petal_length': [petal_length], 
        'petal_width': [petal_width]
    })
    
    pred = predict_model(model, df, raw_score=True)  # Assurez-vous que cette fonction est correctement définie pour utiliser votre modèle
    # Ajustez les clés selon les colonnes retournées par votre modèle
    result = f"La classe prédite est: {pred['prediction_label'][0]}\n\n" \
             f"Iris-setosa: {pred['prediction_score_Iris-setosa'][0].astype('float64')}\n\n" \
             f"Iris-versicolor: {pred['prediction_score_Iris-versicolor'][0].astype('float64')}\n\n" \
             f"Iris-virginica: {pred['prediction_score_Iris-virginica'][0].astype('float64')}"
    
    return result

# Inputs de Gradio
demo=gr.Interface( predict,
    [ 
        gr.Dropdown( list(compare_model_results['Model']), label="Model"),
        gr.Slider(minimum=1, maximum=10, label = 'sepal_length'),
        gr.Slider(minimum=1, maximum=10, label = 'sepal_width'),
        gr.Slider(minimum=1, maximum=10, label = 'petal_length'),
        gr.Slider(minimum=1, maximum=10, label = 'petal_width'),
    ],
    "text",
              )

# Interface Gradio

#==> Pour que demo.launch(share=True), il faut désactiver la protection en temps réel de l'antivirus présent sur l'ordinateur
#demo.launch(share=True)
demo.launch()