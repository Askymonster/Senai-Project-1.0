import streamlit as st
import numpy as np
import pandas as pd 

aba1, aba2, aba3 = st.tabs(["Teorema de Pitagoras", "Pizzas", "Bebidas"])
with aba1:
    st.header("Seno, Cosseno e Tangente no triangulo de Pitagoras")
    col1, col2= st.columns(2)
    with col1: 
        C1 = st.number_input("Cateto 1")
        C2 = st.number_input("Cateto 2")
    with col2:
        st.subheader("Hipotenusa: ")
        H = np.round(np.sqrt(C1**2 + C2**2))
        st.subheader(f"{H}")
    st.markdown("---")
    
    st.subheader("Seno, Cosseno e Tangente")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Seno")
        ang = st.slider('''Angulo $ \\alpha $''',0,90, key = "sen")
        CO = st.number_input("Cateto Oposto (b)")
        H1 = np.round(CO/np.sin(ang*np.pi/180),2)
        st.subheader("Hipotenusa")
        st.subheader(f"{H1}")
    
    with col2:
        st.subheader("Cosseno")
        ang2 = st.slider('''Ángulo $ \\alpha $''',0,90, key = "cos")
        CA = st.number_input("Cateto Adjacente (a)")
        H1 = np.round(CA/np.cos(ang*np.pi/180),2)
        st.subheader("Hipotenusa")
        st.subheader(f"{H1}")        
    
    with col3:
        st.subheader("Tangente")
        ang3 = st.slider('''Ángulo $ \\alpha $''',0,90, key = "tg")
        CO = st.number_input("Cateto Oposto (c)")
        CA = np.round(CO/np.tan(ang*np.pi/180),2)
        st.subheader("Cateto Adjacente")
        st.subheader(f"{CA}")
        

    
