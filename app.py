# Importing required packages
import pickle
from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Login Streamlit", page_icon=":bar_chart:")


# --- USER AUTHENTICATION ---
# load hashed passwords
file_path = Path(__file__).parent / "db.pkl"
with file_path.open("rb") as file:
    data = pickle.load(file)
    
hashed_passwords = data[0]
names = data[1]
usernames = data[2]

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "Login", "abcdef", cookie_expiry_days=2)

name, authentication_status, username = authenticator.login("Welcome to the system", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

print("Application 001 is runnning......")    
if authentication_status:
    # ---- READ EXCEL ----
    

    # ---- SIDEBAR ----
    st.sidebar.title(f"Hello {name}") 
    authenticator.logout("Logout", "sidebar")
    st.sidebar.header("Instructions")
    st.sidebar.info(
        '''This is a web application sample that allows you use docker 
           and python 3.9.   
           '''
        )

    # ---- MAINPAGE ----
    st.title("Sample of Python and Streamlit authenticador on Docker")
    st.write("authenticator sample works !!!")
    st.markdown("##")

    
    st.markdown("""---""")
