from answer_engine_src.helpers import input_with_default
from answer_engine_src.llm_helpers import get_chat_response
from answer_engine_src.prompts import KEYWORD_GENERATION_PROMPT
from pydantic import BaseModel


class KeywordResponse(BaseModel):
    keywords: list[str]


class KeywordGenerator:
    def __init__(self, prompt_template=KEYWORD_GENERATION_PROMPT):
        self.prompt_template = prompt_template

    def generate_keywords(self, query) -> KeywordResponse:
        """
        Generates a list of keywords from a given raw query.
        """
        message = self.prompt_template.format(query=query)
        kwargs = {"response_format": KeywordResponse}
        response = get_chat_response(message, kwargs, structured_output=True)

        return KeywordResponse.parse_raw(response)


def main():
    keyword_generator = KeywordGenerator()
    query = input_with_default(
        "Enter a query to generate keywords", "What is the capital of North Korea?"
    )
    keywords = keyword_generator.generate_keywords(query)

    print(keywords.keywords)


if __name__ == "__main__":
    main()
