from pymongo import MongoClient 
from pymongo.server_api import ServerApi

from bson import ObjectId

client = MongoClient("mongodb+srv://<youtubepy>:<youtubepy>@cluster0.om2myrw.mongodb.net/?appName=Cluster0" , server_api=ServerApi('1'))

db = client['ytmanager']
collection = db["videos"]
print(collection)


def list_book():
    for video in collection.find():
        print(f"ID:{video['_id']} , name:{video['name']} , author:{video['author']}")

def add_book(name , author):
    collection.insert_one({'name':name , 'author':author})

def update_book(id , name , author):
    collection.update_one({'_id':ObjectId(id)},{"$set":{'name':name ,'author':author}})

def delete_book(id):
    collection.delete_one({'_id':ObjectId(id)})


def main():

    while True:
        print("\n Welcome from Book Data Control.....")

        print("Enter 1 for List the Books")
        print("Enter 2 for Add a new Book")
        print("Enter 3 for Update the Book")
        print("Enter 4 for Delete the Book")
        inp = input("Enter ===== : ")

        if inp == '1':
            list_book()
        
        elif inp == '2':
            name = input("Enter the Book name ")
            author = input("Enter the Book author ")
            add_book(name , author)

        elif inp == '3':
            id  = input("Enter the Id ")
            name = input("Enter the Book name ")
            author = input("Enter the Book author ")

            update_book(id , name , author)

        elif inp == '4':
            id  = input("Enter the Id ")
            delete_book(id)

        elif inp == '5':
            break

        else:
            print("Invalid Number")
    print(collection.find())

        


if __name__ == "__main__":
    main()

# remove the <> from the serial key