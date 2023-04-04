# Shelfie

Shelfie is a service that allows you to manage your books and easily track how much you're reading. With Shelfie, you can add books to your collection, mark them as read or unread, and delete them if you no longer want them in your list.

## Getting started

To get started with Shelfie, you'll need to set up a local instance of MongoDB and run the Flask app locally.
Here's how to do it:

### Prerequisites

Before you can run Shelfie, you'll need to have the following installed on your machine:

- Python 3.6 or higher
- Flask
- MongoDB 4.0 or higher
- pymongo

### Installation

1. Clone the repository from GitHub: `git clone https://github.com/victoriademina/shelfie.git`
2. Install the required Python packages: 
```
cd shelfie
pip install -r requirements.txt
```
### Running the app

1. Start MongoDB: `mongosh`
2. In a new terminal window, export environment variables and start the Flask app:
```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
3. Open a web browser and navigate to http://127.0.0.1:5000 to use the app.

## Usage

To use Shelfie, simply add books to your collection by filling out the book title and its status. Once you've added a book, you can see the list of books right below the form. You can also delete a book by clicking the "Delete" button.

You can check your books in a database as well by using these commands:
```
mongosh
show dbs
use flask_db
db.books.find()
```


## License
Shelfie is released under the MIT License. See [LICENSE](https://github.com/victoriademina/Shelfie/blob/main/LICENSE) for details.
