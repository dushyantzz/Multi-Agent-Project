import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import Tool

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Ensure API keys are set
if not SERPER_API_KEY or not GOOGLE_API_KEY:
    raise ValueError("SERPER_API_KEY and GOOGLE_API_KEY must be set in .env file")

os.environ["SERPER_API_KEY"] = SERPER_API_KEY

search_tool = SerperDevTool()

def create_gemini_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.7
    )

researcher = Agent(
    role='Senior Researcher',
    goal='Uncover groundbreaking technologies in AI in healthcare',
    verbose=True,
    memory=True,
    backstory="Driven by curiosity, you're at the forefront of innovation.",
    tools=[Tool(name="Search", func=search_tool.run, description="Useful for searching the internet")],
    llm=create_gemini_llm(),
    allow_delegation=True
)

writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about AI in healthcare',
    verbose=True,
    memory=True,
    backstory="With a flair for simplifying complex topics, you craft engaging narratives.",
    tools=[Tool(name="Search", func=search_tool.run, description="Useful for searching the internet")],
    llm=create_gemini_llm(),
    allow_delegation=False
)

research_task = Task(
    description="Identify the next big trend in AI in healthcare. Focus on identifying pros and cons and the overall narrative.",
    expected_output="A comprehensive 3 paragraphs long report on the latest AI trends.",
    agent=researcher,
    tools=[Tool(name="Search", func=search_tool.run, description="Useful for searching the internet")]
)

write_task = Task(
    description="Compose an insightful article on the latest trends in AI in healthcare and how it's impacting the industry. This article should be easy to understand, engaging, and positive.",
    expected_output="A 4 paragraph article on AI in healthcare advancements formatted as markdown.",
    agent=writer,
    tools=[Tool(name="Search", func=search_tool.run, description="Useful for searching the internet")],
    async_execution=False,
    output_file="new-blog-post.md",
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    verbose=2 
)
result = crew.kickoff()
print(result)