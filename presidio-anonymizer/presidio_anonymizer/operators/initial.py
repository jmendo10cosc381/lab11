
from typing import Dict
from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    def extract_initial(self, word: str) -> str:
        prefix = ""

        for char in word:
            if char.isalnum():
                return prefix + char.upper() + "."
            else:
                prefix += char
        
        return word

    def operate(self, text: str = None, params: Dict = None) -> str:
        if not text:
            return ""
        
        words = text.strip().split()

        initials = [self.extract_initial(w) for w in words]
        
        return " ".join(initials)

    def validate(self, params: Dict = None) -> None:
        """Redact does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize


