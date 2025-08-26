from flask import Flask, render_template_string, request, session
import json
import os
import random

app = Flask(__name__)
app.secret_key = os.urandom(32).hex() # just for local use

MIN_DIFFICULTY = 3
MAX_DIFFICULTY = 5

# Read in tossups from tossups.json file
with open('tossups.json', encoding='utf8') as tossup_file:
    question_lines = tossup_file.readlines()

tossups = []
for question_line in question_lines:
    question = json.loads(question_line)
    difficulty = int(question['difficulty']['$numberInt'])
    if MIN_DIFFICULTY <= difficulty <= MAX_DIFFICULTY:
        tossups.append(question)

categories = ['History','Literature','Science','Fine Arts','Religion','Mythology','Philosophy','Social Science','Current Events','Geography','Other Academic','Trash']
tossups_per_category = [[] for _ in range(len(categories))]
for tossup in tossups:
    category = tossup['category']
    tossups_per_category[categories.index(category)].append(tossup)

popularity_of_categories = []
with open('category_weights.cfg') as category_weights_file:
    for line in category_weights_file:
        popularity = int(line.split('=')[1])
        popularity_of_categories.append(popularity)

def get_random_tossup():
    random_category = random.choices(categories, weights=popularity_of_categories)[0]
    tossup = random.choice(tossups_per_category[categories.index(random_category)])
    print(tossup) #TODO
    return {
        'category': random_category,
        'difficulty': tossup['difficulty']['$numberInt'],
        'year': tossup['set']['year']['$numberInt'],
        'question': tossup['question_sanitized'],
        'answer': tossup['answer_sanitized']
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'history' not in session:
        session['history'] = []
    history = session['history']

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'show':
            question = {
                'category': request.form['category'],
                'difficulty': request.form['difficulty'],
                'year': request.form['year'],
                'question': request.form['question'],
                'answer': request.form['answer']
            }
            show_answer = True
        elif action == 'next':
            # add the just-answered question to history
            history.append({
                'category': request.form['category'],
                'difficulty': request.form['difficulty'],
                'year': request.form['year'],
                'question': request.form['question'],
                'answer': request.form['answer']
            })
            session['history'] = history
            question = get_random_tossup()
            show_answer = False
        else:
            question = get_random_tossup()
            show_answer = False
    else:
        question = get_random_tossup()
        show_answer = False

    return render_template_string('''
    <html>
    <head>
        <title>Quiz Bowl</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 700px; margin: auto; }
            .question { font-size: 1.15em; margin-bottom: 20px; }
            .answer { color: green; font-weight: bold; margin-top: 10px; }
            .meta { color: #555; margin-bottom: 10px; font-size: 0.9em; }
            ol { padding-left: 20px; }
            li { margin-bottom: 16px; }
            .prev-question { font-size: 0.95em; }
            button { padding: 10px 20px; font-size: 1em; cursor: pointer; }
            hr { margin: 40px 0 20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="meta">Category: {{ question.category }} | Difficulty: {{ question.difficulty }} | Year: {{ question.year }}</div>
            <div class="question">{{ question.question }}</div>
            <form method="post">
                <input type="hidden" name="category" value="{{ question.category }}">
                <input type="hidden" name="difficulty" value="{{ question.difficulty }}">
                <input type="hidden" name="year" value="{{ question.year }}">
                <input type="hidden" name="question" value="{{ question.question }}">
                <input type="hidden" name="answer" value="{{ question.answer }}">
                {% if show_answer %}
                    <div class="answer">ANSWER: {{ question.answer }}</div>
                    <button type="submit" name="action" value="next">Next Question</button>
                {% else %}
                    <button type="submit" name="action" value="show">Show Answer</button>
                {% endif %}
            </form>

            {% if history %}
                <hr>
                <h3>Previous Questions</h3>
                <ol>
                {% for q in history %}
                    <li class="prev-question">
                        <div class="meta">{{ q.year }} | {{ q.category }} ({{ q.difficulty }})</div>
                        <div>{{ q.question }}</div>
                        <div class="answer">ANSWER: {{ q.answer }}</div>
                    </li>
                {% endfor %}
                </ol>
            {% endif %}
        </div>
    </body>
    </html>
    ''', question=question, show_answer=show_answer, history=history)

if __name__ == '__main__':
    app.run(debug=True)
