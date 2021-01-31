import requests
import datetime
import sys, getopt
from bs4 import BeautifulSoup

import json
import csv



str_tdate='20190208' 



# 將查詢參數加入 GET 請求中
#html = requests.get("http://www.twse.com.tw/zh/page/trading/exchange/FMTQIK.html", params=payload)

#def main(argv):
#tdate=datetime.datetime.now()
#str_tdate=str(tdate.year*10000+tdate.month*100+tdate.day)
#str_tdate_MMDDYYYY=str_tdate[4:6:]+"/"+str_tdate[6:8:]+"/" +  str_tdate[0:4:]

#str_tdate=""
#try:
#       opts, args = getopt.getopt(argv,"t:",["tdate="])
#    except getopt.GetoptError:
#       print ('test.py -t <str_tdate>')
 #      sys.exit(2)
#    for opt, arg in opts:
#       if opt in ("-t", "str_tdate(yyyymmdd)"):
#          str_tdate = arg
    #---------------main process ------------- 
     
#    print ('输入的日期：', str_tdate)

#str_tdate_MMDDYYYY=str_tdate[4:6:]+"/"+str_tdate[6:8:]+"/" +  str_tdate[0:4:]
   #payload = {'response': 'csv',
   #         'date': '20181003',
   #          '_':'1538293969927'}
headers = {
        ':authority':'www.dailyfx.com.hk',
        ':method':'GET',
        ':path':'/sentiment',
        ':scheme':'https',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie':'_ga=GA1.3.6052721.1549598601; _gid=GA1.3.323350837.1549598601; _gcl_au=1.1.641519024.1549598601; AMCVS_434717FE52A6476F0A490D4C%40AdobeOrg=1; __gads=ID=3d3173a9dfaad01d:T=1549598601:S=ALNI_Ma0qgJmZ0QaJxxP557IeYOoTcevHg; AMCV_434717FE52A6476F0A490D4C%40AdobeOrg=1406116232%7CMCIDTS%7C17936%7CMCMID%7C79773979325572507580133418210778141435%7CMCAAMLH-1550203401%7C11%7CMCAAMB-1550203401%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1549605801s%7CNONE%7CMCSYNCSOP%7C411-17943%7CMCAID%7CNONE%7CvVersion%7C2.5.0; __adroll_fpc=afdeb8b86e6fd1d60b49887ca1607248; _fbp=fb.2.1549598601832.1918632429; Hm_lvt_299c9d94a991d9c9bd2d6e4856fa0ebf=1549598602; x_userid=XFz-iqwcrgUAAeOrYccAAAAW; AAMC_iggroup_0=REGION%7C11; aam_uuid=71727508038490065850929479691606962116; __atuvc=1%7C6; __atuvs=5c5cff9d3b02ba6d000; aamoptsegs=aam%3D11830771; __ar_v4=IWS3T7TBGVEMNP4EE772SJ%3A20190210%3A5%7CWELRGQVCXBA45CRTIKI22O%3A20190210%3A5%7CA6YYGNDHQRH73PPGEU6OBP%3A20190210%3A5; Hm_lpvt_299c9d94a991d9c9bd2d6e4856fa0ebf=1549599023',
        'upgrade-insecure-requests:':'1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.dailyfx.com.hk/'
}

rs = requests.Session()

	#url="https://www.cmegroup.com/CmeWS/mvc/Settlements/Futures/Settlements/58/FUT?tradeDate=02/01/2019&strategy=DEFAULT&pageSize=50&_=1549069211422"
url="https://www.dailyfx.com.hk/sentiment"
  
	#res.encoding="utf-8"    
	#res = rs.get(url,headers=headers)
res=rs.get(url)    

list_aa=res.text
datafile_JSON ="{0}_PD002_取得IG即時資訊_SSI情緒指數.JSON".format(str_tdate)
with open(datafile_JSON, 'w+'  , encoding='utf8') as fp:
	for item in list_aa:
		fp.write(item)  
           
 
datafile_CSV ="{0}_PD002_取得IG即時資訊_SSI情緒指數.CSV".format(str_tdate)

inputFile = open(datafile_JSON, 'r' , encoding='utf8') #open json file
outputFile = open(datafile_CSV, 'w' , encoding='utf8') #load csv file
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
    
      outf.writerow(row.values())

outputFile.close()    
        
    
   
 

#if __name__ == "__main__":
#   main(sys.argv[1:])
 
