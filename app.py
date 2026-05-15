import streamlit as st
import time

st.set_page_config(page_title="UWorld Clone", layout="wide")

if "mode" not in st.session_state:
    st.session_state.mode = "home"

if st.session_state.mode == "home":
    st.title("🧠 UWorld Style Question Bank")

    block = st.selectbox("Choose Block", ["Block 1", "Block 2"])
    mode = st.selectbox("Mode", ["Tutor Mode", "Exam Mode"])

    if st.button("Start"):
        st.session_state.mode = "exam"
        st.session_state.start_time = time.time()
        st.session_state.q_index = 0
        st.session_state.answers = {}
        st.session_state.bookmarks = set()

elif st.session_state.mode == "exam":
    st.sidebar.title("⏱️ Timer")
    elapsed = int(time.time() - st.session_state.start_time)
    st.sidebar.write(f"{elapsed//60}:{elapsed%60:02d}")

    questions = [
        {
            "q":"Sample Question: Testicular torsion most affects which structure?",
            "choices":["Renal artery","Gonadal artery","Femoral artery","Obturator artery"],
            "answer":1,
            "exp":"Torsion twists the spermatic cord → affects gonadal artery."
        }
    ]

    q = questions[0]
    st.subheader("Question 1")

    st.write(q["q"])
    choice = st.radio("Select answer", q["choices"])

    if st.button("⭐ Bookmark"):
        st.session_state.bookmarks.add(0)

    if st.button("Show Answer"):
        st.success(f"Correct Answer: {q['choices'][q['answer']]}")
        st.info(q["exp"])
