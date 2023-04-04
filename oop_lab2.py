class Person:
    def __init__(self, id, name, age, profession, experience):
        self.id = id
        self.name = name
        self.age = age
        self.profession = profession
        self.experience = experience
    
    def introducing(self):
        print(f"My name is {self.name}, I am {self.age} years old and I am a {self.profession}")

class Book:
    def __init__(self, id, name, authorName, genre, price):
        self.id = id
        self.name = name
        self.authorName = authorName
        self.genre = genre
        self.price = price
    
    def sale(self):
        discounted_price = self.price * 0.8
        return (self.genre, self.name, discounted_price)

person1 = Person(1, "John", 30, "Software Developer", 5)
person2 = Person(2, "Alice", 25, "Data Scientist", 3)
person3 = Person(3, "Bob", 40, "Project Manager", 10)

# Using the introducing() method of Person class
person1.introducing()  # Output: "My name is John, I am 30 years old and I am a Software Developer"
person2.introducing()  # Output: "My name is Alice, I am 25 years old and I am a Data Scientist"
person3.introducing()  # Output: "My name is Bob, I am 40 years old and I am a Project Manager"

# Creating 3 Book objects
book1 = Book(1, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 10.0)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", "Fiction", 12.0)
book3 = Book(3, "The Lean Startup", "Eric Ries", "Business", 15.0)

# Using the sale() method of Book class
print(book1.sale())  # Output: ("Fiction", "The Great Gatsby", 8.0)
print(book2.sale())  # Output: ("Fiction", "To Kill a Mockingbird", 9.6)
print(book3.sale())  # Output: ("Business", "The Lean Startup", 12.0)