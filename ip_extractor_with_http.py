import sys, getopt 
import re 
def arg_check(argv):
   global inputfile
   global outputfile
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Your Fucking Input file is "', inputfile
   print 'your Fucking Output file is "', outputfile
   
if __name__ == "__main__":
  '''Printing .....IP's from Lists or TEXT
  THANKS F0r Wa!t!ing'''
  print(__main__.__doc__)
  arg_check(sys.argv[1:])
  re_pattern = re.compile(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})')
  with open(inputfile, "r") as fh_in:
     with open(outputfile, "a+") as fh_out:
         for line in fh_in:
            match_list = re_pattern.findall(line)
            if match_list:
                fh_out.write('http://' +match_list[0]+"\r\n")
                fh_out.write('https://' +match_list[0]+"\r\n")
