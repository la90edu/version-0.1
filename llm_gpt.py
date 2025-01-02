from openai import OpenAI
client = OpenAI()
import system_prompts

def summerize_conversation(conversation):
 prompt = (
    f"אתה משחק תפקיד של חבר ומנטור לתלמיד או תלמידה בתיכון. "
    f"\nאתה מקבל רשימה של שיחה שהתנהלה בינך לבין התלמיד/ה במסגרת תוכנית ההייטק הלאומית, שמטרתה לקרב תלמידים לעולם ההייטק ולעודד אותם להשתלב בתחום כשיגדלו. "
    f"\nעליך לסכם את השיחה בצורה חיובית ומעודדת, ולפנות ישירות אל התלמיד/ה בגוף שני כדי ליצור תחושת חיבור ואישית. "
    f"התגובה שלך צריכה להיות עד 3-4 משפטים בלבד, בעברית בלבד, תוך שימוש בשפה נעימה, מנומסת ומותאמת לגיל התלמידים, וללא אזכור של נושאים רגישים כמו אלימות או מיניות. "
    f"\nזוהי השיחה: {conversation}"
) 
 response = client.chat.completions.create(
 model="gpt-4o",
 messages=[{"role":"user","content":prompt}]
 )
 return response.choices[0].message.content.strip()



# response=summerize_conversation("היי מה שלומך , הכל בסדר, איזה חיה את אוהבת , אני אוהבת כלבים")
# print(response)


def how_do_you_feel(conversation):
 prompt = (
    f"אתה משחק תפקיד של חבר ומנטור לתלמיד או תלמידה בתיכון. "
    f"\nאתה מקבל רשימה של שיחה שהתנהלה בינך לבין התלמיד/ה במסגרת תוכנית ההייטק הלאומית, שמטרתה לקרב תלמידים לעולם ההייטק ולעודד אותם להשתלב בתחום כשיגדלו. "
    f"אני שולחת את השיחה. תן פידבק חיובי ומעודד לשאלה האחרונה שתגרום לתלמיד להמשיך לשוחח"
    f"התגובה שלך צריכה להיות עד 3-4 משפטים בלבד, בעברית בלבד, תוך שימוש בשפה נעימה, מנומסת ומותאמת לגיל התלמידים, וללא אזכור של נושאים רגישים כמו אלימות או מיניות. "
    f"\nזוהי השיחה: {conversation}"
) 
 response = client.chat.completions.create(
 model="gpt-4o",
 messages=[{"role":"user","content":prompt}]
 )
 return response.choices[0].message.content.strip()


def return_llm_answer_for_common_feedback(conversation):
#  prompt = (
#      system_prompts.return_prompt()
# ) 
    system_prompt=system_prompts.return_system_prompt_for('common_feedback')
    user_prompt="\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation])
 
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
         {"role":"system","content":system_prompt},
         {"role":"user","content":user_prompt}
         ]
    )
    return response.choices[0].message.content#.strip()

# def return_llm_answer(system_prompt_name ,history):
# #  prompt = (
# #      system_prompts.return_prompt()
# # ) 
#     system_prompt=system_prompts.return_system_prompt_for(system_prompt_name)
#     #user_prompt=f"assistant: {last_assistant_history}, user: {user_assistant_history}"
#     user_prompt=history
 
#     response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#          {"role":"system","content":system_prompt},
#          {"role":"user","content":user_prompt}
#          ]
#     )
    # return response.choices[0].message.content

def return_llm_answer(given_system_prompt ,conversation):
    system_prompt = given_system_prompt
    user_prompt=conversation
 

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role":"user","content":user_prompt}
        ]
    )
    return response.choices[0].message.content


# message= [
#     {"role":"assistante","content":"איפה את גרה?"},
#     {"role":"user","content":"ראש העין"}
# ]

# print(return_llm_answer_for_common_feedback(message))

# def return_llm_answer(system_prompt_name ,conversation):
#     system_prompt = system_prompts.return_system_prompt_for(system_prompt_name)
#     user_prompt="\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation])

#     # ודא שהיסטוריה מעוצבת כראוי
#     # formatted_conversation = [
#     #     {"role": msg["role"], "content": str(msg["content"])}
#     #     for msg in history
#     # ]

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": system_prompt},
#             {"role":"user","content":user_prompt}
#         ]
#     )
#     return response.choices[0].message.content
