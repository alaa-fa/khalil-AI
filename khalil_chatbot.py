# IMPORT STATEMENTS
import streamlit as st
import openai
import os
import tempfile
import streamlit as st
from audio_recorder_streamlit import audio_recorder
from streamlit_chat import message as st_message

# DISPLAY RIGHT-ALIGNED TEXT FUNCTIONS
def display_right_aligned_text(text):
    st.markdown(f"<div style='text-align: right;'>{text}</div>", unsafe_allow_html=True)
def display_right_aligned_title(text):
    st.markdown(f"<h1 style='text-align: right;'>{text}</h1>", unsafe_allow_html=True)

# GET AVATAR FUNCTION
def get_avatar(user_role):
    if user_role == 'user':
        return r"C:\Users\user\Downloads\user-icon" 
    if user_role == 'assistant':
        return r"C:\Users\user\Downloads\sameer-icon.jpg" 
    

# API KEY AND ENVIRONMNENT INITIALIZATION
API_KEY = ''  # Replace with your actual key
os.environ["OPENAI_API_KEY"] = API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")
display_right_aligned_title("خليل: رفيقك في رحلة التحسين الذاتي")
client = openai

# create assistant TODO: save one assistant id 
my_assistant = client.beta.assistants.create(
    instructions="You are a personal life coach. Be supportive, encouraging, and friendly. RESPOND IN ARABIC, SPECIFICALLY SAUDI DIALECT.",
    name="Sameer",
    model="gpt-4-turbo"
)
# create empty thread
thread_ = client.beta.threads.create()
history = {}

# Initialize chat history in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.current_user = 'user'

# TESTING



# take in text input from user
user_input = st.text_input(
    "Enter your message:",
    key='user_message_input')

# processing text input and generating gpt response
if st.button("ارسل") and user_input:
    # update session_state and history with user_input 
    st.session_state.current_user = 'user'
    st.session_state.messages.append({"role": "user", "content": user_input})
    history[f"user{len(st.session_state.messages)}"] = user_input

    # create message object from user input
    thread_message = client.beta.threads.messages.create(
        thread_id=thread_.id,
        role="user",
        content=user_input,
    )
    # generate response from gpt 
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread_.id,
        assistant_id=my_assistant.id
    )
    # extract text response 
    messages_ = list(client.beta.threads.messages.list(thread_id=thread_.id, run_id=run.id))
    message_content = messages_[0].content[0].text.value
    
    # update session_state and history with gpt response
    st.session_state.current_user = 'assistant'

    st.session_state.messages.append({"role": "assistant", "content": message_content})
    history[f"sameer{len(st.session_state.messages)}"] = message_content


# DISPLAY CONVERSATION THREAD (chat history)
i=0
for message in st.session_state.messages:
    if message['role'] == 'user':
        # st.write("user: ", message['content'])
        st_message(
        message['content'],
        key=f"{message['role']+str(i)}",
        is_user=(message['role'] == st.session_state.current_user),
    )
    else:
        #st.write("sameer: ", message['content'])
        st_message(
        message['content'],
        key=f"{message['role']+str(i)}",
        is_user=(message['role'] == st.session_state.current_user),
        )
            # Generate the audio file
        response = client.audio.speech.create(
            model="tts-1",
            voice="onyx",
            input=message['content']
        )
        # Save the generated audio to a file
        output_file = "output.mp3"
        response.stream_to_file(output_file)
        st.audio(output_file)
    i+=1
