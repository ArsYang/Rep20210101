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
    tdate=datetime.datetime.now()
    str_tdate=str(tdate.year*10000+tdate.month*100+tdate.day)
    #str_tdate="20190812"

    
    
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
       
            
#str_tdate_MMDDYYYY=str_tdate[4:6:]+"/"+str_tdate[6:8:]+"/" +  str_tdate[0:4:]
       #payload = {'response': 'csv',
       #         'date': '20181003',
       #          '_':'1538293969927'}
    headers = {
  #  ':authority':'www.cmegroup.com',
  #  ':method':'GET',
 #   ':path':'/cn-t/trading/fx/g10/euro-fx_quotes_settlements_futures.html',
 #    ':path':'/CmeWS/mvc/Settlements/Futures/Settlements/58/FUT?tradeDate=01/31/2019&strategy=DEFAULT&pageSize=50&_=1549069211422',
 #   ':scheme':'https',
        'Accept':'application/javascript, */*; q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-TW',
        'Cookie':'na_id=2019052311475917600710610960; na_tc=Y; uvc=0%7C28%2C0%7C29%2C0%7C30%2C0%7C31%2C5%7C32; mus=0; loc=MDAwMDBBU1RXMDAyMDQxMzAxNTAwMDAwMDBDSA==; uid=5ce6886f7413cbf0; ouid=5ce6886f00015bcab00990220cbbdb621dc3cf1e685df5a5b227',
    
        'Host':'s7.addthis.com',
		#'upgrade-insecure-requests:':'1',
        'Referer': 'https://www.cmegroup.com/cn-t/trading/metals/precious/gold_quotes_settlements_futures.html',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
  #  'x-requested-with': 'XMLHttpRequest',
   
    }
    
    rs = requests.Session()
    
#08,17,2019  mm,dd,yyyy 
    #url="https://www.cmegroup.com/CmeWS/mvc/Settlements/Futures/Settlements/437/FUT?strategy=DEFAULT&tradeDate=08%2F15%2F2019&pageSize=50&_=1566022124769"  
    url="https://www.cmegroup.com/CmeWS/mvc/Settlements/Futures/Settlements/437/FUT?strategy=DEFAULT&tradeDate={0}%2F{1}%2F{2}&pageSize=50&_=1566017916661".format(str_tdate[4:6],str_tdate[6:8],str_tdate[0:4])
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
    
    
    
    datafile_JSON ="{0}_D003_取得CME交易所資訊_盤後_每日市場成交資訊.JSON".format(str_tdate)
    with open(datafile_JSON, 'w+'  , encoding='utf8') as fp:
        for item in list_aa:
            fp.write(item)  
           
     
    datafile_CSV ="{0}_D003_取得CME交易所資訊_盤後_每日市場成交資訊.CSV".format(str_tdate)

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
       
     
     
