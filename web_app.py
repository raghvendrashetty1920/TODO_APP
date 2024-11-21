#Run the app on terminal by typing:-[streamlit run web_app.py]

import streamlit as st
import function

TODOS=function.get_todo()

def add_todo():
    todo=st.session_state["new_todo"] +'\n' # it store the of new list.
    TODOS.append(todo)
    function.write_todo(TODOS)


st.title("TODO-LIST",)
st.subheader("Enter your check-list")

for i,todo in enumerate(TODOS):# gives us check_box
    check_box=st.checkbox(todo,key=todo)
    if check_box:
        TODOS.pop(i)#remove the check_list after selecting
        function.write_todo(TODOS)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",
              placeholder="Add new todo",
              on_change=add_todo,key='new_todo')












