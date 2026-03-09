def brand_voice_prompt(brand, industry, campaign, product, audience):

    prompt = f"""
You are an expert social media strategist.

Analyze the following brand details and infer the brand voice.

Brand Name: {brand}
Industry: {industry}
Campaign Objective: {campaign}
Product Description: {product}
Target Audience: {audience}

Return the following:

1. Brand Tone
2. Target Audience
3. Content Themes
4. Communication Style

Return concise bullet points.
"""

    return prompt


def tweet_generation_prompt(voice_summary, campaign, product):

    prompt = f"""
You are the social media manager of a brand.

Brand voice summary:
{voice_summary}

Campaign objective:
{campaign}

Product:
{product}

Generate 10 tweets consistent with the brand voice.

Rules:
- Maximum 280 characters
- Mix tweet styles:
    • engaging
    • promotional
    • witty
    • informative
- Natural social media tone
- Optional emojis or hashtags
- Number the tweets 1-10
"""

    return prompt
