import streamlit as st
import base64




st.markdown(
     """
    <style>
    @import url('                                                       ;500;700&display=swap');

    .main-title {
        font-family: 'Rubik', sans-serif;
        font-size: 36px;
        font-weight: 700;
        color: #9034c8;
        text-align: right;
        padding: 20px 0;
        direction: rtl;
    }

    .chat-message {
        padding: 0.5rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
        display: flex;
        flex-direction: row;
        width: fit-content;
        max-width: 80%;
    }

    .user-message {
        background: #9034c8;
        border-radius: 15px;
        margin-left: 0;
        margin-right: auto;
        direction: rtl;
        color:#f0efff
    }

    .bot-message {
        margin-left: auto;
        margin-right: 0;
        direction: rtl;
        display: flex;
        align-items: center;
    }

    .message-text {
        font-family: 'Rubik', sans-serif;
        font-size: 16px;
        margin: 0;
    }

    .stButton button {
        direction: rtl;
        text-align: right;
        background-color: #9034c8;
        border: 1px solid rgba(250, 250, 250, 0);
        color: #f0efff;
        padding: 0.5em 1em;
        border-radius: 20px;
        font-size: 1em;
        cursor: pointer;
    }

    .stButton button:hover {
        background-color: #7E2FAD;
        color: #f0efff;
        border: 1px solid rgb(38, 39, 48);
    }

    .stTextInput input {
        background-color: rgb(165, 221, 234);
        color: #ff6347;
        border: 1px solid rgba(0, 110, 184, 0.8);
        padding: 10px;
    }

    .stSelectbox div[role="combobox"] {
        direction: rtl;
        text-align: right;
    }

    .stButton {
        display: flex;
        justify-content: flex-end;
    }
    </style>
    """,
    unsafe_allow_html=True
)