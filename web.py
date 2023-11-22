import streamlit as st

import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todes(todos)


st.title("My Todo App")
st.subheader("this is my todo app ")
st.write("this app is to increase your productivity.")

for index ,todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todes(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="enter a todo ", key='new_todo', on_change=add_todo)

st.session_state
