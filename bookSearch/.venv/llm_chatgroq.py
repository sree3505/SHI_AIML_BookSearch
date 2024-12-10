import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

class chatgroq:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def summerize_bookresults(self, text_request):
        prompt_extract = PromptTemplate.from_template(
            """
            ### JSON Document from OpenLibrary:
            {json_data}
            ### INSTRUCTION:
            The JSON list is the book search result from openlibrary search api.
            Your job is to to summerize the list and provide relavent information about book for a user`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"json_data": text_request})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
            return res
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse response from llm.")