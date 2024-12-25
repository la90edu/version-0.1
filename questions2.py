import schools
import ids

ids_levels1 = [
    "😡 לא דומה בכלל",
    "🙁 לא כל כך דומה",
    "😐 קצת דומה",
    "🙂 דומה",
    "😃 דומה לחלוטין",   
]

ids_levels2=[
    "בדיוק כמוני 🎯",       # פגיעה מדויקת
    "כמוני 🔗",            # חיבור קרוב
    "קצת כמוני 🌗",        # חצי דרך, כמו חצי ירח
    "קצת לא כמוני 🌪️",    # קצת מבולבל או רחוק
    "כלל לא כמוני 🚫"       # שלילה מוחלטת
]

ids_levels3= [
    "תמיד 🔄",               # חזרה אינסופית
    "לעיתים קרובות 📈",      # משהו שמתרחש הרבה, כמו עלייה
    "לפעמים ⏳",             # משהו קורה לעיתים, כמו חול שעובר
    "לעיתים רחוקות 🌍",      # משהו רחוק, כאילו במדינה אחרת
    "אף פעם ❌"              # שלילה מוחלטת
]



questions = [
    
     
    {
        "question": """
👋 אתם עומדים למלא שאלון מטעם תכנית ההייטק. נבקש שתענו על השאלות באופן המדויק ביותר לגביכם. השאלון אנונימי ולא יזוהה איתכם.

📋 לשאלון שלושה חלקים: 
1. **חלק של פרטים יבשים אודותיכם** (למשל: עיר מגורים).
2. **חלק של היגדים אותם תצטרכו לדרג** (מ"מאוד דומה לי" ועד "ממש לא דומה לי").
3. **חלק של ניסוי** (משימת חשיבה, פתרון ושאלות נוספות).

⚠️ חשוב לנו שכל אחד ימלא את השאלון ויבצע את המשימה **באופן עצמאי**. בסוף השאלון, מתוך המידע שמילאתם, תקבלו **משוב על עצמכם**.

אז שווה להתאמץ ולסיים את המענה על השאלון עד הסוף. קדימה, בואו נתחיל! 🚀
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
        "question": "בחר את שם בית הספר שלך:",
        "type": "selectbox_schools",  # שאלה מסוג Selectbox
        "options": "null" ,#["אפק", "גוונים", "בגין"],  # שמות בתי הספר
        "feedbacks": "תודה",
        "feedback_type":"auto",
        "time_count":"no"
    },
    {
        "question": "סמנ/י את הפעילויות שאת/ה משתתפ/ת בהן מחוץ לבית הספר:",
        "type": "closed",  # שאלה סגורה
        "options": [
            "תנועת נוער",
            "פעילות ספורטיבית עצמאית / מאורגנת",
            "פעילות טכנולוגית",
            "פעילות אומנותית מאורגנת / עצמאית",
            "מסגרת דתית לימודית",
            "עבודה בחופשים / במהלך שנת הלימודים",
            "אחר"
            ],
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name":'common_feedback',
        "feedback_type":"none",
        "time_count":"no"
    },
    
     {
        "question": "האם את/ה מכיר/ה מישהו שעובד בהיי-טק?",
        "type": "closed",  # שאלה סגורה
        "options":[
            "מישהו מהמשפחה הגרעינית",
            "משפחה מורחבת",
            "מישהו מהשכונה",
            "חברים של ההורים",
            "מישהו שלא קשור למשפחה",
            "אחר"
            ],
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name":'common_feedback',
        "feedback_type":"none",
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
        "time_count":"no"
    },
     
     ####היגדים #####################################

        #הקדמה
      {
        "question": "בחלק הקרוב יוצגו היגדים. עבור כל היגד, בחר את התשובה שהכי דומה להתנהגותך, עמדתך או דעתך",
        "type": "text",  
        "time_count":"no"
    },
      #Q1
      {
        "question": ids.return_text_by_the_id("Q1"),
        "type": "text",  
        "time_count":"no"
    }, 
   
    {
        "question": ids.return_text_by_the_id("ICI2"),
        "type": "closed",
        "options": ids_levels1,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
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
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI1"),
        "type": "closed",
        "options": ids_levels1,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI4"),
        "type": "closed",
        "options": ids_levels1,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI13"),
        "type": "closed",
        "options": ids_levels1,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "time_count": "no"
    },


##### Q2
        {
        "question": ids.return_text_by_the_id("Q2"),
        "type": "text",  
        "time_count":"no"
    },
       
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
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI9"),
        "type": "closed",
        "options": ids_levels2,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("RISC4"),
        "type": "closed",
        "options": ids_levels2,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
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
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ICI3"),
        "type": "closed",
        "options": ids_levels3,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "time_count": "no"
    },
    {
        "question": ids.return_text_by_the_id("ZPTI14"),
        "type": "closed",
        "options": ids_levels3,
        "options_style":"horizontal",
        "feedbacks": ["הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת.",
                      "הבנתי. תודה על התשובה. אשמח שתספרו לי על זה עוד קצת."],
        "feedback_system_prompt_name": 'common_feedback',
        "feedback_type": "none",
        "time_count": "no"
    },

    {
        "question": "",
        "type": "simulation",  # סימולציות
        "time_count":"no"
    }
   
     
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
     
    
]
