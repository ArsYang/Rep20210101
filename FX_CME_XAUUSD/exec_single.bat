


SET TDATE=%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%
rem ���o�e�@�骺���
set TDATE=20200302
echo "�t�Τ��:"
ECHO %TDATE%
cd "C:\Users\Arthur\Documents\MT5\FX_CME_XAUUSD"

type NotWorkDay.txt |find "%TDATE%"
goto STEP%ERRORLEVEL%
:STEP0
  ECHO "EXIST in (NotWorkDay.txt) , NOT A WORKDY...."
  timeout /t  5
  EXIT
:STEP1
   C:\Users\Arthur\Anaconda\python.exe P003_���oCME����Ҹ�T_�L��_�C�饫�������T.py -t %TDATE%
  timeout /t  5
EXIT  