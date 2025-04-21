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

import streamlit as st
import pandas as pd





# # הצגת ה-DataFrame הראשון בעמודה הראשונה
# with col1:
#     st.dataframe(df1, use_container_width=True)

# # הצגת ה-DataFrame השני בעמודה השנייה
# with col2:
#     st.dataframe(df2, use_container_width=True)




# def count_schools(df):
#     """
#     מקבלת DataFrame וסופרת את מספר הפעמים שכל בית ספר מופיע בעמודה 'school'.
    
#     :param df: DataFrame של פנדס המכיל את העמודה 'school'.
#     :return: DataFrame עם עמודות 'school' ו-'count' המציגות את מספר הפעמים שכל בית ספר מופיע.
#     """
#     if 'school' not in df.columns:
#         raise ValueError("העמודה 'school' לא קיימת ב-DataFrame")

#     # ספירת מופעים של כל בית ספר
#     school_counts = df['school'].value_counts().reset_index()
#     school_counts.columns = ['school', 'count']
    
#     return school_counts


# def count_schools_with_heg(df):
#     """
#     מקבלת DataFrame וסופרת:
#     1. כמה פעמים כל בית ספר מופיע בעמודה 'school'.
#     2. כמה פעמים יש ערך שאינו ריק בעמודה 'heg_27' לכל בית ספר.
    
#     :param df: DataFrame של פנדס המכיל את העמודות 'school' ו-'heg_27'.
#     :return: DataFrame עם ספירת בתי הספר וספירת הערכים הלא ריקים בעמודה 'heg_27'.
#     """
#     if 'school' not in df.columns:
#         raise ValueError("העמודה 'school' לא קיימת ב-DataFrame")
#     if 'heg_27' not in df.columns:
#         raise ValueError("העמודה 'heg_27' לא קיימת ב-DataFrame")

#     # ספירת מספר השורות לכל בית ספר
#     school_counts = df['school'].value_counts().reset_index()
#     school_counts.columns = ['school', 'total_count']

#     # ספירת מספר השורות עם ערכים לא ריקים בעמודה 'heg_27' לכל בית ספר
#     heg_counts = df.groupby('school')['heg_27'].apply(lambda x: x.notna().sum()).reset_index()
#     heg_counts.columns = ['school', 'heg_27_count']

#     # שילוב שתי הספירות
#     result = pd.merge(school_counts, heg_counts, on='school', how='left')

#     return result

def return_end_result_for_student_that_answer_reflection():
    data = gd.return_data()
    df_all = pd.DataFrame(data)
    df_with_reflection = df_all[df_all[START_REFLACTION_COL].notna() & (df_all[START_REFLACTION_COL] != "")]
    return df_with_reflection

st.title("מה אחוזי מילוי השאלון בבית הספר שלי?")

school_8_numbers= schools_8th_grade.schools_8_with_student_number
school_10_numbers= schools_10th_grade.schools_10_with_student_number
df_schools_8 = pd.DataFrame(list(school_8_numbers.items()), columns=["school", "student_count"])
df_schools_10 = pd.DataFrame(list(school_10_numbers.items()), columns=["school", "student_count"])
#st.dataframe(df_schools)

df = return_end_result_for_student_that_answer_reflection()
df_class_8 = df[df["class"] == "class_8"]
df_class_10 = df[df["class"] == "class_10"]



#st.dataframe(df_class_8)
school_counts_df_schools_8 = df_class_8["school"].value_counts().reset_index()
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

def color_high_percentage(row):
    # נשנה את שם העמודה לשם המדויק שיש אצלך
    color = 'red' if row["percentage"] < 40 else ''
    return ['background-color: ' + color] * len(row)

df_filtered_schools_8 = df_merged_schools_8.drop(columns=["student_count", "count"])

styled_df_schools_8 = df_filtered_schools_8.style.apply(color_high_percentage, axis=1)

#st.dataframe(styled_df_schools_8,height=550)



#### 10th grade
# school_counts_df = df_class_10["school"].value_counts().reset_index()
# school_counts_df.columns = ["school", "count"]
school_counts_df_schools_10 = df_class_10["school"].value_counts().reset_index()
school_counts_df_schools_10.columns = ["school", "count"]

#st.title("כיתה י")
df_merged_schools_10= df_schools_10.merge(school_counts_df_schools_10, on="school", how="outer")
df_merged_schools_10.fillna(0, inplace=True)

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
df_filtered_schools_10 = df_merged_schools_10.drop(columns=["student_count", "count"])


styled_df_schools_10 = df_filtered_schools_10.style.apply(color_high_percentage, axis=1)

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


#st.dataframe(df_schools)

# pivot_counts = data.pivot_table(index='school', columns='class', aggfunc='size', fill_value=0)
# pivot_counts['Total'] = pivot_counts.sum(axis=1)
# pivot_counts.loc['Grand Total'] = pivot_counts.sum(axis=0)

# student_8_max= schools_8th_grade.schools_8_with_student_number
# student_10_max= schools_10th_grade.schools_10_with_student_number

# st.dataframe(pivot_counts)




#pivot_counts_reflection = df_with_reflection.pivot_table(index='school', columns='class', aggfunc='size', fill_value=0)
# pivot_counts_reflection['Total'] = pivot_counts_reflection.sum(axis=1)
# pivot_counts_reflection.loc['Grand Total'] = pivot_counts_reflection.sum(axis=0)
# st.dataframe(pivot_counts_reflection)
# # school_counts_ref = df_with_reflection['school'].value_counts()


# data = gd.return_data()
# # Convert the data to a pandas DataFrame
# df_all = pd.DataFrame(data)
# st.dataframe(df_all)

# # pivot_counts_all = df_all.pivot_table(index='school', columns='class', aggfunc='size', fill_value=0)
# # pivot_counts_all['Total'] = pivot_counts_all.sum(axis=1)
# # pivot_counts_all.loc['Grand Total'] = pivot_counts_all.sum(axis=0)
# # st.dataframe(pivot_counts_all)

# # school_counts_all = df_all['school'].value_counts()
# # st.dataframe(school_counts_all)

# df_with_hegedim = df_all[df_all[START_HEGEDIM_COL].notna() & (df_all[START_HEGEDIM_COL] != "")]
# st.dataframe(df_with_hegedim)

# pivot_counts_hegedim = df_with_hegedim.pivot_table(index='school', columns='class', aggfunc='size', fill_value=0)
# pivot_counts_hegedim['Total'] = pivot_counts_hegedim.sum(axis=1)
# pivot_counts_hegedim.loc['Grand Total'] = pivot_counts_hegedim.sum(axis=0)
# st.dataframe(pivot_counts_hegedim)

# df_with_reflection = df_all[df_all[START_REFLACTION_COL].notna() & (df_all[START_REFLACTION_COL] != "")]
# st.dataframe(df_with_reflection)

# pivot_counts_reflection = df_with_reflection.pivot_table(index='school', columns='class', aggfunc='size', fill_value=0)
# pivot_counts_reflection['Total'] = pivot_counts_reflection.sum(axis=1)
# pivot_counts_reflection.loc['Grand Total'] = pivot_counts_reflection.sum(axis=0)
# st.dataframe(pivot_counts_reflection)
# # school_counts_ref = df_with_reflection['school'].value_counts()
# # st.dataframe(school_counts_ref)

# # איחוד הטבלאות על בסיס האינדקס (school)
# merged_pivot = pivot_counts_hegedim.join(pivot_counts_reflection, lsuffix='_hegedim', rsuffix='_reflection')

# # הצגת הטבלה
# st.dataframe(merged_pivot)



# result = count_schools_with_heg(df)
# st.write(result)

# st.title("הדמיית נתונים")
# st.write("### נתונים גולמיים ")
# st.dataframe(df)

# הצגת גרף בצורה פשוטה לפי העמודות הקיימות
# if not df.empty:
#     # נניח שהעמודה הראשונה היא קטגוריה והשנייה היא ערך מספרי
#     category_column = df.columns[0]  # שם העמודה הראשונה
#     value_column = df.columns[1]     # שם העמודה השנייה
    
#     st.bar_chart(df.set_index(category_column)[value_column])
    
# # הצגת גרף אינטראקטיבי לדוגמה
# fig = px.line(df, x=category_column, y=value_column, title='')
# st.plotly_chart(fig)
