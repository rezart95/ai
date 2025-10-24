import os
from dotenv import load_dotenv
from typing import Annotated, TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# useful to generate sql query
model_low_temp = ChatOpenAI(temperature=0.1, api_key=openai_api_key)

# useful to generate natural language
model_high_temp = ChatOpenAI(temperature=0.7, api_key=openai_api_key)


class State(TypedDict):
    # to track conversation history
    message: Annotated[list, add_messages]
    # input
    user_query: str
    # output
    sql_query: str
    sql_explanation: str


class Input(TypedDict):
    user_query: str


class Output(TypedDict):
    sql_query: str
    sql_explanation: str


generate_prompt = SystemMessage(
    """You are a helpful data analyst who generates SQL queries for users based 
    on their questions."""
)


def generate_sql(state: State) -> State:
    user_message = HumanMessage(state["user_query"])
    messages = [generate_prompt, *state["messages"], user_message]
    res = model_low_temp.invoke(messages)
    return {
        "sql_query": res.content,
        # update conversation history
        "messages": [user_message, res],
    }


explain_prompt = SystemMessage(
    "You are a helpful data analyst who explains SQL queries to users."
)


def explain_sql(state: State) -> State:
    messages = [
        explain_prompt,
        # contains user's query and SQL query from previous step
        *state["messages"],
    ]
    res = model_high_temp.invoke(messages)
    return {
        "sql_explanation": res.content,
        # update conversation history
        "messages": res,
    }


builder = StateGraph(State, input_schema=Input, output_schema=Output)
builder.add_node("generate_sql", generate_sql)
builder.add_node("explain_sql", explain_sql)
builder.add_edge(START, "generate_sql")
builder.add_edge("generate_sql", "explain_sql")
builder.add_edge("explain_sql", END)

graph = builder.compile()
