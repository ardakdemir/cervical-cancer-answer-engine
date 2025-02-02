from ast import literal_eval
import nltk
from nltk.tokenize import sent_tokenize
import pandas as pd
from answer_engine_src.definitions import Article


# Add this at the top of the file to ensure the required NLTK data is downloaded
nltk.download("punkt")


CERVICAL_CANCER_FIELD_MAP = {
    "date": "publication_date",
    "url": "open_access.oa_url",
    "title": "title",
    "topic": "primary_topic.display_name",
    "article_name": "title",
    "article_contents_sources": ["abstract", "title"],
}


def split_text_to_sentences(text: str) -> list[str]:
    """
    Splits text into sentences using NLTK sentence tokenizer.
    """
    if not text:
        return []
    return sent_tokenize(text)


def get_article_contents_cervical_cancer(row: pd.Series) -> list[str]:
    """
    Parses a row from a dataframe into an Article object and splits contents into sentences.
    """
    article_sections = [row["abstract"], row["title"]]

    # Split each section into sentences and flatten the list
    sentences = []
    for section in article_sections:
        if section:
            sentences.extend(split_text_to_sentences(section))
    return sentences


def parse_row_to_article(df, index) -> Article:
    """
    Parses a row from a dataframe into an Article object.
    """
    row = df.iloc[index]
    article_contents = literal_eval(row["article_contents"])
    article = Article(
        date=row["date"],
        url=row["url"],
        title=row["title"],
        topic=row["topic"],
        article_contents=article_contents,
        article_name=row["article_name"],
    )
    return article


def df_to_article_list(df) -> list[Article]:
    """
    Converts a dataframe into a list of Article objects.
    """
    articles = []
    for i in range(len(df)):
        article = parse_row_to_article(df, i)
        articles.append(article)
    return articles


def input_with_default(prompt, default):
    user_input = input(f"{prompt} (default: {default}): ")
    return user_input if user_input else default
