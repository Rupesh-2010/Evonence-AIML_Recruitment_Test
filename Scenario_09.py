# Scenario 9: Structured Response Generation
# Task: Use the Gemini API to generate a response in JSON format for the query:
#     "List 3 benefits of Python for data science."
# Handle cases where the response isn’t valid JSON.


import google.generativeai as genai      # Google Gemini API library
import json                             # JSON handling tools (JavaScript Object Notation)

genai.configure(api_key='your_api_key_here')        # Enter your Gemini API key

model = genai.GenerativeModel('gemini-1.5-flash')   # Load the Gemini model (Version- gemini-1.5-flash)

def generate_structured_response(query):

    # Ask Gemini to reply only in JSON
    prompt = f"Respond to the query in valid JSON format: {query}"

    try:
        response = model.generate_content(prompt)  # Get AI response
        json_response = json.loads(response.text)        # Convert text to JSON
        return json_response
    except (json.JSONDecodeError, ValueError):
    
        return {"error": "Invalid JSON response", "query": query}    # If response is not valid JSON

# Test the function
query = "List 3 benefits of Python for data science."
result = generate_structured_response(query)

print(result)   # Print final structured response of code.

