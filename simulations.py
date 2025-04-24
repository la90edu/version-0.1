# קובץ סימולציות עם רמות, שאלות, תשובות ומזהה ייחודי
from schools import School_Type


simulations = [
    
        ### SCHOOL_8 HARD ###
{
    "school_type": "SCHOOL_8",
    "difficulty": "hard",
    "question": """
   כמה משלושים בתמונה?
""",
    "options": [
        "14",
        "18",
        "19",
        "24"
        # "יצור כחול ועגול ויצור אדום ומרובע"
    ],
    "correct_answer": "18",
    "image": "img/H_hard.png"
},

    ### SCHOOL_8 MEDIUM###
    {
    "school_type": "SCHOOL_8",
    "difficulty": "medium",
    "question": """
   מה המספרים הבאים בסדרה 1, 4, 10, 22, 46
""",
    "options": [
        "85, 133",
        "67, 88",
        "82, 126",
        "94, 190"
  
    ],
    "correct_answer": "94, 190",
    "image": ""
},
    
    ### SCHOOL_8 EASY ###
    {
    "school_type": "SCHOOL_8",
    "difficulty": "easy",
    "question": """
מה האותיות הבאות בסדרה א, ה, ט, י\"ג, י\"ז, __, __
""",
    "options": [
        "י\"ח, י\"ט",
        "כ, כ\"ג",
        "כ\"א, כ\"ח",
        "כ\"א, כ\"ה"
        # "גם אני חשבתי שהם לא צדקו"
    ],
    "correct_answer": "כ\"א, כ\"ה",
    "image": ""
},
    ### SCHOOL_10 HARD ###
    
    {
    "school_type": "SCHOOL_10",
    "difficulty": "hard",
    "question": """
    מה המספר במקום סימן השאלה?
    """,
    "options": [
        "23",
        "30",
        "32",
        "36"
    ],
    "correct_answer": "30",
    "image": "img/Y_hard.png"
},
    ### SCHOOL_10 MEDIUM ###
    {
    "school_type": "SCHOOL_10",
    "difficulty": "medium",
    "question": """מה המספר במקום סימן השאלה כאשר מוסיפים את סכום כלל הלבבות בשורה התחתונה, כלומר ירוק+כחול+אדום+ירוק+כחול+אדום?""",
    "options": [
        "28",
        "30",
        "31",   
        "32"
    ],
    "correct_answer": "30",
    "image": "img/Y_mid.png"
},
    ### SCHOOL_10 EASY ###
    {
    "school_type": "SCHOOL_10",
    "difficulty": "easy",
    "question": """
    מה התבנית הבאה בסדרה?
    """,
    "options": [
        "A",
        "B",
        "C",
        "D"
    ],
    "correct_answer": "A",
    "image": "img/Y_easy.png"
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
    


#return "id simulation" by :"school_type" and "level"
def find_simulation_index( school_type, difficulty_hebrew):
    #grade=School_Type.to_string(school_type) #school type in string 
    difficulty=translate_to_english(difficulty_hebrew)
    for i, simulation in enumerate(simulations):
        if (simulation["school_type"] == school_type):
            if simulation["difficulty"] == difficulty:
                return i  # מחזיר את האינדקס הראשון שבו שני התנאים מתקיימים
    return None  # מחזיר None אם לא נמצא



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

def return_simulation_image_by_id(id):
    if 0 <= id < len(simulations):  # בדיקת אינדקס תקין
        return simulations[id]["image"]  # מחזיר את השאלה
    else:
        return None  # מחזיר None אם האינדקס לא תקין

#return "true/false" by :"id", "student_answer"
def is_answer_correct(id,student_answer):
    correct_answer=simulations[id]["correct_answer"] 
    if (correct_answer==student_answer):
        return True
    else:
        return False


      
