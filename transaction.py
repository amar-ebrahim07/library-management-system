class Transaction:
    
    def __init__(self, transactionid, memberid, bookid, date, type):
        self.transactionid = transactionid
        self.memberid = memberid
        self.bookid = bookid
        self.date = date
        self.type = type

    def display_info(self):
        return(f"{self.transactionid}, {self.memberid}, {self.bookid}, {self.date}, {self.type}")

    def __str__(self):
        return(self.bookid)