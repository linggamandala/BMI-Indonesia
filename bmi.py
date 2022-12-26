#input
name = input('Masukkan nama anda: ')
sex = input('masukkan jenis kelamin (pria/wanita): ')
weight = float(input('masukkan berat anda (kg): '))
height = float(input('masukkan tinggi anda (m): '))
height_in_m = height / 10

bmi = weight / (height ** 2)
print(f'\nBMI {name} adalah', bmi)

#rumus BMI berdasarkan situs kemkes.go.id
#BMI versi wanita
if sex == 'wanita':
    if bmi <= 17:
        print(f'{name} terlalu kurus. Naikkan berat badannya ya dengan asupan yang bergizi.')
    elif bmi >= 17 and bmi <= 23:
        print(f'{name} normal. Jaga pola makan dan pola hidup yang teratur.')
    elif bmi >= 23 and bmi <= 27:
        print(f'{name} gemuk. Kurangi sedikit berat badan dengan olahraga ya.')
    elif bmi >= 27:
        print(f'{name} obesitas. Silahkan diet dan olahraga ya')

#BMI versi pria
elif sex == 'pria':
    if bmi <= 18:
        print(f'{name} terlalu kurus. Naikkan berat badannya ya dengan asupan yang bergizi.')
    elif bmi >= 18 and bmi <= 25:
        print(f'{name} normal. Jaga pola makan dan pola hidup yang teratur.')
    elif bmi >= 25 and bmi <= 27:
        print(f'{name} gemuk. Kurangi sedikit berat badan dengan olahraga ya.')
    elif bmi >= 27:
        print(f'{name} obesitas. Silahkan diet dan olahraga ya')
