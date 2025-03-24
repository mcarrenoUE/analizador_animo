from deep_translator import GoogleTranslator
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

etiquetas = ['Negativo', 'Neutral', 'Positivo']

def analizar_sentimiento(texto):
    texto_traducido = GoogleTranslator(source='auto', target='en').translate(texto)

    tokens = tokenizer(texto_traducido, return_tensors="pt")
    resultado = model(**tokens)
    scores = resultado[0][0].detach().numpy()
    scores = softmax(scores)

    indice = scores.argmax()
    etiqueta = etiquetas[indice]
    porcentaje = round(float(scores[indice]) * 100, 2)

    return etiqueta, porcentaje
