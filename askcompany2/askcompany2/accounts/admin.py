from django.contrib import admin
from django.utils import timezone
from .models import Profile, User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from dateutil.relativedelta import relativedelta

# Register your models here.

class UserDateJoinedFilter(admin.SimpleListFilter):
    title = '유저 가입일'
    parameter_name = 'date_joined__match'

    def lookups(self, request, model_admin):
        return [
            ['2018-7', '2018년 7월 가입자'],
            ['2018-6', '2018년 6월 가입자'],
            ['2018-5', '2018년 5월 가입자'],
            ['2018-4', '2018년 4월 가입자'],
            ['2018-3', '2018년 3월 가입자'],
        ]

    def queryset(self, request, queryset):
        value = self.value()

        if not value:
            return queryset

        try:
            year, month = map(int, value.split('-'))
            queryset = queryset.filter(date_joined__year=year, date_joined__month=month)
        except ValueError:
            return queryset.none()

        return queryset
@admin.register(User)
class UserAdmin(AuthUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'sex', UserDateJoinedFilter)
    search_fields = ('username', 'first_name', 'last_name', 'email')
    action = ['마케팅_이메일보내기']

    def 마케팅_이메일보내기(self, request, queryset):
        for user in queryset:
            pass
        self.message_user(request, 'hello world')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display =['user', 'bio']
