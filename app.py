import os
import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "aicompass.db")

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def serve_next_question(conn, session_id, current_score, questions_answered, total_requested, target_topic=None):
    if target_topic:
        row = conn.execute('SELECT * FROM quiz_questions WHERE topic = ? COLLATE NOCASE ORDER BY RANDOM() LIMIT 1', (target_topic,)).fetchone()
    else:
        row = conn.execute('SELECT * FROM quiz_questions ORDER BY RANDOM() LIMIT 1').fetchone()

    if not row:
        return "I couldn't find any questions matching your request right now.", None

    bot_response = (
        f"Topic: {str(row['topic']).title()}\n\n"
        f"Question {questions_answered + 1} of {total_requested}: {row['question']}\n\n"
        f"1. {row['option_1']}\n"
        f"2. {row['option_2']}\n"
        f"3. {row['option_3']}\n"
        f"4. {row['option_4']}\n\n"
        f"Reply with 1, 2, 3, or 4!"
    )

    context_payload = {
        "name": f"{session_id}/contexts/quiz-state",
        "lifespanCount": 5,
        "parameters": {
            "current_q_id": str(row['id']),
            "correct_answer": str(row['answer']).strip(),
            "current_score": str(current_score),
            "questions_answered": str(questions_answered),
            "total_requested": str(total_requested),
            "target_topic": str(target_topic) if target_topic else ""
        }
    }
    return bot_response, context_payload

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def api_chat():
    user_text = request.json.get('message')
    session_id = request.json.get('session_id', 'demo-session-123')
    project_id = os.environ.get('DIALOGFLOW_PROJECT_ID')

    fallback_msg = "I didn't quite catch that. Try checking the guide on the side for examples, like asking for a definition or a quiz!"

    if not project_id:
         return jsonify({"reply": fallback_msg})

    try:
        from google.cloud import dialogflow
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(project_id, session_id)
        
        text_input = dialogflow.TextInput(text=user_text, language_code="en")
        query_input = dialogflow.QueryInput(text=text_input)
        
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        
        bot_reply = response.query_result.fulfillment_text
        if not bot_reply and len(response.query_result.fulfillment_messages) > 0:
            try:
                bot_reply = response.query_result.fulfillment_messages[0].text.text[0]
            except Exception:
                pass
                
        if not bot_reply or bot_reply.strip() == "":
            bot_reply = fallback_msg
            
        return jsonify({"reply": bot_reply})
        
    except Exception:
        return jsonify({"reply": fallback_msg})

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    try:
        query_result = req.get('queryResult')
        intent_name = query_result.get('intent').get('displayName')
        session_id = req.get('session')
        parameters = query_result.get('parameters', {})
        output_contexts = query_result.get('outputContexts', [])
    except AttributeError:
        return jsonify({"fulfillmentText": "I didn't quite catch that. Try checking the guide on the side for examples, like asking for a definition or a quiz!"})
    
    conn = get_db_connection()
    bot_response = "I didn't quite catch that. Try checking the guide on the side for examples, like asking for a definition or a quiz!"
    out_contexts_response = []

    if intent_name == 'Default Welcome Intent':
        bot_response = "Welcome to AICompass! Want to learn definitions, hear fun facts, or start a quiz?"

    elif intent_name == 'module.dictionary':
        requested_topic = parameters.get('ai_topic')
        if requested_topic:
            row = conn.execute('SELECT definition FROM definitions WHERE topic = ? COLLATE NOCASE', (requested_topic,)).fetchone()
            if row:
                bot_response = f"Topic: {str(requested_topic).title()}\n\nDefinition: {row['definition']}\n\n(Ask for an example if you want to know more!)"
            else:
                bot_response = f"I know you are asking about {requested_topic}, but I don't have that in my database yet!"
        else:
            bot_response = "I missed that. What topic do you want me to define?"

    elif intent_name == 'module.dictionary.example':
        requested_topic = None
        for context in output_contexts:
            if 'parameters' in context and 'ai_topic' in context['parameters']:
                requested_topic = context['parameters']['ai_topic']
                break
        if requested_topic:
            row = conn.execute('SELECT example FROM definitions WHERE topic = ? COLLATE NOCASE', (requested_topic,)).fetchone()
            if row and row['example']:
                bot_response = f"Topic: {str(requested_topic).title()}\n\nExample: {row['example']}"
            else:
                bot_response = f"I don't have a specific example for {requested_topic} written down yet."
        else:
            bot_response = "I forgot what we were talking about! What topic did you want an example for?"

    elif intent_name == 'module.funfact':
        row = conn.execute('SELECT * FROM funfacts ORDER BY RANDOM() LIMIT 1').fetchone()
        if row:
            bot_response = f"Topic: {str(row['topic']).title()}\n\n💡 Fun Fact: {row['fun_fact']}"

    elif intent_name == 'module.quiz.start':
        target_topic = parameters.get('ai_topic')
        num_questions_raw = parameters.get('number')
        
        total_requested = 1
        if num_questions_raw:
            try:
                total_requested = int(float(num_questions_raw))
            except (ValueError, TypeError):
                total_requested = 1

        bot_response, new_context = serve_next_question(conn, session_id, 0, 0, total_requested, target_topic)
        if new_context:
            out_contexts_response.append(new_context)

    elif intent_name == 'module.quiz.answer':
        user_answer = str(parameters.get('quiz_choice', '')).strip()
        
        quiz_state = None
        for ctx in output_contexts:
            if ctx.get('name', '').endswith('/contexts/quiz-state'):
                quiz_state = ctx.get('parameters', {})
                break
                
        if quiz_state:
            current_q_id = int(float(quiz_state.get('current_q_id', 0)))
            correct_ans = str(quiz_state.get('correct_answer', '')).strip()
            score = int(float(quiz_state.get('current_score', 0)))
            answered_count = int(float(quiz_state.get('questions_answered', 0))) + 1
            total_needed = int(float(quiz_state.get('total_requested', 1)))
            saved_topic = quiz_state.get('target_topic')
            
            q_row = conn.execute('SELECT topic, explanation FROM quiz_questions WHERE id = ?', (current_q_id,)).fetchone()
            explanation = q_row['explanation'] if q_row else "No explanation available."
            topic_title = str(q_row['topic']).title() if q_row else "Quiz"
            
            if user_answer == correct_ans:
                score += 1
                feedback = "Correct!"
            else:
                feedback = f"Incorrect. The correct choice was option {correct_ans}."
                
            feedback_payload = f"Topic: {topic_title}\n\n{feedback}\n\nExplanation: {explanation}\n\n──────────────\n\n"
            
            if answered_count < total_needed:
                next_text, next_context = serve_next_question(conn, session_id, score, answered_count, total_needed, saved_topic)
                bot_response = feedback_payload + next_text
                if next_context:
                    out_contexts_response.append(next_context)
            else:
                bot_response = f"{feedback_payload}🏁 Quiz complete! Final Score: {score}/{total_needed}."
                out_contexts_response.append({"name": f"{session_id}/contexts/quiz-state", "lifespanCount": 0})
        else:
            bot_response = "I don't see an active quiz currently open. Type 'start quiz' to test your skills!"

    conn.close()

    json_response = {"fulfillmentText": bot_response}
    if out_contexts_response:
        json_response["outputContexts"] = out_contexts_response

    return jsonify(json_response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)