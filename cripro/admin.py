from django.contrib import admin
# Register your models here.
from cripro.models import Team,Players,Matches,Points

admin.site.register(Team)
admin.site.register(Players)
admin.site.register(Matches)
admin.site.register(Points)