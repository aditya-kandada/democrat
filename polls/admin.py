from django.contrib import admin

# Register your models here.
from polls.models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'upvote', 'downvote']


admin.site.register(Candidate, CandidateAdmin)

