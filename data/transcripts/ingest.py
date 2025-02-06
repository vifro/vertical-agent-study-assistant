import os
from datetime import datetime
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient('mongodb://localhost:27017/')
db = client['study_agent']            # Database name
collection = db['transcripts']        # Collection for transcripts

# Define the directory where your transcripts are stored
transcripts_dir = os.path.join(os.getcwd(), 'apache_kafka_3_0')
print(f"Transcripts directory: {transcripts_dir}")
# Iterate over each .txt file in the directory
for filename in os.listdir(transcripts_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(transcripts_dir, filename)
        
        # Read the transcript content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Derive the lecture title from the file name.
        # Example: "01_topics_partitions_offsets.txt" -> "Topics Partitions Offsets"
        try:
            # Remove the numeric prefix and file extension
            base_name = filename.split('_', 1)[1].replace('.txt', '')
        except IndexError:
            base_name = filename.replace('.txt', '')
        
        lecture_title = base_name.replace('_', ' ').title()
        
        # Build the document for MongoDB
        document = {
            'course': 'Apache Kafka',
            'lecture_title': lecture_title,
            'file_name': filename,
            'content': content,
            'ingested_at': datetime.now()
        }
        
        # Insert the document into the collection
        result = collection.insert_one(document)
        print(f"Inserted document for '{lecture_title}' with ID: {result.inserted_id}")
