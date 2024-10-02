import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga_mobil_toyota.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas Toyota')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input KM Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')

predict = ''

if st.button('Estimasi Harga'):
  predict = model.predict(
    [[year, mileage, tax, mpg, engineSize]]
  )
  st.write('Estimasi Harga Mobil Bekas dalam Pounds :', predict)
  st.write('Estimasi Harga Mobil Bekas dalam Rupiah :', predict*16000)