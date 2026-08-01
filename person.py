class Person:
    
    def __init__(self, memberid, name):
        self.name = name
        self.memberid = memberid

    def display_info(self):
        return f"{self.name}, {self.memberid}"
