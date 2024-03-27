import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/Aus10.png")  # add logo.png

with col2:
    st.title("Austin Jones")
    content = """A Virginia State University Alum with nearly 6 years of professional software engineering IT 
    experience; working with Government contracting companies. Full Stack and Automation Engineer. I specialize 
    in python, kubernetes, helm, and docker work. I also run a Junk Removal and Trash Collection Company that 
    services the Northern VA, DC, and Maryland region I also strive to exceed professional and personal goals. 
    In my free time I enjoy spending time with family, refereeing, being outside and taking it easy."""
    st.write(content)

content2 = """Below you can find my git repositories, some apps I've built, and my company's website"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[App]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[App]({row['url']})")
