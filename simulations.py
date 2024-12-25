# קובץ סימולציות עם רמות, שאלות, תשובות ומזהה ייחודי
from schools import School_Type


simulations = [
    {
        "school_type":"SCHOOL_8",
         "difficulty": "hard",
        "question": "איש אחד דובר אמת בימים א', ב', ג', ואיש אחר דובר אמת בימים ד', ה', ו'. בשבת שניהם דוברים אמת. יום אחד נפגשו ואמרו זה לזה: 'אתמול שיקרתי'. באיזה יום נפגשו?",
        "options": [
            "יום א'",
            "יום ב'",
            "יום ד'",
            "יום שבת"
        ],
       "correct_answer":"יום ד'"
    },
    {
        "school_type":"SCHOOL_8",
         "difficulty": "easy",
        "question": 
            """
            ישנם חמישה אנשים.
כל איש יכול או לשקר, או להגיד את האמת.

איש אחד אומר: ישנו רק שקרן אחד בלבד ביננו.
איש שני אומר: ישנם בדיוק שני שקרנים ביננו.
איש שלישי אומר: ישנם בדיוק שלושה שקרנים ביננו.
איש רביעי אומר: ישנם בדיוק ארבעה שקרנים ביננו.
איש חמישי אומר: ישנם בדיוק חמישה שקרנים ביננו.

מי דובר אמת?
            """,
        "options": [
            "איש מס' 1",
            "איש מס' 3",
            "איש מס' 4",
            "איש מס' 5"  
            ],
        "correct_answer":"איש מס' 5"  


    },
    {
        "school_type":"SCHOOL_10",
         "difficulty": "hard",
        "question": "איש אחד דובר אמת בימים א', ב', ג', ואיש אחר דובר אמת בימים ד', ה', ו'. בשבת שניהם דוברים אמת. יום אחד נפגשו ואמרו זה לזה: 'אתמול שיקרתי'. באיזה יום נפגשו?",
        "options": [
            "יום א'",
            "יום ב'",
            "יום ד'",
            "יום שבת"
        ],
        "correct_answer": "יום ד'"
    }
]

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


index = find_simulation_index("SCHOOL_8", "קשה")
print(index)
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
      
