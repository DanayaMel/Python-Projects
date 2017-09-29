# The libraries to plot, load webpages, and use regular expressions
# By: Danaya Melendez CMP464
import matplotlib.pyplot as plt
import matplotlib.pyplot as jlt
import urllib.request, urllib.error, urllib.parse
import re

def getTempFromWeb(kind, url):
    page = urllib.request.urlopen(url)
    lines = page.readlines()
    for i in range(len(lines)):
        if lines[i].decode("utf8").find(kind + " Temperature") >= 0:
            m = i
            break
    searchObj = re.search('\d+', lines[m + 2].decode("utf8"))
    return int(searchObj.group(0))

def ques1():
    prefix = "http://www.wunderground.com/history/airport/KLGA/"
    suffix = "/02/16/DailyHistory"
    years = []
    maxs = []
    for year in range(1991, 2017):
        years.append(year)
        url = prefix + str(year) + suffix
        M = getTempFromWeb("Max", url)
        maxs.append(M)
        print(year, M)
    plt.plot(years, maxs, color='m', label="Max Temp")
    plt.title("NYC High Temps for Danaya's Birthday February 16")
    plt.xlabel('Years')
    plt.ylabel('Degrees')
    plt.legend(loc=2, fontsize='x-small')
    plt.show()

    plt.hist(maxs)
    plt.title("Histogram for NYC Temps, February 16, 1992-2017")
    plt.xlabel("Temperatures")
    plt.show()
ques1()

def ques3():
    prefix = "http://www.wunderground.com/history/airport/KLGA/"
    suffix = "/02/16/DailyHistory"
    years = []
    maxs = []
    mins = []
    for year in range(1991, 2017):
        years.append(year)
        url = prefix + str(year) + suffix
        M = getTempFromWeb("Max", url)
        m = getTempFromWeb("Min", url)
        maxs.append(M)
        mins.append(m)
        print(year, M, m)
    plt.plot(years, maxs, color='y', label="Max Temp")
    plt.plot(years, mins, color='c', label="Min Temp")
    plt.title("NYC High & Low Temps for Danaya's Birthday February 16")
    plt.xlabel('Years')
    plt.ylabel('Degrees')
    plt.legend(loc=2, fontsize='x-small')
    plt.show()

    plt.hist(maxs)
    plt.title("Histogram for NYC Temps, February 16, 1992-2017")
    plt.xlabel("Temperatures")
    plt.show()
ques3()

def ques5():
    prefix = "http://www.wunderground.com/history/airport/KLGA/2017/01/"
    suffix = "/DailyHistory"
    days = []
    min = []
    for day in range(1, 32):
        days.append(day)
        url = prefix + str(day) + suffix
        n = getTempFromWeb("Min", url)
        min.append(n)
        print(day, n)

    jlt.hist(min)
    jlt.title("Histogram for NYC Min Temps, January 2017")
    jlt.xlabel("Temperatures")
    jlt.show()

print("The list of min values is: ", min)
ques5()
