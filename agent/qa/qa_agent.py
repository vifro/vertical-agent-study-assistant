import json
from typing import Dict, Any
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from jsonschema import validate, ValidationError
from ..agent import Agent
from .qa_prompt import QA_SYSTEM_PROMPT, QA_HUMAN_TEMPLATE, QA_JSON_SCHEMA

class QAGenerationAgent(Agent):
    def __init__(self, model_name: str = "deepseek-r1:8b"):
        """
        Initialize the QA Generation Agent with a local model.
        Example model_name: "deepseek-r1:8b"
        """
        super().__init__(model_name)
        
        # Initialize the prompt template using separate system and human messages
        system_message = SystemMessagePromptTemplate.from_template(QA_SYSTEM_PROMPT)
        human_message = HumanMessagePromptTemplate.from_template(QA_HUMAN_TEMPLATE)
        chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message])
        
        self._initialize_chain(chat_prompt)

    def _extract_and_validate_json(self, response: str) -> Dict[str, Any]:
        """
        Extract JSON from the response and validate it against the schema.
        """
        try:
            # Try to find JSON in the response
            json_start = response.find('{')
            json_end = response.rfind('}')
            
            if json_start == -1 or json_end == -1:
                raise ValueError("No JSON structure found in response")
            
            json_str = response[json_start:json_end + 1]
            data = json.loads(json_str)
            
            # Validate against schema
            validate(instance=data, schema=QA_JSON_SCHEMA)
            return data
            
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {str(e)}")
        except ValidationError as e:
            raise ValueError(f"JSON schema validation failed: {str(e)}")

    def process(self, transcript_text: str) -> Dict[str, Any]:
        """
        Generate a multiple-choice question from the provided transcript text.
        
        Returns:
        {
            "status": "success/error",
            "data": {
                "qa": {
                    "question": "Your generated question here...",
                    "options": {
                        "A": "Option A",
                        "B": "Option B",
                        "C": "Option C",
                        "D": "Option D"
                    },
                    "correct_answer": "X",  // X is one of A, B, C, D
                    "explanation": "A brief explanation of the correct answer."
                }
            }
        }
        """
        try:
            # Get response from the model
            response = self.chain.invoke({
                "text": transcript_text
            })
            
            # Extract and validate JSON from the response
            qa_data = self._extract_and_validate_json(response)
            
            return self._create_success_response({"qa": qa_data})
            
        except Exception as e:
            return self._create_error_response(e)
            
    def _create_error_response(self, error: Exception) -> Dict[str, Any]:
        """
        Create a detailed error response.
        """
        return {
            "status": "error",
            "error": {
                "type": type(error).__name__,
                "message": str(error),
                "details": "Failed to generate or validate QA response"
            }
        }