response_list = [
    {"key": "😄 מתארת אותי בול", "content": 5},
    {"key": "😊  מתארת אותי לא רע", "content": 4},
    {"key": "😐 קצת מתארת אותי", "content": 3},
    {"key": "🙁 לא מתארת אותי ", "content": 2},
    {"key": "😡 ממש לא מתארת אותי ", "content": 1},
    
    {"key": "בדיוק כמוני 😄", "content": 5},
    {"key": " כמוני 🙂", "content": 4},
    {"key": "קצת כמוני 😐", "content": 3},
    {"key": "קצת לא כמוני 😕", "content": 2},
    {"key": "כלל לא כמוני 🙁", "content": 1},


    {"key": "😄 מתאר אותי במדויק", "content": 5},
    {"key": "😊 מתאר אותי", "content": 4},
    {"key": "😐 מתאר אותי מעט", "content": 3},
    {"key": "🙁 לא ממש מתאר אותי ", "content": 2},
    {"key": "😡 כלל לא מתאר אותי ", "content": 1},
    
    {"key": "כיתה י", "content": "class_10"},
    {"key": "כיתה ח", "content": "class_8"}


]

def get_content_by_key(key):
    for item in response_list:
        if item["key"] == key:
            return item["content"]
    return key  # אם ה-key לא נמצא, נחזיר את המפתח עצמו

