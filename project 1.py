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
        "options":["a.Wick van Rossum","b.Rasmus Lerdorf","c.Guido van Rossum","d.Niene Stom"],
        "answer":"c",
        },
    {
        "question":"2. Which type of Programming does Python support?",
        "options":["a.object-oriented programming","b.structured programming","c.functional programming","d.all of the mentioned"],
        "answer":"d",
        },
    {
        "question":"3. Is Python case sensitive when dealing with identifiers?",
        "options":["a.no","b.yes","c.machine dependent","d.none of the mentioned"],
        "answer":"b",
        },
    {
        "question":"4. Which of the following is the correct extension of the Python file?",
        "options":["a) .python","b) .pl","c) .py","d) .p"],
        "answer":"c",
        },
    {
        "question":"5. Is Python code compiled or interpreted?",
        "options":["a) Python code is both compiled and interpreted","b) Python code is neither compiled nor interpreted","c) Python code is only compiled","d) Python code is only interpreted"],
        "answer":"a",
        },
    {
        "question":"6. All keywords in Python are in _________",
        "options":["a) Capitalized","b) lower case","c) UPPER CASE","d) None of the mentioned"],
        "answer":"d",
        },
   {
       "question":"7. What will be the value of the following Python expression? 4 + 3 % 5",
       "options":["a) 7","b) 2","c) 4","d) 1"],
       "answer":"d",
      },
    {
        "question":"8. Which of the following is used to define a block of code in Python language?",
        "options":["a) Indentation","b) Key","c) Brackets","d) All of the mentioned"],
        "answer":"a",            
        },
    {
        "question":"9. Which keyword is used for function in Python language?",
        "options":["a) Function","b) def","c) Fun","d) Define"],
        "answer":"b",
        },
    {
        "question":"10. Which of the following character is used to give single-line comments in Python?",
        "options":["a) //","b) #","c) !","d) /*"],
        "answer":"b",
        }]
##x = col.insert_many(questions)      
##print(x.inserted_ids)
questions=col.find({},{"question":1,"options":1,"answer":1})
score = 0
wrong = 0
y=["a,b,c,d"]
for i in questions:
    print(f"{i['question']}")
    for j in i["options"]:
        print(j)
    while True:
        a=str(input("Enter your answer:"))
        if a in y:
            break
        else:
             print("Please enter a valid option (a, b, c, or d)")
    if a == i["answer"]:
        score += 1
    else:
        wrong += 1
print(f"Your total score is:{score}|10.and the wrong answer is {wrong}")
##questions = col.find({}, {"question": 1, "options": 1, "answer": 1})
##score = 0
##wrong = 0
##
##valid_options = ["a", "b", "c", "d"]
##
##for i in questions:
##    print(f"{i['question']}")
##    for j in i["options"]:
##        print(j)
##    
##    while True:
##        a = input("Enter your answer: ").lower()
##        if a in valid_options:
##            break
##        else:
##            print("Please enter a valid option (a, b, c, or d)")
##
##    if a == i["answer"]:
##        score += 1
##    else:
####        print("Incorrect answer")
##        wrong += 1
##
##print(f"Your total score is: {score}/10, and the wrong answers are {wrong}")

   
