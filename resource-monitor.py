import pandas as pd
from matplotlib import pyplot as plt
import os
import datetime
import psutil

def main():
    #grabs the current ram usage and cpu usage data
    RAM = psutil.virtual_memory()[2]
    CPU = psutil.cpu_percent()

    check()
    cwd = os.path.dirname(os.path.realpath(__file__))
    date = getDate()
    rampath = cwd+"\\Data\\RAM\\"+date
    cpupath = cwd+"\\Data\\CPU\\"+date
    ramgraph = cwd+"\\Graphs\\"+date
    cpugraph = cwd+"\\Graphs\\"+date
    #pulls the existing excel docs and parses them
    ramfile = pd.ExcelFile(rampath+".xls")
    cpufile = pd.ExcelFile(cpupath+".xls")
    ramdata = []
    ramvalues = ramfile.parse()
    cpudata = []
    cpuvalues = cpufile.parse()
    
    #takes the already existing elements in the excel docs into a list
    for data in ramvalues.values:
        ramdata.append(data[1])
    for data in cpuvalues.values:
        cpudata.append(data[1])
    #appends the usage data to the list of elements
    ramdata.append(RAM)
    cpudata.append(CPU)

    #creates the dataframes that are then converted into excel docs and graphs
    df = pd.DataFrame(ramdata)
    df.to_excel(rampath+".xls")
    df.plot(yticks = [0,25,50,75,100], title="RAM Usage", legend=False)
    plt.savefig(ramgraph+"-RAM.png")
    df = pd.DataFrame(cpudata)
    df.to_excel(cpupath+".xls")
    df.plot(yticks = [0,25,50,75,100], title="CPU Usage", legend=False)
    plt.savefig(cpugraph+"-CPU.png")

    print("success")


#method grabs the current date down to the day constructing a string for file naming
def getDate():
    now = datetime.datetime.now()
    date = "/"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)
    return date

#method checks if the file structures are in place
def check():
    print("checking")
    date = getDate()
    cwd = os.getcwd()
    rampath = cwd+"\\Data\\RAM"
    cpupath = cwd+"\\Data\\CPU"
    ramgraph = cwd+"\\Graphs"
    cpugraph = cwd+"\\Graphs"
    if not os.path.exists(rampath):
        os.makedirs(rampath)
    if not os.path.exists(cpupath):
        os.makedirs(cpupath)
    if not os.path.isfile(rampath+date+".xls"):
        df = pd.DataFrame()
        fullpath = rampath+date+".xls"
        df.to_excel(fullpath)
    if not os.path.isfile(cpupath+date+".xls"):
        df = pd.DataFrame()
        fullpath = cpupath+date+".xls"
        df.to_excel(fullpath)
    if not os.path.exists(ramgraph):
        os.makedirs(ramgraph)
    if not os.path.exists(cpugraph):
        os.makedirs(cpugraph)
if __name__ == "__main__":
    main()
