import streamlit as st
import numpy as np
import libreria_funciones as lf

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
  
  limite_inferior = st.number_input("ingrese el limite inferior",value=1200)
  limite_superior = st.number_input("ingrese el limite superior",value = 1250)
  cantidad_datos = st.number_input("Ingrese totalidad de datos a crear", value = 31)
  
  datos_produccion = np.random.randint(limite_inferior, limite_superior, cantidad_datos)
  
  st.write(datos_produccion)
  
  st.write("La produccion total es:" , np.sum(datos_produccion))
  st.write("La produccion promedio es:" , np.mean(datos_produccion))


else: 
  st.write("Estas en el modulo de funciones")
  
  principal = st.number_input("ingrese el Monto del prestamo",value=0)
  tasa anual = st.number_input("ingrese la tasa anual en decimal",value=0.10)
  anios = st.number_input("ingrese el numero de años del prestamos ",value=1)
  pagos_por_anio = st.number_input("ingrese la Cantidad de pagos por año",value=12)

  cuota = lf.cuota.prestamo(principal, tasa_anual, anios, pagos_por_anio)

  st.write("La cuota mensual de pago sera:", cuota)
   
