from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are an intelligent content extractor.\n"
    "Your task is to extract information **only** relevant to the following user query:\n\n"
    "Query: {parse_description}\n\n"
    "From the provided main website content below:\n\n"
    "{dom_content}\n\n"
    "### Instructions:\n"
    "1. Only return information that matches the query.\n"
    "2. Be concise. No explanations or extra text.\n"
    "3. If nothing matches, return an empty string ('').\n"
)

model = OllamaLLM(model="deepseek-r1:1.5b")#deepseek-r1:1.5b#llama3.1

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    
    parsed_results = []
    
    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)
        
    return "\n".join(parsed_results)    