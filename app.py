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

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text
