import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def arrhenius(T_C, A, Ea):
    R = 8.314
    T = T_C + 273.15
    k = A * np.exp(-Ea / (R * T))
    return k

def reaction(C, t, k):
    return -k * C

st.title('과산화수소 분해 반응 시뮬레이터')

T_C = st.slider('온도 (°C)', 0, 100, 25)
A = st.number_input('빈도인자 A (s⁻¹)', value=1e11, format="%.1e")
Ea = st.number_input('활성화 에너지 Ea (J/mol)', value=75000)
C0 = st.number_input('초기 농도 (mol/L)', value=0.1)
t_max = st.number_input('시뮬레이션 시간 (초)', value=300)

k = arrhenius(T_C, A, Ea)
st.write(f'계산된 반응속도상수 k = {k:.4e} s⁻¹')

t = np.linspace(0, t_max, 100)
C = odeint(reaction, C0, t, args=(k,))

fig, ax = plt.subplots()
ax.plot(t, C)
ax.set_xlabel('Time (s)')
ax.set_ylabel('H2O2 Concentration (mol/L)')
ax.set_title(f'Decomposition Reaction at {T_C}°C')
st.pyplot(fig)
