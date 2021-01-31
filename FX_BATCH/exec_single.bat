


rem SET TDATE=%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%
rem 取得前一日的資料

echo "EURUSD系統日期:"
ECHO %TDATE%
set TDATE1=%1
 
ECHO "---------EURUSD-------------"
cd "C:\Users\arthur\Documents\MT5\FX_CME" 
C:\Users\user\Anaconda3\python.exe P001_取得CME交易所資訊_盤後_每日市場成交資訊.py -t %TDATE1%

ECHO "------- XAUUSD-----------"
cd "C:\Users\arthur\Documents\MT5\FX_CME_XAUUSD"
C:\Users\user\Anaconda3\python.exe P003_取得CME交易所資訊_盤後_每日市場成交資訊.py -t %TDATE1%
rem timeout /t  15

 