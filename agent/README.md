# POC Agent for Generating Questions & Answers

This document explains how to implement a proof-of-concept (POC) agent that generates multiple-choice questions (MCQs) from transcript text stored in MongoDB. The agent uses an AI language model to produce a question, a set of four answer options (A-D), the correct answer, and a brief explanation.

## Overview

The POC Agent follows these steps:
1. **Retrieve Transcript Text**: Query a transcript document from the MongoDB collection.
2. **Construct a Prompt**: Create a prompt that instructs the AI model to generate an MCQ based on the transcript text.
3. **Generate the Question & Answers**: Pass the prompt to the language model (via LangChain) to generate the question, options, correct answer, and explanation.
4. **Output & (Optional) Store the Result**: Display the result on the console or integrate it into a UI.

## Prerequisites

- **MongoDB**: Ensure your MongoDB instance is running and that transcript data has been ingested.
- **Python 3.x**: Ensure Python is installed.
- **Required Python Packages**:
  - `pymongo` for MongoDB access.
  - `langchain` for prompt management and LLM integration.
  - An LLM wrapper package (e.g., `openai` if using the OpenAI API or a Hugging Face model wrapper).

Install the required packages using pip:

```bash
conda install pymongo langchain langchain-core langchain-community
