import numpy as np

def checkinput():
    key = input("Enter the encryption key (unique, non-repeating, alpha only)...")
    flag = 0
    itr_lis = list(key)
    for i in itr_lis:
        itr_lis.remove(i)
        if i in itr_lis:
            print(f"Your key has more than one '{i}', Enter a valid key (unique, non-repeating, alpha only)!!!")
            checkinput()
        else:
            if ord(i.lower()) >= 97 and ord(i.lower()) <= 122:
                print(i)
                flag+=1
    if flag == len(key):
        return key
    else:
        print(flag,key,len(key))
        print(f"You have entered a non alphabetical character, Enter a valid key (unique, non-repeating, alpha only)")
        checkinput()
     

plaintext = input("Enter the text to be encrypted...")
# enc_key = input("Enter the encryption key (unique, non-repeating, alpha only)...")
enc_key = checkinput()

enc_key_list = list(enc_key)
enc_matrix = np.zeros((5,5))

alp_list = list('abcdefghijklmnopqrstuvwxyz')
index = alp_list.index('h')
alp_list.remove('h')
alp_list.remove('i')
alp_list.insert(index,'hi')

print(enc_key)
# print(alp_list)


# print(enc_matrix)
