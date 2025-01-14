import ids

hegedim_start_phrase =  '1. יש לי רצון לקחת על עצמי משימות שדורשות ממני להיות אחראי/ת על אחרים 💪'
reflection_start_phrase = "תשובתך היא:"

def crop_hegedim(data):
    filtered_data = [message for message in data if message["content"] is not None]
    data_returned=[]
    for i, item in enumerate(filtered_data):
        if hegedim_start_phrase in item.get('content', ''):
            data_returned= data[i:]
            data_returned.pop()
            data_returned.pop()
            return data_returned
    return []  # Return an empty list if the start_phrase is not found

def crop_reflection(data):
    #remove messages with no content (images, etc.)    
    filtered_data = [message for message in data if message["content"] is not None]

    data_returned=[]
    for i, item in enumerate(filtered_data):
        if reflection_start_phrase in item.get('content', ''):
            data_returned= data[i:]
            data_returned.pop()
            return data_returned
    return []  # Return an empty list if the start_phrase is not found


# data2 = [
#     {'role': 'assistant', 'content': '👋 אתם עומדים למלא שאלון מטעם תכנית ההייטק...'},
#     {'role': 'assistant', 'content': '🤔 באיזו מידה ההתנהגות למטה דומה לדרך שבה את/ה מתנהג?'},
#     {'role': 'assistant', 'content': ' יש לי רצון לקחת על עצמי משימות שדורשות ממני להיות אחראי/ת על אחרים. 💪'},
#     {'role': 'user', 'content': '😐 קצת דומה'},
# ]


def data_to_string(data):
    """
    מקבל רשימת אובייקטים עם role ו-content ומחזיר מחרוזת אחת
    """
    result = ""
    for item in data:
        result += f"{item}\n"
    return result.strip()

def return_gender_from_conversation(conversation):
    data=conversation[2]
    answer=data.get('content') 
    if (answer=="אעדיף לא לענות"):
        answer="זכר"
    return answer
    


# data = [
# {'role': 'assistant', 'content': '👋 אתם עומדים למלא שאלון מטעם תכנית ההייטק...'},
# {'role': 'assistant', 'content': 'מה המגדר שלך?'},
# {'role': 'user', 'content': 'נקבה'},
# {'role': 'assistant', 'content': 'באיזו כיתה את/ה?'},
# {'role': 'user', 'content': 'כיתה י'},
# {'role': 'assistant', 'content': 'תודה רבה'},
# {'role': 'assistant', 'content': 'בחר את שם בית הספר שלך:'},
# {'role': 'user', 'content': 'תיכון חדש דרכא - בת ים'},
# {'role': 'assistant', 'content': 'תודה'},
# {'role': 'user', 'content': 'עלחל'},
# {'role': 'assistant', 'content': 'תודה'},
# {'role': 'assistant', 'content': 'הרחבות (מלבד מתמטיקה ואנגלית) - אנא בחר/י את הקרוב ביותר'},
# {'role': 'user', 'content': 'מגמות אומנותיות'},
# {'role': 'assistant', 'content': 'האם את/ה מכיר/ה מישהו שעובד בהיי-טק?'},
# {'role': 'user', 'content': 'מישהו שלא קשור למשפחה'},
# {'role': 'assistant', 'content': 'האם אובחנת באופן רשמי עם אחד או יותר מהבאים?'},
# {'role': 'user', 'content': 'לא אובחנתי'},
# {'role': 'assistant', 'content': 'בחלק הקרוב יוצגו היגדים...'},
# {'role': 'assistant', 'content': '🤔 באיזו מידה ההתנהגות למטה דומה לדרך שבה את/ה מתנהג?'},
# {'role': 'assistant', 'content': 'יש לי רצון לקחת על עצמי משימות שדורשות ממני להיות אחראי/ת על אחרים. 💪'},
# {'role': 'user', 'content': '😐 קצת דומה'},
# {'role': 'assistant', 'content': 'קורה לי הרבה שאני חושב/ת על דברים רעים שקרו לי. 😞'},
# {'role': 'user', 'content': '🙂 דומה'},
# {'role': 'assistant', 'content': 'יש בי אמונה שאי אפשר באמת לתכנן את העתיד כי דברים משתנים כל הזמן. 🤷‍♂️'},
# {'role': 'user', 'content': '🙂 דומה'},
# {'role': 'assistant', 'content': 'גם תחת לחץ, יש לי יכולת להשאר בפוקוס ולחשוב באופן בהיר. 🔍'},
# {'role': 'user', 'content': '😃 דומה לחלוטין'},
# {'role': 'assistant', 'content': 'מייאש אותי לעשות משהו שאני אראה את התוצאות שלו רק בעוד הרבה זמן. 😓'},
# {'role': 'user', 'content': '😃 דומה לחלוטין'},
# {'role': 'assistant', 'content': 'יש לי נטייה להרגיש תחושות של נוסטלגיות על דברים שקרו בעבר שלי. 🌟'},
# {'role': 'user', 'content': '😐 קצת דומה'},
# {'role': 'assistant', 'content': 'תמיד אסיים את כל המטלות למחר לפני שאצא לבלות או לנוח בערב של אותו היום. ⏰'},
# {'role': 'user', 'content': '🙂 דומה'},
# {'role': 'assistant', 'content': 'תמיד אעמוד בהבטחות שלי לחברים או לכל אחד אחר כמו המורה או ההורים שלי. ✔️'},
# {'role': 'user', 'content': '🙁 לא כל כך דומה'},
# {'role': 'assistant', 'content': 'יש לי יכולת להשלים פרויקטים בזמן על ידי כך שאני משקיע/ה בהם לאורך זמן ולא רק ברגע האחרון. 🕰️'},
# {'role': 'user', 'content': '😡 לא דומה בכלל'},
# {'role': 'assistant', 'content': '🔄 מה המידה שהנאמר למטה זהה לתפיסה שלך את עצמך?'},
# {'role': 'assistant', 'content': 'יש לי צורך שמישהו אחר יפרגן ויחמיא לי על העבודה שלי כדי שאהיה מרוצה ממה שעשיתי. 🙌'},
# {'role': 'user', 'content': 'קצת כמוני 😐'}
# ]

# print(return_gender_from_conversation(data))

# print(crop_hegedim(data2))

# print(data_to_string(data))