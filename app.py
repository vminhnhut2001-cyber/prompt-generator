import streamlit as st
import google.generativeai as genai

# ====== API KEY ======
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# ✅ model ổn định nhất
model = genai.GenerativeModel("gemini-pro")

# ====== FUNCTION ======
def generate_prompt(hook, topic, style, platform, mode):

    prompt = f"""
You are a top content strategist.

HOOK:
"{hook}"

CONTENT GOAL:
Topic: {topic}
Style: {style}
Platform: {platform}

REQUIREMENTS:
- Focus on clarity
- Make it educational

STRUCTURE:
1. Reinforce the hook emotionally
2. Reveal hidden insight
3. Give real-life example or visual idea
4. Add psychological trigger
5. Strong memorable closing line

OUTPUT:
- Title
- Full Script (spoken style)
- Visual Suggestions
- Caption
- 5 Keywords
"""

    response = model.generate_content(prompt)
    return response.text


# ====== UI ======
st.title("🔥 Prompt Generator")

hook = st.text_area("Hook")
topic = st.selectbox("Topic", ["social analysis", "business", "mindset"])
style = st.selectbox("Style", ["deep", "viral", "storytelling"])
platform = st.selectbox("Platform", ["TikTok", "YouTube", "Facebook"])
mode = st.selectbox("Mode", ["Normal", "Viral"])

if st.button("🔥 TẠO PROMPT"):
    if hook.strip() == "":
        st.warning("Nhập hook trước đã")
    else:
        result = generate_prompt(hook, topic, style, platform, mode)
        st.write(result)
