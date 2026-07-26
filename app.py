import streamlit as st
st.title("Proyecto módulo 1 Fundamentals")
st.sidebar.title("Parámetros")

st.image("Python_logo.png")
st.sidebar.image("DMC.png")   

modulo = st.sidebar.selectbox("Elija un modulo",["Modulo Listas","Modulo Array","Modulo funciones"])

if modulo == "Modulo Listas":

  valor_inicial = st.number_input("ingrese el valor inicial",value=0)
  valor_final = st.number_input("ingrese el valor final",value = 1)
  lista_numerica = list(range(valor_inicial,valor_final))
  st.write(lista_numerica)

elif modulo == "Modulo Array":
  st.write("Estas en el modulo de arreglos")

else 
  st.write("Estas en el modulo de funciones")
   
