import streamlit as st

import re

st.set_page_config(page_title="Password Strength Checker")

st.title("Password Strength Checker")

st.markdown(
    """
    ## Welcome to the ultimate password strength checker!
    Use this simple tool to check the strength  of your password and get    
    suggestions  on how to make it stronger.
    we will give you helpful tips to create a **strong Password**
    """
)

pasword = st.text_input("Enter Your Password",type="password")

feedback=[]

score =0

if pasword:
    if len(pasword)>=8:
        score+=1
    else:
        feedback.append("❌Password should be at least a character long.")
    
    if re.search(r'[A-Z]',pasword) and re.search(r'[a=z]',pasword):
        score+=1
    else:
         feedback.append("❌Password should contain both upper and lower case character")
   
    if re.search (r'\d',pasword):
       score+=1
    else:
        feedback.append("❌Password should contain at least one digit.")
    
    if re.search (r'[!@%$&*]',pasword):
       score+=1
    
    else:
        feedback.append("❌ Password should contain at least one special character(!@%$&*).")
        
        
    if score==4:
        feedback.append("Your password is strong!")
        
    elif score==3:
        feedback.append("Your password is medium strength. It could be a stronger.!")
    
    else:
       feedback.append ("❌ Your password is week. Please make it stronger")
       
    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
            
    else:
        st.info("Please enter your password to get started")



# Footer
st.markdown("---")
st.markdown("💡 **Keep pushing forward and never stop learning!**")
st.markdown("**Made with by Umema Sultan**")