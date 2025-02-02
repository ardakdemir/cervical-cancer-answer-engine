import os
from answer_engine_src.definitions import RetrievalEngineResponse
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

api_key = os.environ.get("openai_api_key")
client = OpenAI(api_key=api_key or st.secrets["OPENAI_API_KEY"])


client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key,
)


def get_final_messages_for_answer_generation(
    query: str, articles: RetrievalEngineResponse
) -> list[dict[str, str]]:

    articles_str = ""
    for i, article in enumerate(articles.articles):
        articles_str += (
            f"Article [{i+1}]\n**{article.title}**\n{article.article_contents}\n\n"
        )
    final_messages = [
        {
            "role": "user",
            "content": f"""
        ### Relevant Articles

        {articles_str}

        ### End of Relevant Articles
    """,
        },
        {"role": "user", "content": f"Here is the query: {query}"},
        {
            "role": "user",
            "content": "Refuse to give an answer if the query is not about North Korea.",
        },
    ]

    return final_messages


def get_chat_response(
    message: str | list[dict[str, str]],
    kwargs: dict = None,
    structured_output: bool = False,
) -> str:

    kwargs = kwargs or {}

    if isinstance(message, str):
        messages = [
            {
                "role": "user",
                "content": message,
            }
        ]
    elif isinstance(message, list) and all(isinstance(item, dict) for item in message):
        messages = message
    else:
        raise ValueError("message must be a string or a list of dictionaries")

    kwargs.update({"model": "gpt-4o-mini", "messages": messages})
    if structured_output:
        chat_completion = client.beta.chat.completions.parse(**kwargs)
    else:
        chat_completion = client.chat.completions.create(**kwargs)

    return chat_completion.choices[0].message.content


def main():
    message = input("Say something to ChatGpt: ")
    response = get_chat_response(message)
    print(response)


if __name__ == "__main__":
    main()
