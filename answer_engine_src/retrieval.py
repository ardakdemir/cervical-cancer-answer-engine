from dataclasses import dataclass
import os
from answer_engine_src.cervical_cancer_parser import CervicalCancerParser
from answer_engine_src.constants import (
    PARSED_ARTICLES_PATH,
    PARSED_ARTICLES_PROCESSED_SAVE_PATH,
    PARSED_ARTICLES_PROCESSED_GDRIVE_URL,
)
from answer_engine_src.definitions import RetrievalEngineResponse
from answer_engine_src.gdown_helpers import get_gdrive_file
from answer_engine_src.helpers import df_to_article_list, input_with_default
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from answer_engine_src.keyword_generator import KeywordGenerator
from answer_engine_src.preprocessing import TextPreprocessor
import pickle as pkl
import gzip

# if not os.path.exists(PARSED_ARTICLES_PROCESSED_SAVE_PATH):
#     print("Downloading processed articles from ", PARSED_ARTICLES_PROCESSED_GDRIVE_URL)
#     get_gdrive_file(
#         PARSED_ARTICLES_PROCESSED_GDRIVE_URL, PARSED_ARTICLES_PROCESSED_SAVE_PATH
#     )
# all_articles = df_to_article_list(pd.read_csv(PARSED_ARTICLES_PATH))
# print("Saving to ",PARSED_ARTICLES_PROCESSED_SAVE_PATH)
# with gzip.open(PARSED_ARTICLES_PROCESSED_SAVE_PATH, 'wb') as f:
#     pkl.dump(all_articles, f)

# print("Loading processed articles from ", PARSED_ARTICLES_PROCESSED_SAVE_PATH)
# with gzip.open(PARSED_ARTICLES_PROCESSED_SAVE_PATH, "rb") as f:
#     all_articles = pkl.load(f)
# print(f"{len(all_articles)=} are loaded")


# Change this to your own path and parser if the data changes
parser = CervicalCancerParser(
    "data/OpenAlex_cervical_cancer_screening_2008.csv", "data"
)
all_articles = parser.load_articles(parser.pickle_path)


class RetrievalEngine:
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.keyword_generator = KeywordGenerator()

    def retrieve(self, query, n=5):
        """
        Retrieves the top n articles from the corpus that are most relevant to the query.
        """
        # Combine all articles into a list
        articles = [" ".join(article.article_contents) for article in all_articles]

        # Add the query to the list of articles

        keywords = " ".join(self.keyword_generator.generate_keywords(query).keywords)
        print("\n###\nKeywords from keyword generator: ", keywords, "\n###\n")

        articles.append(keywords)

        # Vectorize the articles and the query
        vectorizer = TfidfVectorizer(
            preprocessor=self.preprocessor.preprocess
        ).fit_transform(articles)

        # Compute the cosine similarity matrix
        cosine_similarities = cosine_similarity(
            vectorizer[-1], vectorizer[:-1]
        ).flatten()

        # Get the indices of the top n most similar articles
        most_similar_indices = cosine_similarities.argsort()[-n:][::-1]

        # Retrieve the top n articles
        top_articles = [all_articles[i] for i in most_similar_indices]
        cosine_similarities = [
            round(float(cosine_similarities[i]), 3) for i in most_similar_indices
        ]

        return RetrievalEngineResponse(
            articles=top_articles, cosine_similarities=cosine_similarities
        )


def main():
    retrieval_engine = RetrievalEngine()
    query = input_with_default(
        "Enter some text to find most relevant articles", "Yangdok Hot spring resort"
    )
    retrieval_engine_response = retrieval_engine.retrieve(query, n=5)
    for article, cos_sim in zip(
        retrieval_engine_response.articles,
        retrieval_engine_response.cosine_similarities,
    ):
        print(article.title, cos_sim)


if __name__ == "__main__":
    main()
