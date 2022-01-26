
def write_file(file_name,stuff):
    try:
        file = open(file_name,"w")
        file = file.write(stuff)
        file.close()
    except:
        print("cant write the file")
#can raise exception any time byusing raise
raise Exception("WTF**")