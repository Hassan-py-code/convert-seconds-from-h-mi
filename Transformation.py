# يقوم المستخدم بإدخال عدد الثواني ثم تقوم بتحويلها إلى دقائق وساعات وثوان.
second=int(input('Entre the second:\n'))

minuts=second//60

hours=second//3600 

seconds=second%60

print(f"The duration is:{hours} hours,{minuts} minuts,and {seconds} seconds")
