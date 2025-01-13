response_list = [
    {"key": "😃 דומה לחלוטין", "content": 5},
    {"key": "🙂 דומה", "content": 4},
    {"key": "😐 קצת דומה", "content": 3},
    {"key": "🙁 לא כל כך דומה", "content": 2},
    {"key": "😡 לא דומה בכלל", "content": 1},
    
    {"key": "בדיוק כמוני 😄", "content": 5},
    {"key": "כמוני 🙂", "content": 4},
    {"key": "קצת כמוני 😐", "content": 3},
    {"key": "קצת לא כמוני 😕", "content": 2},
    {"key": "כלל לא כמוני 🙁", "content": 1},


    {"key": "😄 נכון מאוד לגביי", "content": 5},
    {"key": "😊 נכון לגביי", "content": 4},
    {"key": "😐 נכון לגביי באופן חלקי", "content": 3},
    {"key": "🙁 לא כל כך נכון לגביי", "content": 2},
    {"key": "😡 ממש לא נכון לגביי", "content": 1}
]

def get_content_by_key(key):
    for item in response_list:
        if item["key"] == key:
            return item["content"]
    return key  # אם ה-key לא נמצא, נחזיר את המפתח עצמו
