import ids

hegedim_start_phrase =  'יש לי רצון לקחת על עצמי משימות שדורשות ממני להיות אחראי/ת על אחרים. 💪'
reflection_start_phrase = "תשובתך היא:"

def crop_hegedim(data):
    for i, item in enumerate(data):
        if hegedim_start_phrase in item.get('content', ''):
            return data[i:]
    return []  # Return an empty list if the start_phrase is not found

def crop_reflection(data):
    for i, item in enumerate(data):
        if reflection_start_phrase in item.get('content', ''):
            return data[i:]
    return []  # Return an empty list if the start_phrase is not found

# def convert_to_string(data):
#     result = []
#     for item in data:
#         role = item.get('role', '')
#         content = item.get('content', '')
#         result.append(f"{{'role': '{role}', 'content': '{content}'}}")
#     #return "\n".join(result)
#     return result

# # Example usage
# data2 = [
#     {'role': 'assistant', 'content': '👋 אתם עומדים למלא שאלון מטעם תכנית ההייטק...'},
#     {'role': 'assistant', 'content': '🤔 באיזו מידה ההתנהגות למטה דומה לדרך שבה את/ה מתנהג?'},
#     {'role': 'assistant', 'content': ' יש לי רצון לקחת על עצמי משימות שדורשות ממני להיות אחראי/ת על אחרים. 💪'},
#     {'role': 'user', 'content': '😐 קצת דומה'},
#     # Add more data items here...
# ]


def data_to_string(data):
    """
    מקבל רשימת אובייקטים עם role ו-content ומחזיר מחרוזת אחת
    """
    result = ""
    for item in data:
        result += f"{item}\n"
    return result.strip()

# a=convert_to_string(data)
# print(a)


# def crop_and_change_to_string(data,start_phrase):
#     filtered_data = crop_hegedim(data, start_phrase)
#     if filtered_data==[]:
#         return []
#     else:
#         return convert_to_string(filtered_data)

# start_phrase = "🤔 באיזו מידה ההתנהגות למטה דומה לדרך שבה את/ה מתנהג?"
# filtered_data = crop_and_change_to_string(data, start_phrase)

# for entry in filtered_data:
#     print(entry)

# def crop_hegedim(data):
#     for i, item in enumerate(data):
#         if start_phrase in item.get('content', ''):
#             return data[i:]
#     return []  # Return an empty list if the start_phrase is not found


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

# # print(crop_hegedim(data))

# print(data_to_string(data))