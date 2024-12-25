import gd
import streamlit as st
import pandas as pd
import plotly.express as px

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

data = gd.return_data()
# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

st.title("הדמיית נתונים")
st.write("### נתונים גולמיים ")
st.dataframe(df)

# הצגת גרף בצורה פשוטה לפי העמודות הקיימות
if not df.empty:
    # נניח שהעמודה הראשונה היא קטגוריה והשנייה היא ערך מספרי
    category_column = df.columns[0]  # שם העמודה הראשונה
    value_column = df.columns[1]     # שם העמודה השנייה
    
    st.bar_chart(df.set_index(category_column)[value_column])
    
# הצגת גרף אינטראקטיבי לדוגמה
fig = px.line(df, x=category_column, y=value_column, title='')
st.plotly_chart(fig)
