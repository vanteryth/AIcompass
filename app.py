import os
import sqlite3
import uuid
from flask import Flask, request, jsonify, render_template
from google.cloud import dialogflow_v2 as dialogflow

app = Flask(__name__)
app.secret_key = os.urandom(24)

PROJECT_ID = os.getenv("DIALOGFLOW_PROJECT_ID", "your-project-id")
SESSION_ID = str(uuid.uuid4())

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    text = data.get('message', '')
    
    if not text:
        return jsonify({"reply": "I didn't quite catch that. Try checking the guide on the side for examples, like asking for a definition or a quiz!"})

    try:
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(PROJECT_ID, SESSION_ID)
        text_input = dialogflow.TextInput(text=text, language_code="en-US")
        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        reply = response.query_result.fulfillment_text
        
        if not reply:
            reply = "I didn't quite catch that. Try checking the guide on the side for examples, like asking for a definition or a quiz!"
            
        return jsonify({"reply": reply})
    
    except Exception:
        return jsonify({"reply": "I didn't quite catch that. Try checking the guide on the side for examples, like asking for a definition or a quiz!"})

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent_name = req.get('queryResult', {}).get('intent', {}).get('displayName')
    parameters = req.get('queryResult', {}).get('parameters', {})
    
    reply_text = req.get('queryResult', {}).get('fulfillmentText', "I didn't quite catch that. Try checking the guide on the side for examples, like asking for a definition or a quiz!")

    if intent_name == 'Get Definition':
        topic = parameters.get('topic')
        if topic:
            conn = get_db_connection()
            row = conn.execute("SELECT definition FROM topics WHERE name = ?", (topic.lower(),)).fetchone()
            conn.close()
            if row:
                reply_text = f"Topic: {topic.title()}\n\nDefinition: {row['definition']}\n\n(Ask for an example if you want to know more!)"
            else:
                reply_text = f"I know you are asking about {topic}, but I don't have that in my database yet!"
        else:
            reply_text = "I missed that. What topic do you want me to define?"

    elif intent_name == 'Get Example':
        topic = None
        for ctx in req.get('queryResult', {}).get('outputContexts', []):
            if 'topic' in ctx.get('parameters', {}):
                topic = ctx['parameters']['topic']
                break
                
        if topic:
            conn = get_db_connection()
            row = conn.execute("SELECT example FROM topics WHERE name = ?", (topic.lower(),)).fetchone()
            conn.close()
            if row:
                reply_text = f"Topic: {topic.title()}\n\nExample: {row['example']}"
            else:
                reply_text = f"I don't have an example for {topic} yet!"
        else:
            reply_text = "I forgot what we were talking about! What topic did you want an example for?"

    elif intent_name == 'Fun Fact':
        conn = get_db_connection()
        row = conn.execute("SELECT name, fact FROM topics ORDER BY RANDOM() LIMIT 1").fetchone()
        conn.close()
        if row:
            reply_text = f"💡 Fun Fact ({row['name'].title()}): {row['fact']}"
        else:
            reply_text = "I don't have any fun facts right now!"

    elif intent_name == 'Start Quiz':
        num_questions = parameters.get('number', 1)
        if isinstance(num_questions, (int, float)):
            num_questions = int(num_questions)
        elif isinstance(num_questions, str) and num_questions.isdigit():
            num_questions = int(num_questions)
        else:
            num_questions = 1
            
        reply_text = f"Starting a {num_questions}-question quiz. Good luck!"

    return jsonify({"fulfillmentText": reply_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)