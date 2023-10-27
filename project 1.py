import pymongo
con = pymongo.MongoClient("mongodb+srv://gvijayasarathi286:sarathivs2806@cluster0.y1fo9ht.mongodb.net/?retryWrites=true&w=majority")
##print("Connected successfully")
db = con["python"]
##print("Database created successfully")
col = db["Project"]
##print("Collection created successfully")
questions=[
    {
        "question":"1. Who developed Python Programming Language?",
        "options":["a) Wick van Rossum","b) Rasmus Lerdorf","c) Guido van Rossum","d) Niene Stom"],
        },
    {
        "question":"2. Which type of Programming does Python support?",
        "options":["a) object-oriented programming","b) structured programming","c) functional programming","d) all of the mentioned"],
        },
    {
        "question":"3. Is Python case sensitive when dealing with identifiers?",
        "options":["a) no","b) yes","c) machine dependent","d) none of the mentioned"],
        },
    {
        "question":"4. Which of the following is the correct extension of the Python file?",
        "options":["a) .python","b) .pl","c) .py","d) .p"],
        },
    {
        "question":"5. Is Python code compiled or interpreted?",
        "options":["a) Python code is both compiled and interpreted","b) Python code is neither compiled nor interpreted","c) Python code is only compiled","d) Python code is only interpreted"],
        },
    {
        "question":"6. All keywords in Python are in _________",
        "options":["a) Capitalized","b) lower case","c) UPPER CASE","d) None of the mentioned"],
        },
    {
        "quesion":"7. What will be the value of the following Python expression?",
        "4 + 3 % 5"
        "options":["a) 7","b) 2","c) 4","d) 1"],
        },
    {
        "quesion":"8. Which of the following is used to define a block of code in Python language?",
        "options":["a) Indentation","b) Key","c) Brackets","d) All of the mentioned"],
        },
    {
        "question":"9. Which keyword is used for function in Python language?",
        "options":["a) Function","b) def","c) Fun","d) Define"],
        },
    {
        "question":"10. Which of the following character is used to give single-line comments in Python?",
        "options":["a) //","b) #","c) !","d) /*"],
        },
    {
        "Answer":["1.c","2.d","3.b","4.c","5.a","6.d","7.a","8.a","9.b","10.b"],
        }]
##x = col.insert_many(questions)
##print(x.inserted_ids)
x=col.find({},{"question":1,"options":1,"Answer":1})
score=0
for i in x:
    print(f"i.questions{questions}")
    for j in questions["options"]:
        print(j)
a=str(input("Enter the options"))
if a in questions["Answer"]:
    score+=1
    print("your total mark is",score)







