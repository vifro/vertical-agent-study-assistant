# Vertical Study Agent Proof-of-Concept
## TODO: Add functionality
Download transcript, ask which questions are most likely to come up on the exam. Find different ways to to prompt for new information, given the transscrupts, and then create questions around that. 

So questions would then become 
* General questions, about everything
* topics & questions most likely on the exam.
* * Generate for each topic and questions. 

## Overview

The Vertical Study Agent is an AI-driven study companion designed to help learners master complex subjects by dynamically generating multiple-choice questions from pre-generated transcripts. The primary goal of this proof-of-concept (POC) is to validate the core idea: ingesting course transcripts, generating targeted questions with feedback, and tracking user progress—all with a simple, prompt-based user interface.

![Overview](/image/image.png)

## Motivation

In traditional online courses, note-taking and self-assessment can be tedious and inefficient. This project aims to:
- Automate note summarization from transcripts.
- Generate multiple-choice questions (with A-D options) using AI.
- Provide immediate feedback (correct/incorrect plus explanations).
- Track user progress across different topics.

By proving these points in a lightweight prototype, we set the stage for more advanced adaptive learning and intelligent tutoring systems.

## Objectives

- **Transcript Ingestion:** Read pre-generated transcript files (`.txt`) and organize content by topics (e.g., for Kafka: brokers, topics, consumers, producers).
- **AI-Driven Question Generation:** Use a language model (via Hugging Face/Ollama) and orchestration frameworks (Langchain/Langgraph) to generate multiple-choice questions.
- **User Interaction:** Implement a simple prompt-based interface using Streamlit to display questions and capture responses.
- **Data Storage:** Use a local NoSQL database to store transcript content, questions, user responses, and track progress.
- **Adaptive Learning (Future Scope):** Enable the system to adjust focus based on user performance.

## Requirements

### Functional Requirements
1. **Transcript Ingestion**
   - Read and parse `.txt` transcript files.
   - Organize content into predefined topics.
2. **AI-Based Question Generation**
   - Leverage a language model to generate multiple-choice questions.
   - Ensure each question includes options (A-D) and a rationale for the correct answer.
3. **User Interaction**
   - Present questions via a simple, prompt-based interface.
   - Capture user responses and provide immediate feedback.
4. **Data Storage & Tracking**
   - Store content and interactions in a local NoSQL database.
   - Schema suggestions:
     - **Content Collection:** `{ topic: string, part: string, text: string }`
     - **Question/Interaction Collection:** `{ user_id: string, topic: string, question: string, options: [string], correct_answer: string, user_answer: string, explanation: string, timestamp: datetime }`
5. **Adaptive Learning (Future)**
   - Analyze user performance per topic.
   - Adjust question selection frequency based on past performance.

### Non-Functional Requirements
- **Simplicity:** Keep the initial prototype as simple as possible.
- **Local Deployment:** All components (database, app, and processing) run locally.
- **Modularity:** Ensure the design is modular for future enhancements (e.g., integration of vector databases for semantic search).

## Technology Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend & AI:**
  - Python as the primary language.
  - [Hugging Face Transformers](https://huggingface.co/transformers/) or Ollama for language modeling.
  - [Langchain](https://python.langchain.com/) or [Langgraph](https://github.com/your-langgraph-link) to manage prompt orchestration and retrieval-augmented generation (RAG).
- **Database:** Local NoSQL database (e.g., MongoDB or a simple JSON-based store for rapid prototyping).
- **Optional (Future):** A vector database (e.g., FAISS, Pinecone, or Weaviate) for enhanced semantic search.

## Implementation Plan

### Phase 1: Setup & Transcript Ingestion
1. **Project Initialization**
   - Set up the project repository with a clear folder structure.
   - Define directories for transcripts, modules, and UI components.
2. **Transcript Processing Module**
   - Implement a module to read `.txt` files.
   - Parse and organize the transcripts into topics (e.g., brokers, topics, consumers, producers).
3. **Data Storage**
   - Configure the NoSQL database.
   - Store parsed transcript content with appropriate metadata (topic, part, text).

### Phase 2: AI-Based Question Generation
1. **Integration of AI Models**
   - Integrate the Hugging Face Transformers (or Ollama) for language generation.
   - Set up Langchain/Langgraph to construct prompts that:
     - Accept a segment of transcript text.
     - Generate a multiple-choice question (with A-D options).
     - Include feedback/explanation for the correct answer.
2. **Testing the Pipeline**
   - Run tests on sample transcript segments.
   - Fine-tune prompt designs to improve question quality and answer accuracy.

### Phase 3: User Interface Development
1. **Streamlit App Setup**
   - Develop a basic UI that lists topics and displays questions.
   - Implement a simple prompt interface where:
     - The user can select a topic or get a random question.
     - Questions are presented with multiple-choice options.
2. **Feedback and Interaction**
   - Capture the user’s selected answer.
   - Provide immediate feedback (correct/incorrect with explanation).
   - Save each interaction (question, answer, feedback) to the NoSQL database.

### Phase 4: Adaptive Learning & Progress Tracking (Future Scope)
1. **User Performance Analysis**
   - Build modules to analyze response data and identify weak areas.
   - Adjust the frequency of question types based on past performance.
2. **Dashboard and Reporting**
   - Develop a dashboard in Streamlit to visualize progress.
   - Allow users to review past interactions and focus on improvement areas.

## Running the Proof-of-Concept

1. **Setup Environment**
   - Ensure you have Python installed.
   - Create and activate a virtual environment.
     ```bash
     conda create -n vertical-study-agent python=3.10
     conda activate vertical-study-agent
     ```
   - Install required packages:
     ```bash
     conda install streamlit langchain transformers pymongo
     ```
2. **Prepare Transcript Files**
   - Place your pre-generated `.txt` transcripts in the designated `transcripts/` directory.
3. **Configure the Database**
   - Set up your local NoSQL database (e.g., MongoDB or configure your JSON store).
   - Update any configuration files with connection details.
4. **Start Ollama**
   - **Important:** Ensure that your Ollama service is running locally. The error `[Errno 61] Connection refused` indicates that the local model server is not active.
   - Start Ollama with your local model (e.g., DeepSeek R1) by running:
     ```bash
     ollama serve
     ```
     then in separate terimnal run 
     ```bash
     ollama run [model name]
     ```
   - Verify that Ollama is running before proceeding. Write something in terminal where you ran ollama run [model name] 
       ```bash
       >>> hello, glad to have you here
       ```
5. **Run the Application**
   - Start the Streamlit app:
     ```bash
     streamlit run app.py
     ```
6. **Interact with the Agent**
   - Use the web interface to select topics and answer generated questions.
   - Review the feedback provided and observe how interactions are stored for future progress analysis.


## Future Enhancements

- **Semantic Search:** Integrate a vector database to enable semantic retrieval of transcript content.
- **User Management:** Add user authentication for personalized tracking.
- **Expanded Question Formats:** Incorporate different question types (e.g., open-ended questions).
- **Cloud Deployment:** Transition from local storage to a scalable cloud-based solution.

## Conclusion

This POC is designed to validate the feasibility of an AI-driven study agent that leverages transcript ingestion and dynamic question generation to support self-directed learning. By starting simple and iterating based on user feedback, this project lays the groundwork for a more robust and adaptive learning platform.

## License

This project is licensed under the MIT License.

## Contact

For questions, contributions, or suggestions, please open an issue.
