import gd
import streamlit as st
import pandas as pd
import plotly.express as px

import schools_10th_grade
import schools_8th_grade

START_HEGEDIM_COL="heg_1"
START_REFLACTION_COL="ref_1"
# עיצוב מותאם אישית להצמדת התוכן לצד ימין
st.markdown(
    """
    <style>
    /* הגדרת כיוון הכתיבה לימין */
    .css-18e3th9 {
        direction: rtl;
    }
    /* מרכז את התוכן של היישום */
    .block-container {
        max-width: 90%;
        margin: 0 auto;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)
def return_hegedim_count(df_class_hegedim):
    school_counts_df_schools = df_class_hegedim["school"].value_counts().reset_index()
    school_counts_df_schools.columns = ["school", "count_hegedim"]
    temp_total_row = pd.DataFrame({"school": ["סה\"כ"], "count_hegedim": [school_counts_df_schools["count_hegedim"].sum()]})
    df_hegedim_after_concat = pd.concat([school_counts_df_schools, temp_total_row],axis=0)
    df_hegedim_after_concat.columns = ["שם בית הספר", "מספר ממלאי שאלון חלקי"]
    return df_hegedim_after_concat

def make_coloum_for_hegedim():
    data = gd.return_data()
    df_all = pd.DataFrame(data)
    df_with_hegedim = df_all[df_all[START_HEGEDIM_COL].notna() & (df_all[START_HEGEDIM_COL] != "")]
    return df_with_hegedim

def color_high_percentage(row):
    # נשנה את שם העמודה לשם המדויק שיש אצלך
    color = 'yellow' if row["percentage"] < 40 else ''
    return ['background-color: ' + color] * len(row)

#takes the data from googlesheet

data = gd.return_data()
df_all = pd.DataFrame(data)
df_with_reflection = df_all[df_all[START_REFLACTION_COL].notna() & (df_all[START_REFLACTION_COL] != "")]
st.dataframe(df_with_reflection)


st.title("הדמיית נתונים")

school_8_numbers= schools_8th_grade.schools_8_with_student_number
school_10_numbers= schools_10th_grade.schools_10_with_student_number
df_schools_8 = pd.DataFrame(list(school_8_numbers.items()), columns=["school", "student_count"])
df_schools_10 = pd.DataFrame(list(school_10_numbers.items()), columns=["school", "student_count"])
#st.dataframe(df_schools)

df = df_with_reflection
df_class_8_reflection = df[df["class"] == "class_8"]
df_class_10_reflection = df[df["class"] == "class_10"]

df_class_8_hegedim = df[df["class"] == "class_8"]
df_class_10_hegedim = df[df["class"] == "class_10"]



school_counts_df_schools_8 = df_class_8_reflection["school"].value_counts().reset_index()
school_counts_df_schools_8.columns = ["school", "count"]


#st.title("כיתה ח")
df_merged_schools_8= df_schools_8.merge(school_counts_df_schools_8, on="school", how="outer")
df_merged_schools_8.fillna(0, inplace=True)

df_merged_schools_8["percentage"] = ((df_merged_schools_8["count"] / df_merged_schools_8["student_count"]) * 100).fillna(0).astype(int)
# חישוב סכומים של העמודות המספריות
total_students_schools_8 = df_merged_schools_8["student_count"].sum()
total_count_scools_8 = df_merged_schools_8["count"].sum()
total_percentage_schools_8 = ((total_count_scools_8 / total_students_schools_8) * 100).astype(int)
# נניח שה-DataFrame שלך נקרא df והעמודה נקראת 'percentage'
#df['percentage'] = df['percentage'].astype(str) + '%'



# יצירת שורת סה"כ
total_row_schools_8 = pd.DataFrame({"school": ["סה\"כ"], "student_count": [total_students_schools_8], "count": [total_count_scools_8], "percentage": [total_percentage_schools_8]})

# הוספת השורה לטבלה
df_merged_schools_8 = pd.concat([df_merged_schools_8, total_row_schools_8], ignore_index=True)

hegedim=return_hegedim_count(df_class_8_hegedim)
##now to do concat between hegedim and df_merged_schools_8


styled_df_schools_8 = df_merged_schools_8.style.apply(color_high_percentage, axis=1)
#st.dataframe(styled_df_schools_8,height=550)



#### 10th grade
# school_counts_df = df_class_10["school"].value_counts().reset_index()
# school_counts_df.columns = ["school", "count"]
school_counts_df_schools_10 = df_class_10_reflection["school"].value_counts().reset_index()
school_counts_df_schools_10.columns = ["school", "count"]

#st.title("כיתה י")
df_merged_schools_10= df_schools_10.merge(school_counts_df_schools_10, on="school", how="outer")
df_merged_schools_10.fillna(0, inplace=True)
x=df_merged_schools_10["student_count"]
print (x)
df_merged_schools_10["percentage"] = ((df_merged_schools_10["count"] / df_merged_schools_10["student_count"]) * 100).fillna(0).astype(int)
# חישוב סכומים של העמודות המספריות
total_students_schools_10 = df_merged_schools_10["student_count"].sum()
total_count_scools_10 = df_merged_schools_10["count"].sum()
total_percentage_schools_10 = ((total_count_scools_10 / total_students_schools_10) * 100).astype(int)
# נניח שה-DataFrame שלך נקרא df והעמודה נקראת 'percentage'
#df['percentage'] = df['percentage'].astype(str) + '%'



# יצירת שורת סה"כ
total_row_schools_10 = pd.DataFrame({"school": ["סה\"כ"], "student_count": [total_students_schools_10], "count": [total_count_scools_10], "percentage": [total_percentage_schools_10]})

# הוספת השורה לטבלה
df_merged_schools_10 = pd.concat([df_merged_schools_10, total_row_schools_10], ignore_index=True)
#change coloms names
df = df.rename(columns={'student_count': 'סך התלמידים בכיתה', 'count': 'תלמידים שמילאו שאלון ','percentage':"  אחוז מילוי שאלון"})


styled_df_schools_10 = df_merged_schools_10.style.apply(color_high_percentage, axis=1)
#st.dataframe(styled_df_schools_10,height=700)



# יצירת שתי עמודות
col1, col2 = st.columns(2)

# הצגת DataFrame בעמודה הראשונה
with col1:
    st.subheader("כיתות ח")
    st.dataframe(styled_df_schools_8,height=550)

# הצגת DataFrame בעמודה השנייה
with col2:
    st.subheader("כיתות י")                 
    st.dataframe(styled_df_schools_10,height=600)


#היגדים 
df_with_hegedim = df_all[df_all[START_HEGEDIM_COL].notna() & (df_all[START_HEGEDIM_COL] != "")]
st.dataframe(df_with_hegedim)