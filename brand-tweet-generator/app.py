import streamlit as st
from openai import OpenAI
from prompts import brand_voice_prompt, tweet_generation_prompt
import os

st.set_page_config(page_title="Brand Tweet Generator", page_icon="🐦")

st.title("🐦 AI Brand Tweet Generator")

st.write(
"Generate 10 on-brand tweets using AI by analyzing the brand voice."
)

api_key = st.text_input("Enter OpenAI API Key", type="password")

brand = st.text_input("Brand Name")

industry = st.text_input("Industry / Category")

campaign = st.selectbox(
    "Campaign Objective",
    ["Engagement", "Promotion", "Awareness", "Product Launch"]
)

product = st.text_area("Describe the product or service")

audience = st.text_input("Target Audience (optional)")

if st.button("Generate Tweets"):

    if not api_key:
        st.error("Please enter your OpenAI API key")
        st.stop()

    client = OpenAI(api_key=api_key)

    with st.spinner("Analyzing brand voice..."):

        voice_prompt = brand_voice_prompt(
            brand,
            industry,
            campaign,
            product,
            audience
        )

        voice_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": voice_prompt}
            ]
        )

        voice_summary = voice_response.choices[0].message.content

    st.subheader("Brand Voice Summary")

    st.write(voice_summary)

    with st.spinner("Generating tweets..."):

        tweet_prompt = tweet_generation_prompt(
            voice_summary,
            campaign,
            product
        )

        tweet_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": tweet_prompt}
            ]
        )

        tweets = tweet_response.choices[0].message.content

    st.subheader("Generated Tweets")

    st.write(tweets)

    st.success("Tweets generated successfully!")
