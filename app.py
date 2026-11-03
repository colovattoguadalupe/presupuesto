import streamlit as st
import pdf_presupuesto
import calculos
import mi_negocio   

 
st.title(mi_negocio.nombre)
st.caption(mi_negocio.rubro)

numero = st.number_input("N° de presupuesto", min_value=1, step=1) 
fecha = st.date_input("Fecha")
cliente = st.text_input("Ingrese su nombre")

# Usás las listas desde mi_negocio:
producto = st.selectbox("Producto", mi_negocio.productos)
cant = st.number_input("Ingrese cantidad", min_value=0, step=1)

pos = calculos.buscar_posicion(mi_negocio.productos, producto)
precio = mi_negocio.precios[pos]
subtotal = precio * cant


pago = st.radio("Forma de pago", ["Efectivo", "Transferencia"])
#elegir forma de pago


con_desc = calculos.aplicar_descuento(subtotal, pago)
desc = subtotal - con_desc
iva = calculos.calcular_iva(con_desc)
total = round(con_desc + iva, 2)


st.metric("Precio", f"${precio}")
st.metric("subtotal", f"${subtotal}")
st.metric("Descuento", f"${desc}")
st.metric("Neto con descuento", f"${con_desc}")
st.metric("iva", f"${iva}")
st.metric("TOTAL", f"${total}")

archivo = pdf_presupuesto.armar_pdf(
    numero=numero, fecha=fecha, cliente=cliente, producto=producto,
    cantidad=cant, precio=precio, subtotal=subtotal,
    descuento=desc, iva=iva, total=total)




st.download_button("Descargar presupuesto (PDF)", archivo,
                   file_name=f"presupuesto_{numero}.pdf", mime="application/pdf")



