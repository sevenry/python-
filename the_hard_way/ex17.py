from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("copying from %s to %s" % (from_file, to_file))

in_file = open(from_file)
indata = in_file.read()

print("the input file is %d bytes long" % len(indata))

print("does the output file exists %r" % exists(to_file))#exists仅仅返回了True/False的值，并没有起作用。
print("ready, hit return to continnue, c to abort.")
input()#这一行提供了判断的功能。即接受了上一行的返回命令，continue/abort。

out_file = open(to_file, 'w')
out_file.write(indata)

print("all done.")

out_file.close()
in_file.close()