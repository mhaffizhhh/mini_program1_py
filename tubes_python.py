import os

os.system("cls")

while True:
    nama1 = str(input('Masukkan Nama Anda: ')).title()

    print('\n')

    konsonan1=vokal1=0

    for huruf in nama1:
        if huruf=='a' or huruf=='i' or huruf=='u' or huruf=='e' or huruf=='o':
            vokal1+=1
        elif huruf=='A' or huruf=='I' or huruf=='U' or huruf=='E' or huruf=='O':
            vokal1+=1
        else:
            if huruf!=" ":
                konsonan1+=1
            else:
                pass

    nama2 = str(input('Masukkan Nama Anda: ')).title()

    konsonan2=vokal2=0

    for huruf in nama2:
        if huruf=='a' or huruf=='i' or huruf=='u' or huruf=='e' or huruf=='o':
            vokal2+=1
        elif huruf=='A' or huruf=='I' or huruf=='U' or huruf=='E' or huruf=='O':
            vokal2+=1
        else:
            if huruf!=" ":
                konsonan2+=1
            else:
                pass

    print("""
    Kecocokan sebagai:
    1. Pasangan
    2. Teman
    3. Sahabat
    """)

    pilih = input('Pilihan Anda: ')

    #jika input huruf
    if pilih.isalpha():
        while True:
            pilih = input('Pilihan Anda: ')

            #coba ngecek jika input direntang 1-3
            try:  
                if int(pilih) in range(1,4):
                    break
            except:
                pass
    #jika input diluar rentang 1-3
    elif int(pilih)<1 or int(pilih)>3:
        while True:
            pilih = input('Pilihan Anda: ')
    
            #coba ngecek jika input direntang 1-3
            try:  
                if int(pilih) in range(1,4):
                    break
            except:
                pass
    else:
        pass

    print('\n')

    #jika milih 1
    if pilih=='1':
        #agar hasil tidak lebih dari 100%
        if len(nama1)>len(nama2):
            print(f'Kecocokan {nama1} dan {nama2} sebagai pasangan adalah {int(len(nama2)/len(nama1)*100)}%')
        else:
            print(f'Kecocokan {nama1} dan {nama2} sebagai pasangan adalah {int(len(nama1)/len(nama2)*100)}%')
    #jika milih 2
    elif pilih=='2':
        #agar hasil tidak lebih dari 100%
        if vokal1>vokal2:
            print(f'Kecocokan {nama1} dan {nama2} sebagai teman adalah {int(vokal2/vokal1*100)}%')
        #jika nama gada huruf vokal
        elif vokal1==0 and vokal2==0:
            print(f'Kecocokan {nama1} dan {nama2} sebagai teman adalah 0%')
        else:
            print(f'Kecocokan {nama1} dan {nama2} sebagai teman adalah {int(vokal1/vokal2*100)}%')
    #jika milih 3
    elif pilih=='3':
        #agar hasil tidak lebih dari 100%
        if konsonan1>konsonan2:
            print(f'Kecocokan {nama1} dan {nama2} sebagai sahabat adalah {int(konsonan2/konsonan1*100)}%')
        #jika nama gada huruf konsonan
        elif konsonan2==0 and konsonan1==0:
            print(f'Kecocokan {nama1} dan {nama2} sebagai sahabat adalah 0%')
        else:
            print(f'Kecocokan {nama1} dan {nama2} sebagai sahabat adalah {int(konsonan1/konsonan2*100)}%')
    else:
        pass

    print('\n')

    berhenti = input('Lanjut bermain (y/n): ')

    if berhenti=='n':
        break
    else:
        os.system("cls")

print('\nAkhir dari program terimakasih')