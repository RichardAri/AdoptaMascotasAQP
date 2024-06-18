import spacy

nlp = spacy.load('es_core_news_sm')

def analizar_descripcion(descripcion):
    doc = nlp(descripcion)
    # Extraer entidades y palabras clave
    entidades = [(ent.text, ent.label_) for ent in doc.ents]
    return entidades
