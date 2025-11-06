from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from data import text_data

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY", None)
if API_KEY is None:
    print("ERROR: GEMINI_API_KEY not set in .env file")
    exit(1)

client = genai.Client(api_key=API_KEY)
DEFAULT_MODEL = "gemini-2.0-flash"

config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0)
)

app = Flask(__name__, template_folder=".")
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        query = data.get("query") or data.get("prompt") or data.get("text")
        
        if not query:
            return jsonify({"answer": "Please enter a question."}), 400

        print(f"\n Processing query: {query}")
        
        system_prompt = """You are a helpful chatbot that answers questions based on provided context documents.
        
Instructions:
- Be friendly and welcoming. If someone greets you (like "Hi", "Hello", etc), respond warmly
- Answer questions factually based on the provided context
- Do NOT mention the context documents in your answer
- For general greetings or chitchat, respond naturally and warmly
- If a question is too vague or unrelated to the documents, respond with 'I'm here to help with questions about the provided documents. What would you like to know?'
- If the context doesn't contain the answer, respond with 'I don't have enough information to answer this question. Please ask in person for more details.'
- Keep answers concise and helpful"""


 
        full_prompt = f"""{system_prompt}

CONTEXT DOCUMENTS:
{text_data}

USER QUESTION:
{query}"""
        
        
        print("Calling Gemini API...")
        response = client.models.generate_content(
            model=DEFAULT_MODEL,
            contents=[full_prompt],
            config=config,
        )
        
        reply = getattr(response, "text", None)
        if reply is None:
            reply = "No response from model"
        
        print(f"✓ Response generated\n")
        return jsonify({"answer": str(reply).strip()}), 200
        
    except Exception as e:
        print(f"❌ Error: {str(e)}\n")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("\n" + "="*60)
    print("STARTING FLASK SERVER")
    print("="*60)
    print("✓ Open http://127.0.0.1:3000 in your browser\n")
    app.run(host="127.0.0.1", port=3000, debug=True)

