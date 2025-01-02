from anthropic import Anthropic
#from dotenv import load_dotenv
#load_dotenv()
import os
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def return_llm_answer(conversation,system_prompt):
    # # קריאת ה-system prompt מקובץ
    # try:
    #     with open('system.txt', 'r', encoding='utf-8') as file:
    #         system_prompt = file.read().strip()
    # except FileNotFoundError:
    #     print("שגיאה: הקובץ system.txt לא נמצא")
    #     return None
    
    user_prompt = conversation

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system=system_prompt,
        messages=[
           {"role":"user","content":user_prompt}
        ]
    )
    if isinstance(response.content, list):
        return '\n'.join(item.text if hasattr(item, 'text') else str(item) for item in response.content)
    return response.content[0].text if hasattr(response.content[0], 'text') else str(response.content)

# conversation = """
# {'role': 'assistant', 'content': 'תשובה נכונה'}
# {'role': 'assistant', 'content': '\n        עכשיו יוצגו בפניך שאלות לגבי המשימה שזה עתה ביצעת.\n        '}
# {'role': 'assistant', 'content': 'מה ההרגשה שלך לגבי ההתמודדות שלך עם השאלה?'}
# {'role': 'user', 'content': 'מאוד מרוצה'}
# {'role': 'assistant', 'content': 'היכולת לפתור את הבעיה גרמה לי'}
# {'role': 'user', 'content': 'להרגיש שהיה לי מזל והבעיה היתה קלה'}
# {'role': 'assistant', 'content': 'חבריך לכיתה התקשו בפתרון הבעיה הזו, למה לדעתך זה קרה?'}
# {'role': 'user', 'content': 'יכול להיות שחסר להם חלק מהידע הנדרש לפתרון'}
# {'role': 'assistant', 'content': 'כשאני נתקל/ת בבעיה מאתגרת אני'}
# {'role': 'user', 'content': 'מחכה עד שאני אדע לפתור אותן ואז מנסה'}
# {'role': 'assistant', 'content': 'הסיבה העיקרית שהצלחתי לפתור את הבעיה היא'}
# {'role': 'user', 'content': 'שילוב של היכולות שלי והמאמץ שהשקעתי'}
# {'role': 'assistant', 'content': 'אם אני אתמודד עם בעיה דומה ואתקשה בפתרון שלה'}
# {'role': 'user', 'content': 'ארגיש נבוכ/ה שאני לא מסוגל/ת לפתור אותה'}
# {'role': 'assistant', 'content': 'אם הייתי טועה בפתרון של הבעיה הנוכחית, אז'}
# {'role': 'user', 'content': 'אחשוש שהטעות יכולה להעיד על זה שאין לי את היכולות לפתור כזו בעיה'}
# {'role': 'assistant', 'content': 'כשניגשתי לבעיה הנוכחית'}
# {'role': 'user', 'content': 'מיד חיפשתי דרכים שכבר השתמשתי בהם לפתרון בעיות בעבר'}
# """

# # answer = return_llm_answer(conversation, "סכם את הטקסט")
# # print(answer)
# # # במקום להדפיס, נכתוב לקובץ
# # with open('text2.txt', 'a', encoding='utf-8') as file:
# #     file.write(answer)  