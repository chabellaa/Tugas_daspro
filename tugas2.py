# Data dictionary berisi username dan password mahasiswa
data_mahasiswa = {
    'Nurul': {'password': 'pass1'},
    'Nurdalifa': {'password': 'pass2'},
    'Maulidia': {'password': 'pass3'},
    'Manda': {'password': 'pass4'},
    'Diva': {'password': 'pass5'},
    'Wahdania': {'password': 'pass6'},
    'Rahmawati': {'password': 'pass7'},
    'Riskawati': {'password': 'pass8'},
    'Arfa': {'password': 'pass9'},
    'Rafika': {'password': 'pass10'},
 
}

# Fungsi login
def login(username, password):
    if username in data_mahasiswa and password == data_mahasiswa['Nurul', 'Arfa', 'Diva', 'Manda', 'Maulidia', 'Nurdalifa', 'Rafika', 'Rahmawati',
                                                                  'Riskawati', 'Wahdania']['password']:
        print(f"Selamat datang, {username}!")
    else:
        print("Data yang dimasukkan tidak ada.")

# Input dari pengguna
input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

# Melakukan login
login(input_username, input_password)
