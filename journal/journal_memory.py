from utility.math import get_embedding_vector

class JournalMemory:
    def __init__(self):
        self.entries = []
    
    def add_entry(self, text: str, date):
        entry = {
            "text": text, 
            "date": date, 
            "vector": get_embedding_vector(text)
        }
        self.entries.append(entry)