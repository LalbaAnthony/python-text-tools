class deduplicateLines:
    
    types = {
        "deduplicate": {
            "slug": "deduplicate",
            "name": "Deduplicate",
            "description": "Remove duplicate words from the text",
            "function": "deduplicate",
        },
        "deduplicate_lines": {
            "slug": "deduplicate_lines",
            "name": "Deduplicate Lines",
            "description": "Remove duplicate lines from the text",
            "function": "deduplicate_lines",
        },
        "deduplicate_case_insensitive": {
            "slug": "deduplicate_case_insensitive",
            "name": "Deduplicate Case Insensitive",
            "description": "Remove duplicate words from the text case insensitive",
            "function": "deduplicate_case_insensitive",
        },
        "deduplicate_lines_case_insensitive": {
            "slug": "deduplicate_lines_case_insensitive",
            "name": "Deduplicate Lines Case Insensitive",
            "description": "Remove duplicate lines from the text case insensitive",
            "function": "deduplicate_lines_case_insensitive",
        },
    }

    @staticmethod
    def _deduplicate(text):
        return " ".join(list(set(text.split())))
    
    @staticmethod
    def _deduplicate_lines(text):
        return "\n".join(list(set(text.split("\n"))))
    
    @staticmethod
    def _deduplicate_case_insensitive(text):
        return " ".join(list(set(text.lower().split())))
    
    @staticmethod
    def _deduplicate_lines_case_insensitive(text):
        return "\n".join(list(set(text.lower().split("\n"))))
    
    @staticmethod
    def deduplicate(text, type):
        
        if not text:
            return text

        if type not in deduplicateLines.types:
            raise ValueError("Invalid type!")
        
        function = getattr(deduplicateLines, f"_{deduplicateLines.types[type]['function']}")
        return function(text)
    