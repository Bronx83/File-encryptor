There are two scripts in this repository:
* Must do 'pip install cryptography'
* The program creates a table with the folder and the key used under a folder named '/Encrypted Folders'
  that should be located in the folder of the script.
[+] Encrypt - you give it a folder and it encrypts the files under it with a random key
	      (same key for all of the files), if there are sub-folders it will encrypt
	      them as well, but with a unique key. (AES algorithem).
	      [!] you may use drag-n-drop of the folder you wish to encrypt to the cmd window
		  instead of writing the whole path to it.
		  (same is possible in decrypting).
[+] Decrypt - shows you the root folders you encrypted using 'Encrypt' so you can copy the
	      path of the directories from there (but you may still use drag-n-drop.
	      uses the table Encrypt created and decrypts the folders, after that it removes
	      the file.

* The reason it works like that is when you wish to encrypt files, you don't want to keep the
  key anywhere in the computer, so you can put the program on a USB device and always run it
  from there.

[!!] * Don't forget to create the folder '/Encrypted Folders'.
     * I don't take any responsability of any usage of all of my programs.
