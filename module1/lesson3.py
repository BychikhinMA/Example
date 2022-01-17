str1 = 'сегодня'
str2 = '7 января'
str3 = 'хороший день'

result = str1 + ' ' + str2 + ' ' + str3 + ' для игр '
result_f = 'сегодня 7 января хороший день для игр'
print(result)
#
print(result_f) 
result_f1= '{1} {0} {1} {2}'.format(str1, str2, str3) 
print(result_f1)
#
result_f2 = f"{str1} '{str2}' {str3 }"
print(result_f2)