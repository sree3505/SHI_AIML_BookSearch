import os
from openai import OpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

class openai_helper:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def get_llm_response(self,json_data):
        prompt = f"""
                ### JSON Document from OpenLibrary:
                {json_data}
                ### INSTRUCTION:
                The JSON list is the book search result from openlibrary search api.
                Your job is to to summerize the list and provide relavent information about book for a user`.
                Only return the valid JSON.
                ### VALID JSON (NO PREAMBLE):
                """

        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful but terse AI assistant who gets straight to the point.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
        )
        response = completion.choices[0].message.content
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(response)
            return res
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse response from llm.")
