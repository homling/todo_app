import streamlit as st
import functions as func

st.title("Todo app")

todos = func.get_todos()


def add_todo():
    if st.session_state.input_text != "":
        todos.append(st.session_state.input_text + "\n")
        func.write_todos(todos)


def item_select_tocomplete_callback(sindex: str):
    todos.pop(sindex)
    func.write_todos(todos)


for index, item in enumerate(todos):
    st.checkbox(item, key=index, on_change=item_select_tocomplete_callback, args=(index,))

input_content = st.text_input(label="", key="input_text", placeholder="add new todo", on_change=add_todo)
