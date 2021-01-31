import requests
import sys, getopt
#from bs4 import BeautifulSoup

import json
import csv
from datetime import datetime
from datetime import timedelta
import time
import datetime
 

def main(argv):
    #tdate=datetime.datetime.now()
    #str_tdate=str(tdate.year*10000+tdate.month*100+tdate.day)
    #str_tdate_MMDDYYYY=str_tdate[4:6:]+"/"+str_tdate[6:8:]+"/" +  str_tdate[0:4:]


    try:
       opts, args = getopt.getopt(argv,"t:",["tdate="])
    except getopt.GetoptError:
      print ('test.py -t <str_tdate>')
      sys.exit(2)
    for opt, arg in opts:
       if opt in ("-t", "str_tdate(yyyymmdd)"):
          str_tdate = arg
    
    
    
    #---------------main process ------------- 
     
#    print ('输入的日期：', str_tdate)
    
#    str_tdate='20190201'
    # 計算前一日
    int_YYYY=int(str_tdate[0:4:])
    int_MM=int(str_tdate[4:6:])
    int_DD=int(str_tdate[6:8:])
    dt_tdate = datetime.date(int_YYYY,int_MM,int_DD)
	 # 計算前一日
   # aDay = timedelta(days=-1)
   # dt_tdate_prev = dt_tdate + aDay
   # str_tdate= dt_tdate_prev.strftime('%Y%m%d')
   
        
    str_tdate_MMDDYYYY=str_tdate[4:6:]+"/"+str_tdate[6:8:]+"/" +  str_tdate[0:4:]
   #payload = {'response': 'csv',
   #         'date': '20181003',
   #          '_':'1538293969927'}
    headers = {
        ':authority':'www.cmegroup.com',
        ':method':'GET',
     #   ':path':'/cn-t/trading/fx/g10/euro-fx_quotes_settlements_futures.html',
     #    ':path':'/CmeWS/mvc/Settlements/Futures/Settlements/58/FUT?tradeDate=01/31/2019&strategy=DEFAULT&pageSize=50&_=1549069211422',
        ':scheme':'https',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie':'_gcl_au=1.1.508778187.1548988960; _ga=GA1.2.541760782.1548988960; _gid=GA1.2.1154718833.1548988960; AKA_A2=A; _gat_UA-6562664-1=1; _gat_UA-63130032-1=1; __atuvc=7%7C5; __atuvs=5c54eb9e80e9a120000; _fbp=fb.1.1549069215264.1489692529',
        'upgrade-insecure-requests:':'1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.cmegroup.com/cn-t/trading/fx/g10/euro-fx_quotes_settlements_futures.html'
    }

    rs = requests.Session()

#url="https://www.cmegroup.com/CmeWS/mvc/Settlements/Futures/Settlements/58/FUT?tradeDate=02/01/2019&strategy=DEFAULT&pageSize=50&_=1549069211422"
    url="https://www.cmegroup.com/CmeWS/mvc/Settlements/Futures/Settlements/58/FUT?tradeDate={0}&strategy=DEFAULT&pageSize=50&_=1549069211422".format(str_tdate_MMDDYYYY)
 #   url=url.replace("$today", str_tdate_MMDDYYYY)
  
#res.encoding="utf-8"    
#res = rs.get(url,headers=headers)
    res=rs.get(url)    

    list_aa=res.text
    
    
    
#soup = BeautifulSoup(res.text, 'html.parser')

#print (soup.find_all("a"))
# items = soup.select(find_all) 
#for item in items:
 #  print(item.select('.date')[0].text, item.select('.author')[0].text, item.select('.title')[0].text)
    
    
    
    datafile_JSON ="{0}_D001_取得CME交易所資訊_盤後_每日市場成交資訊.JSON".format(str_tdate)
    with open(datafile_JSON, 'w+'  , encoding='utf8') as fp:
        for item in list_aa:
            fp.write(item)  
           
 
    datafile_CSV ="{0}_D001_取得CME交易所資訊_盤後_每日市場成交資訊.CSV".format(str_tdate)

    inputFile = open(datafile_JSON, 'r') #open json file
    outputFile = open(datafile_CSV, 'w') #load csv file
    data = json.load(inputFile) #load json content 
    inputFile.close() #close the input file

    outf = csv.writer(outputFile) #create a csv.write

    row_data = data['settlements']
    count = 0
#for row in data.keys():
#    output = csv.writer(outputFile) #create a csv.write 
#    output.writerow(data.keys())
#    output.writerow(data[row])
    
   


    for row in row_data:
        if count == 0:            
           header = row.keys() 
           outf.writerow(header) 
           count += 1 
	   
        row["open"]=row["open"].replace("A","").replace("B","")
        row["high"]=row["high"].replace("A","").replace("B","")
        row["low"]=row["low"].replace("A","").replace("B","")
        row["last"]=row["last"].replace("A","").replace("B","")
        outf.writerow(row.values())

    outf.writerow(str_tdate)
    outputFile.close()    
        

if __name__ == "__main__":
   main(sys.argv[1:])    
   
 
 
