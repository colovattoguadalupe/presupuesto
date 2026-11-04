import streamlit as st
import pdf_presupuesto
import calculos
import mi_negocio   

st.title(mi_negocio.nombre)
st.caption(mi_negocio.rubro)

numero = st.number_input("N° de presupuesto", min_value=1, step=1) 
fecha = st.date_input("Fecha")
cliente = st.text_input("Ingrese su nombre")

# Selección de productos
RENGLONES = 3
nombres = []
cantidades = []
precios_unitarios = []
for i in range(RENGLONES):
    producto = st.selectbox(f"Producto {i + 1}", mi_negocio.productos)
    cantidad = st.number_input(f"Cantidad {i + 1}", min_value=0, step=1)
    if cantidad > 0:
        pos = calculos.buscar_posicion(mi_negocio.productos, producto)
        nombres.append(producto)
        cantidades.append(cantidad)
        precios_unitarios.append(mi_negocio.precios[pos])

#elegir forma de pago
pago = st.radio("Forma de pago", ["Efectivo", "Transferencia"])

# Sumamos el total de cada producto ingresado:
subtotal = 0
for i in range(len(cantidades)):
    subtotal = subtotal + (cantidades[i] * precios_unitarios[i])

con_desc = calculos.aplicar_descuento(subtotal, pago)
desc = subtotal - con_desc
iva = calculos.calcular_iva(con_desc)
total = round(con_desc + iva, 2)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Subtotal", f"${subtotal:,.2f}")
col2.metric("Descuento", f"-${desc:,.2f}")
col3.metric("IVA (21%)", f"${iva:,.2f}")
col4.metric("TOTAL", f"${total:,.2f}")

archivo = pdf_presupuesto.armar_pdf(
    numero=numero,
    fecha=fecha,
    cliente=cliente,
    nombres=nombres,
    cantidades=cantidades,
    precios_unitarios=precios_unitarios,
    subtotal=subtotal,
    descuento=desc,
    iva=iva,
    total=total
)

st.download_button("Descargar presupuesto (PDF)", archivo,
                   file_name=f"presupuesto_{numero}.pdf", mime="application/pdf")

