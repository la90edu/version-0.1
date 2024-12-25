from enum import Enum

class School_Type(Enum):
    SCHOOL_8 = 1
    SCHOOL_10 = 2
    
    @staticmethod
    def to_string(school_type):
        return str(school_type)
    
    @staticmethod
    def to_School_Type(string_type):
        return School_Type[string_type]
    
import schools_8th_grade
import schools_10th_grade

def return_schools_list(school_type: School_Type):
    match school_type:
        case School_Type.SCHOOL_8:
            return schools_8th_grade.schools
        case School_Type.SCHOOL_10:
            return schools_10th_grade.schools
        case _:
            return []
 
 
# print(return_schools_list(School_Type.SCHOOL_10))
# x = School_Type.SCHOOL_10
# y = School_Type.to_string(x)
# print(y)
# print(type(y))

# z = School_Type.to_School_Type('SCHOOL_10')
# print(z)
# print(type(z))

    
# schools = [
#     "מקיף ב",
#     "אורט הנרי רונסון",
#     "מקיף ד' דרכא",
#     "תיכון דוד טוביהו",
#     "אורט אמירים בית שאן",
#     "דרכא בית וגן",
#     "תיכון חדש דרכא",
#     "נתיבי נעם",
#     "דרכא ליהמן",
#     "בית חינוך",
#     "מקיף עש קאסם גאנם",
#     "אורט שרת",
#     "אורט אלון",
#     "עירוני מקיף שי עגנון",
#     "שרת",
#     "אורט רונסון עוספיה",
#     "אורט אריה מאיר",
#     "אבו-סלים סלמאן אלשיך",
#     "גולדווטר",
#     "בגין",
#     "אורט מקיף א אשקלון",
#     "מקיף ו דרכא רונסון",
#     "מקיף ה דרכא",
#     "אולפנת אמית אוריה",
#     "הרב תחומי עמל רמות",
#    "חטב עש המנוח גאלב מנסור",
#     "אורט פסגות",
#     "אולפנת אהבת ישראל",
#     "ברנקו וייס",
#     "אורט מלטון",
#     "מקיף עש שזר",
#     "מקיף דרכא ג'וליס",
#     "מקיף שש שנתי חורפיש",
#     "עירוני א'",
#     "מקיף קריית חיים",
#     "עירוני חוגים",
#     "חטהב שקד תיכון קריית חיים",
#     "מקיף גילה",
#     "עירוני פסגת זאב ע\"ש טדי קולק",
#     "חט\"ב אורט גבעת רם",
#     "אלדד",
#     "מקיף ע\"ש ש.טשרנחובסקי",
#     "תיכון שיטים-דרכא",
#     "\"עלייה שנייה\" אורט עכו",
#     "אולפנת צביה עפולה",
#     "אורט יהודה",
#     "קרית חינוך אורט אורן עפולה",
#     "מקיף שש שנתי פקיעין",
#     "אולפנית אמית צפת",
#     "גימנסיה דרכא",
#     "אורט כרמי גת",
#     "חטיבת דגן תיכון קרית חיים",
#     "קריית חינוך אמית",
#     "רב תחומי עמל אלסייד",
#     "מקיף ד",
#     "אולפנת עלמא אשדוד",
#     "מקיף ח",
#     "חטיבת הנעורים יערת העמק",
#     "תיכון מרחבים",
#     "חט\"ב אורט מדעים ואומנויות",
#     "ישיבת בני עקיבא נווה הרצוג",
#     "תיכון המר דרכא נתיבות",
#     "רוז",
#     "אורט ערד",
#     "מקיף אגיאל ערערה בנגב",
#     "אורט דפנה",
#     "קרית חינוך אלון עמל רמלה"
# ]
