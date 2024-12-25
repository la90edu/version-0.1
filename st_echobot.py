# import streamlit as st

# import pathlib


# # Function to load CSS from the 'assets' folder
# def load_css(file_path):
#     with open(file_path) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# # Load the external CSS
# css_path = pathlib.Path("styles.css")
# load_css(css_path)

# st.title("Echo Bot")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"], avatar="🤖"):
#         st.markdown(message["content"])

# # React to user input
# if prompt := st.chat_input("What is up?", avatar="🤖"):
#     # Display user message in chat message container
#     st.chat_message("user").markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     response = f"Echo: {prompt}"
#     # Display assistant response in chat message container
#     with st.chat_message("assistant", avatar="🤖"):
#         st.markdown(response)
#     # Add assistant response to chat history
#     st.session_state.messages.append({"role": "assistant", "content": response})

import streamlit as st
from enum import Enum, auto

# Define a custom enum
class UserRole(Enum):
    ADMIN = auto()
    USER = auto()
    GUEST = auto()

# Initialize session state with the enum
if 'current_role' not in st.session_state:
    st.session_state.current_role = UserRole.GUEST

# You can modify and check the enum in session state
st.write(f"Current Role: {st.session_state.current_role}")

if st.button("Upgrade to Admin"):
    st.session_state.current_role = UserRole.ADMIN
    st.write(f"Role updated to: {st.session_state.current_role}")