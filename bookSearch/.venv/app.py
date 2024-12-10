from flask import Flask, render_template, request
from open_library import search_api
from llm_chatgroq import chatgroq
from llm_openai import  openai_helper

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/books/<string:title>")
def api_getbooks(title):
    limit = request.args.get('limit')
    #Call Open Library Search API
    openLib = search_api()
    bookResults = openLib.call_bookapi(title, limit)
    #Invoke Groq cloud using LangChain
    llm = chatgroq()
    resp = llm.summerize_bookresults(bookResults)
    #Call OpenAI Model
    #llm = openai_helper()
    #resp = llm.get_llm_response(bookResults)
    return resp
