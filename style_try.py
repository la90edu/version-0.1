# # import streamlit as st
# # # import pathlib
# from PIL import Image


# # image_path = "logo1.jpg"  # or "img/logo1.png" if it's a PNG file
# # image = Image.open(image_path)

# # st.image(image, use_column_width=False, width=200)


# # with st.chat_message('Momos', avatar="🤖"):
# #     st.write('Hello there!')
# # av="👤"
# # with st.chat_message('Me', avatar=av):
# #     st.write("Hi!")
    
# #     חדש

# # import streamlit as st
# # from PIL import Image

# # # פתיחת התמונה ושינוי גודלה
# # image = Image.open("logo1.jpg")  # יש להחליף בשם קובץ התמונה
# # new_width = 200  # קביעת רוחב חדש
# # new_height = int((new_width / image.width) * image.height)  # חישוב הגובה בהתאמה
# # resized_image = image.resize((new_width, new_height))

# # # הצגת התמונה בגודל מותאם
# # st.image(resized_image, use_column_width=False)

# import streamlit as st
# from PIL import Image
# import base64
# from io import BytesIO

# # פונקציה להמרת תמונה ל-Base64
# def image_to_base64(image):
#     buffered = BytesIO()
#     image.save(buffered, format="PNG")
#     return base64.b64encode(buffered.getvalue()).decode()

# # פתיחת התמונה ושינוי גודלה
# image = Image.open("logo1.jpg")  # יש להחליף בשם קובץ התמונה
# new_width = 200  # קביעת רוחב חדש
# new_height = int((new_width / image.width) * image.height)  # חישוב הגובה בהתאמה
# resized_image = image.resize((new_width, new_height))

# # המרת התמונה ל-Base64
# image_base64 = image_to_base64(resized_image)

# # הצגת התמונה במרכז
# st.markdown(
#     f"""
#     <div style="display: flex; justify-content: center;">
#         <img src="data:image/png;base64,{image_base64}" width="{new_width}"/>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

import streamlit as st
from PIL import Image

# פתיחת התמונה
image = Image.open("logo1.jpg")  # יש להחליף בשם קובץ התמונה

# שינוי גודל התמונה לחצי
new_width = image.width // 2
new_height = image.height // 2
resized_image = image.resize((new_width, new_height))

# הצגת התמונה במרכז עם התאמה רספונסיבית
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(resized_image, use_container_width=True)


with st.chat_message('Momos', avatar="🤖"):
        st.write('Hello there!')
        av="👤"
with st.chat_message('Me', avatar=av):
        st.write("Hi!")