from answer_engine_src.csv_to_article_parser import CsvToArticleParser
from answer_engine_src.helpers import (
    CERVICAL_CANCER_FIELD_MAP,
    get_article_contents_cervical_cancer,
)
import pandas as pd
from typing import Dict


class CervicalCancerParser(CsvToArticleParser):
    def field_map(self) -> Dict[str, str]:
        return CERVICAL_CANCER_FIELD_MAP

    def get_article_contents(self, row: pd.Series) -> list[str]:
        return get_article_contents_cervical_cancer(row)


if __name__ == "__main__":
    parser = CervicalCancerParser("data/OpenAlex_cervical_cancer_screening_2008.csv")
    articles = parser.load_articles(parser.pickle_path)
