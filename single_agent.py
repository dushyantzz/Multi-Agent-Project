import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import Tool

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  

search_tool = SerperDevTool(api_key=SERPER_API_KEY)

def create_research_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.7,
        convert_system_message_to_human=True
    )
    
    tools = [
        Tool(
            name="Search",
            func=search_tool.run,
            description="Useful for searching information on the internet"
        )
    ]
  
    return Agent(
        role="Research Specialist",
        goal="Conduct thorough research on given topics",
        backstory="You are an experienced researcher with expertise in finding and synthesizing information from various sources",
        verbose=True,
        allow_delegation=False,
        tools=tools,
        llm=llm
    )

def create_research_task(agent, topic):
    return Task(
        description=f"Research the following topic and provide a comprehensive summary: {topic}",
        agent=agent,
        expected_output = "A detailed summary of the research findings, including key points and insights related to the topic"
    )

def run_research(topic):
    agent = create_research_agent()
    task = create_research_task(agent, topic)

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=2
    )
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    print("Welcome to the Research Agent!")
    topic = input("Enter the research topic: ")
    result = run_research(topic)
    print("\nResearch Result:")
    print(result)