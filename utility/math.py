import google.generativeai as genai
import numpy as np

model = "models/text-embedding-004";

def get_embedding_vector(text: str) -> list[float]:
    result = genai.embed_content(
        model,
        text
    )
    return result['embedding']

def get_simalrity(vector1: list[float], vector2: list[float]):
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    
def get_simalrity_ranking(cosine_simalarity: float) -> str:
    print(f"Simalarity score: {cosine_simalarity}")
    if cosine_simalarity == 1:
        return "Perfect match!"
    elif cosine_simalarity < 1 and cosine_simalarity >= .7:
        return "Very Similar"
    elif cosine_simalarity < .7 and cosine_simalarity >= .5:
        return "Similarish"
    else:
       return "Not very Similar :("
        