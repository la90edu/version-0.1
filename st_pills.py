# import streamlit as st

# # הגדרת סגנון מותאם עבור pills
# st.markdown("""
# <style>
# .stPills {
#     display: flex;
#     justify-content: flex-end;  /* יישור לצד ימין */
#     gap: 10px;  /* מרווח בין הכפתורים */
# }

# .stPills [data-baseweb="pill"] {
#     background-color: purple !important;  /* רקע סגול קבוע */
#     color: white !important;  /* צבע טקסט לבן */
#     border-radius: 20px !important;
#     padding: 10px 15px !important;
#     margin: 0 !important;
#     transition: all 0.3s ease !important;
# }

# .stPills [data-baseweb="pill"]:hover {
#     background-color: darkviolet !important;
#     transform: scale(1.05);
# }

# .stPills [data-baseweb="pill"][aria-selected="true"] {
#     background-color: #8A2BE2 !important;  /* סגול בהיר יותר לבחירה */
#     box-shadow: 0 4px 6px rgba(0,0,0,0.2);
# }
# </style>
# """, unsafe_allow_html=True)

# # יצירת pills עם כמה אפשרויות
# options = ["תפוח", "בננה", "ענבים", "תות"]
# selected_pill = st.pills("בחר פרי:", options)

# # הצגת הערך הנבחר
# st.write(f"בחרת: {selected_pill}")

import streamlit as st
import st_pills2


# הגדרת סרגל הצד כפתוח כברירת מחדל
st.set_page_config(initial_sidebar_state="expanded")

def write_hello1():
    st.markdown("hello from page pills1")
    
# יצירת סרגל צד
with st.sidebar:
    st.header('תפריט אפשרויות')

# הצגת התוכן בהתאם לבחירה
st.header('ברוכים הבאים לדף הבית')
st.write('זהו העמוד הראשי של האפליקציה')
    
st_pills2.write_hello2()