from answer_engine_src.answer_engine import AnswerEngineResponseWithArticles
from answer_engine_src.definitions import Article


answer_engine_response = {
    "answers": [
        {
            "content": 'Recently, Russian schoolchildren participated in a friendship camping event with North Korean students at the Songdowon International Children’s Camp. This lively occasion allowed the children from both countries to enjoy pleasant days together in a scenic location by the East Sea of Korea. An event titled "Evening of Friendship" was held where schoolchildren exchanged impressions and showcased their cultural talents through joint performances.',
            "citations": [2, 3],
        },
        {"content": "Something else", "citations": [1, 2]},
    ]
}

relevant_articles = [
    Article(
        date="2024-08-01",
        url="http://www.rodong.rep.kp/en/index.php?MTJAMjAyNC0wOC0wMS1IMDAzQDE1QDFAQDBAMQ==",
        title="War Veterans Enjoy Themselves at Yangdok Hot Spring Resort",
        topic="Politics",
        article_contents=[
            "The war veterans, who had the great honor of participating in the celebrations of the 71st anniversary of the victory in the Fatherland Liberation War, are spending a pleasant time at the Yangdok Hot Spring Resort.",
            "The central artistic information team and others gave a colorful performance there to delight the war veterans.",
            "The veterans spent a pleasant time, singing wartime songs and dancing together with the performers.",
            "Officials and employees of the Yangdok Hot Spring Resort Service Management Office prepared birthday spreads for those veterans who marked their birthdays.",
            "Rodong Sinmnun",
        ],
        article_name="article_0000",
    ),
    Article(
        date="2024-08-01",
        url="http://www.rodong.rep.kp/en/index.php?MTJAMjAyNC0wOC0wMS1IMDA1QDE1QDFAQDBAMg==",
        title="New Houses Built in Haeju City",
        topic="Politics",
        article_contents=[
            "New houses have been built at the Jangbang Farm in Haeju City, South Hwanghae Province of the DPRK this year.",
            "Dwelling houses for hundreds of families built in a cozy and peculiar way are the cradle of happiness provided under the energetic leadership of the respected Comrade Kim Jong Un who is working heart and soul to provide the people in South Hwanghae Province who are defending the agricultural province of the country with an affluent and civilized life as soon as possible.",
            "Present at the ceremony for moving into new houses were Pak Thae Sop, secretary of the South Hwanghae Provincial Committee of the Workers’ Party of Korea, officials, builders and agricultural workers in Haeju City.",
            "Kim Chol Pom, chairman of the South Hwanghae Provincial People’s Committee, made a congratulatory address and licenses for the use of dwelling houses were conveyed. Then oath-taking speeches were made.",
            "Amid a cheerful music and dancing, the village was in a festive mood.",
            "Rodong Sinmun",
        ],
        article_name="article_0001",
    ),
    Article(
        date="2024-08-01",
        url="http://www.rodong.rep.kp/en/index.php?MTJAMjAyNC0wOC0wMS1IMDA0QDE1QDFAQDBAMw==",
        title="Meeting of DPRK and Russian Schoolchildren’s Camping Groups Held",
        topic="Culture",
        article_contents=[
            "DPRK and Russian schoolchildren spent pleasant days since they started the camping at the Songdowon International Children’s Camp, the nice palace of the children well built in Songdowon, the scenic spot of the East Sea of Korea.",
            'A meeting "Evening of Friendship" of DPRK and Russian schoolchildren’s friendship campers took place at the international friendship children’s hall on July 30.',
            "Present there were Kim Song Il, vice-chairman of the Central Committee of the Socialist Patriotic Youth League, officials concerned, schoolchildren’s camping groups of the DPRK and Russia.",
            "First, a letter to the respected Comrade Kim Jong Un by the Russian campers who took part in the DPRK-Russia schoolchildren’s friendship camping was read out and courteously handed over to an official concerned.",
            "A video on the pleasant days of camping was shown, and a joint art performance of the schoolchildren of the two countries was given.",
            "Members of the Russian schoolchildren’s camping group gave their impressions on the camping at the Songdowon International Children’s Camp.",
            "The camping served as a significant occasion for further deepening friendship between the schoolchildren of the two countries.",
            "Rodong Sinmun",
        ],
        article_name="article_0002",
    ),
]


dummy_answer_engine_response_with_articles = AnswerEngineResponseWithArticles(
    answer_engine_response=answer_engine_response, articles=relevant_articles
)

DPRK_QUESTION_LIST_STR = """
1. Could you explain in detail North Korea's recent constitutional developments?
2. What is the purpose of North Korea's trash balloons?
3. What does the Russia-Ukraine war mean to North Korea?
4. What is the intention behind North Korea's destruction of the inter-Korean roads?
5. How has North Korean media's evaluation of Russian President Putin changed over the past year?
6. What does North Korea’s situation, as seen through the August 2024 flooding, reveal?
7. How does the North Korean government evaluate its new ballistic missile?
8. What are the current trends in North Korean dietary habits?
9. What is the North Korean government's stance on U.S. presidential candidates?
10. How advanced is North Korea’s digital reform?
11. What is North Korea's stance on Iran's retaliatory attack on Israel?
12. What does North Korea think of the recent formation of the Ishiba Cabinet?
13. How does North Korea view its own nuclear arsenal?
14. What is the current state of North Korea's scientific and technological development?
15. What is the current state of North Korea's forest development?
16. What is the current state of poverty in North Korea?
17. What is the current state of electricity in North Korea?
18. Which countries does North Korea recognize as legitimate states?
19. How does North Korea perceive itself as a nation?
20. How does North Korea currently view reunification with South Korea?
21. What did Russian schoolchildren do in North Korea?"""

DPRK_DEFAULT_QUESTION_LIST = []
for i, line in enumerate(DPRK_QUESTION_LIST_STR.strip().split("\n")):
    question = line.split(f"{i+1}.")[1].strip()
    DPRK_DEFAULT_QUESTION_LIST.append(question)


CERVICAL_QUESTIONS = [
    "What are the symptoms of cervical cancer?",
]
