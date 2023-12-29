# OpenAI Api With Simple Books API Project
This project uses the OpenAI API to interact with the Simple Books API, a mock API that provides information about books. The project defines three functions that use the OpenAI API to call the Simple Books API endpoints:

https://simple-books-api.glitch.me/books

-- Watch -- 
[![Watch the video](https://i.ytimg.com/vi/ToefrGde6NY/hqdefault.jpg?sqp=-oaymwE2CPYBEIoBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB_gmAAtAFigIMCAAQARhaIGUoWjAP&rs=AOn4CLDmEa-5rzsbChZJSsF9OWOv3TaBtw)] (https://youtu.be/ToefrGde6NY?si=sBTNDhw5Cv_UKZ3j)


- `get_all_books:` This function returns a list of all books in the Simple Books API database, along with their titles, authors, and prices.
- `get_price:` This function takes a book title as an argument and returns the price of the book from the Simple Books API.
- `get_single_book:` This function takes a book title as an argument and returns the whole detail of the book from the Simple Books API, including the title, author, price, description, and rating.
The project also uses Streamlit, a framework for creating web applications, to create a simple user interface that allows users to enter a book title and see the results of the functions.

## Installation and Usage
To run this project, you will need:

Python 3.6 or higher
An OpenAI API key
The requests library
The streamlit library
To install the dependencies, run:

`pip install streamlit`

To run the project, run:

`streamlit run app.py`

This will launch the Streamlit web app in your browser. You can enter a book title in the text box and click the buttons to see the results of the functions.

 - Examples
Here are some examples of book titles and the results of the functions:

-  Book title: “The Catcher in the Rye”

    - get_all_books: The book is in the list of books, along with other books.

    - get_price: The price of the book is $9.99.

    - get_single_book: The book details are:

- Title: The Catcher in the Rye Author: J.D. Salinger Price: $9.99 Description: The classic novel of teenage angst and rebellion. Rating: 4.2/5

Book title: “Harry Potter and the Philosopher’s Stone”

get_all_books: The book is not in the list of books, as the Simple Books API only contains books published before 2000.
get_price: The function returns an error message: “Book not found.”
get_single_book: The function returns an error message: “Book not found.”
###[Connect with me on Linkedin](https://www.linkedin.com/in/therafiali/)
###[Directly Contact with me on email](mailto:therafiali@gmial.com)
- therafiali@gmail.com

License
This project is licensed under the MIT License. See the LICENSE file for details.
