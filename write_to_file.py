
# def write_to_file(data_string):
#     f = open("demofile3.txt", "w")
#     f.write("Woops! I have deleted the content! nnnnnn")
#     f.close()
    
def write_to_file( data_list):
    """
    כותב רשימה לקובץ טקסט, כאשר כל פריט ברשימה נכתב בשורה נפרדת

    :param file_path: מיקום הקובץ לשמירה
    :param data_list: הרשימה לכתיבה בקובץ
    """
    
    with open("demofile3.txt", 'w', encoding='utf-8') as file:
        for item in data_list:
                file.write(f"{item}\n")
    #     print(f"הרשימה נשמרה בהצלחה בקובץ: {file_path}")
    # except Exception as e:
    #     print(f"שגיאה בעת כתיבת הקובץ: {e}")

# דוגמה לשימוש:
# my_list = ["אחד", "שתיים", "שלוש", "ארבע"]
# write_to_file( my_list)
