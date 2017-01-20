from cryptography.fernet import Fernet
from os import listdir
from os import getcwd
from os import chdir
from os.path import isfile, join

def encrypt_auto(filename, key):
    f = open(filename, "rb+")
    data = f.read()
    
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(b"{}".format(data))
    f.close()

    f = open(filename, "rb+")
    f.write(cipher_text)
    f.close()

def enc_files(directory, key):
    allfiles = listFiles(directory)
    for i in range(len(allfiles)):
        if allfiles[i] != "try.py" or allfiles[i] != "Encrypt.py" or allfiles[i] != "Decrypt.py":
            encrypt_auto(directory+"\\"+allfiles[i], key)
        
def listFiles(directory):
    mypath = directory
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles
    
def listDir(directory):
    mypath = directory
    onlydirs = [f for f in listdir(mypath) if not isfile(join(mypath, f))]
    return onlydirs

def enc_all(directory):
    key = Fernet.generate_key()
    enc_files(directory,key)
    k = directory+" : "+ key + "\n"
    alldirs = listDir(directory)
    if len(alldirs) != 0:
        for i in range(len(alldirs)):
            dirpath = directory+"\\"+alldirs[i]
            k += enc_all(dirpath)
    return k
    
################################################################################
def main():
    encfile = ""
    while encfile == "":
        encfile = raw_input("[+] Please the root folder's path: ").strip('"')

    enc_data = enc_all(encfile)

    folder = encfile.replace('\\', ',').replace(':','^')
    chdir(getcwd()+"/Encrypted Folders")
    struct = open(folder +'.txt', 'w')
    struct.write(enc_data)
    struct.close()
    print "[!] The encryption ended successfully!"
    wait = raw_input("[*] Press \'Enter\' to close.")

if __name__ == "__main__":
    main()
