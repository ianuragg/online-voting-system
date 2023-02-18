from django.contrib import admin
from . models import User
from account.models import User
from core.models import Election, Candidate, Result

#Django admin header customization
admin.site.site_header = "Voting App Admin Login"
admin.site.site_title = "Welcome to Admin Dashboard"
admin.site.index_title = "Admin Dashboard"

#User Model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'fname', 'contact', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    ordering = ('email',)
    search_fields = ('email',)

#Election Model
@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ('election_uid', 'election_state', 'election_name', 'start_date', 'end_date', 'is_active')
    ordering = ('election_state',)
    search_fields = ('election_state',)

#Candidate Model
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('cand_election', 'cand_name', 'cand_state', 'cand_party', 'total_votes', 'is_active')
    ordering = ('cand_state',)
    search_fields = ('cand_state',)

#Result Model
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('voter', 'candidate', 'election', 'is_voted')
    ordering = ('voter',)
    search_fields = ('voter',)