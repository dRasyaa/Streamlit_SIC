from google import genai
import streamlit as st

api_key = "AIzaSyA_n6oSH74ywNbLIXBSSMbxZVuJjbyediM"

client = genai.Client(api_key=api_key)

def get_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return response.text