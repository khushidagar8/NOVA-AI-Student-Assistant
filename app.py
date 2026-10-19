import streamlit as st
from datetime import date

st.set_page_config(page_title="NOVA AI | Student Assistant", page_icon="✨", layout="wide")

st.markdown("""
<style>
.stApp {background: linear-gradient(135deg, #080d1b 0%, #10152d 55%, #171033 100%); color: #f4f6ff;}
.block-container {padding-top: 2rem; max-width: 1200px;}
.hero {padding: 28px; border: 1px solid #343b68; border-radius: 22px;
       background: linear-gradient(120deg, rgba(38,49,98,.75), rgba(65,27,94,.55));}
.hero h1 {font-size: 3rem; margin-bottom: 0;}
.hero p {color: #c8cdef; font-size: 1.1rem;}
.pill {display:inline-block; padding:6px 12px; margin:4px; border:1px solid #505b9b;
       border-radius:20px; color:#cfd5ff; font-size:.9rem;}
div[data-testid="stMetric"] {background:#151b35; border:1px solid #303960; padding:15px; border-radius:16px;}
.stButton>button {border-radius:12px; border:1px solid #6b69df; background:#29245a; color:white;}
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm NOVA ✨ Your student-sidekick. Ask me about Python, AI, study planning, or career preparation."}
    ]
if "tasks" not in st.session_state:
    st.session_state.tasks = []

def get_reply(text):
    q = text.lower().strip()
    if any(x in q for x in ["hello", "hi", "hey", "namaste"]):
        return "Hey there! 👋 What are we working on today—coding, studying, or career growth?"
    if "python" in q:
        return "🐍 **Python quick tip:** Start with variables, input/output, `if-else`, loops, functions, and lists. Try a tiny program every day. Want a challenge? Write a program that checks whether a number is even or odd."
    if "machine learning" in q or "ml" in q:
        return "🧠 **ML roadmap:** Python basics → NumPy & Pandas → data visualization → scikit-learn → train/test split → a small prediction project. Learn one step at a time and document what you build."
    if "resume" in q or "cv" in q:
        return "📄 **Resume tip:** Keep it one page as a fresher. Add education, skills you can explain, 2–3 projects, certificates, and measurable achievements. Include GitHub links to projects that actually run."
    if "interview" in q:
        return "🎯 **Interview practice:** Use the STAR method—Situation, Task, Action, Result. Prepare a 30-second introduction, one project explanation, your strengths, and what you are learning."
    if "study" in q or "timetable" in q or "exam" in q:
        return "📚 **Study sprint:** Pick one topic, study for 25 minutes, solve 3 questions without looking at notes, then take a 5-minute break. End by writing what still feels confusing."
    if "ai" in q or "artificial intelligence" in q:
        return "✨ **AI in simple words:** Artificial Intelligence is the field of building systems that perform tasks such as understanding language, recognizing patterns, or making predictions. Start with a small, clear problem before adding complex features."
    if "project" in q or "github" in q:
        return "🚀 **Project tip:** A strong project has a clear problem, a working demo, readable code, screenshots, setup instructions, and honest limitations. Push improvements to GitHub as you build."
    if "motivat" in q or "confidence" in q:
        return "🌱 You don't need to know everything to start. Build one small thing, understand it properly, and improve it. Consistency beats trying to look perfect."
    return "I’m still a starter assistant, so I may not know that yet. Try asking me about Python, AI/ML, study planning, resumes, interviews, or projects. You can also extend my responses in `app.py`."

st.markdown("""
<div class="hero">
  <div class="pill">✦ PYTHON PROJECT</div><div class="pill">✦ AI-INSPIRED ASSISTANT</div><div class="pill">✦ STUDENT PRODUCTIVITY</div>
  <h1>✨ NOVA AI</h1>
  <p>Your personal student assistant — learn smarter, plan better, build boldly.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Learning mode", "ON", "Python • AI • ML")
with col2:
    st.metric("Today's date", date.today().strftime("%d %b %Y"))
with col3:
    st.metric("Tasks added", len(st.session_state.tasks))

left, right = st.columns([1.55, 1], gap="large")
with left:
    st.subheader("💬 Chat with NOVA")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    prompt = st.chat_input("Ask NOVA something…")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        reply = get_reply(prompt)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()

with right:
    st.subheader("⚡ Quick tools")
    with st.expander("📝 Make a mini study plan", expanded=True):
        topic = st.text_input("Topic to study", placeholder="e.g. Java loops")
        minutes = st.select_slider("Study time", options=[15, 25, 30, 45, 60], value=25)
        if st.button("Create plan", use_container_width=True):
            if topic.strip():
                st.success(f"Your {minutes}-minute plan for **{topic}**")
                st.write(f"1. {minutes//2} min — revise the concept")
                st.write(f"2. {minutes//3} min — solve practice questions")
                st.write(f"3. Remaining time — check mistakes and write a summary")
            else:
                st.warning("Enter a topic first.")

    with st.expander("✅ Task tracker"):
        new_task = st.text_input("Add a task", placeholder="Finish Python practice")
        if st.button("Add task", use_container_width=True):
            if new_task.strip():
                st.session_state.tasks.append({"task": new_task.strip(), "done": False})
                st.rerun()
        for i, task in enumerate(st.session_state.tasks):
            done = st.checkbox(task["task"], value=task["done"], key=f"task_{i}")
            st.session_state.tasks[i]["done"] = done
        if st.session_state.tasks and st.button("Clear completed tasks"):
            st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
            st.rerun()

    with st.expander("🧮 Quick calculator"):
        a = st.number_input("First number", value=12.0, key="a")
        b = st.number_input("Second number", value=3.0, key="b")
        op = st.selectbox("Operation", ["+", "−", "×", "÷"])
        if op == "+": result = a + b
        elif op == "−": result = a - b
        elif op == "×": result = a * b
        else: result = "Cannot divide by zero" if b == 0 else a / b
        st.write("**Result:**", result)

st.divider()
st.caption("Built by Khushi • B.Tech Artificial Intelligence student • Learning by building 💜")
st.caption("Demo version: responses use a small built-in knowledge base; no external AI API is connected yet.")
