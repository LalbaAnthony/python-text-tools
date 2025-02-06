from engines.caseConverter import caseConverter
from engines.orderLines import orderLines
from engines.deduplicateLines import deduplicateLines

class pttController:
    def __init__(self, view):
        self.view = view
        self.caseConverter = caseConverter()
        self.orderLines = orderLines()
        self.deduplicateLines = deduplicateLines()

        # Bind events
        self.view.sentence_case_button.config(command=lambda: self.handle_case_conversion("sentence_case"))
        self.view.lower_case_button.config(command=lambda: self.handle_case_conversion("lower_case"))
        self.view.upper_case_button.config(command=lambda: self.handle_case_conversion("upper_case"))
        self.view.alternating_case_button.config(command=lambda: self.handle_case_conversion("alternating_case"))
        self.view.title_case_button.config(command=lambda: self.handle_case_conversion("title_case"))
        self.view.inverse_case_button.config(command=lambda: self.handle_case_conversion("inverse_case"))

        self.view.deduplicate_button.config(command=lambda: self.handle_deduplicate("deduplicate"))
        self.view.deduplicate_lines_button.config(command=lambda: self.handle_deduplicate("deduplicate_lines"))
        self.view.deduplicate_case_insensitive_button.config(command=lambda: self.handle_deduplicate("deduplicate_case_insensitive"))
        self.view.deduplicate_lines_case_insensitive_button.config(command=lambda: self.handle_deduplicate("deduplicate_lines_case_insensitive"))

        self.view.order_alphabetically_button.config(command=lambda: self.handle_order("order_alphabetically"))
        self.view.order_alphabetically_descending_button.config(command=lambda: self.handle_order("order_alphabetically_descending"))
        self.view.order_numerically_button.config(command=lambda: self.handle_order("order_numerically"))
        self.view.order_numerically_descending_button.config(command=lambda: self.handle_order("order_numerically_descending"))
        
        self.view.clear_button.config(command=self.view.clear_textarea)

    def handle_case_conversion(self, type):
        
        text = self.view.get_textarea_value()
        
        try:
            result = self.caseConverter.convert(text, type)
        except ValueError as e:
            self.view.show_warning(str(e))
            return

        self.view.set_textarea_value(result)

    def handle_deduplicate(self, type):
            
            text = self.view.get_textarea_value()
            
            try:
                result = self.deduplicateLines.deduplicate(text, type)
            except ValueError as e:
                self.view.show_warning(str(e))
                return
    
            self.view.set_textarea_value(result)

    def handle_order(self, type):
            
            text = self.view.get_textarea_value()
            
            try:
                result = self.orderLines.order(text, type)
            except ValueError as e:
                self.view.show_warning(str(e))
                return
    
            self.view.set_textarea_value(result)