#
import re
import sys
# Defaults

# sys.argv.append("email_venice.txt")
# sys.argv.append("venice.txt")

argslen = len(sys.argv)

# path='/proj/lwa_workarea/CCX_Diag/Nirvana/BRH/A0/CDL_IT_Logs/Dense/'
# Read excel.xlsx to Get the log***.log,
#  and companion dmesg***.log in the same root (directory).
input_emails = "email.txt"
outfile   = "output_diag_mi350.txt"

if argslen < 2:
    print("Example invocations include: python dl_extract_email.py <input emails> <output filename>")
    print("input emails <filename[" + input_emails + "]>")
    print("output emails <filename[" + outfile + "]>")
    sys.exit(0)
else:
    if( argslen > 1 ):
        if(sys.argv[1]):
            input_emails = sys.argv[1] 
    if( argslen > 2 ):
        if(sys.argv[2]):
            outfile = sys.argv[2]
print("Input File: " + input_emails)
print("Output File: " + outfile)

outf=open(outfile,'w+')
with open(input_emails,'r') as f:
    for string in f:
      for line in string.split(";"):
        m = re.search("<(.*)>", line)
        print (m[1])
        outf.write(m[1] + "\n")
f.close()
outf.close()