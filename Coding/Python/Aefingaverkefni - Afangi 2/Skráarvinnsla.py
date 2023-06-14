
#Skrifa í skrá
#Ný skrá verður til og skrifast yfir gömlu með "w"
with open("test.txt","w",encoding="utf-8") as f:
    f.write("This is my first file\n")
    f.write("This file\n")
    f.write("contains three lines\n")
#Bæta við nýjum línum með "a"
with open("test.txt","a",encoding="utf-8") as f:
    f.write("Konráð")
    f.write("\nGuðmundsson")
    f.write("\nHraunbraut 27")

#Opna og loka skrá
try:
    f = open("test.txt","a",encoding="utf-8")
finally:
    f.close()

#Opna bara fyrstu 4 gildin
f = open("test.txt","r",encoding="utf-8")
breyta = f.read(4)
print(breyta)
breyta = f.read()
print(breyta)
#Skoða hvar bendillinn er
skoda = f.tell()
#Færa bendilinn
faera = f.seek(0)
#Lesa úr skrá línu fyrir línu
for line in f:
    print(line, end="")
#Lesa eina línu
lina = f.readline()
print(lina)
linur = f.readlines()
print(linur)
#fleiri aðferðir
f.close() #Close an open file. No effect if file is already closed
f.fileno() #Return an integer number of the file
f.flush() #Flush the write buffer of the file stream
f.isatty() #Return True if the file stream is interactive
f.read() #Read atmonst n characters from the file
f.readable() #Returns True if the file stream can be read from
f.readline(n = -1) #Read and return one line
f.readlines(n = -1) #Read and return a list of lines from the file
f.seek() #Change the file posistion to offset
f.seekable() #Returns True if file supports random access
f.tell() #Returns current file location
f.truncate(size=none)#Resize the file
f.writable() #Returns True if the file stream can be written to
f.write() #Write string to the file and return a number of charcters written
f.writelines() #Write a list of lines to the file

r #Open a file for reading
w #Open a file for writing. Creates a new file if it does not exist. Overwrites the file if it exists
x #Open a file for exclusive creation. Operation failes if the file exists
a #Open for appending at the end of the file. Creates a new file if it not exists
t #Open in text mode
b #Open in binary mode
+ #Open a file for updating reading and writing
