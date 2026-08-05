import os

try:
    from groq import Groq
except ImportError:  # pragma: no cover - runtime fallback
    Groq = None

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - runtime fallback
    def load_dotenv():
        return False

# Load environment variables
load_dotenv()

# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")
client = None

if Groq and api_key:
    client = Groq(api_key=api_key)

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

    if client is None:
        return (
            "AI recommendations are unavailable right now, so here is a practical fallback: "
            f"{risk} employees should be reviewed for workload balance, recognition, and career growth. "
            f"Focus on improving satisfaction, reducing overtime, and offering targeted retention support."
        )

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
        return f"Groq API Error: {str(e)}"# Updated 2026-08-05 for GitHub timestamp refresh
