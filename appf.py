# appf.py

import streamlit as st
import yfinance as yf
from etfs_info import ETFs_Data  # Importamos la lista de ETFs

# Título principal de la aplicación
st.title("Simulador de Inversión - Allianz")

# Descripción amigable
st.write("Selecciona uno o más ETFs para ver su rendimiento y simular una inversión:")

# Cargar nombres de los ETFs
etf_nombres = [etf['nombre'] for etf in ETFs_Data]

# Selector de multiselección para los ETFs
seleccion_etfs = st.multiselect('Selecciona uno o más ETFs para comparar', etf_nombres)

# Verificar si se seleccionaron ETFs
if len(seleccion_etfs) > 0:
    for etf_nombre in seleccion_etfs:
        # Buscar el símbolo del ETF en la lista
        simbolo = [etf['simbolo'] for etf in ETFs_Data if etf['nombre'] == etf_nombre][0]
        
        # Descargar los datos históricos del ETF usando yfinance
        datos_etf = yf.download(simbolo, period='1y')
        
        # Verificar si se descargaron datos
        if datos_etf.empty:
            st.write(f"No se encontraron datos para {etf_nombre}.")
        else:
            # Mostrar los datos del ETF
            st.write(f"Datos del ETF: {etf_nombre}")
            st.write(datos_etf.tail())  # Mostrar las últimas filas
            
            # Calcular el rendimiento del ETF
            rendimiento = (datos_etf['Adj Close'][-1] - datos_etf['Adj Close'][0]) / datos_etf['Adj Close'][0] * 100
            st.write(f"Rendimiento en el último año: {rendimiento:.2f}%")
else:
    st.write("Por favor, selecciona al menos un ETF para mostrar los resultados.")
