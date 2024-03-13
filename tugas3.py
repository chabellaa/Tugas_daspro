def create_dictionary(keys, values):
    result = {}
    if len(keys) != len(values):
        print("Panjang list kunci dan list nilai harus sama")
        return None

    for i in range(len(keys)):
        result[keys[i]] = values[i]

    return result

# List key
keys = ['minggu', 'bulan', 'tahun']

# List values
values = ['7 Hari', '4 Minggu', '12 Bulan']

data_dictionary = create_dictionary(keys, values)

print("Data Dictionary:")
print(data_dictionary)