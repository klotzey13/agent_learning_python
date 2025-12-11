import google.generativeai as genai
import os
from dotenv import load_dotenv
from utility.math import *
from journal.journal_memory import JournalMemory
from datetime import datetime

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-2.5-flash')
journal = JournalMemory()

while True:
    user_input = input("\nPlease enter a journal entry: ")
    
    if user_input.lower() in ["quit", "exit", "cancel"]:
        break
    elif user_input.lower() in ["compare"]:
        if len(journal.entries) < 2:
            print("Add more entries to the journal before comparing!")
        else:
            entry1 = input("\nWhat Index for first Journal Entry: ")
            entry2 = input("\nWhat Index for Second Journal Entry: ")
            simalrity = get_simalrity(journal.entries[int(entry1)]["vector"], journal.entries[int(entry2)]["vector"])
            print(f"{journal.entries[int(entry1)]["text"]}\nand\n{journal.entries[int(entry2)]["text"]}")
            print(f"\n... {get_simalrity_ranking(simalrity)}")
    else:
        JournalMemory.add_entry(journal, user_input, datetime.now())
        print(f"\nJournal Entries: {len(journal.entries)}")
    
    """
    response = model.generate_content(user_input, stream=True)
    
    for chunk in response:
        print(f"{chunk.text}")
    """

