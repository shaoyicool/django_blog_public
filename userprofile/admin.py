from django.contrib import admin

from .models import InvitationCode

# Register your models here.
class InvitationCodeAdmin(admin.ModelAdmin):
    list_display = ("code",)

    class Meta:
        model = InvitationCode


from django.contrib import admin
from .models import InvitationCode

admin.site.register(InvitationCode, InvitationCodeAdmin)

