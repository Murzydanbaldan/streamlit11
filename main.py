import streamlit as st
import pandas as pd
import numpy as np
import requests 
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
from PyPDF2 import PdfReader

st.set_page_config(page_title="Dashboard Penjualan", layout="wide")

st.title("hello semua")
st.text("perkenalkan nama saya nabila")
st.header('Bagian 1: Pendahuluan')
st.caption('Data ini hanya untuk tujuan demonstrasi.')



# Menambahkan elemen ke Sidebar
st.sidebar.header("Ini Sidebar")
st.sidebar.radio("Pilih Opsi", ["Opsi 1", "Opsi 2", "Opsi 3"])

# Konten utama
st.title("Konten Utama")
st.write("Ini adalah konten utama yang ditampilkan di layar.")

st.code('import pandas as pd, import numpy as np')

st.text('saya adalah seorang mahasiswa bisdig feb unm.')

st.latex(r' ')

st.markdown('**Teks Tebal** dan _Teks Miring_ serta [Tautan](https://docs.hermanto.xyz/algoritma-dan-pemrograman-dasar/python-dan-machine-learning/streamlit#id-3.1-elemen-text)')

st.divider()

aploaded_file = st.file_uploader("Pilih file CSV", type="csv")

if aploaded_file is not None:
    df = pd.read_csv(aploaded_file)
    st.dataframe(df)
else:
    st.write("tidak ada file yang diunggah")



# Data sederhana
data = {
    'Nama': ['nabila', 'ecaa', 'zidan'],
    'Umur': [25, 30, 35],
    'Kota': ['Makasssar', 'Bandung', 'enrekang']
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan DataFrame
st.write("Tabel Data:")
st.write(df)


# Membuat DataFrame random
df_random = pd.DataFrame(
    np.random.randn(10, 5),
    columns=['col %d' % i for i in range(5)]
)

# Menampilkan DataFrame random di Streamlit
st.write("DataFrame Random:")
st.dataframe(df_random)


# Menampilkan 3 metrik dalam 3 kolom
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Omset", value="Rp 200 Juta", delta="+5%")

with col2:
    st.metric(label="User Aktif", value="1.250", delta="+2%")

with col3:
    st.metric(label="Refund", value="15", delta="-1%")

# Menyiapkan layout untuk 2 kolom lagi (bisa digunakan untuk konten tambahan)
col1, col2 = st.columns(2)

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

# Membuat line chart Altair dari kolom 'a'
chart = alt.Chart(data.reset_index()).mark_line().encode(
    x='index',
    y='a'
)

# Menampilkan chart di Streamlit
st.altair_chart(chart, use_container_width=True)

data = pd.DataFrame(
    np.random.randn(1000, 2) / [100, 100] + [-6.2, 106.8],
    columns=['lat', 'lon']
)

# Menampilkan peta
st.map(data)

# Konfigurasi halaman


# Judul dashboard
st.title("📊 Dashboard Penjualan 5 Tahun")

# Data penjualan dan laba
data = pd.DataFrame({
    'Tahun': [2018, 2019, 2020, 2021, 2022],
    'Penjualan': [100, 120, 90, 140, 180],
    'Laba': [20, 30, 15, 35, 50]
})


fig_penjualan = px.line(
    data,
    x='Tahun',
    y='Penjualan',
    markers=True,
    text='Penjualan',
    title="📈 Tren Penjualan Tiap Tahun",
    labels={'Penjualan': 'Jumlah Penjualan', 'Tahun': 'Tahun'},
    template='plotly_white'
)
fig_penjualan.update_traces(textposition="top center")
fig_penjualan.update_layout(title_x=0.5)

# Grafik batang laba
fig_laba = px.bar(
    data,
    x='Tahun',
    y='Laba',
    color='Tahun',
    title="💹 Laba Tahunan",
    labels={'Laba': 'Jumlah Laba'},
    template='plotly_dark'
)
fig_laba.update_layout(title_x=0.5)

# Tampilkan grafik dalam dua kolom
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_penjualan, use_container_width=True)

with col2:
    st.plotly_chart(fig_laba, use_container_width=True)

st.divider()
st.caption('Dibuat dengan ❤️ menggunakan Streamlit dan Plotly')


with st.form("form_input"):
    nama = st.text_input("Nama")
    alamat = st.text_area("Alamat")
    usia = st.number_input("Usia", min_value=0)
    tanggal_lahir = st.date_input("Tanggal Lahir")
    waktu_janji = st.time_input("Waktu Janjian")
    jenis_kelamin = st.radio("Jenis Kelamin", ("Pria", "Wanita"))
    hobi = st.multiselect("Hobi", ["Membaca", "Olahraga", "Musik", "Traveling"])
    warna_favorit = st.color_picker("Pilih warna favorit")
    file_foto = st.file_uploader("Upload Foto")
    foto_kamera = st.camera_input("Ambil Foto dari Kamera")
    rating = st.slider("Rating Kepuasan", 1, 10)
    submitted = st.form_submit_button("Kirim Data")

if submitted:
    st.success(f"Data {nama} berhasil dikirim!")


from PIL import Image

image = Image.open('ilaa.jpg')
st.image(image, caption='Gambar Contoh')

st.image ('https://www.bing.com/th/id/OIP.4JF4xKSznSNzZHh1wEW_9gHaE8?w=274&h=211&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2', caption='Gambar dari URL', use_column_width=True)


# Menampilkan video dari file lokal

# Menampilkan video dari URL (misalnya YouTube)
st.video('https://youtu.be/VuK584MoguY?si=tg3PmHrGw5CVdCxX')

# Menampilkan audio dari file lokal
st.audio('ilaa.mp3')

# Menampilkan audio dari URL
st.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')


# Upload file
uploaded_file = st.file_uploader("Pilih file PDF atau CSV", type=['pdf', 'csv'])

if uploaded_file is not None:
    st.write("File berhasil di-upload:")
    st.write(uploaded_file.name)
    # Tombol untuk mengunduh kembali file yang sudah di-upload
    st.download_button(
        label="Unduh file",
        data=uploaded_file,
        file_name=uploaded_file.name  # Nama file sesuai file asli
    
    )


# Menampilkan PDF
uploaded_pdf = st.file_uploader("Pilih file PDF", type=["pdf"])

if uploaded_pdf is not None:
    reader = PdfReader(uploaded_pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    st.write(text)



# Menampilkan HTML langsung
html_code = """
<h1>Selamat datang di Aplikasi Streamlit!</h1>
<p>Ini adalah <strong>paragraf</strong> HTML yang dapat diproses oleh Streamlit.</p>
"""
st.markdown(html_code, unsafe_allow_html=True)



# Upload file
uploaded_file = st.file_uploader("Pilih file PDF atau CSV", type=['pdf', 'csv'], key="file_uploader_1")


if uploaded_file is not None:
    st.write("File berhasil di-upload:")
    st.write(uploaded_file.name)
    # Tombol download file
    st.download_button(
        label="Unduh file",
        data=uploaded_file,
        file_name=uploaded_file.name  # agar nama file tetap sama saat diunduh
    )


# Membuat dua kolom
col1, col2 = st.columns(2)

# Menampilkan konten di kolom pertama
with col1:
    st.header("Kolom 1")
    st.write("Ini adalah konten di kolom pertama.")
    st.button("Tombol Kolom 1")

# Menampilkan konten di kolom kedua
with col2:
    st.header("Kolom 2")
    st.write("Ini adalah konten di kolom kedua.")
    st.button("Tombol Kolom 2")

import streamlit as st

with st.expander("Klik untuk melihat lebih banyak"):
    st.write("Ini adalah konten tersembunyi yang bisa dilihat saat pengguna klik expander.")
    st.image("https://media.istockphoto.com/id/541993270/id/foto/seseorang-melompat-ke-danau-tahoe.jpg?s=612x612&w=is&k=20&c=ogNrw9DOtGG9NPVeSVTJTRi1KOV0aEkHA_fZnJmB3D4=", caption="Contoh Gambar")


# Membuat container
container = st.container()

# Menambahkan elemen ke dalam container
with container:
    st.header("Konten di dalam Container")
    st.write("Ini adalah elemen-elemen yang ada dalam container.")
    st.button("Tombol dalam Container")




