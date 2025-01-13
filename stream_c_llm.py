import streamlit as st
from anthropic import Anthropic
import os

# Set up the API client
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

st.title("Cat Story Generator")

def generate_claude_stream(system_prompt,user_prompt):
# Create the stream
    with client.messages.stream(
        model="claude-3-sonnet-20240229",  
        max_tokens=1024,  
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    ) as stream:
    
    # Create a placeholder for the story
        story_placeholder = st.empty()
        full_response = ""
    
    # Process each chunk of the response
        for chunk in stream:
            if chunk.type == "content_block_delta":
                full_response += chunk.delta.text
                #story_placeholder.markdown(full_response + "▌")
                story_placeholder.markdown(f'<div style="direction: rtl; text-align: right;">{full_response}▌</div>', unsafe_allow_html=True)

    
    # Show final response without cursor
        #story_placeholder.markdown(full_response)
        story_placeholder.markdown(f'<div style="direction: rtl; text-align: right;">{full_response}</div>', unsafe_allow_html=True)

    
    #insert full_response to the history 

#generate_cloaude_steam("תמציא לי שיר על . response with mardown " , "מדינת ישראל")