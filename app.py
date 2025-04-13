from flask import Flask, render_template, request, session, redirect, url_for
import random
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key for session management

# Route to serve the quiz page
@app.route('/')
def index():
    # Reset session data when starting a new quiz
    session.clear()
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    # Get the number of questions from the form
    question_count = request.args.get('question_count', 10, type=int)
    
    # Validate question count (between 5 and 30)
    if question_count < 5:
        question_count = 5
    elif question_count > 30:
        question_count = 30
    
    # Initialize session data if not already set
    if 'questions' not in session:
        # Get all questions from the questions.py file
        from questions import quiz_data
        
        # Shuffle and select the specified number of questions
        shuffled_questions = random.sample(quiz_data, min(question_count, len(quiz_data)))
        session['questions'] = shuffled_questions
        session['current_question'] = 0
        session['correct'] = 0
        session['incorrect'] = 0
        session['wrong_answers'] = []
        session['start_time'] = datetime.now().timestamp()
    
    # Check if we've reached the end of the quiz
    if session['current_question'] >= len(session['questions']):
        return redirect(url_for('results'))
    
    # Get the current question
    question_data = session['questions'][session['current_question']]
    
    return render_template('quiz.html', 
                          question=question_data,
                          question_number=session['current_question'] + 1,
                          total_questions=len(session['questions']))

@app.route('/submit', methods=['POST'])
def submit():
    # Get the user's answer
    user_answer = request.form.get('answer')
    
    # If no answer was selected, redirect back to the quiz
    if not user_answer:
        return redirect(url_for('quiz'))
    
    # Get the current question
    question_data = session['questions'][session['current_question']]
    
    # Check if the answer is correct
    if user_answer == question_data['correct']:
        session['correct'] = session.get('correct', 0) + 1
    else:
        session['incorrect'] = session.get('incorrect', 0) + 1
        # Store wrong answer information
        session['wrong_answers'].append({
            'question': question_data['question'],
            'user_answer': user_answer,
            'user_option': question_data[user_answer],
            'correct_answer': question_data['correct'],
            'correct_option': question_data[question_data['correct']],
            'explanation': question_data['explanation']
        })
    
    # Move to the next question
    session['current_question'] = session.get('current_question', 0) + 1
    
    # Redirect to the next question or results
    return redirect(url_for('quiz'))

@app.route('/timeout', methods=['POST'])
def timeout():
    # Get the current question
    if 'current_question' in session and session['current_question'] < len(session['questions']):
        question_data = session['questions'][session['current_question']]
        
        # Mark as incorrect due to timeout
        session['incorrect'] = session.get('incorrect', 0) + 1
        session['wrong_answers'].append({
            'question': question_data['question'],
            'user_answer': 'timeout',
            'user_option': 'Time expired',
            'correct_answer': question_data['correct'],
            'correct_option': question_data[question_data['correct']],
            'explanation': question_data['explanation']
        })
        
        # Move to the next question
        session['current_question'] = session.get('current_question', 0) + 1
    
    return redirect(url_for('quiz'))

@app.route('/results')
def results():
    # Calculate score
    correct = session.get('correct', 0)
    total = len(session.get('questions', []))
    wrong_answers = session.get('wrong_answers', [])
    
    # Calculate percentage
    percentage = (correct / total * 100) if total > 0 else 0
    
    return render_template('results.html', 
                          correct=correct, 
                          total=total, 
                          percentage=percentage,
                          wrong_answers=wrong_answers)

if __name__ == '__main__':
    app.run(debug=True)
