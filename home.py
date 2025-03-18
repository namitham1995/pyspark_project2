from dataloading import Create_dataframe
import logs.log_fn as log
data_path= 'Data/Chocolate Sales.csv'
try:
   chocolate = Create_dataframe(data_path,True)
   chocolate.show()
   print('**************************')
   log.log_Info(f'Data frame created successfully')
except Exception as e:
    print(f'There is some error while creating table:{e}')
    print('**************************')
    log.log_Error(f'There is some error while creating table:{e}')
print('******************Analytics1****************************')
from Analytics.file1 import Analytics1
try:
   result1=Analytics1(chocolate)
   result1.show()
   result1.write.csv('RESULT/Analytics1',header=True,mode='overwrite')
   log.log_Info(f'Analytics1 executed successfully')
except Exception as e:
    log.log_Error(f'There is some error in analytics1:{e}')
print('******************Analytics2****************************')
from Analytics.file2 import Analytics2
try:
    result2 = Analytics2(chocolate)
    result2.show()
    result2.write.csv('RESULT/Analytics2',header=True,mode='overwrite')
    log.log_Info(f'Analytics2 executed successfully')
except Exception as e:
    log.log_Error(f'There is some error in analytics2:{e}')

