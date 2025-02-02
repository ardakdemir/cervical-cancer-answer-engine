import streamlit as st
import time

from answer_engine_src.answer_engine import (
    AnswerEngine,
    AnswerEngineResponseWithArticles,
)

st.title("(Upcoming) Cervical Cancer Answer Engine")
st.caption(
    "A ChatGpt based answer engine for answering cervical cancer related questions using OpenAlex citations as the reference."
)
st.text("Developed by Arda Akdemir and Iwaki Yoko, 2025.")

answer_engine = AnswerEngine()


# Streamed response emulator
def response_generator_with_sections(query: str):
    print("Querying the answer engine...")
    t_s = time.time()
    answer_engine_response: AnswerEngineResponseWithArticles = answer_engine.answer(
        query
    )
    dur = round(time.time() - t_s, 3)
    print("Answer engine runtime: ", dur)
    relevant_articles = answer_engine_response.articles
    response = answer_engine_response.answer_engine_response

    for section in response.answers:
        response = section.content
        citations = section.citations
        response = response + f"*({','.join([str(c) for c in citations])})"

        def get_response_text():
            for word in response.split():
                yield word + " "
                time.sleep(0.03)

        st.write_stream(get_response_text())
        for citation in citations:
            url = relevant_articles[citation - 1].url
            title = relevant_articles[citation - 1].title
            st.html(
                f'<a href="{url}" target="_blank" style="color: blue;">[{citation}] {title}</a>'
            )


# Initialize chat history
st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask a question about recent cervical cancer research."):
    # Add user message to chat history
    st.session_state.messages = []
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = response_generator_with_sections(prompt)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
