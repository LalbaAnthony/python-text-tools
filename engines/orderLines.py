class orderLines:
    
    types = {
        "order_alphabetically": {
            "slug": "order_alphabetically",
            "name": "Order Alphabetically",
            "description": "Order the lines alphabetically",
            "function": "order_alphabetically",
        },
        "order_alphabetically_descending": {
            "slug": "order_alphabetically_descending",
            "name": "Order Alphabetically Descending",
            "description": "Order the lines alphabetically descending",
            "function": "order_alphabetically_descending",
        },
        "order_numerically": {
            "slug": "order_numerically",
            "name": "Order Numerically",
            "description": "Order the lines numerically",
            "function": "order_numerically",
        },
        "order_numerically_descending": {
            "slug": "order_numerically_descending",
            "name": "Order Numerically Descending",
            "description": "Order the lines numerically descending",
            "function": "order_numerically_descending",
        },
    }

    @staticmethod
    def _order_alphabetically(text):
        return "\n".join(sorted(text.split("\n")))
    
    @staticmethod
    def _order_alphabetically_descending(text):
        return "\n".join(sorted(text.split("\n"), reverse=True))
    
    @staticmethod
    def _order_numerically(text):

        for line in text.split("\n"):
            if not line.isdigit():
                raise ValueError("Invalid input, some lines are not numbers!")

        return "\n".join(sorted(text.split("\n"), key=lambda x: int(x)))
    
    @staticmethod
    def _order_numerically_descending(text):

        for line in text.split("\n"):
            if not line.isdigit():
                raise ValueError("Invalid input, some lines are not numbers!")

        return "\n".join(sorted(text.split("\n"), key=lambda x: int(x), reverse=True))
    

    @staticmethod
    def order(text, type):
        
        if not text:
            return text

        if type not in orderLines.types:
            raise ValueError("Invalid type!")
        
        function = getattr(orderLines, f"_{orderLines.types[type]['function']}")
        return function(text)