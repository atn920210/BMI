# 這是一個檢測 BMI 的程式
height = input('請輸入您的身高(cm):')
weight = input('請輸入您的體重(Kg):')
height = float(height)
weight = float(weight)
bmi = weight / (height * height * 0.0001) 
# print('您的BMI:', bmi)
if bmi < 18.5:
	print('您的BMI:', bmi, '過輕')
elif bmi >= 18.5 and bmi < 24:
	print('您的BMI:', bmi, '正常')
elif bmi >= 24 and bmi < 27:
	print('您的BMI:', bmi, '過重')
elif bmi >= 27 and bmi < 30:
	print('您的BMI:', bmi, '輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('您的BMI:', bmi, '中度肥胖')
else:
	print('您的BMI:', bmi, '重度肥胖')