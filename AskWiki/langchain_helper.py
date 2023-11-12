from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv
import requests


# Load environment variables
load_dotenv()

def fetch_wiki_content(page_link):
    try:
        response = requests.get(page_link, verify=True)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def langchain_agent(agentInstructions, pageLink):
    # Initialize the language model
    llm = openai.OpenAI(temperature=0.5)

    # Load required tools
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    # Create a prompt template with the correct variable names
    prompt_template = PromptTemplate(
        input_variables=['pageLink', 'agentInstructions'],
        template="Absorb the information on this wikipage: {pageLink} " + "{agentInstructions}"
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="output")

    chain_response  = name_chain({'pageLink': pageLink, "agentInstructions": agentInstructions})
    # Initialize the agent
    agent = initialize_agent(llm=llm, tools=tools, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    agent_input = {"input": chain_response }
    # Run the agent with the prompt template
    result = agent.run(agent_input)
    
    return result

if __name__ == "__main__":
    # Test the function with a specific instruction and a Wikipedia page
    print(langchain_agent("What food do they eat?", "https://en.wikipedia.org/wiki/Farm_cat"))

