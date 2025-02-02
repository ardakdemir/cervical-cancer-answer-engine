from dataclasses import dataclass


@dataclass
class Article:
    date: str
    url: str
    title: str
    topic: str
    article_contents: list[str]
    article_name: str


@dataclass
class RetrievalEngineResponse:
    articles: list[Article]
    cosine_similarities: list[float]
