from answer_engine_src.cervical_cancer_parser import CervicalCancerParser
import pickle as pkl
import gzip

from answer_engine_src.constants import PARSED_ARTICLES_PROCESSED_SAVE_PATH


def cercival_cancer_parser():
    parser = CervicalCancerParser(
        "data/OpenAlex_cervical_cancer_screening_2008.csv", "data"
    )
    articles = parser.load_articles(parser.pickle_path)
    return articles


def main():

    # change this to your own path and parser if the data changes
    articles = cercival_cancer_parser()
    print("Saving to ", PARSED_ARTICLES_PROCESSED_SAVE_PATH)
    with gzip.open(PARSED_ARTICLES_PROCESSED_SAVE_PATH, "wb") as f:
        pkl.dump(articles, f)


if __name__ == "__main__":
    main()
