from answer_engine_src.helpers import input_with_default
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

# Ensure necessary NLTK resources are downloaded
nltk.download("punkt_tab")
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")


class TextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess(self, text):
        # Tokenize the text
        tokens = word_tokenize(text)

        # Convert to lowercase
        tokens = [word.lower() for word in tokens]

        # Remove punctuation
        tokens = [word for word in tokens if word.isalnum()]

        # Remove stopwords
        tokens = [word for word in tokens if word not in self.stop_words]

        # Lemmatize tokens
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens]

        return " ".join(tokens)


def main():
    text_processor = TextPreprocessor()
    text = input_with_default(
        "Enter some text to preprocess", "The quick brown fox jumps over the lazy dog."
    )
    tokens = text_processor.preprocess(text)
    print(tokens)


if __name__ == "__main__":
    main()
