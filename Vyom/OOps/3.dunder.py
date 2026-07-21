class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    
    def __str__(self):
        return f"{self.title},by {self.title}"
    
    def __eq__(self,other):
        return self.title==other.title and self.author ==other.author
    

book1=Book("abc","cba")
book2=Book("def","fed")

print(book2)
print(book1==book2)