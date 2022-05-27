def greetings(nama, waktu):
    print('hello', nama, 'selamat', waktu)

# greetings('malam', 'wahyu') #Positional parameter
# greetings(waktu='malam', nama='wahyu')  #named parameter

def penjumlahan(a,b):
    hasil = a+b
    return hasil

data_greeting = greetings('wahyu', 'pagi')

hasil_jumlah = penjumlahan(2,5)

print(data_greeting)
print(hasil_jumlah)