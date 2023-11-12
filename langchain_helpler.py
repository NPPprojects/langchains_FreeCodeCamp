from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()



def generate_oil_info(oil_type, count):
    llm = openai.OpenAI(temperature=0.5)
    prompt_template_name = PromptTemplate(
        input_variables=['oil_type',"count"],
        template="I have {oil_type} oil and want to learn more about it. List {count} of its properties"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="output")

    response = name_chain({'oil_type': oil_type, "count": count})
    return response

def Test():
    return "Hello World"


if __name__ == "__main__":
    print(Test())
    print(generate_oil_info("Synthetic blend",5))
    
