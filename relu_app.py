import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title = "ReLU Activation", layout = "centered")
st.title("ReLU Activation Fuction")

st.write("ReLU(x) = max(0, x)")

x_min, x_max = st.slider("x range", -20, 20, (-10, 10))
x = np.linspace(x_min, x_max, 500)
y = np.maximum(0,x)

fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_xlabel("x")
ax.set_ylabel("ReLU(x)")
ax.set_title("ReLU Curve")
st.pyplot(fig)

st.markdown("**Why used : ** simple + helps with vanishing gradient compared to sigmoid/tanh.")