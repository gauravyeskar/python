# W.A.P.P.which will copy the content of one file into another file.
srcfile = input("Enter the Source file: ")
with open(srcfile,'r') as rp:
    dstfile = srcfile+'-copy'
    with open(dstfile,'a') as wp:
        srcdata = rp.read()
        wp.write(srcdata)
        print("File Made Successfully...!!")
