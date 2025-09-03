import streamlit as st

st.set_page_config(page_title="To-Do List App", page_icon=chr(0x1F4DD))

st.title("To-Do List App")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Enter a new task:")

if st.button(f"{chr(0x2795)} Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success(f"Task '{new_task}' added!")

# Display tasks
st.subheader("Your Tasks")
for i, task in enumerate(st.session_state.tasks):
    cols = st.columns([6, 1, 1])
    with cols[0]:
        st.session_state.tasks[i]["done"] = st.checkbox(
            task["task"], value=task["done"], key=f"task_{i}"
        )
    with cols[1]:
        if st.button("Delete", key=f"delete_{i}"):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()
    with cols[2]:
        if st.session_state.tasks[i]["done"]:
            st.markdown(chr(0x2713))

# Clear completed tasks
if st.button("Clear Completed"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
    st.experimental_rerun()