class Book:

    def __init__(self, bookid, title, author, category, publication, availability):
        self.bookid = bookid
        self.title = title
        self.author = author
        self.category = category
        self.publication = publication
        self.availability = availability
    

    def display_info(self):
        return (f"{self.bookid}, {self.title}, {self.author}, {self.category}, {self.publication}, {self.availability}")

    def update_details(self, title=None, author=None, category=None, publication=None, availability=None):
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if category is not None:
            self.category = category
        if publication is not None:
            self.publication = publication
        if availability is not None:
            self.availability = availability


    def __str__(self):
        return(self.title)
