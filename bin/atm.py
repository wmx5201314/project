import os,sys
path=os.getcwd()
s_path=os.path.dirname(path)
main_path="{}\\core".format(s_path)
sys.path.append(main_path)
import main
main.start()