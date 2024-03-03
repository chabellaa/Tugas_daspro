#menentukan variabel
hari_kerja = 27
hari_kerja_perbulan = 24
gaji_pokok = 670000
gaji_lembur = 250000

#membuat pengecekan dengan kondisi else if
if hari_kerja > hari_kerja_perbulan:
    total_gaji = (hari_kerja/hari_kerja_perbulan)* gaji_pokok + gaji_lembur
elif hari_kerja < hari_kerja_perbulan:
    total_gaji = (hari_kerja/hari_kerja_perbulan)* gaji_pokok

#cetak hasil
print ('total_gaji : Rp.', (f"{total_gaji:,}"))
