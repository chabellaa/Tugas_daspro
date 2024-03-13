# Data dictionary berisi username dan password mahasiswa
data_mahasiswa = {
    'Nurul': {'password': 'pass1'},
    'Nurdalifa': {'password': 'pass2'},
    'Maulidia': {'password': 'pass3'},
 
}

# Fungsi login
def login(username, password):
    if username in data_mahasiswa and password == data_mahasiswa['Nurul']['password']:
        print(f"Selamat datang, {username}!")
    else:
        print("Data yang dimasukkan salah.")

# Input dari pengguna
input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

# Melakukan login
login(input_username, input_password)