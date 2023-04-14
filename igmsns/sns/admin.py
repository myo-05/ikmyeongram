from django.contrib import admin # django에서 admin 툴을 사용하겠다
from .models import Post # 우리가 생성한 모델을 불러온다

# Register your models here.
admin.site.register(Post) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다