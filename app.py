import streamlit as st
st.set_page_config(
    page_title="מבט לרגע",
    page_icon="🚀",  # אייקון של בוט
    layout="wide",  # הגדרה לתצוגה רחבה
    # initial_sidebar_state="expanded",
    # menu_items={
    #     "Get Help": None,
    #     "Report a bug": None,
    #     "About": None
    
)

import init

import base64
from pathlib import Path
from questions2 import questions  # ייבוא השאלות מקובץ חיצוני
import time
import gd
import llm_gpt
import pathlib
from PIL import Image
import time_1 as ti
from schools import School_Type
import schools
import simulations
import write_to_file
import llm_manager
import data_translation
import crop_for_llm
import llm_claude
import os
import translate_hegedim
import date
import os
from anthropic import Anthropic, APIError
from after_simulation import ReflectiveQuestions

import base64
import conversation
import data
import active_sim




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



def start_counting_time():
                st.session_state.is_counting_time=True
                ti.begin()
                
    
def stop_counting_time():
                st.session_state.is_counting_time=False
                response_time_count=ti.end()
                #st.session_state.user_data.append(response_time_count)
                data.add_and_update_user_data(response_time_count)

def show_simulation0():
    q1="21. לפניך אתגר חשיבה, אנא בחר/י את רמת הקושי המתאימה לך"
    q2="פתרו את השאלה הבאה"

    if (st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]):
        conversation.display_bot_message_with_typing_effect(q1)
        st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]=False
    string_grade=st.session_state.grade
    School_Type.to_School_Type(st.session_state.grade)    
    grade=School_Type.to_School_Type(st.session_state.grade)    

    # ע"פ הכיתה - נותןאת האפשרויות לסימולציות 
    #options=simulations.return_options(grade)
    
    levels=simulations.hebrew_levels
  
    cols = st.columns(len(levels))
    for i, level in enumerate(levels):
        if cols[i].button(level, key=f"{st.session_state.current_question}_{level}"):
            # הוספת השאלה והתשובה להיסטוריה
            st.session_state.messages.append({"role": "assistant", "content": q1})
            st.session_state.messages.append({"role": "user", "content": level})
             # שמירת התשובה של המשתמש במשתנה user_data
            #st.session_state.user_data.append(level)
            data.add_and_update_user_data(level)
            # st.session_state.simulation_id=i
            
            st.session_state.question_stage=1
            #step 2 
            simulation_id=simulations.find_simulation_index(string_grade,level)
            st.session_state.simulation_id=simulation_id

            st.rerun()

def show_simulation1():
    simulation_question=simulations.return_simulation_question_by_id(st.session_state.simulation_id)
    simulation_image_path=simulations.return_simulation_image_by_id(st.session_state.simulation_id)
    
    if (st.session_state.is_question_waiting_to_be_written_simulation[0]):
        if (simulation_image_path!=""):
            conversation.display_bot_image_without_increase_question_number(simulation_image_path)
                    # st.session_state.messages.append({"role": "assistant", "content": simulation_image_path})
        conversation.display_bot_message_with_typing_effect(simulation_question)
        
            # st.session_state.messages.append({"role": "assistant", "content": simulation_image_path})
        start_counting_time() ##start counting time of simulations
        st.session_state.messages.append({"role": "assistant", "content": simulation_question})
        data.update_data_in_sheet_without_increasing_question_number()

        st.session_state.is_question_waiting_to_be_written_simulation[0]=False
          
    options=simulations.return_simulation_options_by_id(st.session_state.simulation_id)
    cols = st.columns(len(options))
    for i, option in enumerate(options):
         if cols[i].button(option, key=f"{st.session_state.current_question}_{option}"):
    #         # הוספת השאלה והתשובה להיסטוריה
    #         st.session_state.messages.append({"role": "assistant", "content": q1})
            st.session_state.messages.append({"role": "user", "content": option})
            
    #          # שמירת התשובה של המשתמש במשתנה user_data
            #st.session_state.user_data.append(option)
            stop_counting_time() #stop time counting
            is_correct_answer=simulations.is_answer_correct(st.session_state.simulation_id,option)
            stam=simulations.is_answer_correct
            st.session_state.is_correct_answer=is_correct_answer
            #st.session_state.user_data.append(is_correct_answer)
            data.add_and_update_user_data(is_correct_answer)
            
            ReflectiveQuestions.simulation_answer=is_correct_answer
            x=ReflectiveQuestions.simulation_answer
            st.session_state.question_stage=2  
            st.rerun()         
    
def show_simulation2():

    if st.session_state.is_correct_answer:
        conversation.display_bot_message_with_typing_effect("תשובתך היא:")
        st.session_state.messages.append({"role": "assistant", "content": "תשובתך היא:"})

        conversation.display_bot_message_with_typing_effect("תשובה נכונה")
        st.session_state.messages.append({"role": "assistant", "content": "תשובה נכונה"})

    else:
        conversation.display_bot_message_with_typing_effect("תשובתך היא:")
        st.session_state.messages.append({"role": "assistant", "content": "תשובתך היא:"})
        
        conversation.display_bot_message_with_typing_effect("תשובה לא נכונה")   
        st.session_state.messages.append({"role": "assistant", "content": "תשובה לא נכונה"})

        
    st.session_state.question_stage=0
    st.session_state.current_question += 1

    st.rerun()
   


#questions functions
def show_closed_question(question, options,options_style, feedbacks,not_for_school_8,not_for_school_10): 
    if (((not_for_school_8=="True")and(st.session_state.grade=='SCHOOL_8')) or ((not_for_school_10=="True")and(st.session_state.grade=='SCHOOL_10'))):
        #st.session_state.user_data.append("ללא")
        data.add_and_update_user_data("ללא")
        st.session_state.current_question += 1
        st.rerun()
    else:     
        if st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]:
            conversation.display_bot_message_with_typing_effect(question)
            st.session_state.messages.append({"role": "assistant", "content": question})
            st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]=False
    
    # if ((not_for_school_10=="True")and(st.session_state.grade=='SCHOOL_10')):
    #     #st.session_state.user_data.append("ללא")
    #     data.add_and_update_user_data("ללא")
    #     st.session_state.current_question += 1
    #     st.rerun()
    # else:     
    #     if st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]:
    #         conversation.display_bot_message_with_typing_effect(question)
    #         st.session_state.messages.append({"role": "assistant", "content": question})
    #         st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]=False

    flag=st.session_state.is_current_button_was_clicked
    if (not flag):
        cols = st.columns(len(options))
        for i, option in enumerate(options):
            if cols[i].button(option, key=f"{st.session_state.current_question}_{option}"):
        # for option in options:
        #     if st.button(option):
                st.session_state.is_current_button_was_clicked=True
                st.session_state.question_stage = 1
                st.session_state.messages.append({"role": "user", "content": option})
                data.add_and_update_user_data(option)
                st.close_question_selection_i = options.index(option)
                st.session_state.question_stage = 1
                st.rerun()
                        
           
          
def show_closed_question2(feedback_type,system_prompt_name,auto_feedbacks):
     # הוספת הפידבק
            #feedback=""
        match feedback_type:
                case "auto":
                    i=st.close_question_selection_i
                    feedback=auto_feedbacks[i]
                    conversation.display_bot_message_with_typing_effect(feedback)#feedbacks[i])
                    st.session_state.messages.append({"role": "assistant", "content": feedback})#feedbacks[i]})
                case "llm":
                    user=next((entry['content'] for entry in reversed(st.session_state.temp_history) if entry['role'] == 'user'), None)
                    assistant=last_assistant_content = next((entry['content'] for entry in reversed(st.session_state.temp_history) if entry['role'] == 'assistant'), None)

                    feedback=llm_gpt.return_llm_answer(system_prompt_name,assistant,user)
                    st.session_state.temp_history=[]
                    conversation.display_bot_message_with_typing_effect(feedback)#feedbacks[i])
                    st.session_state.messages.append({"role": "assistant", "content": feedback})#feedbacks[i]})
                case "none":
                    feedback=""
                    
        st.session_state.current_question += 1
        st.session_state.question_stage=0

        st.session_state.is_current_button_was_clicked=False

        st.rerun()

def show_closed_grade_question(question, options,feedbacks, session_state_answer):
    # time.sleep(0.5)  # הוספת השהיה של 0.5 שניות
        
    if (st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]):
        conversation.display_bot_message_with_typing_effect(question)
        st.session_state.messages.append({"role": "assistant", "content": question})
        st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]=False
    cols = st.columns(len(options))
    for i, option in enumerate(options):
        if cols[i].button(option, key=f"{st.session_state.current_question}_{option}"):
            # הוספת השאלה והתשובה להיסטוריה
            st.session_state.messages.append({"role": "user", "content": option})

            # שמירת התשובה של המשתמש במשתנה user_data
            data.add_and_update_user_data(option)
            #st.session_state.user_data.append(option)
            # שמירת הכיתה במשתשנה בsession_state
            grade=session_state_answer[i]
            st.session_state.grade=grade
            
            # הוספת הפידבק
            # display_bot_message_with_typing_effect(feedbacks[i])
            # st.session_state.messages.append({"role": "assistant", "content": feedbacks[i]})
            st.session_state.current_question += 1
            st.rerun()
    
# פונקציה להצגת שאלה פתוחה
def show_open_question(question, feedback):
    # הצגת השאלה הפתוחה מהבוט
    # time.sleep(0.5)  # הוספת השהיה של 0.5 שניות

    if st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]:
        conversation.display_bot_message_with_typing_effect(question)
        st.session_state.messages.append({"role": "assistant", "content": question})
        st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]=False
 
# פונקציה להצגת היסטוריית השיחה
def show_open_question_llm():
    st.session_state.current_question += 1
    st.rerun()
    

# def show_open_question_llm(llm_prompt_name):
#         # time.sleep(0.5)  # הוספת השהיה של 0.5 שניות
#         prompt=llm_manager.get_active_bot_1()
#         if st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]:
#             conversation.display_bot_message_with_typing_effect(question)
#             st.session_state.messages.append({"role": "assistant", "content": question})
#             st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]=False
            


# פונקציה להצגת תיבת הקלט הקבועה בתחתית
def display_input_box(disabled,save_to_messages_reflection_bot):
    user_input = st.chat_input("הכנס את התשובה שלך כאן", disabled=disabled)
    
    if user_input:
        if save_to_messages_reflection_bot:
            st.session_state.messages_bot_reflection.append({"role": "user", "content": user_input})
        # אם המשתמש מקליד לאחר סיום השאלות, נוסיף להיסטוריה בלבד
        if st.session_state.current_question >= len(questions):
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.messages.append({"role": "assistant", "content": "תודה! השיחה הסתיימה, אבל אני כאן לשמוע אם יש עוד משהו שתרצה לשתף."})
        # אם המשתמש מקליד תשובה לשאלה פתוחה
        elif not disabled:
            # הוספת התשובה להיסטוריה
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # שמירת התשובה של המשתמש במשתנה user_data
            if (not save_to_messages_reflection_bot):
                data.add_and_update_user_data(user_input)

            # טיפול בשאלה הפתוחה או החזרה לשאלה הסגורה
            if st.session_state.current_question < len(questions):
                current_q = questions[st.session_state.current_question]

                # אם זו שאלה פתוחה, השאלה תטופל כאן
                if current_q["type"] == "open":
                    st.session_state.messages.append({"role": "assistant", "content": current_q["feedback"]})
                    # st.session_state.current_question += 1
                # אם זו שאלה סגורה, השאלה תוצג מחדש כדי שהמשתמש יבחר באחת האפשרויות
                elif current_q["type"] == "closed":
                    st.session_state.messages.append({"role": "assistant", "content": current_q["question"]})
        
        st.session_state.current_question += 1
        st.rerun()
        
def llm_function_finish_conversation():
    st.session_state.finish_conversation=True

def handle_llm(system_prompt_name):
    text=""
    if (system_prompt_name=="hegedim"):
        give_feedback_hegedim(st.session_state.messages)
    elif (system_prompt_name=="reflection"):
        give_feedback_reflection(st.session_state.messages)
    st.session_state.current_question += 1
    st.rerun()   
    
def handle_llm_his(system_prompt_name):
    gender=get_gender(st.session_state.messages)
    prompt=llm_manager.get_active_bot_1(gender)
    history=st.session_state.messages_bot_reflection
    if (len(history)==0):
        #llm with out history
        generate_claude_stream(prompt, "היי",save_to_messages=True)
    if (len(history)>0):
            generate_claude_stream_with_history(prompt, history,save_to_messages=True)
        
    st.session_state.current_question += 1
    st.rerun()
    
def get_gender(conversation_history):
    gender=crop_for_llm.return_gender_from_conversation(conversation_history)
    return gender
    
def give_feedback_hegedim(conversation_history):
    gender=crop_for_llm.return_gender_from_conversation(conversation_history)
    croped=crop_for_llm.crop_hegedim(conversation_history)
    hegedim_after_translation=translate_hegedim.translate_hegedim(croped)
    #gd.add_row_to_sheet2([hegedim_after_translation])

    string_format=crop_for_llm.data_to_string(hegedim_after_translation)

    generate_claude_stream(llm_manager.get_hegedim_prompt(gender),string_format)
  
    

def give_feedback_reflection(conversation_history):
    gender=crop_for_llm.return_gender_from_conversation(conversation_history)
    croped=crop_for_llm.crop_reflection(conversation_history)
    string_format=crop_for_llm.data_to_string(croped)
    #send_to_llm
    #gd.add_row_to_sheet2(["reflection:"])
    generate_claude_stream(llm_manager.get_reflection_prompt(gender),string_format)
    #text=llm_claude.return_llm_answer(string_format,reflection_prompt)
    



client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_claude_stream(system_prompt, user_prompt,save_to_messages=False):
    # try:
        # Create the stream
        with client.messages.stream(
            model="claude-3-7-sonnet-20250219", 
            temperature=0.5,
            max_tokens=1024,  
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        ) as stream:
        
            # Create a placeholder for the story
            story_placeholder = st.empty()
            full_response = " 🤖 "
        
            # Process each chunk of the response
            for chunk in stream:
                if chunk.type == "content_block_delta":
                    full_response += chunk.delta.text
                    story_placeholder.markdown(f'<div style="direction: rtl; text-align: right;">{full_response}</div>', unsafe_allow_html=True)

            # Show final response without cursor
            story_placeholder.markdown(f'<div style="direction: rtl; text-align: right;">{full_response}</div>', unsafe_allow_html=True)

            # Insert full_response to the history 
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            # gd.add_row_to_sheet2([full_response])  # אם צריך לשמור את התשובה
            if (save_to_messages):
                st.session_state.messages_bot_reflection.append({"role": "assistant", "content": full_response})
                
            return full_response  # מחזיר את התשובה המלאה

    # except APIError as e:
    #     st.warning(e)
    #     #print(f"שגיאת API: {e}")
    #     return ""  # מחזיר מחרוזת ריקה במקרה של שגיאה
    
    # except Exception as e:
    #     st.error("❌ שגיאה בלתי צפויה התרחשה.")
    #     #print(f"שגיאה כללית: {e}")
    #     return ""  # מחזיר מחרוזת ריקה עבור כל שגיאה אחרת

def end_conversation():
    st.session_state.finish_conversation=True
    to_save=st.session_state.messages_bot_reflection
    #save history
    
    #feedback hegedim
    handle_llm(current_q["system_prompt_name"])
    display_input_box(disabled=True,save_to_messages_reflection_bot=False)  # השבתת תיבת ה-input
    #show finish_text
    
    conversation.show_text("סיימנו את השיחה, תודה על השיחה!")
    # display_input_box(disabled=True,save_to_messages_reflection_bot=False)  # השבתת תיבת ה-input
    

def generate_claude_stream_with_history(system_prompt, messages,save_to_messages=False):#user_prompt, conversation_history=None,save_to_messages=False):
    # try:
        # Prepare messages list with history if provided
        # messages = []
        
        # # Add conversation history if provided
        # if conversation_history and len(conversation_history) > 0:
        #     for message in conversation_history:
        #         # Check if message is a dictionary before accessing 'role'
        #         if isinstance(message, dict) and message.get("role") in ["user", "assistant"]:
        #             messages.append({"role": message["role"], "content": message["content"]})
        
        # # Add the current user prompt
        # messages.append({"role": "user", "content": user_prompt})
        
        # Create the stream
        with client.messages.stream(
            model="claude-3-sonnet-20240229", 
            temperature=0.5,
            max_tokens=1024,  
            system=system_prompt,
            messages=messages
        ) as stream:
        
            # Create a placeholder for the story
            story_placeholder = st.empty()
            full_response = " "
        
            # Process each chunk of the response
            for chunk in stream:
                if chunk.type == "content_block_delta":
                    full_response += chunk.delta.text
                    story_placeholder.markdown(f'<div style="direction: rtl; text-align: right;">{full_response}</div>', unsafe_allow_html=True)
                    
                    # Check if "END" appears in the response
                    if "END" in full_response:
                        # Remove "END" from the response
                        full_response = full_response.replace("END", "")
                        st.session_state.finish_conversation = True

                        string_conversation= crop_for_llm.data_to_string(st.session_state.messages_bot_reflection)
                        data.add_and_update_user_data(string_conversation)
                        # st.session_state.user_data.append(string_conversation)
                        # end_conversation()
                        break  # Exit the loop if "END" is found

            # Show final response without cursor
            story_placeholder.markdown(f'<div style="direction: rtl; text-align: right;">{full_response}</div>', unsafe_allow_html=True)

            # Insert full_response to the history 
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            # gd.add_row_to_sheet2([full_response])  # אם צריך לשמור את התשובה
            if (save_to_messages):
                st.session_state.messages_bot_reflection.append({"role": "assistant", "content": full_response})
            return full_response  # מחזיר את התשובה המלאה

    # except APIError as e:
    #     st.warning("⚠️ מערכת עמוסה כרגע. נסה שוב בעוד כמה רגעים.")
    #     #print(f"שגיאת API: {e}")
    #     return ""  # מחזיר מחרוזת ריקה במקרה של שגיאה
    
    # except Exception as e:
    #     st.error("❌ שגיאה בלתי צפויה התרחשה.")
    #     #print(f"שגיאה כללית: {e}")
    #     return ""  # מחזיר מחרוזת ריקה עבור כל שגיאה אחרת

 

def show_selectbox_schools_question(question, feedbacks):
    # הצגת השאלה
    if st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]:
        conversation.display_bot_message_with_typing_effect(question)
        st.session_state.messages.append({"role": "assistant", "content": question})
        st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]=False

    # קבלת סוגי בתי הספר
    school_type = schools.School_Type.to_School_Type(st.session_state.grade)
    options = schools.return_schools_list(school_type)

    # יצירת Selectbox עבור הבחירה
    selected_option = st.selectbox(
        "",
        options,
        key=f"{st.session_state.current_question}_selectbox",
        index=None,
        placeholder="שם בית הספר שלך...",
    )
    
    # לחצן אישור לבחירת התשובה
    if st.button("אישור", key=f"{st.session_state.current_question}_confirm"):
        if selected_option is not None:  # בדיקה אם נבחרה תשובה
            # הוספת השאלה והתשובה להיסטוריה
            st.session_state.messages.append({"role": "user", "content": selected_option})

            # שמירת התשובה של המשתמש במשתנה user_data
            #st.session_state.user_data.append(selected_option)
            data.add_and_update_user_data(selected_option)

            # הוספת הפידבק לפי הבחירה
            # feedback_index = options.index(selected_option)  # אין בעיה כי בדקנו קודם
            # display_bot_message_with_typing_effect(feedbacks)
            st.session_state.messages.append({"role": "assistant", "content": feedbacks})
            st.session_state.current_question += 1
            st.rerun()
        else:
            # הודעת שגיאה אם לא נבחרה תשובה
            st.error("אנא בחר/י תשובה לפני שאתם ממשיכים.")


   

#MAIN#####
# כותרתt ru

# write_to_file.write_to_file("messages.txt")
st.markdown('<h1 class="main-title">מבט לרגע🚀</h1>', unsafe_allow_html=True)
# אתחול משתני session_state במידת הצורך
if 'messages' not in st.session_state:
        st.session_state.messages = []
        st.session_state.current_question = 0
        st.session_state.finished = False
        st.session_state.user_data = []  # אתחול המשתנה לאחסון התשובות
        st.session_state.is_counting_time= False 
        st.session_state.grade=[]
        st.session_state.write=True
        st.session_state.is_question_waiting_to_be_written=[True]*(len(questions))
        st.session_state.is_buttoms_needs_to_be_displayed=[True]*(len(questions))
        st.session_state.is_question_waiting_to_be_written_simulation=[True]*(1)
        st.session_state.close_question_answer=None
        st.session_state.question_stage=0
        st.session_state.simulation_id=None
        st.session_state.close_question_selection_i=None
        st.session_state.temp_history=[]
        st.session_state.is_correct_answer=None
        st.session_state.gd_line=None
        st.session_state.current_question_answer=""
        st.session_state.is_current_button_was_clicked=False
        st.session_state.messages_bot_reflection=[]
        # st.session_state.messages_bot_reflection.append({"role": "assistant", "content": active_sim.question})
        st.session_state.finish_conversation=False
        st.session_state.count_conversation_questions=0
        st.session_state.max_conversation_questions=15
    
    # הצגת היסטוריית השיחה
conversation.show_chat_history()


#checks if it counting time - stop time
# if (st.session_state.is_counting_time==True):
#                 stop_counting_time()

    # הצגת השאלה הנוכחית (אם עדיין לא סיימנו את כל השאלות)
if not st.session_state.finished:
        if st.session_state.current_question < len(questions):
            current_q = questions[st.session_state.current_question]
            match current_q["type"]:
                case("insert_data"):
                    data.update_data_in_sheet()
                case "open":
                    show_open_question(current_q["question"], current_q["feedback"])
                    display_input_box(disabled=False,save_to_messages_reflection_bot=False)  # הפעלת תיבת ה-input
                case "open_save":
                    if (not st.session_state.finish_conversation):
                        st.session_state.count_conversation_questions+=1
                        display_input_box(disabled=False,save_to_messages_reflection_bot=True)
                        # show_open_question_llm()
                    else :
                        # questions_to_pass=st.session_state.max_conversation_questions-st.session_state.count_conversation_questions-1
                        # st.session_state.current_question += questions_to_pass
                        st.session_state.current_question += 2
                        st.rerun()
                case "llm_history":
                    if (not st.session_state.finish_conversation):
                        st.session_state.count_conversation_questions+=1
                        handle_llm_his(current_q["system_prompt_name"])
                        display_input_box(disabled=True,save_to_messages_reflection_bot=False)  # השבתת תיבת ה-input
                    else :
                        # questions_to_pass=st.session_state.max_conversation_questions-st.session_state.count_conversation_questions-1
                        # st.session_state.current_question += questions_to_pass
                        st.session_state.current_question += 1
                        st.rerun()
                case "closed":
                    question=current_q["question"]
                    options=current_q["options"]
                    reflection=current_q["reflection"]
                    if (reflection =="True"):
                        is_correct_answer_in_simulation=st.session_state.is_correct_answer
                        if is_correct_answer_in_simulation:
                            question=question[0]
                            options=options[0]
                        else:
                            question=question[1]
                            options=options[1]
                    match st.session_state.question_stage:
                        case 0:show_closed_question(question, options,current_q["options_style"] ,current_q["feedbacks"],current_q["not_for_school_8"],current_q["not_for_school_10"])
                        case 1:show_closed_question2(current_q["feedback_type"],current_q["feedback_system_prompt_name"],current_q["feedbacks"])
                        #case 3:show_closed_question_other
                    display_input_box(disabled=True,save_to_messages_reflection_bot=False)  # השבתת תיבת ה-input
                #case "close_with_othewise"
                case "simulation":
                    stage=st.session_state.question_stage
                    match stage:
                        case 0:show_simulation0()
                        case 1:show_simulation1()
                        case 2:show_simulation2()
                    display_input_box(disabled=True,save_to_messages_reflection_bot=False)  # השבתת תיבת ה-input
                case "selectbox_schools":
                    show_selectbox_schools_question(current_q["question"], current_q["feedbacks"])
                    display_input_box(disabled=True,save_to_messages_reflection_bot=False)  # השבתת תיבת ה-input
                case "image":
                    conversation.display_bot_image(current_q["url"])
                    display_input_box(disabled=True,save_to_messages_reflection_bot=False)  # השבתת תיבת ה-input
                case "video":
                    conversation.display_bot_video(current_q["url"])
                    display_input_box(disabled=True,save_to_messages_reflection_bot=False)  # השבתת תיבת ה-input
                case "closed_grade":
                    show_closed_grade_question(current_q["question"], current_q["options"], current_q["feedbacks"], current_q["session_state_answer"])
                    display_input_box(disabled=True,save_to_messages_reflection_bot=False)  # השבתת תיבת ה-input
                case "text":
                    conversation.show_text(current_q["question"])
                    display_input_box(disabled=True,save_to_messages_reflection_bot=False)  # השבתת תיבת ה-input
                case "text_llm":
                        handle_llm(current_q["system_prompt_name"])
                        display_input_box(disabled=True,save_to_messages_reflection_bot=False)  # השבתת תיבת ה-input

                
            # if current_q["time_count"] == "yes":
            #     start_counting_time()
                
        else:
            st.session_state.finished = True

            
            # summary_message = llm.summerize_conversation(st.session_state.messages)
            
            # display_bot_message_with_typing_effect(summary_message)
            
            # st.session_state.messages.append({"role": "assistant", "content": summary_message})

            # השבתת תיבת ה-input בסיום השיחה
            display_input_box(disabled=True,save_to_messages_reflection_bot=False)

            
#            write_to_file.write_to_file(st.session_state.messages)
