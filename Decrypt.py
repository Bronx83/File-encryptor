from cryptography.fernet import Fernet
from os import listdir
from os import getcwd
from os.path import isfile, join
from os import remove
from os import chdir

def decrypt(filename, key):
    f = open(filename, "rb+")
    data = f.read()

    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(b"{}".format(data))
    f.close()

    open(filename, 'w').close() #clear file
    
    f = open(filename, "rb+")
    f.write(plain_text)
    f.close()
    print "[!] The decryption was successfull for :" + filename

def dec_files(directory, key):
    allfiles = listFiles(directory)
    for i in range(len(allfiles)):
        if allfiles[i] != "try.py" or allfiles[i] != "Encrypt.py" or allfiles[i] != "Decrypt.py":
            decrypt(directory+"\\"+allfiles[i], key)
        
def listFiles(directory):
    mypath = directory
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles
    
################################################################################
def main():
    for file in listdir(getcwd()+"/Encrypted Folders"):
        if file.endswith(".txt"):
            print('[+] ' + file.strip(".txt").replace(',','\\').replace('^',':'))
    folder = raw_input("[!] Which root folder would you like to Decrypt?\n")
    folder = folder.strip('"')
    folder = folder.replace('\\', ',').replace(':','^')+'.txt'
    
    chdir(getcwd()+"/Encrypted Folders")
    struct = open(folder, 'r')
    enc_data = struct.readlines()

    num = 0
    lines = []
    for line in enc_data:
        lines.insert(num, line.split(' : '))
        num+=1

    for dec in lines:
        dec_files(dec[0], dec[1])
    
    struct.close()
    print "[!] The decryption ended successfully!"
    open(folder, 'w').close() #clear file
    remove(folder)
    wait = raw_input("[*] Press \'Enter\' to close.")
if __name__ == "__main__":
    main()
