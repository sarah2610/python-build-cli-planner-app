class PrefixedReminder:
    def __init__(self,prefix="Hey, dont forget to"):
        self.prefix=prefix
        self.text=prefix + '<placeholder_text>'
    
class PoliteReminder(PrefixedReminder):
    def __init__(self,text):
        super().__init__(prefix="Please remember to ")
        self.text=self.prefix + text
