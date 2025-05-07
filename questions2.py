import schools
import ids
from after_simulation import ReflectiveQuestions
import active_sim

ids_levels1 = [
     "😄 מתארת אותי בול",
    "😊  מתארת אותי לא רע",
    "😐 קצת מתארת אותי",
    "🙁 לא מתארת אותי ",
    "😡 ממש לא מתארת אותי "
     
       
]

ids_levels2 = [
    "בדיוק כמוני 😄",  
    " כמוני 🙂",         
    "קצת כמוני 😐",     
    "קצת לא כמוני 😕", 
    "כלל לא כמוני 🙁"   
]

ids_levels3= [
    "😄 מתאר אותי במדויק",
    "😊 מתאר אותי",
    "😐 מתאר אותי מעט",
    "🙁 לא ממש מתאר אותי ",
    "😡 כלל לא מתאר אותי "
]


# is_simulation_correct=None

questions = [
    
     
    {
        "question": """
כיף שהצטרפת לתוכנית ההייטק הלאומית🤩

ב-10-15 דק' הקרובות 
ארצה ללמוד עלייך כמה דברים

✔️ קצת עלייך ומה עושה ביום יום  

✔️ החוזקות שלך 

✔️ איך מתמודד/ת עם אתגרים 

קח/י בחשבון 
שהכל אנונימי לגמרי,
ככה שתיקח/י את הזמן להגיב ולענות, 

ומה הקשר לבינה מלאכותית? 
מלא/י עד הסוף ותגלה/י 🚀
        """,
        "type": "text",  
        "time_count":"no"
    },
    {
        "question": "מה המגדר שלך?",
        "type": "closed",  # שאלה סגורה
        "options": [
            "אעדיף לא לענות",
            "נקבה",
           "זכר"
        ],
        "options_style":"horizontal",
        "feedbacks": ["הבנתי.זכר תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name":'common_feedback',
        "feedback_type":"none",
        "reflection"  : "False",
        "not_for_school_8":"False",
        "not_for_school_10":"False",
        "time_count":"no"
    },
     
    {
        "question": "באיזו כיתה את/ה?",
        "type": "closed_grade",  # שאלה סגורה
        "options": [ "כיתה י", "כיתה ח"],
        "session_state_answer":["SCHOOL_10","SCHOOL_8"],
        "feedbacks": ["תודה רבה",
                      "תודה רבה",
                      "תודה רבה",
                      "תודה רבה"],
        "feedback_type":"auto",
        "time_count":"no"
    },
    
    
     
    {
        "question": "בחר/י את שם בית הספר שלך:",
        "type": "selectbox_schools",  # שאלה מסוג Selectbox
        "options": "null" ,#["אפק", "גוונים", "בגין"],  # שמות בתי הספר
        "feedbacks": "תודה",
        "feedback_type":"auto",
        "time_count":"no"
    },
    

    
    {
        "question": """
אנא כתב/י את הפעילויות שאת/ה משתתפ/ת בהן מחוץ לבית הספר למשל חוגים, אימונים, תנועות נוער וכו
""",
        "type": "open",  # שאלה פתוחה
        "feedback": "תודה",
        "time_count":"no",
    },
    
    {
        "question": """
        הרחבות (בנוסף למתמטיקה, אנגלית, פיזיקה/מדמ"ח), אנא בחר/י את הקרוב ביותר
        """,
        "type": "closed",  # שאלה סגורה
        "options":[
             "אין הרחבות נוספות",
             "מגמות טכנולוגיות", 
             "מגמות מדעיות", 
             "מגמות שפה",
             "מגמות אומנותיות",
             "מגמות מדעי החברה", 
             "מגמות מדעי הרוח", 
             "אחר"
             ],
        "options_style":"horizontal",
        "feedbacks": [],
        "feedback_system_prompt_name":'common_feedback',
        "feedback_type":"none",
        "reflection"  : "False",
        "not_for_school_8":"True",
        "not_for_school_10":"False",
        "time_count":"no"
    },
    
     
    {
        "question": """
        בהסתכלות קדימה לקראת שנה הבאה, האם היית רוצה לפרוש מ-5 יחידות מתמטיקה?
        """,
        "type": "closed",  # שאלה סגורה
        "options":[
             "בוודאי",
             "כנראה שכן", 
             "כנראה שלא", 
             "בוודאות לא"
             ],
        "options_style":"horizontal",
        
        "feedbacks": [],
        "feedback_system_prompt_name":'common_feedback',
        "feedback_type":"none",
        "reflection"  : "False",
        "not_for_school_8":"True",
        "not_for_school_10":"False",
        "time_count":"no"
    },
    
     {
        "question": """
בהסתכלות קדימה לקראת שנת התיכון, האם היית רוצה ללמוד 5 יחידות מתמטיקה?        """,
        "type": "closed",  # שאלה סגורה
        "options":[
             "בוודאי",
             "כנראה שכן", 
             "כנראה שלא", 
             "בוודאות לא"
             ],
        "options_style":"horizontal",
        
        "feedbacks": [],
        "feedback_system_prompt_name":'common_feedback',
        "feedback_type":"none",
        "reflection"  : "False",
        "not_for_school_8":"False",
        "not_for_school_10":"True",
        "time_count":"no"
    },
    
     {
        "question": "האם את/ה מכיר/ה מישהו שעובד בהיי-טק?",
        # שאלה סגורה
        "type": "closed",  # שאלה סגורה
        "options":[
                "לא מכיר/ה",
                "כן, מישהו מהמשפחה הגרעינית -אמא, אבא, אח, אחות",
                "כן, מישהו מהמשפחה המורחבת - דוד, דודה, בן דוד, אחיינית וכו'",
                "כן, מישהו מהשכונה",
                "כן, חברים של ההורים",
                "כן, מישהו שלא קשור למשפחה"
            # "אחר"
            ],
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name":'common_feedback',
        "feedback_type":"none",
        "reflection"  : "False",
        "not_for_school_8":"False",
        "not_for_school_10":"False",
        "time_count":"no"
    },
     
     {
        "question": "האם אובחנת באופן רשמי עם אחד או יותר מהבאים?",
        "type": "closed",  # שאלה סגורה
        "options": [
                "לא אובחנתי",
                "דיסלקציה",
                "דיסגרפיה",
                "דיסקלקוליה",
                "ADHD/ADD",
                "לקות למידה אחרת",
                "מעדיף/ה לא לציין"
                ],
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name":'common_feedback',
        "feedback_type":"none",
        "reflection"  : "False",
        "not_for_school_8":"False",
        "not_for_school_10":"False",
        "time_count":"no"
    },
     
     ####היגדים #####################################

        #הקדמה
    #   {
    #     "question":"""
    #     עכשיו נעבור לחלק השני!
    #     בחלק הקרוב יוצגו לפניך 20 היגדים.
    #     אנא ענה/י עליהם בכנות לגבי עצמך.
    #     """,
    #     "type": "text",  
    #     "time_count":"no"
    # },
      
      
      #Q1
      {
        "question": ids.return_text_by_the_id("Q1"),
        "type": "text",  
        "time_count":"no"
    }, 
   
    {
        "question": ids.return_text_by_the_id('ICI2'),
        "type": "closed",
        "options": ids_levels1,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
        "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI16"),
        "type": "closed",
        "options": ids_levels1,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",

        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI10"),
        "type": "closed",
        "options": ids_levels1,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("RISC2"),
        "type": "closed",
        "options": ids_levels1,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ICI5"),
        "type": "closed",
        "options": ids_levels1,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI7"),
        "type": "closed",
        "options": ids_levels1,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
  


##### Q2
       
       
    {
        "question": ids.return_text_by_the_id("ICI4"),
        "type": "closed",
        "options": ids_levels2,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI15"),
        "type": "closed",
        "options": ids_levels2,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ICI7"),
        "type": "closed",
        "options": ids_levels2,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",#          "not_for_school_10":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI6"),
        "type": "closed",
        "options": ids_levels2,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",#          "not_for_school_10":"False",
        "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("RISC1"),
        "type": "closed",
        "options": ids_levels2,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI12"),
        "type": "closed",
        "options": ids_levels2,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI3"),
        "type": "closed",
        "options": ids_levels2,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
 

#########Q3

        {
        "question": ids.return_text_by_the_id("Q3"),
        "type": "text",  
        "time_count":"no"
    },
    {
        "question": ids.return_text_by_the_id("RISC3"),
        "type": "closed",
        "options": ids_levels3,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("GRT1"),
        "type": "closed",
        "options": ids_levels3,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI2"),
        "type": "closed",
        "options": ids_levels3,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
        "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI11"),
        "type": "closed",
        "options": ids_levels3,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI5"),
        "type": "closed",
        "options": ids_levels3,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ICI6"),
        "type": "closed",
        "options": ids_levels3,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI8"),
        "type": "closed",
        "options": ids_levels3,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "reflection"  : "False",
        "not_for_school_8":"False",
         "not_for_school_10":"False",
        "time_count": "no"
    },
    
     {
        "type": "insert_data",  
        "options": [""],
        "time_count":"no"
    },

#  ###LLM
 
# #   {
# #         "question": """
# #         כל הכבוד, סיימת את החלק השני ועוד מעט נעבור לחלק השלישי! 
# # בינתיים אני מנתח את התשובות שלך...
# # עוד כמה רגעים אומר לך מה אפשר ללמוד מהן       
# #         """,
# #         "type": "text",  
# #         "time_count":"no"
# #     },
# #       {
# #          "question": "מנתח תשובות...",
# #          "type": "image",  # שאלה סגורה
# #          "url":"cat.gif",
# #          "time_count":"no"
# #      },

    
      
#     #    {
#     #     "question": """
#     #     כל הכבוד, הגעת לחלק השלישי! 
#     #       תוצג בפניך חידת חשיבה, ולאחריה יוצגו שאלות בנוגע אליה.
#     #        בהצלחה!""",
#     #     "type": "text",  
#     #     "time_count":"no"
#     # },

    {
        "question": "",
        "type": "simulation",  # סימולציות
        "time_count":"no"
    },
    
    {
        "question": """
        עכשיו יוצגו בפניך שאלות לגבי המשימה שזה עתה ביצעת.
        """,
        "type": "text",  
        "time_count":"no"
    },
    
    {
         "question":  ReflectiveQuestions.get_question_by_id(0),
         "type": "closed",
         "options": ReflectiveQuestions.get_options_by_id(0),
         "options_style":"horizontal",
         "feedbacks": [],
         "feedback_system_prompt_name": 'common_feedback',
         "feedback_type": "none",
         "reflection"  : "True",
         "not_for_school_8":"False",
         "not_for_school_10":"False",

         "time_count": "no"
    },
    {
         "question": ReflectiveQuestions.get_question_by_id(1),
         "type": "closed",
         "options": ReflectiveQuestions.get_options_by_id(1),
         "options_style":"horizontal",
         "feedbacks": [],
         "feedback_system_prompt_name": 'common_feedback',
         "feedback_type": "none",
         "reflection"  : "True",
         "not_for_school_8":"False",
         "not_for_school_10":"False",
         "time_count": "no"
    },
    {
         "question": ReflectiveQuestions.get_question_by_id(2),
         "type": "closed",
         "options": ReflectiveQuestions.get_options_by_id(2),
         "options_style":"horizontal",
         "feedbacks": [],
         "feedback_system_prompt_name": 'common_feedback',
         "feedback_type": "none",
         "reflection"  : "True",
         "not_for_school_8":"False",
         "not_for_school_10":"False",
         "time_count": "no"
    },
    {
         "question": ReflectiveQuestions.get_question_by_id(3),
         "type": "closed",
         "options": ReflectiveQuestions.get_options_by_id(3),
         "options_style":"horizontal",
         "feedbacks": [],
         "feedback_system_prompt_name": 'common_feedback',
         "feedback_type": "none",
         "reflection"  : "True",
         "not_for_school_8":"False",
         "not_for_school_10":"False",
         "time_count": "no"
    },
    
    
      ##LLM
      
         
    {
        "question": """
          .בקטע הבא תשוחח/י עם בינה מלאכותית שתציג לך דילמה. השיחה לגמרי אנונימית - אף אחד לא ידע שזה את/ה, בדיוק כמו בשאר השאלון. אז תרגיש/י בנוח להגיב בכנות   """,
        #   הודעות הבינה המלאכותית יסומנו ב-XX.
        "type": "text",  
        "time_count":"no"
    },
    # {
    #      "question": "מנתח תשובות...",
    #      "type": "image",  # שאלה סגורה
    #      "url":"cat.gif",
    #      "time_count":"no"
    #  },
  
    
    {
         "question": "",
         "type": "llm_history",
         "system_prompt_name":"active_bot_1",
         "time_count":"no"
     },
     
     {
        "question": "",
        "type": "open_save",  #  1 שאלה פתוחה
        "feedback": "",
        "time_count":"no",
    },
    
    {
         "question": "",
         "type": "llm_history",
         "system_prompt_name":"active_bot_1",
         "time_count":"no"
     },
    {
        "question": "",
        "type": "open_save",  #2 שאלה פתוחה
        "feedback": "",
        "time_count":"no",
    },
    {
         "question": "",
         "type": "llm_history",
         "system_prompt_name":"active_bot_1",
         "time_count":"no"
     },
    {
        "question": "",
        "type": "open_save",  #  3 שאלה פתוחה
        "feedback": "",
        "time_count":"no",
    },
    {
         "question": "",
         "type": "llm_history",
         "system_prompt_name":"active_bot_1",
         "time_count":"no"
     },
    {
        "question": "",
        "type": "open_save",  #  4 שאלה פתוחה
        "feedback": "",
        "time_count":"no",
    },
    {
         "question": "",
         "type": "llm_history",
         "system_prompt_name":"active_bot_1",
         "time_count":"no"
     },
    {
        "question": "",
        "type": "open_save",  #  5 שאלה פתוחה
        "feedback": "",
        "time_count":"no",
    },
    {
         "question": "",
         "type": "llm_history",
         "system_prompt_name":"active_bot_1",
         "time_count":"no"
     },
    {
        "question": "",
        "type": "open_save",  #  6 שאלה פתוחה
        "feedback": "",
        "time_count":"no",
    },
    {
         "question": "",
         "type": "llm_history",
         "system_prompt_name":"active_bot_1",
         "time_count":"no"
     },
    {
        "question": "",
        "type": "open_save",  #  7 שאלה פתוחה
        "feedback": "",
        "time_count":"no",
    },
    {
         "question": "",
         "type": "llm_history",
         "system_prompt_name":"active_bot_1",
         "time_count":"no"
     },
    
     {
        "type": "insert_data",  
        "options": [""],
        "time_count":"no"
    },
 
    
    
    
    # ###LLM
    #   {
    #      "question": "",
    #      "type": "text_llm",
    #      "system_prompt_name":"reflection",
    #      "time_count":"no"
    #  },
    
#         {
#         "question": """
# ולסיום, הבינה המלאכותית עברה על התשובות שלך מהחלק הראשון של השאלון, ורוצים לשתף אותך בתובנות שהיא מצאה. קבל/י אותן כאן!      
# """,
#         "type": "text",  
#         "time_count":"no"
#     },
      
      {
         "question": "",
         "type": "text_llm",
         "system_prompt_name":"hegedim",
         "time_count":"no"
    },
      
          {
        "question": """
אם נראה לך שהבינה המלאכותית לא דייקה, זה הגיוני לגמרי, סך הכל היא רק בינה מלאכותית, את/ה יודע/ת הכי טוב מי את/ה""",
        "type": "text",  
        "time_count":"no"
    }

         
]
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     ####old#########################
    # {
    #     "question": "בנקודת זמן זאת, לפני תחילת התוכנית, אשמח לדעת מה אתם חושבים שהסיכוי שלכם להשתלב בעתיד בתחום ההייטק:",
    #     "type": "closed_new",  # שאלה סגורה
    #     "options": ["אין סיכוי בעולם", "סיכוי נמוך", "יש מצב טוב", "ברור שכן!", "בשמחה רבה " , "בגיל ובשוון"],
    #     "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
    #                   "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
    #                   "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
    #                   "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
    #     "time_count":"no"
    # },
    # {
    #     "question": "למה זה המצב לדעתכם?",
    #     "type": "open",  # שאלה פתוחה
    #     "feedback": "תודה, אני חושב שזה יהיה רעיון טוב לדבר על זה עם המורה שלך או מישהו מבוגר בחיים שלכם שאתם סומכים עליו, ותשתפו אותו במחשבות האלה.",
    #     "time_count":"no"
    # },
    # {
    #     "question": "אשמח אם תדרגו את השיחה:",
    #     "type": "closed",  # שאלה סגורה
    #     "options": ["1", "2", "3", "4", "5"],
    #     "feedbacks": ["תודה על הדירוג!", "תודה על הדירוג!", "תודה על הדירוג!", "תודה על הדירוג!", "תודה על הדירוג!"],
    #     "time_count":"yes"
    # },
    
    
    
    # {
    #     "question": "צפה בתמונה הבאה",
    #     "type": "image",  # שאלה סגורה
    #     "url":"almond.jpg",
    #     "time_count":"no"
    # },
    
    
    
    #  {
    #     "question": "צפה בוידאו הבא",
    #     "type": "video",  # שאלה סגורה
    #     "url":"bird.mp4",
    #     "time_count":"no"
    # },
    #  {
    #     "question": "אשמח אם תדרגו את השיחה:",
    #     "type": "closed",  # שאלה סגורה
    #     "options": ["1", "2", "3", "4", "5"],
    #     "feedbacks": ["תודה על הדירוג!", "תודה על הדירוג!", "תודה על הדירוג!", "תודה על הדירוג!", "תודה על הדירוג!"],
    #     "time_count":"yes"
    # }
     
#      {
#         "question": "סמנ/י את הפעילויות שאת/ה משתתפ/ת בהן מחוץ לבית הספר:",
#         "type": "closed",  # שאלה סגורה
#         "options": [
#             "תנועת נוער",
#             "פעילות ספורטיבית עצמאית / מאורגנת",
#             "פעילות טכנולוגית",
#             "פעילות אומנותית מאורגנת / עצמאית",
#             "מסגרת דתית לימודית",
#             "עבודה בחופשים / במהלך שנת הלימודים",
#             "אחר"
#             ],
#         "options_style":"horizontal",
#         "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
#                       "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
#                       "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
#                       "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
#         "feedback_system_prompt_name":'common_feedback',
#         "feedback_type":"none",
#         "reflection"  : "False",
#         "time_count":"no"
#     },
    





 # {
    #      "question": ReflectiveQuestions.get_question_by_id(4),
    #      "type": "closed",
    #      "options": ReflectiveQuestions.get_options_by_id(4),
    #      "options_style":"horizontal",
    #      "feedbacks": [],
    #      "feedback_system_prompt_name": 'common_feedback',
    #      "feedback_type": "none",
    #      "reflection"  : "True",
    #      "not_for_school_8":"False",
    #       "not_for_school_10":"False",
    #      "time_count": "no"
    # },
    # {
    #      "question": ReflectiveQuestions.get_question_by_id(5),
    #      "type": "closed",
    #      "options": ReflectiveQuestions.get_options_by_id(5),
    #      "options_style":"horizontal",
    #      "feedbacks": [],
    #      "feedback_system_prompt_name": 'common_feedback',
    #      "feedback_type": "none",
    #      "reflection"  : "True",
    #      "not_for_school_8":"False",
    #      "not_for_school_10":"False",
    #      "time_count": "no"
    # },
    # {
    #      "question": ReflectiveQuestions.get_question_by_id(6),
    #      "type": "closed",
    #      "options": ReflectiveQuestions.get_options_by_id(6),
    #      "options_style":"horizontal",
    #      "feedbacks": [],
    #      "feedback_system_prompt_name": 'common_feedback',
    #      "feedback_type": "none",
    #      "reflection"  : "True",
    #      "not_for_school_8":"False",
    #      "not_for_school_10":"False",
    #      "time_count": "no"
    # },
    
    # {
    #      "question": ReflectiveQuestions.get_question_by_id(7),
    #      "type": "closed",
    #      "options": ReflectiveQuestions.get_options_by_id(7),
    #      "options_style":"horizontal",
    #      "feedbacks": [],
    #      "feedback_system_prompt_name": 'common_feedback',
    #      "feedback_type": "none",
    #      "reflection"  : "True",
    #      "not_for_school_8":"False",
    #       "not_for_school_10":"False",
    #      "time_count": "no"
    # },
    
    #simulation - קבלת החלטות 
#      {
#         "question": """
# חבר וחברה טובים שלך (עומר והילה) התחילו לעבוד בקיוסק השכונתי אחרי שעות בית הספר, שלוש פעמים בשבוע, ומקבלים 200 ש"ח לכל שבוע עבודה – לפעמים אפילו יותר עם טיפים.
# הבעלים של הקיוסק מציע לך להצטרף אליהם, אבל זה ברור לך שזה יתנגש החוג האהוב עליך ויכול להיות שגם עם תנועת הנוער וכמובן יוכל לפגוע בהתקדמות שלך בלימודים. מצד שני ההצטרפות אליהם תגרום לכך שתהיה לך הזדמנות להרוויח הרבה כסף שיהיה שלך ויאפשר לך לעשות איתו לא מעט דברים.
# החלטה: מה היית עושה?,""",
#         "type": "open",  # שאלה פתוחה
#         "feedback": "",
#         "time_count":"no",
#     },

    #   {
    #     "question":  active_sim.question,
    #     "type": "text",  
    #     "time_count":"no"
    # },
    
   