import streamlit as st 
import time 



st.title("Pomodoro Timer")

work_time = st.slider("Work Time (minutes)", 1, 90, 25)
break_time = st.slider("Break Time (minutes)",1, 30, 5)

def pomodoro(work_time, break_time):
    work_seconds = work_time * 60 
    break_seconds = break_time * 60 

    spacer = st.empty()
    work_placeholder = st.empty()
    break_placeholder = st.empty()


    # work_placeholder.write("Work!")
    for i in range(work_seconds):
        time.sleep(1) # 1 seconds sleep
        # work_placeholder.write(f"Work Countdown : {work_seconds-i} seconds left")
        # st.html("<br>")
        # st.html("<br>")
        # st.markdown("<br>", unsafe_allow_html=True)
        # st.markdown("<br>", unsafe_allow_html=True)
        spacer.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)

        work_placeholder.html(f"<span style='font-size: 24px; background-color: red; color: white; padding: 15px; margin-top: 10px; border-radius: 40px;'>Work Countdown:  {work_seconds-i} Seconds Left</span>")
        


    # break_placeholder.write("Break!")
    for i in range(break_seconds):
        time.sleep(1) # 1 seconds sleep
        # break_placeholder.write(f"Break Countdown : {break_seconds-i} seconds left")
        spacer.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)
        work_placeholder.html(f"<span style='font-size: 24px; background-color: green; color: white; padding: 15px; margin-top: 10px; border-radius: 40px;'>Break Countdown:  {break_seconds-i} Seconds Left</span>")

if st.button("Start Timer"):
    pomodoro(work_time, break_time)