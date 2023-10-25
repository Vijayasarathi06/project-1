import pymongo
con = pymongo.MongoClient("mongodb+srv://gvijayasarathi286:sarathivs2806@cluster0.y1fo9ht.mongodb.net/?retryWrites=true&w=majority")
print("Connected successfully")
db = con["python"]
print("Database created successfully")
col = db["Project"]
print("Collection created successfully")
mylist = {"question": "1. Who developed Python Programming Language?",
          "options": ["a) Wick van Rossum", "b) Rasmus Lerdorf", "c) Guido van Rossum", "d) Niene Stom"]}
x = col.insert_one(mylist)
print(x.inserted_id)






