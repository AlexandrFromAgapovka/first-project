from dotenv import load_dotenv
import os

load_dotenv()           # загружаем переменные из .env

def print_author():
    author = os.getenv("AUTHOR")    # читаем значение переменной AUTHOR
    print(f"Автор проекта: {author}")

print_author()
