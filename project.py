import streamlit as st
st.title('Growth Mindset Challenge')
st.write("""
Welcome to the Growth Mindset Challenge!

In this app, you will learn how to develop a growth mindset by setting learning goals and reflecting on your progress.

Remember, growth happens when we embrace challenges and learn from our mistakes!
""")
goal = st.text_input("What's your learning goal for the next month?")
mindset = st.slider("How would you rate your current growth mindset?", 0, 100, 50)
if mindset < 50:
    st.write("It looks like you may have a more fixed mindset. Try focusing on learning from challenges!")
else:
    st.write("Great job! You're already embracing a growth mindset. Keep pushing yourself to grow even more.")
if st.button('Set Goal'):
    if goal:
        st.write(f"Your goal is: {goal}. Stay focused, and don't forget to track your progress!")
    else:
        st.write("Please enter a goal to set it!")
st.markdown("""
> "Success is the ability to go from one failure to another with no loss of enthusiasm." - Winston Churchill
""")
reflection = st.checkbox("Would you like to reflect on your learning so far?")
if reflection:
    st.text_area("Write your reflections here:", height=150)
