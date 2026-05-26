from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Create Groq client
client = Groq(
    api_key=api_key
)

# Generate HR recommendation
def generate_hr_recommendation(employee_data, risk, probability):

    prompt = f"""
    You are an expert HR strategist.

    Analyze this employee attrition prediction.

    Employee Data:
    {employee_data}

    Attrition Risk:
    {risk}

    Probability of Leaving:
    {probability:.2f}%

    Generate:
    1. Attrition analysis
    2. Main risk factors
    3. HR recommendations
    4. Retention strategies

    Keep response concise and professional.
    """

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Groq API Error: {str(e)}"