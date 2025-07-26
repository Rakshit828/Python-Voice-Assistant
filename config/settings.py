from dotenv import load_dotenv
import os


load_dotenv()  # Loads from .env in root directory

WEATHER_API_KEY = os.getenv("WEATHER_API_SHRIJAN")
GROQ_API_KEY = os.getenv('GROQ_API')
DEEPSEEK_V3_0324_API_KEY = os.getenv('DEEPSEEK_V3_0324')
DEEPSEEK_R1_API_KEY = os.getenv("DEEEPSEEK R1")

NEWS_API_KEY = os.getenv("NEWS_API")

