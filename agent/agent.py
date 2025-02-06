from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from langchain.chains import LLMChain
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import StringPromptTemplate, ChatPromptTemplate


class Agent(ABC):
    def __init__(self, model_name: str = "llama2"):
        self.model_name = model_name
        self.llm = OllamaLLM(model=model_name, temperature=0.0)
        self.chain: Optional[LLMChain] = None
        self.debug_logs: list = []

    def _log_debug(self, message: str):
        """Add debug message to logs"""
        self.debug_logs.append(message)
        print(f"DEBUG: {message}")

    def _initialize_chain(self, prompt_template: ChatPromptTemplate):
        """Initialize the LLM chain with given prompt template"""
        self.chain = prompt_template | self.llm

    def _create_error_response(self, error: Exception) -> Dict[str, Any]:
        """Create standardized error response"""
        return {
            "status": "error",
            "message": str(error),
            "debug_logs": self.debug_logs
        }

    def _create_success_response(self, data: Any) -> Dict[str, Any]:
        """Create standardized success response"""
        return {
            "status": "success",
            "data": data,
            "debug_logs": self.debug_logs
        }

    @abstractmethod
    def process(self, *args, **kwargs) -> Dict[str, Any]:
        """Main processing method to be implemented by each agent"""
        pass