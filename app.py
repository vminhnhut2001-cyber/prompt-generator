import streamlit as st
from datetime import datetime

def generate_prompt(hook, topic, style, platform, mode):
    structure = """
1. Reinforce the hook emotionally
2. Reveal hidden insight
3. Give real-life example or visual idea
4. Add psychological trigger
5. Strong memorable closing line
"""

    if mode == "Viral":
        extra = "- Optimize for virality\n- Use emotional tension\n- Add curiosity gaps"
    else:
        extra = "- Focus on clarity\n- Make it educational"

    prompt = f"""
You are a top content strategist.

HOOK:
"{hook}"

CONTENT GOAL:
Topic: {topic}
Style: {style}
Platform: {platform}

REQUIREMENTS:
{extra}

STRUCTURE:
{structure}

OUTPUT:
- Title
- Full Script (spoken style)
- Visual Suggestions
- Caption
- 5 Keywords
"""
    return prompt.strip()

st.set_page_config(page_title="Hook → Prompt Generator", layout="centered")
st.title("🎯 Hook → Prompt Generator")
st.caption("Tool tạo prompt từ hook")

hook = st.text_area("Nhập HOOK", height=120)

col1, col2 = st.columns(2)
with col1:
    topic = st.text_input("Topic", "social analysis")
    style = st.text_input("Style", "deep, smart, simple")
with col2:
    platform = st.selectbox("Platform", ["TikTok","YouTube","Facebook","Instagram"])
    mode = st.selectbox("Mode", ["Normal","Viral"])

if st.button("🔥 TẠO PROMPT"):
    if hook.strip() == "":
        st.warning("Bạn chưa nhập hook")
    else:
        result = generate_prompt(hook, topic, style, platform, mode)
        st.subheader("PROMPT TỐI ƯU")
        st.code(result, language="markdown")
        st.download_button(
            "📥 Tải prompt .txt",
            result,
            file_name=f"prompt_{datetime.now().strftime('%H%M%S')}.txt"
        )

