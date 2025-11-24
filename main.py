import os
from dotenv import load_dotenv
import google.generativeai as genai
from pydantic_ai import Agent 
from tools import list_files, create_text_file, move_file, delete_file
from logger import logger



load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)
# Now here we give tools to agent
agent = Agent(
    "google-gla:gemini-2.5-flash",
    system_prompt="You are a file Management AI. only Manage files inside this current directory safely.",
    tools=[list_files, create_text_file, move_file, delete_file],
)

if __name__ == "__main__":
    logger.info("Agent is started!")
    print("file management Agent is started! (type 'exit' to quit )\n")

    while True:
        
        user_input = input("You: ")
        if user_input.lower() in ["exit" , "quit"]:
            logger.info("Agent is stopped!")
            break

        result = agent.run_sync(user_input)
        print("Agent : " , result.output)



