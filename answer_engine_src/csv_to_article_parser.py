from abc import ABC, abstractmethod
import os
import pandas as pd
import pickle
from typing import Dict
from answer_engine_src.definitions import Article
import csv


class CsvToArticleParser(ABC):
    def __init__(self, csv_path: str, storage_dir: str):
        self.csv_path = csv_path
        self.storage_dir = storage_dir
        self.pickle_path = os.path.join(
            storage_dir, os.path.splitext(os.path.basename(csv_path))[0] + ".pkl"
        )

        # Create storage directory if it doesn't exist
        os.makedirs(storage_dir, exist_ok=True)

        # Initialize pickle file if it doesn't exist
        if not os.path.exists(self.pickle_path):
            articles = self.parse_csv(self.csv_path)
            self.save_articles(articles, self.pickle_path)

    @abstractmethod
    def field_map(self) -> Dict[str, str]:
        """Return mapping of Article fields to CSV column names"""
        pass

    @abstractmethod
    def get_article_contents(self, row: pd.Series) -> list[str]:
        """Extract and process article contents from a DataFrame row"""
        pass

    def parse_csv(self, csv_path: str) -> list[Article]:
        """Read CSV and convert to list of Article objects"""
        with open(csv_path, mode="r", encoding="utf-8", errors="ignore") as f:
            reader = csv.DictReader(f)  # Reads rows as dictionaries
            data = [row for row in reader]  # Convert to list of dicts
            df = pd.DataFrame.from_records(data)  # Convert to DataFrame
        return self.parse_dataframe(df)

    def parse_dataframe(self, df: pd.DataFrame) -> list[Article]:
        """Convert DataFrame to list of Article objects"""
        articles = []
        field_mapping = self.field_map()

        for _, row in df.iterrows():

            # This pattern is very fragile and difficult to maintain
            if any(
                pd.isna(row[field_mapping[field]])
                for field in field_mapping
                if field != "article_contents_sources"
            ):
                continue
            if any(
                pd.isna(row[field])
                for field in field_mapping["article_contents_sources"]
            ):
                continue
            article = Article(
                date=str(row[field_mapping["date"]]),
                url=str(row[field_mapping["url"]]),
                title=str(row[field_mapping["title"]]),
                topic=str(row[field_mapping["topic"]]),
                article_contents=self.get_article_contents(row),
                article_name=str(row[field_mapping["article_name"]]),
            )
            articles.append(article)

        print(
            "Number of parsed documents with required fields non-null: ", len(articles)
        )
        return articles

    def save_articles(self, articles: list[Article], output_path: str) -> None:
        """Save list of Article objects to pickle file"""
        with open(output_path, "wb") as f:
            pickle.dump(articles, f)

    def load_articles(self, input_path: str) -> list[Article]:
        """Load list of Article objects from pickle file"""
        with open(input_path, "rb") as f:
            return pickle.load(f)

    def process_and_save(self, csv_path: str, output_path: str) -> None:
        """Convenience method to parse CSV and save results in one step"""
        articles = self.parse_csv(csv_path)
        self.save_articles(articles, output_path)
