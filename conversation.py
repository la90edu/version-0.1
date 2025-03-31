import streamlit as st
import data
import base64
import time

def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# המרת התמונה ל-base64
try:
    img_base64 = img_to_base64("mop_logo.jpg")
    avatar_img = f"data:image/jpeg;base64,{img_base64}"
except Exception as e:
    avatar_img = ""

# def show_closed_question_new(question,options):
    # display_bot_message_with_typing_effect(question)
    # #st.text("hey")
    # #options = ["North", "East", "South", "West"]
    # selection = st.pills("Directions", options, selection_mode="single")
    # st.session_state.close_question_answer=selection
    # st.session_state.close_question_stage=1
    # return()
    
def feedback_after_selection():
    selection=st.session_state.close_question_answer
    st.markdown(f"Your selected options: {selection}.")
    st.session_state.messages.append({"role": "user", "content": selection})

            # שמירת התשובה של המשתמש במשתנה user_data
    #st.session_state.user_data.append(selection)
    data.add_and_update_user_data(selection)
    

def display_bot_image(image_path):
    img_base64 = img_to_base64(image_path)
    # הוספת התמונה להיסטוריית השיחה
    st.session_state.messages.append({
        "role": "assistant",
        "content": None,  # אין טקסט במקרה הזה
        "type": "image",
        "url": image_path
    })
    # הצגת התמונה
    st.image(image_path)
   
    st.session_state.current_question += 1
    # אתחול מחדש של האפליקציה
    st.rerun()
    
def display_bot_image_without_increase_question_number(image_path):
    img_base64 = img_to_base64(image_path)
    # הוספת התמונה להיסטוריית השיחה
    st.session_state.messages.append({
        "role": "assistant",
        "content": None,  # אין טקסט במקרה הזה
        "type": "image",
        "url": image_path
    })
    # הצגת התמונה
    st.image(image_path)

def display_bot_video(video_path):
    st.video(video_path)
    st.session_state.messages.append({
        "role": "assistant",
        "type": "video",
        "url": video_path
    })
     # עדכון השאלה הנוכחית
    st.session_state.current_question += 1
    st.rerun()
    
def display_user_message(text):
    st.markdown(f"""
    <div class="chat-message user-message">
        <div class="message-content">
            <p class="message-text">{text}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_bot_message_with_typing_effect(text, typing_speed=0.015):
    """
    מציג הודעה מהבוט עם אפקט הקלדה
    
    :param text: הטקסט להצגה
    :param typing_speed: מהירות ההקלדה (בשניות בין תווים)
    """
    placeholder = st.empty()
    displayed_text = ""
    
    for char in text:
        displayed_text += char
        placeholder.markdown(f"""
        <div class="chat-message bot-message">
            <div class="message-content">
                <p class="message-text">{displayed_text}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(typing_speed)
            
   
def display_bot_message(text):
    st.markdown(f"""
    <div class="chat-message bot-message">
        <div class="message-content">
            <p class="message-text">{text}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
st.logo("logo1.jpg",size="large")
 
def ask_question_with_buttons(question, options):
    for option in options:
        if st.button(option):  # יוצר כפתור לכל אפשרות
            return option

 
def show_chat_history():
     for message in st.session_state.messages:
        if message["role"] == "assistant":
            if message.get("type") == "image":  # הודעה מסוג תמונה
                st.image(message['url'])
            elif message.get("type") == "video":  # הודעה מסוג וידאו
                st.video(message['url'])
            else:  # הודעת טקסט רגילה
                display_bot_message(message["content"])
        elif message["role"] == "user":  # הודעת משתמש
            display_user_message(message["content"])
            
def show_text(text):
    #if st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]:
    display_bot_message_with_typing_effect(text)
        #st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]=False
    st.session_state.messages.append({"role": "assistant", "content": text})
    st.session_state.current_question += 1

    st.rerun()
    
       