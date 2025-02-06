# Data Ingestion for Apache Kafka Transcripts

This directory contains the sample transcript files and an ingestion script to load them into a local MongoDB instance. The goal is to provide a quick way for anyone to replicate the proof-of-concept data ingestion process.

## Folder Structure
Example folder structure:
```bash
data/ 
├── transcripts/ 
│└── apache_kafka/ 
│ ├── 01_topics_partitions_offsets.txt 
│ ├── 02_brokers.txt 
│ ├── 03_consumers.txt 
│ └── 04_producers.txt 
└── ingest.py
```
- **transcripts/apache_kafka/**: Store your transcript files here. Each transcript should be a plain text (`.txt`) file.
- **ingest.py**: A Python script that reads each transcript file, extracts its content and metadata, and then inserts a document into MongoDB.

## File Naming & Organization

- **Naming Convention**:  
  Each transcript file is prefixed with a number (e.g., `01_`, `02_`) to maintain the order of lectures.  
  Use descriptive names for clarity. For example, `01_topics_partitions_offsets.txt` corresponds to a lecture on Kafka topics, partitions, and offsets.

- **Transcript Content**:  
  The entire transcript of the lecture should be contained in the `.txt` file. You can optionally annotate or segment the content later as needed.

## Prerequisites

- **Python 3.x**:  
  Ensure you have Python installed on your computer.

- **MongoDB**:  
  Install and run MongoDB locally. The script uses the default connection string `mongodb://localhost:27017/`.

- **Python Packages**:  
  Install the required packages using pip:
  
  ```bash
  pip install pymongo
  ```

## Ingesting the Data
1. Organize Your Transcripts:
Place your .txt files in the data/transcripts/apache_kafka/ directory following the naming conventions described above.

2. Configure MongoDB:
Ensure that your local MongoDB instance is running.

3. Run the Ingestion Script:
From the data/ folder, run the script:

```bash
python ingest.py
```
The script will:

- Read each transcript file.
- Parse the file name to derive a lecture title.
- Insert a document into the study_agent database, transcripts collection in MongoDB.

4. Verify the Data:
Use your MongoDB client to inspect the study_agent database and ensure that documents have been inserted correctly.