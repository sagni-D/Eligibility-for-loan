import streamlit as st
from PIL import Image
import pickle


model = pickle.load(open('D:\streamlit projects\ML_Model.pkl', 'rb'))

def run():
    img1 = Image.open('yenebank logo.PNG')
    img1 = img1.resize((200,160))
    st.image(img1,use_column_width=False)
    st.title("የኔ ባንክ የብድር ግምገማ ገፅ")

    ## Account No
    account_no = st.text_input('አካወንት ቁጥር')

    ## Full Name
    fn = st.text_input('ሙሉ ስም')

    ## For gender
    gen_display = ('ወንድ ','ሰት ')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("ፆታ",gen_options, format_func=lambda x: gen_display[x])

    ## For Marital Status
    mar_display = ('ኣይ','ኣዎ')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("የጋብቻ ሁነታ", mar_options, format_func=lambda x: mar_display[x])

    ## No of dependets
    dep_display = ('ምንም',' ኣንድ ','ሁለት  ','ከሁለት በላይ')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("በርሶ ስር የምተዳደር",  dep_options, format_func=lambda x: dep_display[x])

    ## For edu
    edu_display = ('ያልተመረቀ','ተመራቂ')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("የትምርት ሁነታ",edu_options, format_func=lambda x: edu_display[x])

    ## For emp status
    emp_display = ('ሰራተኛ ','ቢዝነስ ')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("የስራ ሁነታ",emp_options, format_func=lambda x: emp_display[x])

    ## For Property status
    prop_display = ('ገጠር','ታዳጊ ','ከተማ ')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("የኑሮ ና ንብረት ቦታ",prop_options, format_func=lambda x: prop_display[x])

    ## For Credit Score
    cred_display = ('300 ና 500 መካከል','ከ 500 በላይ')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("ከዚበፊት የወሰዱት የብድር መጠን",cred_options, format_func=lambda x: cred_display[x])

    ## Applicant Monthly Income
    mon_income = st.number_input("የጠያቂዉ ወረሃዊ ገቢ($)",value=0)

    ## Co-Applicant Monthly Income
    co_mon_income = st.number_input("የጠያቂዉ  የስራ ባልደረባ ወረሃዊ ገቢ($)",value=0)

    ## Loan AMount
    loan_amt = st.number_input("የብድር መጠን",value=0)

    ## loan duration
    dur_display = ['2 ወር','6 ወር','8 ወር','1 ወር','16 ወር']
    dur_options = range(len(dur_display))
    dur = st.selectbox("የብድር ግዘ",dur_options, format_func=lambda x: dur_display[x])

    if st.button("ኣስገምግም"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
                "ሰላም: " + fn +" || "
                "አካወንት ቁጥር: "+account_no +' || '
                ' ይቅርታ!! በባንኩ ሕግ መሰረት በድር ማግኘት ኣይችሉምk'
            )
        else:
            st.success(
                "ሰላም: " + fn +" || "
                "አካወንት ቁጥር: "+account_no +' || '
                'እንካን ደስ ኣሎት!!  ከባንካችን ብድር ማግኘት ይችላሉ'
            )

run() 