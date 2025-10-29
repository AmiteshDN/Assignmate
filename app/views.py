from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render(
        request,
        "assignmate/index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )