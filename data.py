import streamlit as st
import data_translation
import gd
import date

def update_data_in_sheet():
    if  (st.session_state.gd_line==None):
             st.session_state.gd_line=gd.return_next_row()
             current_date=date.return_current_time()
             st.session_state.user_data=[current_date]+st.session_state.user_data
             
    user_data = st.session_state.user_data
    gd.add_data_to_the_row(st.session_state.gd_line, user_data)
    
    st.session_state.current_question += 1
    st.rerun()
    
def update_data_in_sheet_without_increasing_question_number():
    if  (st.session_state.gd_line==None):
             st.session_state.gd_line=gd.return_next_row()
    user_data = st.session_state.user_data
    gd.add_data_to_the_row(st.session_state.gd_line, user_data)
    


    
def add_and_update_user_data(data_to_add):
    data_after_translation=data_translation.get_content_by_key(data_to_add)
    st.session_state.user_data.append(data_after_translation)
        