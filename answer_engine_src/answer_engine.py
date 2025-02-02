from dataclasses import dataclass
from answer_engine_src.helpers import input_with_default
from answer_engine_src.llm_helpers import (
    get_chat_response,
    get_final_messages_for_answer_generation,
)
from answer_engine_src.retrieval import RetrievalEngine
from answer_engine_src.definitions import Article, RetrievalEngineResponse
from answer_engine_src.prompts import (
    ANSWER_GENERATION_CERVICAL_CANCER_PROMPT,
)
from pydantic import BaseModel


class Section(BaseModel):
    content: str
    citations: list[int]


class AnswerEngineResponseModel(BaseModel):
    answers: list[Section]


@dataclass
class AnswerEngineResponseWithArticles:
    articles: list[Article]
    answer_engine_response: AnswerEngineResponseModel


class AnswerEngine:
    def __init__(self):
        self.retriever = RetrievalEngine()
        self.relevant_article_num = 10

    def answer(self, query: str) -> AnswerEngineResponseModel:
        retrieval_engine_response: RetrievalEngineResponse = self.retriever.retrieve(
            query, n=self.relevant_article_num
        )

        print(
            "\n\n ###\nRetrieved articles:",
            "\n".join(
                [article.title for article in retrieval_engine_response.articles]
            ),
            "\n###\n\n",
        )

        final_messages = get_final_messages_for_answer_generation(
            query, retrieval_engine_response
        )
        answer_generation_prompt = (
            ANSWER_GENERATION_CERVICAL_CANCER_PROMPT + final_messages
        )
        kwargs = {"response_format": AnswerEngineResponseModel}

        print(
            "\n\n ###\nAnswer generation prompt:", answer_generation_prompt, "\n###\n\n"
        )
        response = get_chat_response(
            answer_generation_prompt, kwargs, structured_output=True
        )

        print(response)

        answer_engine_response = AnswerEngineResponseModel.parse_raw(response)

        return AnswerEngineResponseWithArticles(
            articles=retrieval_engine_response.articles,
            answer_engine_response=answer_engine_response,
        )


def main():
    answer_engine = AnswerEngine()
    query = input_with_default(
        "Enter a query to generate keywords", "What is the capital of North Korea?"
    )
    answer = answer_engine.answer(query)


if __name__ == "__main__":
    main()
