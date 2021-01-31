


SET TDATE=%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%
rem 取得前一日的資料
set TDATE=20200302
echo "系統日期:"
ECHO %TDATE%
cd "C:\Users\Arthur\Documents\MT5\FX_CME_XAUUSD"

type NotWorkDay.txt |find "%TDATE%"
goto STEP%ERRORLEVEL%
:STEP0
  ECHO "EXIST in (NotWorkDay.txt) , NOT A WORKDY...."
  timeout /t  5
  EXIT
:STEP1
   C:\Users\Arthur\Anaconda\python.exe P003_取得CME交易所資訊_盤後_每日市場成交資訊.py -t %TDATE%
  timeout /t  5
EXIT  