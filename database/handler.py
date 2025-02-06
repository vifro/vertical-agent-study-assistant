# agent/database_handler.py

from pymongo import MongoClient

class DatabaseHandler:
    def __init__(self, uri='mongodb://localhost:27017/', db_name='study_agent', collection_name='transcripts'):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def fetch_all_lecture_titles(self):
        """
        Fetch a list of all available lecture titles from the database.
        """
        # Assuming each document has a "lecture_title" field.
        titles = self.collection.distinct("lecture_title")
        return list(titles)

    def get_transcript(self, lecture_title: str) -> str:
        """
        Retrieve the transcript content for the specified lecture title.
        Returns an empty string if no transcript is found.
        """
        doc = self.collection.find_one({"lecture_title": lecture_title})
        if doc:
            return doc.get("content", "")
        else:
            return ""
