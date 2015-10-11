import sys

n = int(sys.argv[1])
i=1
for line in sys.stdin :
   if (i > n):
      sys.stdout.write(line)
   i+=1
