from answer_engine_src.cervical_cancer_parser import CervicalCancerParser
import pickle as pkl
import gzip
import os

from answer_engine_src.constants import PARSED_ARTICLES_PROCESSED_SAVE_PATH
from answer_engine_src.definitions import Article


def generate_from_folder(folder_path: str) -> list[Article]:
    all_articles = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            print("Parsing file: ", file_name)
            file_path = os.path.join(folder_path, file_name)
            articles = cervical_cancer_parser(file_path)
            all_articles.extend(articles)

    return all_articles


def cervical_cancer_parser(file_path: str) -> list[Article]:
    parser = CervicalCancerParser(file_path, "data")
    articles = parser.load_articles(parser.pickle_path)
    return articles


def main():

    # change this to your own path and parser if the data changes
    folder_path = "data/openalex_cervical_cancer_all_years"
    articles = generate_from_folder(folder_path)
    print("Saving to ", PARSED_ARTICLES_PROCESSED_SAVE_PATH)
    with gzip.open(PARSED_ARTICLES_PROCESSED_SAVE_PATH, "wb") as f:
        pkl.dump(articles, f)


if __name__ == "__main__":
    main()
