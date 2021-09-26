from django.contrib import admin
from .models import CustomUser, Certificate, PreviewSettings, ManualPosts, MainPagePost, \
                    QiwiSecretKey, Deposit, Withdrawal


class CertAdmin(admin.ModelAdmin):
    list_display = ('number', 'nominal', 'creator', 'owner', 'is_paid', )
    list_display_links = ('number', 'nominal',)
    ordering = ['-published_date']
    list_filter = ('nominal', 'creator', 'owner', 'is_paid',)
    search_fields = ('number', 'nominal', 'creator', 'owner', 'is_paid', )


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'real_account',
                    'balance', 'telegram_id',)
    list_display_links = ('first_name', 'email',)
    ordering = ['-real_account']
    list_filter = ('real_account', 'balance',)
    search_fields = ('first_name', 'email', 'real_account',
                     'balance', 'telegram_id',)


class ManualAdmin(admin.ModelAdmin):
    list_display = ('index_number', 'title',)
    list_display_links = ('index_number', 'title',)
    ordering = ['index_number']


class MainPagePostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'id', 'date_create',)
    list_display_links = ('headline',)
    ordering = ['-date_create']


class DepositAdmin(admin.ModelAdmin):
    list_display = ('bill_id', 'amount', 'status', 'user', 'time',)
    list_display_links = ('bill_id', 'amount', 'status',)
    ordering = ['-time']
    list_filter = ('status', 'user',)
    search_fields = ('bill_id', 'amount', 'status', 'user', 'time',)

    
class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ('bill_id', 'amount', 'status', 'user', 'qiwi_wallet','time',)
    list_display_links = ('bill_id', 'amount', 'status',)
    ordering = ['-time']
    list_filter = ('status', 'user',)
    search_fields = ('amount', 'status', 'user', 'time', 'bill_id')


class PreviewAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=PreviewSettings):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=PreviewSettings):
        return True


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Certificate, CertAdmin)
admin.site.register(PreviewSettings, PreviewAdmin)
admin.site.register(ManualPosts, ManualAdmin)
admin.site.register(MainPagePost, MainPagePostAdmin)
admin.site.register(QiwiSecretKey)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(Withdrawal, WithdrawalAdmin)


admin.site.site_title = 'Панель администратора'
admin.site.site_header = 'Money Certificates'
