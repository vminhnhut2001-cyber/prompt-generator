import streamlit as st
import google.generativeai as genai

# ====== API KEY ======
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# ✅ model mới ổn định
model = genai.GenerativeModel("gemini-1.5-pro")

# ====== FUNCTION ======
def generate_prompt(hook, topic, style, platform, mode):

    prompt = f"""
You are a top content strategist.

Your task is to generate a HIGH-QUALITY social media script.

You MUST follow the exact output format below.
DO NOT explain anything.
DO NOT add extra text outside the format.

HOOK:
"{hook}"

CONTENT GOAL:
Topic: {topic}
Style: {style}
Platform: {platform}

REQUIREMENTS:
- Clear and educational
- Spoken natural style
- Emotionally engaging
- Suitable for short-form video

STRUCTURE:
1. Reinforce the hook emotionally
2. Reveal hidden insight
3. Give real-life example or visual idea
4. Add psychological trigger
5. Strong memorable closing line

OUTPUT FORMAT (MANDATORY):

## TITLE
(write one strong title)

## FULL SCRIPT
(spoken style, natural, no bullet points)

## VISUAL SUGGESTIONS
- Scene ideas
- Camera angle ideas
- Visual metaphors if possible

## CAPTION
(short, viral, educational)

## KEYWORDS
5 short keywords separated by commas
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
        st.markdown(result)
