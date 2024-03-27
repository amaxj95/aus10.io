import streamlit as st
import functions

st.set_page_config(layout="wide")

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("The todo app")
st.subheader("Aus10's variation of a todo app")
st.write("This app is to help increase productivity.")

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
