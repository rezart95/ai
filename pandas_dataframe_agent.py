from sklearn.datasets import load_iris
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")


df = load_iris(as_frame=True)["data"]
df.to_csv("iris.csv", index=False)

chat = ChatOpenAI(
    model="gpt-4o-mini", api_key=openai_api_key, max_completion_tokens=1000
)


PROMPT = (
    "If you do not know the answer, say you don't know.\n"
    "Think step by step.\n"
    "\n"
    "Below is the query.\n"
    "Query: {query}\n"
)

prompt = PromptTemplate(template=PROMPT, input_variables=["query"])


agent = create_pandas_dataframe_agent(chat, df, verbose=True, allow_dangerous_code=True)

agent.run(prompt.format(query="What's this dataset about?"))

# agent.run(prompt.format(query="Which row has the biggest difference between petal length and petal width"))

# agent.run(prompt.format(query="Show the distributions for each column visually!"))
