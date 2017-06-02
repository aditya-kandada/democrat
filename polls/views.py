from django.shortcuts import render
from polls.models import Candidate


def index(request):


    candidates = Candidate.objects.all().order_by('name')

    return render(request, 'index.html', {'candidates':candidates})