


rem SET TDATE=%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%
rem ���o�e�@�骺���

echo "EURUSD�t�Τ��:"
ECHO %TDATE%
set TDATE1=%1
 
ECHO "---------EURUSD-------------"
cd "C:\Users\arthur\Documents\MT5\FX_CME" 
C:\Users\user\Anaconda3\python.exe P001_���oCME����Ҹ�T_�L��_�C�饫�������T.py -t %TDATE1%

ECHO "------- XAUUSD-----------"
cd "C:\Users\arthur\Documents\MT5\FX_CME_XAUUSD"
C:\Users\user\Anaconda3\python.exe P003_���oCME����Ҹ�T_�L��_�C�饫�������T.py -t %TDATE1%
rem timeout /t  15

 