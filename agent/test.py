# --- MongoDB Setup ---
import json
from pymongo import MongoClient

from agent.qa.qa_agent import QAGenerationAgent




client = MongoClient('mongodb://localhost:27017/')
db = client['study_agent']          # Database name used previously
collection = db['transcripts']      # Collection with transcript documents

def get_transcript(lecture_title=None):
    """
    Retrieve a transcript from MongoDB.
    If lecture_title is provided, fetch that specific lecture; otherwise, fetch one document.
    """
    if lecture_title:
        doc = collection.find_one({"lecture_title": lecture_title})
    else:
        doc = collection.find_one()
    if not doc:
        raise Exception("No transcript found in the database.")
    return doc['content']

# --- Main Execution ---
if __name__ == "__main__":
    try:
        # Retrieve a transcript (modify parameter to choose a specific lecture)
        transcript_text = get_transcript()
        print(f"Transcript: {transcript_text}")
        # Initialize the QA generation agent with your local model (e.g., "deepseek-r1")
        qa_agent = QAGenerationAgent(model_name="deepseek-r1:8b")
        
        # Generate the question and answer set from the transcript
        qa_result = qa_agent.process(transcript_text)
        
        print("Generated Question and Answer:")
        print(json.dumps(qa_result, indent=2))
    except Exception as e:
        print("An error occurred:", str(e))
