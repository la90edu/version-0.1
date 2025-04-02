response_list = [
    {"key": "😃 דומה לחלוטין", "content": 5},
    {"key": "🙂 דומה", "content": 4},
    {"key": "😐 קצת דומה", "content": 3},
    {"key": "🙁 לא כל כך דומה", "content": 2},
    {"key": "😡 לא דומה בכלל", "content": 1},
    
    {"key": "לגמרי כמוני 😄", "content": 5},
    {"key": "די כמוני 🙂", "content": 4},
    {"key": "קצת כמוני 😐", "content": 3},
    {"key": "בקושי כמוני 😕", "content": 2},
    {"key": "ממש לא כמוני 🙁", "content": 1},


    {"key": "😄 מתאר אותי במדויק", "content": 5},
    {"key": "😊 מתאר אותי", "content": 4},
    {"key": "😐 מתאר אותי במעט", "content": 3},
    {"key": "🙁 לא ממש מתאר אותי", "content": 2},
    {"key": "😡 כלל לא מתאר אותי ", "content": 1},
    
    {"key": "כיתה י", "content": "class_10"},
    {"key": "כיתה ח", "content": "class_8"}


]

def get_content_by_key(key):
    for item in response_list:
        if item["key"] == key:
            return item["content"]
    return key  # אם ה-key לא נמצא, נחזיר את המפתח עצמו

