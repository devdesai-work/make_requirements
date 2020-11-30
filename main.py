import argparse
import glob
from subprocess import check_output


ap = argparse.ArgumentParser()
ap.add_argument("-f",'--location',required=True,help="Path to the Directory for which you need requirements.txt file")
args = vars(ap.parse_args())


file_loc = args["location"]
files = []
for file_name in glob.iglob(file_loc+'/**/*.py', recursive=True):
  files.append(file_name)

final_list = []
for name in files :
    f = open(name,"r")
    lis = f.read().split("\n")
    f.close()

    modules = []
    get = check_output("pip freeze")
    installed_modules = str(get.decode("utf-8")).split("\n")

    for line in lis:
        if "import" in line:
            modules.append(line.split(" ")[1])

    module_names =[]
    [module_names.append(x) for x in modules if x not in module_names]


    for module_ in module_names:
        for module in installed_modules:
            if module_ in module:
               final_list.append(module.split("\r")[0])



with open(file_loc + "\\requirements.txt",'w') as f:
    for name in final_list:
        f.write("%s\n" % name)
f.close()









