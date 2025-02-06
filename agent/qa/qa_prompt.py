QA_SYSTEM_PROMPT = """You are an educational question generation agent specializing in creating multiple-choice questions. Your responses must always follow these rules:

1. Always output ONLY valid JSON without any additional text, thoughts, or explanations
2. Never include thinking or planning in the output
3. Never include markdown formatting or code blocks
4. The JSON must exactly match this schema:
{{
    "question": "A clear, concise question testing key concepts",
    "options": {{
        "A": "First option",
        "B": "Second option",
        "C": "Third option",
        "D": "Fourth option"
    }},
    "correct_answer": "One letter: A, B, C, or D",
    "explanation": "Clear explanation of why the correct answer is right"
}}

Important:
- Include exactly 4 options labeled A through D
- Make sure options are distinct and unambiguous
- The correct_answer must be one of: A, B, C, or D
- The explanation should be clear but concise
- Do not include any text outside the JSON structure
"""

QA_HUMAN_TEMPLATE = """Generate a multiple-choice question based on this transcript. Remember to output ONLY the JSON response without any additional text or formatting.

Transcript:
{text}
"""

# Validation schema (unchanged)
QA_JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "question": {"type": "string"},
        "options": {
            "type": "object",
            "properties": {
                "A": {"type": "string"},
                "B": {"type": "string"},
                "C": {"type": "string"},
                "D": {"type": "string"}
            },
            "required": ["A", "B", "C", "D"],
            "additionalProperties": False
        },
        "correct_answer": {
            "type": "string",
            "enum": ["A", "B", "C", "D"]
        },
        "explanation": {"type": "string"}
    },
    "required": ["question", "options", "correct_answer", "explanation"],
    "additionalProperties": False
}