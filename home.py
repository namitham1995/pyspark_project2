# from dataloading import Create_dataframe
# import logs.log_fn as log
# from Analytics.file1 import Analytics1
# data_path= 'Data/Chocolate Sales.csv'
# try:
#    chocolate = Create_dataframe(data_path,True)
#    chocolate.show()
#    print('**************************')
#    log.log_Info(f'Data frame created successfully')
#
# except Exception as e:
#     print(f'There is some error while creating table:{e}')
#     print('**************************')
#     log.log_Error(f'There is some error while creating table:{e}')
# print('******************Analytics1****************************')
# try:
#    result1=Analytics1(chocolate)
#    result1.show()
#    result1.write.csv('RESULT/Analytics1',header=True,mode='overwrite')
#    log.log_Info(f'Analytics1 executed successfully')
# except Exception as e:
#     log.log_Error(f'There is some error in analytics1:{e}')
# print('******************Analytics2****************************')
# from Analytics.file2 import Analytics2
# try:
#     result2 = Analytics2(chocolate)
#     result2.show()
#     result2.write.csv('RESULT/Analytics2',header=True,mode='overwrite')
#     log.log_Info(f'Analytics2 executed successfully')
# except Exception as e:
#     log.log_Error(f'There is some error in analytics2:{e}')

# print('******************Analytics4****************************')
# from Analytics.file4 import Analytics4
# try:
#     result4 = Analytics4(chocolate)
#     result4.show()
#     log.log_Info(f'Analytics4 executed successfully')
# except Exception as e:
#     log.log_Error(f'There is some error in analytics4:{e}')
from Analytics.file4 import Analytics4

# Assuming you have a DataFrame called 'df'
# result = Analytics4(chocolate)
# result.show()
# print('****************************************************************************************************')

from dataloading import Create_dataframe
import logs.log_fn as log
from Analytics.file1 import Analytics1
from Analytics.file4 import Analytics4
from Analytics.file5 import Analytics5
data_path = 'Data/Chocolate Sales.csv'

try:
    chocolate = Create_dataframe(data_path, True)
    chocolate.show()  # Show the loaded DataFrame
    print('**************************')
    log.log_Info(f'Data frame created successfully')

except Exception as e:
    print(f'There is some error while creating table: {e}')
    print('**************************')
    log.log_Error(f'There is some error while creating table: {e}')


print('****************** Analytics1 ****************************')
try:
    result1 = Analytics1(chocolate)  # Apply Analytics1 function
    result1.show()  # Show the transformed DataFrame
    result1.write.csv('RESULT/Analytics1', header=True, mode='overwrite')  # Save the result to CSV
    log.log_Info(f'Analytics1 executed successfully')
except Exception as e:
    log.log_Error(f'There is some error in Analytics1: {e}')
print('******************Analytics2****************************')
from Analytics.file2 import Analytics2
try:
    result2 = Analytics2(chocolate)
    result2.show()
    result2.write.csv('RESULT/Analytics2',header=True,mode='overwrite')
    log.log_Info(f'Analytics2 executed successfully')
except Exception as e:
    log.log_Error(f'There is some error in analytics2:{e}')

print('******************Analytics3****************************')
from Analytics.file3 import Analytics3
try:
    result3 = Analytics3(chocolate)
    result3.show()

    log.log_Info(f'Analytics3 executed successfully')
except Exception as e:
    log.log_Error(f'There is some error in analytics3:{e}')
print('****************** Analytics4 ****************************')
try:

    result4 = Analytics4(result1)
    result4.show()
    result4.write.csv('RESULT/Analytics4', header=True, mode='overwrite')
    log.log_Info(f'Analytics4 executed successfully')

except Exception as e:
    log.log_Error(f'There is some error in Analytics4: {e}')
print('****************** Analytics5 ****************************')
try:
    result5 = Analytics5(result1)  # Assuming Analytics5 takes result1 as input
    result5.show()
    # result5.write.csv('RESULT/Analytics5', header=True, mode='overwrite')  # Save the result to CSV
    log.log_Info(f'Analytics5 executed successfully')
except Exception as e:
    log.log_Error(f'There is some error in Analytics5: {e}')


