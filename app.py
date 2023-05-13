from flask import Flask, render_template, request, redirect

app = Flask(__name__)

Questions = [
                {
                    "Question": "What is the capital of France?", 
                    "Options":  ["Paris", "Berlin", "Madrid","Rome"],
                    "Answer": "Paris"
                },

                {
                    "Question": "What is the biggest planet in our solar system?",
                    "Options":["Mercury", "Venus", "Jupiter", "Mars"],
                    "Answer":"Jupiter"


                },
                
                {
                    "Question": "Who wrote the novel 'To kill a Mockingbird'? ",
                    "Options": ["Harper Lee", "Ernest Hemmingway", "F.Scott FLtzgerald", "Mark Twain"],
                    "Answer":"Harper Lee"
                },
                
                {
                    "Question": "Who painted the famous artwork 'The Starry Night'?",
                    "Options": ["Vincent van Gogh", "Pablo Picasso", "Claude Monet", "Leonardo da vinci"],
                    "Answer": "Vincent van Gogh" 
                },
                
                {
                    "Question": "What is the currency used in Japan?",
                    "Options": ["Yen", "Dollar", "Euro", "Pound"],
                    "Answer": "Yen"
                },
                
                {
                    "Question": "Who was the first president of the United States?",
                    "Options": ["George Washington", "Abraham Licoln", "Thomas Jefferson", "John F. Kennedy"],
                    "Answer": "George Washington"
                },
                
                {
                    "Question": "What's the formula of water",
                    "Options": ["H2O","CO2", "O2", "N2"],
                    "Answer": "H2O"
                },
                
                {
                    "Question": "What's is the name of the longest river in Africa",
                    "Options": ["Nile","Amazon", "Yangtze", "Mississipi"],
                    "Answer": "Nile"
                },
                
                {
                    "Question": "What is the highest mountain in the world",
                    "Options": ["Mount Everest", "Mount Kilimanjaro", "Mount Denali", "Mount Aconcagua"],
                    "Answer": "Mount Everest"
                },
                
                {
                    "Question": "Who composed the famous opera 'La Boheme' ",
                    "Options": ["Wolfgang Amadeus Mozart", "Ludwig van beethoven", "Giacomo Puccini", "Frederic Chopin"],
                    "Answer": "Giacomo Puccini"
                },
                
                {
                    "Question": "What is the capital of Australia",
                    "Options": ["Melbourne", "Perth", "Canberra", "Sydney"],
                    "Answer": "Canberra"
                },
                
                {
                    "Question": "Who wrote the novel 'Pride and Prejudice'",
                    "Options": ["Jane Austen", "Charlotte Bronte", "Louisa May Alcott", "Emily Dickinson"],
                    "Answer": "Jane Austen"
                },
                
                {
                    "Question": "What is the smallest country in the world",
                    "Options": ["Vatican City", "Monaco", "San marino", "Liechtenstein"],
                    "Answer": "Vatican City"
                },
                
                {
                    "Question": "Who was the first man to walk on the moon?",
                    "Options": ["Neil Armstrong", " Buzz Aldrin", "Yuri Gagarin", "Michael Collins"],
                    "Answer": "Neil Armstrong"
                },
                
                {
                    "Question": "What is the name of the first movie in the Star Wars franchise? ",
                    "Options": ["Star Wars: Episode I - The Phantom Menace","Star Wars: Episode IV - A New Hope", "Star Wars: Episode V - The Empire Strikes Back","Star Wars: Episode VI - Return of the Jedi"],
                    "Answer": "Star Wars: Episode IV - A new Hope"
                },
                
                {
                    "Question": "Who wrote the play 'Romeo and Juliet'?",
                    "Options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
                    "Answer": "William Shakespeare"
                },
                
                {
                    "Question": "Who wrote the novel 'The Great Gatsby'?",
                    "Options": ["F. Scott Fitzgerald","Ernest Hemingway"," William Faulkner","John Steinbeck"],
                    "Answer": "F. Scott Fitzgerald"
                },
                
                {
                    "Question": "What is the name of the biggest ocean in the world?",
                    "Options": ["Pacific Ocean","Atlantic Ocean","Indian Ocean","Artic Ocean"],
                    "Answer": "Pacific Ocean"
                },
                 
                {
                    "Question": "What is the capital of Germany?",
                    "Options": ["Berlin","Paris","London","Rome"],
                    "Answer": "Berlin"
                }, 
                
                {
                    "Question": "Who played the character 'Indiana Jones' in the movie series?",
                    "Options": ["Tom Cruise","Sean Connery","Nicolas Cage","Harrison Ford"],
                    "Answer": "Harrison Ford"
                }
            ]

marks = 0
total_questions = len(Questions) 
@app.get("/")
def index():
    return render_template("index.html")
marks = 0

@app.route("/quiz/Question<int:number>", methods=['GET', 'POST'])
def quiz(number):
    global total_questions
    if request.method == 'POST':
        user_value = request.form.get("answer")
        if user_value == Questions[number]["Answer"]:
            global marks
            marks += 1
            
        if number == total_questions - 1:
            return redirect("/result")
        else:
            return redirect("/quiz/Question" + str(number + 1))
    return render_template("quiz.html", number=int(number), question=Questions[number]["Question"], options=Questions[number]["Options"], total_questions=total_questions)



@app.get("/result")
def result():
    return render_template("result.html", result=marks)

@app.route("/restart")
def restart():
    global marks
    marks = 0
    return redirect("/")