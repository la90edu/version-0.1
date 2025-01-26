import questions2
import hegedim_algorithem

ids_level1=questions2.ids_levels1
ids_level2=questions2.ids_levels2
ids_level3=questions2.ids_levels3





def return_levels(question_num):
        if (question_num<=9): 
           levels=questions2.ids_levels1
        elif (question_num<=18):
               levels=questions2.ids_levels2
        else:
           levels=questions2.ids_levels3
        return levels

def translate_hegedim(original_hegedim):
    
        
    hegedim_result =[]
    j=1
    for i in range(1,28):
         
        levels=return_levels(i)        
   
        
        hegedim_answer=original_hegedim[j].get('content', "מפתח לא נמצא")
        
        if (hegedim_answer==levels[0]):
            answer=hegedim_algorithem.return_hamara(i,0)
            hegedim_result.append(answer)
        if (hegedim_answer==levels[1]):
            answer=hegedim_algorithem.return_hamara(i,1)
            hegedim_result.append(answer)
        if (hegedim_answer==levels[3]):
            answer=hegedim_algorithem.return_hamara(i,3)
            hegedim_result.append(answer)
        if (hegedim_answer==levels[4]):
            answer=hegedim_algorithem.return_hamara(i,4)
            hegedim_result.append(answer)  
            
        j=j+2  
    
    answer=hegedim_result   
    return hegedim_result
                
        # case 2:
        #     return "Two"
        # case 3:
        #     return "Three"
        # case _:
        #     return "Other"  
            
       
       
       
       # {'role': 'assistant', 'content': 'יש לי רצון לקחת על עצמי משימות שדורשות ממני להיות אחראי/ת על אחרים. 💪'},
# {'role': 'user', 'content': '😐 קצת דומה'},
# {'role': 'assistant', 'content': 'קורה לי הרבה שאני חושב/ת על דברים רעים שקרו לי. 😞'},
# {'role': 'user', 'content': '🙂 דומה'},
# {'role': 'assistant', 'content': 'יש בי אמונה שאי אפשר באמת לתכנן את העתיד כי דברים משתנים כל הזמן. 🤷‍♂️'},
# {'role': 'user', 'content': '🙂 דומה'},
# {'role': 'assistant', 'content': 'גם תחת לחץ, יש לי יכולת להשאר בפוקוס ולחשוב באופן בהיר. 🔍'},
# {'role': 'user', 'content': '😃 דומה לחלוטין'},
# {'role': 'assistant', 'content': 'מייאש אותי לעשות משהו שאני אראה את התוצאות שלו רק בעוד הרבה זמן. 😓'},
# {'role': 'user', 'content': '😃 דומה לחלוטין'},
# {'role': 'assistant', 'content': 'יש לי נטייה להרגיש תחושות של נוסטלגיות על דברים שקרו בעבר שלי. 🌟'},
# {'role': 'user', 'content': '😐 קצת דומה'},
# {'role': 'assistant', 'content': 'תמיד אסיים את כל המטלות למחר לפני שאצא לבלות או לנוח בערב של אותו היום. ⏰'},
# {'role': 'user', 'content': '🙂 דומה'},
# {'role': 'assistant', 'content': 'תמיד אעמוד בהבטחות שלי לחברים או לכל אחד אחר כמו המורה או ההורים שלי. ✔️'},
# {'role': 'user', 'content': '🙁 לא כל כך דומה'},
# {'role': 'assistant', 'content': 'יש לי יכולת להשלים פרויקטים בזמן על ידי כך שאני משקיע/ה בהם לאורך זמן ולא רק ברגע האחרון. 🕰️'},
# {'role': 'user', 'content': '😡 לא דומה בכלל'},
# {'role': 'assistant', 'content': '🔄 מה המידה שהנאמר למטה זהה לתפיסה שלך את עצמך?'},
# {'role': 'assistant', 'content': 'יש לי צורך שמישהו אחר יפרגן ויחמיא לי על העבודה שלי כדי שאהיה מרוצה ממה שעשיתי. 🙌'},
# {'role': 'user', 'content': 'קצת כמוני 😐'}