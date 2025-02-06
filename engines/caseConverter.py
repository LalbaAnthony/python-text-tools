class caseConverter:

    types = {
        "sentence_case": {
            "slug": "sentence_case",
            "name": "Sentence Case",
            "description": "Convert the text to sentence case (the first letter of the text is capitalized)",
            "function": "to_sentence_case",
        },
        "lower_case": {
            "slug": "lower_case",
            "name": "lower case",
            "description": "Convert the text to lowercase",
            "function": "to_lower_case",
        },
        "upper_case": {
            "slug": "upper_case",
            "name": "UPPER CASE",
            "description": "Convert the text to uppercase",
            "function": "to_upper_case",
        },
        "alternating_case": {
            "slug": "alternating_case",
            "name": "aLtErNaTiNg CaSe",
            "description": "Convert the text to aLtErNaTiNg CaSe (one character is uppercase, the next is lowercase)",
            "function": "to_alternating_case",
        },
        "title_case": {
            "slug": "title_case",
            "name": "Title Case",
            "description": "Convert the text to title case (each word starts with a capital letter)",
            "function": "to_title_case",
        },
        "inverse_case": {
            "slug": "inverse_case",
            "name": "InVeRsE CaSe",
            "description": "Inverse the case of the text",
            "function": "to_inverse_case",
        },
    }

    @staticmethod
    def _to_sentence_case(text):
        return text.capitalize()

    @staticmethod
    def _to_lower_case(text):
        return text.lower()

    @staticmethod
    def _to_upper_case(text):
        return text.upper()

    @staticmethod
    def _to_alternating_case(text):
        return "".join([char.lower() if i % 2 == 0 else char.upper() for i, char in enumerate(text)])

    @staticmethod
    def _to_title_case(text):
        return text.title()

    @staticmethod
    def _to_inverse_case(text):
        return text.swapcase()
    
    @staticmethod
    def convert(text, type):
        
        if not text:
            return text

        if type not in caseConverter.types:
            raise ValueError("Invalid type!")
        
        function = getattr(caseConverter, f"_{caseConverter.types[type]['function']}")
        return function(text)
    

