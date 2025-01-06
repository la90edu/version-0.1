
import streamlit as st
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
from after_simulation import ReflectiveQuestions
import write_to_file
import llm_manager

st.set_page_config(
    page_title="מבט לרגע",
    page_icon="🚀",  # אייקון של בוט
    layout="wide",  # הגדרה לתצוגה רחבה
)


# # פונקציה להמרת תמונה ל-base64
# def img_to_base64(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode('utf-8')

# # המרת התמונה ל-base64
# try:
#     img_base64 = img_to_base64("mop_logo.jpg")
#     avatar_img = f"data:image/jpeg;base64,{img_base64}"
# except Exception as e:
#     avatar_img = ""

st.markdown(
     """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700&display=swap');

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

# def show_closed_question_new(question,options):
    # display_bot_message_with_typing_effect(question)
    # #st.text("hey")
    # #options = ["North", "East", "South", "West"]
    # selection = st.pills("Directions", options, selection_mode="single")
    # st.session_state.close_question_answer=selection
    # st.session_state.close_question_stage=1
    # return()

def add_and_update_user_data(data_to_add):
    st.session_state.user_data.append(data_to_add)
    user_data = st.session_state.user_data
    gd.add_row_to_sheet(user_data)
    
def feedback_after_selection():
    selection=st.session_state.close_question_answer
    st.markdown(f"Your selected options: {selection}.")
    st.session_state.messages.append({"role": "user", "content": selection})

            # שמירת התשובה של המשתמש במשתנה user_data
    st.session_state.user_data.append(selection)
    

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
    
def start_counting_time():
                st.session_state.is_counting_time=True
                ti.begin()
                
    
def stop_counting_time():
                st.session_state.is_counting_time=False
                response_time_count=ti.end()
                st.session_state.user_data.append(response_time_count)

def show_simulation0():
    q1="בחר דרגת קושי "
    q2="פטרו את השאלה הבאה"

    if (st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]):
        display_bot_message_with_typing_effect(q1)
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
            st.session_state.user_data.append(level)
            # st.session_state.simulation_id=i
            
            st.session_state.question_stage=1
            #step 2 
            simulation_id=simulations.find_simulation_index(string_grade,level)
            st.session_state.simulation_id=simulation_id

            st.rerun()

def show_simulation1():
    simulation_question=simulations.return_simulation_question_by_id(st.session_state.simulation_id)
    
    if (st.session_state.is_question_waiting_to_be_written_simulation[0]):
        display_bot_message_with_typing_effect(simulation_question)
        start_counting_time() ##start counting time of simulations
        st.session_state.messages.append({"role": "assistant", "content": simulation_question})
        st.session_state.is_question_waiting_to_be_written_simulation[0]=False
          
           
    
    options=simulations.return_simulation_options_by_id(st.session_state.simulation_id)
    cols = st.columns(len(options))
    for i, option in enumerate(options):
         if cols[i].button(option, key=f"{st.session_state.current_question}_{option}"):
    #         # הוספת השאלה והתשובה להיסטוריה
    #         st.session_state.messages.append({"role": "assistant", "content": q1})
            st.session_state.messages.append({"role": "user", "content": option})
            
    #          # שמירת התשובה של המשתמש במשתנה user_data
            st.session_state.user_data.append(option)
            stop_counting_time() #stop time counting
            is_correct_answer=simulations.is_answer_correct(st.session_state.simulation_id,option)
            stam=simulations.is_answer_correct
            st.session_state.is_correct_answer=is_correct_answer
            st.session_state.user_data.append(is_correct_answer)
            #after_simulation.is_correct_answer=is_correct_answer
            #after_simulation.update_simulation_answer(is_correct_answer)
            # questions2.is_simulation_correct=is_correct_answer
            ReflectiveQuestions.simulation_answer=is_correct_answer
            x=ReflectiveQuestions.simulation_answer
            st.session_state.question_stage=2  
            st.rerun()         
    
def show_simulation2():

    if st.session_state.is_correct_answer:
        display_bot_message_with_typing_effect("תשובתך היא:")
        st.session_state.messages.append({"role": "assistant", "content": "תשובתך היא:"})

        display_bot_message_with_typing_effect("תשובה נכונה")
        st.session_state.messages.append({"role": "assistant", "content": "תשובה נכונה"})

    else:
        display_bot_message_with_typing_effect("תשובתך היא:")
        st.session_state.messages.append({"role": "assistant", "content": "תשובתך היא:"})
        
        display_bot_message_with_typing_effect("תשובה שגויה")   
        st.session_state.messages.append({"role": "assistant", "content": "תשובה שגויה"})

        
    st.session_state.question_stage=0
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

def display_bot_message_with_typing_effect(text, typing_speed=0.03):
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
    

    
st.logo("logo1.jpg")#,size="large")
 
#questions functions
def show_closed_question(question, options,options_style, feedbacks,not_for_school_8): 
    if ((not_for_school_8=="True")and(st.session_state.grade=='SCHOOL_8')):
        st.session_state.user_data.append("ללא")
        st.session_state.current_question += 1
        st.rerun()
    else:     
        if st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]:
            display_bot_message_with_typing_effect(question)
            st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]=False

    #options_style="vertical"
    
        match options_style:
            case "horizontal":
                # יצירת כפתורים לבחירת תשובה
                    cols = st.columns(len(options))
                    for i, option in enumerate(options):
                        if cols[i].button(option, key=f"{st.session_state.current_question}_{option}"):
                            st.session_state.messages.append({"role": "assistant", "content": question})
                            st.session_state.messages.append({"role": "user", "content": option})

                            st.session_state.temp_history.append({"role": "assistant", "content": question})
                            st.session_state.temp_history.append({"role": "user", "content": option})

                        # שמירת התשובה של המשתמש במשתנה user_data
                            st.session_state.user_data.append(option)
            
                            st.close_question_selection_i = i
                            st.session_state.question_stage = 1
                            st.rerun()
                        
            case "vertical":
                    for i, option in enumerate(options):
                        if st.button(option, key=f"{st.session_state.current_question}_{option}"):
                        # הוספת השאלה והתשובה להיסטוריה
                            st.session_state.messages.append({"role": "assistant", "content": question})
                            st.session_state.messages.append({"role": "user", "content": option})

                            st.session_state.temp_history.append({"role": "assistant", "content": question})
                            st.session_state.temp_history.append({"role": "user", "content": option})

                        # שמירת התשובה של המשתמש במשתנה user_data
                            st.session_state.user_data.append(option)
            
                            st.close_question_selection_i = i
                            st.session_state.question_stage = 1
                            st.rerun()
            
          
def show_closed_question2(feedback_type,system_prompt_name,auto_feedbacks):
     # הוספת הפידבק
            #feedback=""
        match feedback_type:
                case "auto":
                    i=st.close_question_selection_i
                    feedback=auto_feedbacks[i]
                    display_bot_message_with_typing_effect(feedback)#feedbacks[i])
                    st.session_state.messages.append({"role": "assistant", "content": feedback})#feedbacks[i]})
                case "llm":
                    user=next((entry['content'] for entry in reversed(st.session_state.temp_history) if entry['role'] == 'user'), None)
                    assistant=last_assistant_content = next((entry['content'] for entry in reversed(st.session_state.temp_history) if entry['role'] == 'assistant'), None)

                    feedback=llm_gpt.return_llm_answer(system_prompt_name,assistant,user)
                    st.session_state.temp_history=[]
                    display_bot_message_with_typing_effect(feedback)#feedbacks[i])
                    st.session_state.messages.append({"role": "assistant", "content": feedback})#feedbacks[i]})
                case "none":
                    feedback=""
                    
        st.session_state.current_question += 1
        st.session_state.question_stage=0

        st.rerun()

def show_closed_grade_question(question, options,feedbacks, session_state_answer):
    # time.sleep(0.5)  # הוספת השהיה של 0.5 שניות
        
    if (st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]):
        display_bot_message_with_typing_effect(question)
        st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]=False
    cols = st.columns(len(options))
    for i, option in enumerate(options):
        if cols[i].button(option, key=f"{st.session_state.current_question}_{option}"):
            # הוספת השאלה והתשובה להיסטוריה
            st.session_state.messages.append({"role": "assistant", "content": question})
            st.session_state.messages.append({"role": "user", "content": option})

            # שמירת התשובה של המשתמש במשתנה user_data
            st.session_state.user_data.append(option)
            # שמירת הכיתה במשתשנה בsession_state
            grade=session_state_answer[i]
            st.session_state.grade=grade
            
            # הוספת הפידבק
            display_bot_message_with_typing_effect(feedbacks[i])
            st.session_state.messages.append({"role": "assistant", "content": feedbacks[i]})
            st.session_state.current_question += 1
            st.rerun()
    
# פונקציה להצגת שאלה פתוחה
def show_open_question(question, feedback):
    # הצגת השאלה הפתוחה מהבוט
    time.sleep(0.5)  # הוספת השהיה של 0.5 שניות

    if st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]:
        display_bot_message_with_typing_effect(question)
        st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]=False
 
# פונקציה להצגת היסטוריית השיחה
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

       

# פונקציה להצגת תיבת הקלט הקבועה בתחתית
def display_input_box(disabled):
    user_input = st.chat_input("הכנס את התשובה שלך כאן", disabled=disabled)
    
    if user_input:
        # אם המשתמש מקליד לאחר סיום השאלות, נוסיף להיסטוריה בלבד
        if st.session_state.current_question >= len(questions):
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.messages.append({"role": "assistant", "content": "תודה! השיחה הסתיימה, אבל אני כאן לשמוע אם יש עוד משהו שתרצה לשתף."})
        # אם המשתמש מקליד תשובה לשאלה פתוחה
        elif not disabled:
            # הוספת התשובה להיסטוריה
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # שמירת התשובה של המשתמש במשתנה user_data
            st.session_state.user_data.append(user_input)

            # טיפול בשאלה הפתוחה או החזרה לשאלה הסגורה
            if st.session_state.current_question < len(questions):
                current_q = questions[st.session_state.current_question]

                # אם זו שאלה פתוחה, השאלה תטופל כאן
                if current_q["type"] == "open":
                    st.session_state.messages.append({"role": "assistant", "content": current_q["feedback"]})
                    st.session_state.current_question += 1
                # אם זו שאלה סגורה, השאלה תוצג מחדש כדי שהמשתמש יבחר באחת האפשרויות
                elif current_q["type"] == "closed":
                    st.session_state.messages.append({"role": "assistant", "content": current_q["question"]})
            
        st.rerun()
        
def show_text(text):
    #if st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]:
    display_bot_message_with_typing_effect(text)
        #st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]=False
    st.session_state.messages.append({"role": "assistant", "content": text})
    st.session_state.current_question += 1

    st.rerun()

def handle_llm(system_prompt_name):
    text=""
    if (system_prompt_name=="hegedim"):
        text=llm_manager.give_feedback_hegedim(st.session_state.messages)
    elif (system_prompt_name=="reflection"):
        text=llm_manager.give_feedback_reflection(st.session_state.messages)
    show_text(text)


def show_selectbox_schools_question(question, feedbacks):
    # הצגת השאלה
    if st.session_state.is_question_waiting_to_be_written[st.session_state.current_question]:
        display_bot_message_with_typing_effect(question)
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
        # הוספת השאלה והתשובה להיסטוריה
        st.session_state.messages.append({"role": "assistant", "content": question})
        st.session_state.messages.append({"role": "user", "content": selected_option})

        # שמירת התשובה של המשתמש במשתנה user_data
        st.session_state.user_data.append(selected_option)

        # הוספת הפידבק לפי הבחירה
        feedback_index = options.index(selected_option)
        display_bot_message_with_typing_effect(feedbacks)
        st.session_state.messages.append({"role": "assistant", "content": feedbacks})
        st.session_state.current_question += 1
        st.rerun()
        

#MAIN#####
# כותרת

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

    # הצגת היסטוריית השיחה
show_chat_history()


#checks if it counting time - stop time
# if (st.session_state.is_counting_time==True):
#                 stop_counting_time()

    # הצגת השאלה הנוכחית (אם עדיין לא סיימנו את כל השאלות)
if not st.session_state.finished:
        if st.session_state.current_question < len(questions):
            current_q = questions[st.session_state.current_question]
            match current_q["type"]:
                case "open":
                    show_open_question(current_q["question"], current_q["feedback"])
                    display_input_box(disabled=False)  # הפעלת תיבת ה-input
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
                        case 0:show_closed_question(question, options,current_q["options_style"] ,current_q["feedbacks"],current_q["not_for_school_8"])
                        case 1:show_closed_question2(current_q["feedback_type"],current_q["feedback_system_prompt_name"],current_q["feedbacks"])
                        #case 3:show_closed_question_other
                    display_input_box(disabled=False)  # השבתת תיבת ה-input
                #case "close_with_othewise"
                case "simulation":
                    stage=st.session_state.question_stage
                    match stage:
                        case 0:show_simulation0()
                        case 1:show_simulation1()
                        case 2:show_simulation2()
                    display_input_box(disabled=True)  # השבתת תיבת ה-input
                case "selectbox_schools":
                    show_selectbox_schools_question(current_q["question"], current_q["feedbacks"])
                    display_input_box(disabled=True)  # השבתת תיבת ה-input
                case "image":
                    display_bot_image(current_q["url"])
                    display_input_box(disabled=True)  # השבתת תיבת ה-input
                case "video":
                    display_bot_video(current_q["url"])
                    display_input_box(disabled=True)  # השבתת תיבת ה-input
                case "closed_grade":
                    show_closed_grade_question(current_q["question"], current_q["options"], current_q["feedbacks"], current_q["session_state_answer"])
                    display_input_box(disabled=True)  # השבתת תיבת ה-input
                case "text":
                    show_text(current_q["question"])
                    display_input_box(disabled=True)  # השבתת תיבת ה-input
                case "text_llm":
                    handle_llm(current_q["system_prompt_name"])
                    display_input_box(disabled=True)  # השבתת תיבת ה-input

                
            # if current_q["time_count"] == "yes":
            #     start_counting_time()
                
        else:
            st.session_state.finished = True

            
            # summary_message = llm.summerize_conversation(st.session_state.messages)
            
            # display_bot_message_with_typing_effect(summary_message)
            
            # st.session_state.messages.append({"role": "assistant", "content": summary_message})

            # השבתת תיבת ה-input בסיום השיחה
            display_input_box(disabled=True)

            user_data = st.session_state.user_data
            gd.add_row_to_sheet(user_data)
            
#            write_to_file.write_to_file(st.session_state.messages)
    

