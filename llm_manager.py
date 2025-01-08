import crop_for_llm
import llm_claude
import llm_gpt
import ids
import gd

reflection_prompt="""
המשתמש ענה על חידה. לאחר שענה נאמר לו האם התשובה היא נכונה או לא, והוצגו לו שאלות בנוגע לחוויה שלו בפתרון השאלה. 
אני רוצה שהתלמיד אשר מילא את השאלון ילמד משהו חדש על עצמו דרך הניתוח שלך את תשובותיו, אנא עשה זאת. 
מדובר בתלמיד בן 15, אנא התאם את השפה ואת הרמה בה הדברים כתובים, פשט את הדברים.
אנא נסה לאתר האם הנבדק מאופיין יותר במוטיבציית למידה או מוטבציית הישג, ושלב זאת בתשובתך באופן בהיר ונהיר
התלמיד לא מכיר את המושג מוטיבציית למידה ומוטיבציית הישג
סיים את ההודעה בברכת הצלחה.
"""

hamarat_hegedim_prompt="""
אנא המר את ההיגדים לאמירות של הנבדק על עצמו. 
למשל: "יש לי רצון לקחת על עצמי משימות שדורשות ממני להיות אחראי על אחרים", "לא דומה בכלל" = "אין לי רצון לקחת על עצמי משימות שדורשות ממני להיות אחראי על אחרים"

"יש לי נטיה להרגיש תחושות של נוסטלגיות על דברים שקרו בעבר שלי", "דומה" = "יש לי נטיה להרגיש תחושות של נוסטלגיות על דברים שקרו בעבר שלי"

"יש בי אמונה שאי אפשר באמת לתכנן את העתיד כי דברים משתנים כל הזמן", "קצת דומה" = "אני קצת מאמין שאי אפשר באמת לתכנן את העתיד כי דברים משתנים כל הזמן."
"""
hegedim_prompt="""
לפניך היגדים של נער או נערה בני 15. הפק מתוכו פרופיל פסיכולוגי אותו תכתוב בשפה שמותאמת לבני נוער.
התייחס לתמות של יחס לעבר, הווה ועתיד, התמודדות עם לחץ וקשיים, וערך עצמי.
עטוף את אזורי הקושי בחוזקות. בסוף תן לו חלק של "עתידות". 
כתוב זאת ישירות לנער או הנערה. המנע משימוש במושג "פרופיל פסיכולוגי"
"""

def give_feedback_reflection(conversation_history):
    croped=crop_for_llm.crop_reflection(conversation_history)
    string_format=crop_for_llm.data_to_string(croped)
    #send_to_llm
    text=llm_claude.return_llm_answer(string_format,reflection_prompt)
    return text
    
    
def give_feedback_hegedim(conversation_history):
    save_data=[]
    croped=crop_for_llm.crop_hegedim(conversation_history)
    string_format=crop_for_llm.data_to_string(croped)
    save_data.append(string_format)
    #send_to_llm for hamarat_hideim  #gpt4o
    # croped_string=conversation_history ## temporary
    tenslated_hegedim=llm_gpt.return_llm_answer(hamarat_hegedim_prompt,string_format)
    save_data.append(tenslated_hegedim) 
    #send_to_llm for hegedim
    text=llm_claude.return_llm_answer(tenslated_hegedim,hegedim_prompt)
    save_data.append(text)
    gd.add_row_to_sheet2(save_data)
    return text
    
    
    
# data = """
# {'role': 'assistant', 'content': 'יש לי רצון לקחת על עצמי משימות שדורשות ממני להיות אחראי/ת על אחרים. 💪'}
# {'role': 'user', 'content': '😐 קצת דומה'}
# {'role': 'assistant', 'content': 'קורה לי הרבה שאני חושב/ת על דברים רעים שקרו לי. 😞'}
# {'role': 'user', 'content': '🙂 דומה'}
# {'role': 'assistant', 'content': 'יש בי אמונה שאי אפשר באמת לתכנן את העתיד כי דברים משתנים כל הזמן. 🤷‍♂️'}
# {'role': 'user', 'content': '🙂 דומה'}
# {'role': 'assistant', 'content': 'גם תחת לחץ, יש לי יכולת להשאר בפוקוס ולחשוב באופן בהיר. 🔍'}
# {'role': 'user', 'content': '😃 דומה לחלוטין'}
# {'role': 'assistant', 'content': 'מייאש אותי לעשות משהו שאני אראה את התוצאות שלו רק בעוד הרבה זמן. 😓'}
# {'role': 'user', 'content': '😃 דומה לחלוטין'}
# {'role': 'assistant', 'content': 'יש לי נטייה להרגיש תחושות של נוסטלגיות על דברים שקרו בעבר שלי. 🌟'}
# {'role': 'user', 'content': '😐 קצת דומה'}
# {'role': 'assistant', 'content': 'תמיד אסיים את כל המטלות למחר לפני שאצא לבלות או לנוח בערב של אותו היום. ⏰'}
# {'role': 'user', 'content': '🙂 דומה'}
# {'role': 'assistant', 'content': 'תמיד אעמוד בהבטחות שלי לחברים או לכל אחד אחר כמו המורה או ההורים שלי. ✔️'}
# {'role': 'user', 'content': '🙁 לא כל כך דומה'}
# {'role': 'assistant', 'content': 'יש לי יכולת להשלים פרויקטים בזמן על ידי כך שאני משקיע/ה בהם לאורך זמן ולא רק ברגע האחרון. 🕰️'}
# {'role': 'user', 'content': '😡 לא דומה בכלל'},
# {'role': 'assistant', 'content': '🔄 מה המידה שהנאמר למטה זהה לתפיסה שלך את עצמך?'}
# {'role': 'assistant', 'content': 'יש לי צורך שמישהו אחר יפרגן ויחמיא לי על העבודה שלי כדי שאהיה מרוצה ממה שעשיתי. 🙌'}
# {'role': 'user', 'content': 'קצת כמוני 😐'}
# """
    
    
data = [
{'role': 'assistant', 'content': '👋 אתם עומדים למלא שאלון מטעם תכנית ההייטק...'},
{'role': 'assistant', 'content': 'מה המגדר שלך?'},
{'role': 'user', 'content': 'נקבה'},
{'role': 'assistant', 'content': 'באיזו כיתה את/ה?'},
{'role': 'user', 'content': 'כיתה י'},
{'role': 'assistant', 'content': 'תודה רבה'},
{'role': 'assistant', 'content': 'בחר את שם בית הספר שלך:'},
{'role': 'user', 'content': 'תיכון חדש דרכא - בת ים'},
{'role': 'assistant', 'content': 'תודה'},
{'role': 'user', 'content': 'עלחל'},
{'role': 'assistant', 'content': 'תודה'},
{'role': 'assistant', 'content': 'הרחבות (מלבד מתמטיקה ואנגלית) - אנא בחר/י את הקרוב ביותר'},
{'role': 'user', 'content': 'מגמות אומנותיות'},
{'role': 'assistant', 'content': 'האם את/ה מכיר/ה מישהו שעובד בהיי-טק?'},
{'role': 'user', 'content': 'מישהו שלא קשור למשפחה'},
{'role': 'assistant', 'content': 'האם אובחנת באופן רשמי עם אחד או יותר מהבאים?'},
{'role': 'user', 'content': 'לא אובחנתי'},
{'role': 'assistant', 'content': 'בחלק הקרוב יוצגו היגדים...'},
{'role': 'assistant', 'content': '🤔 באיזו מידה ההתנהגות למטה דומה לדרך שבה את/ה מתנהג?'},
{'role': 'assistant', 'content': 'יש לי רצון לקחת על עצמי משימות שדורשות ממני להיות אחראי/ת על אחרים. 💪'},
{'role': 'user', 'content': '😐 קצת דומה'},
{'role': 'assistant', 'content': 'קורה לי הרבה שאני חושב/ת על דברים רעים שקרו לי. 😞'},
{'role': 'user', 'content': '🙂 דומה'},
{'role': 'assistant', 'content': 'יש בי אמונה שאי אפשר באמת לתכנן את העתיד כי דברים משתנים כל הזמן. 🤷‍♂️'},
{'role': 'user', 'content': '🙂 דומה'},
{'role': 'assistant', 'content': 'גם תחת לחץ, יש לי יכולת להשאר בפוקוס ולחשוב באופן בהיר. 🔍'},
{'role': 'user', 'content': '😃 דומה לחלוטין'},
{'role': 'assistant', 'content': 'מייאש אותי לעשות משהו שאני אראה את התוצאות שלו רק בעוד הרבה זמן. 😓'},
{'role': 'user', 'content': '😃 דומה לחלוטין'},
{'role': 'assistant', 'content': 'יש לי נטייה להרגיש תחושות של נוסטלגיות על דברים שקרו בעבר שלי. 🌟'},
{'role': 'user', 'content': '😐 קצת דומה'},
{'role': 'assistant', 'content': 'תמיד אסיים את כל המטלות למחר לפני שאצא לבלות או לנוח בערב של אותו היום. ⏰'},
{'role': 'user', 'content': '🙂 דומה'},
{'role': 'assistant', 'content': 'תמיד אעמוד בהבטחות שלי לחברים או לכל אחד אחר כמו המורה או ההורים שלי. ✔️'},
{'role': 'user', 'content': '🙁 לא כל כך דומה'},
{'role': 'assistant', 'content': 'יש לי יכולת להשלים פרויקטים בזמן על ידי כך שאני משקיע/ה בהם לאורך זמן ולא רק ברגע האחרון. 🕰️'},
{'role': 'user', 'content': '😡 לא דומה בכלל'},
{'role': 'assistant', 'content': '🔄 מה המידה שהנאמר למטה זהה לתפיסה שלך את עצמך?'},
{'role': 'assistant', 'content': 'יש לי צורך שמישהו אחר יפרגן ויחמיא לי על העבודה שלי כדי שאהיה מרוצה ממה שעשיתי. 🙌'},
{'role': 'user', 'content': 'קצת כמוני 😐'}
]


# answer=give_feedback_hegedim(data)
# print(answer)
# answer=give_feedback_reflection(data)
# print(answer)
