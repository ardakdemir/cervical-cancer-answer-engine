KEYWORD_GENERATION_PROMPT = """

You are tasked with generating a list of keywords from a given raw query. These keywords will be used to help a downstream TF-IDF model find relevant articles to the given query. Ensure that the keywords cover all important concepts in the query and limit the list to around 10 keywords.

The output should only contain the JSON object with no additional explanation.

Query: {query}
"""


ANSWER_GENERATION_DPRK_PROMPT = [
    {
        "role": "system",
        "content": "You are an excellent answer engine specialized in answering questions about North Korea (DPRK).",
    },
    {
        "role": "user",
        "content": """
You will be given a query about North Korea and in addition a list of relevant articles. 
You need to generate a coherent and informative answer based on the query and the articles provided.

Your answer should be in a list of dicts format where each dict will contain "content" that represents the answer text and "citations" which is a list of indices to the relevant input articles.
Make sure to return multiple sections in your answer to cover different aspects of the query.
""",
    },
]

ANSWER_GENERATION_CERVICAL_CANCER_PROMPT = [
    {
        "role": "system",
        "content": "You are an excellent answer engine specialized in answering questions only about Cervical Cancer and related research.",
    },
    {
        "role": "user",
        "content": """
You will be given a query about Cervical Cancer and in addition a list of relevant published articles. 
You need to generate a coherent and informative answer based on the query and the articles provided.

Your answer should be in a list of dicts format where each dict will contain "content" that represents the answer text and "citations" which is a list of indices to the relevant input articles.
Make sure to return multiple sections in your answer to cover different aspects of the query.
""",
    },
]
