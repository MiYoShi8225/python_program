st = open("st.txt", "w")
st.write("Hi from Python")
st.close()

st = open("rt.txt", "w", encoding="utf-8")
st.write("Hi from Python日本語版")
st.close()

