# קובץ סימולציות עם רמות, שאלות, תשובות ומזהה ייחודי
from schools import School_Type


simulations = [
    
        ### SCHOOL_8 HARD ###
{
    "school_type": "SCHOOL_8",
    "difficulty": "hard",
    "question": """
    בלה הקוסמת נוהגת כלפי כל יצור שמגיע אל ביתה לפי הכלל הבא:
היא משנה כל יצור כחול לאדום וכל יצור עגול למרובע, אלא אם כן יצור מסוים הוא גם כחול גם עגול - במקרה כזה היא משאירה אותו כמות שהוא.
שני יצורים עגולים, שאחד מהם כחול והאחר אדום, הגיעו לביתה של בלה הקוסמת.
לפיכך, מן הבית יצאו -
""",
    "options": [
        "יצור כחול ועגול ויצור כחול ומרובע",
        "שני יצורים אדומים ומרובעים",
        "יצור כחול ומרובע ויצור אדום ומרובע",
        "יצור כחול ועגול ויצור אדום ומרובע"
    ],
    "correct_answer": "יצור כחול ועגול ויצור אדום ומרובע"
},

    ### SCHOOL_8 MEDIUM###
    {
    "school_type": "SCHOOL_8",
    "difficulty": "medium",
    "question": """טענה: מי שעיניו כחולות אינו יכול שלא לנהל יומן.
איזו מן האפשרויות הבאות סותרת את הטענה?""",
    "options": [
        "פנינה מנהלת יומן ועיניה כחולות",
        "פנינה מנהלת יומן ועיניה אינן כחולות",
        "פנינה אינה מנהלת יומן ועיניה כחולות",
        "פנינה אינה מנהלת יומן ועיניה אינן כחולות"
    ],
    "correct_answer": "פנינה אינה מנהלת יומן ועיניה כחולות"
},
    
    ### SCHOOL_8 EASY ###
    {
    "school_type": "SCHOOL_8",
    "difficulty": "easy",
    "question": """כל משפט שעידו אומר הוא נכון, אלא אם מופיעות בו שלוש המילים "גם", "אני" ו-"לא", ושתיים מהן, ולא יותר, צמודות זו לזו.
איזה מן המשפטים הבאים שאמר עידו איננו נכון?""",
    "options": [
        "גם הם לא חשבו שאתה צודק",
        "גם אני לא חשבתי שהם צודקים",
        "גם היום אני עדיין לא חושב שהם צודקים",
        "גם אני חשבתי שהם לא צדקו"
    ],
    "correct_answer": "גם אני חשבתי שהם לא צדקו"
},
    ### SCHOOL_10 HARD ###
    
    {
    "school_type": "SCHOOL_10",
    "difficulty": "hard",
    "question": """ליאת: "שום אדם אינו צנוע, אלא אם כן הוא חרוץ."
מיכל: "אינך צודקת. קחי לדוגמה את _____."

איזה מהאנשים הבאים יכול להיות הדוגמה שנתנה מיכל כדי להוכיח את טענתה?""",
    "options": [
        "אריק שהוא חרוץ וצנוע",
        "בני שהוא חרוץ אך אינו צנוע",
        "גולן שהוא צנוע אך אינו חרוץ",
        "דודו שאינו חרוץ ואינו צנוע"
    ],
    "correct_answer": "גולן שהוא צנוע אך אינו חרוץ"
},
    ### SCHOOL_10 MEDIUM ###
    {
    "school_type": "SCHOOL_10",
    "difficulty": "medium",
    "question": """- בת-שבע אוכלת מכל מאכל שמגיע אליה, ולעולם אינה אוכלת מאכלים מתוקים.
- יאיר אוכל מכל מה שבת-שבע אוכלת.

לשולחנם של בת-שבע ויאיר הוגשו קרקרים מלוחים ובוטנים מלוחים, עוגה מתוקה ותמרים מתוקים.

מה אינו אפשרי?""",
    "options": [
        "יאיר לא אכל קרקרים מלוחים",
        "יאיר לא אכל עוגה מתוקה",
        "בת-שבע אכלה בוטנים מלוחים",
        "יאיר אכל תמרים מתוקים"
    ],
    "correct_answer": "יאיר לא אכל קרקרים מלוחים"
},
    ### SCHOOL_10 EASY ###
    {
    "school_type": "SCHOOL_10",
    "difficulty": "easy",
    "question": """גברת כהן אפתה עוגיות עם שבבי שוקולד והניחה אותן במטבח להתקרר. כעבור חצי שעה, כשחזרה, מצאה את ארבעת ילדיה ניצבים מול הצלחת הריקה.

"טוב," היא הכריזה. "מי לקח את העוגיות?"

יונתן היה הראשון להגיב. "אני יודע מי לקח את העוגיות," הוא אמר.

אחיו אורי התערב ואמר: "זו לא הייתה תמר או נועה."

נועה מיהרה להתערב: "אורי אכל אותן!"

ואז הודתה תמר: "אני גנבתי את העוגיות."

גברת כהן ידעה שכל הילדים משקרים. אם היא צודקת, מי לקח את העוגיות?""",
    "options": [
        "יונתן",
        "אורי",
        "תמר",
        "נועה"
    ],
    "correct_answer": "נועה"
}
        
 ]       
        
        
#         ###
#         "school_type":"SCHOOL_8",
#          "difficulty": "hard",
#         "question": "איש אחד דובר אמת בימים א', ב', ג', ואיש אחר דובר אמת בימים ד', ה', ו'. בשבת שניהם דוברים אמת. יום אחד נפגשו ואמרו זה לזה: 'אתמול שיקרתי'. באיזה יום נפגשו?",
#         "options": [
#             "יום א'",
#             "יום ב'",
#             "יום ד'",
#             "יום שבת"
#         ],
#        "correct_answer":"יום ד'"
#     },
#     {
#         "school_type":"SCHOOL_8",
#          "difficulty": "easy",
#         "question": 
#             """
#             ישנם חמישה אנשים.
# כל איש יכול או לשקר, או להגיד את האמת.

# איש אחד אומר: ישנו רק שקרן אחד בלבד ביננו.
# איש שני אומר: ישנם בדיוק שני שקרנים ביננו.
# איש שלישי אומר: ישנם בדיוק שלושה שקרנים ביננו.
# איש רביעי אומר: ישנם בדיוק ארבעה שקרנים ביננו.
# איש חמישי אומר: ישנם בדיוק חמישה שקרנים ביננו.

# מי דובר אמת?
#             """,
#         "options": [
#             "איש מס' 1",
#             "איש מס' 3",
#             "איש מס' 4",
#             "איש מס' 5"  
#             ],
#         "correct_answer":"איש מס' 5"  


#     },
#     {
#         "school_type":"SCHOOL_10",
#          "difficulty": "hard",
#         "question": "איש אחד דובר אמת בימים א', ב', ג', ואיש אחר דובר אמת בימים ד', ה', ו'. בשבת שניהם דוברים אמת. יום אחד נפגשו ואמרו זה לזה: 'אתמול שיקרתי'. באיזה יום נפגשו?",
#         "options": [
#             "יום א'",
#             "יום ב'",
#             "יום ד'",
#             "יום שבת"
#         ],
#         "correct_answer": "יום ד'"
#     }


hebrew_levels = ["קל", "בינוני", "קשה"]
def return_hebrew_level():
        return hebrew_levels
    
def translate_to_english(level):
    translations = {
        "קל": "easy",
        "בינוני": "medium",
        "קשה": "hard"
    }
    return translations.get(level, "Translation not found")
    

# def return_options(school_Type):
#     match (school_Type):
#         case (School_Type.SCHOOL_8):
#             simulations=simulations_8_grade
#             return [simulation["level"] for simulation in simulations]
#         case (School_Type.SCHOOL_10):
#             simulations=simulations_10_grade
#             return [simulation["level"] for simulation in simulations]

#return "id simulation" by :"school_type" and "level"
def find_simulation_index( school_type, difficulty_hebrew):
    #grade=School_Type.to_string(school_type) #school type in string 
    difficulty=translate_to_english(difficulty_hebrew)
    for i, simulation in enumerate(simulations):
        if (simulation["school_type"] == school_type):
            if simulation["difficulty"] == difficulty:
                return i  # מחזיר את האינדקס הראשון שבו שני התנאים מתקיימים
    return None  # מחזיר None אם לא נמצא


# index = find_simulation_index("SCHOOL_8", "קשה")
# print(index)
# קריאה לפונקציה
# index = find_simulation_index(simulations, "10_grade", "hard")

# if index is not None:
#     print(f"Simulation found at index: {index}")
# else:
#     print("No simulation found matching the criteria.")

    
#return "simulation" by: "id"
def return_simulation_question_by_id(id):
    if 0 <= id < len(simulations):  # בדיקת אינדקס תקין
        return simulations[id]["question"]  # מחזיר את השאלה
    else:
        return None  # מחזיר None אם האינדקס לא תקין

#return "options" by: "id"
def return_simulation_options_by_id(id):
    if 0 <= id < len(simulations):  # בדיקת אינדקס תקין
        return simulations[id]["options"]  # מחזיר את השאלה
    else:
        return None  # מחזיר None אם האינדקס לא תקין



#return "true/false" by :"id", "student_answer"
def is_answer_correct(id,student_answer):
    correct_answer=simulations[id]["correct_answer"] 
    if (correct_answer==student_answer):
        return True
    else:
        return False


# id=find_simulation_index("8_grade","easy")
# answer=return_simulation_options_by_id(id)
# print(answer[3])
# #print(correct_answer=simulations[id]["correct_answer"] )
# is_currect=is_answer_correct(id,answer[3])
# print(is_currect )

# def return_simulation_by_id(school_type,id):
#     match (school_type):
#         case (School_Type.SCHOOL_8):
#             simulations=simulations_8_grade
#             for simulation in simulations:
#                 if simulation["id"] == id:
#                     return simulation["simulation"]
#             return None
#         case (School_Type.SCHOOL_10):
#             simulations=simulations_10_grade
#             for simulation in simulations:
#                 if simulation["id"] == id:
#                     return simulation["simulation"]
#             return None

# def return_answer_by_id(school_type,id):
#      match (school_type):
#         case (School_Type.SCHOOL_8):
#             simulations=simulations_8_grade
#             for simulation in simulations:
#                 if simulation["id"] == id:
#                     return simulation["answer"]
#             return None
#         case (School_Type.SCHOOL_10):
#             simulations=simulations_10_grade
#             for simulation in simulations:
#                 if simulation["id"] == id:
#                     return simulation["answer"]
#             return None
    
# print(return_answer_by_id(School_Type.SCHOOL_8,2))
# print(return_simulation_by_id(School_Type.SCHOOL_8,2))
      
