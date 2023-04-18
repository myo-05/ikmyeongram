from django.shortcuts import redirect

def homes(request):
    return redirect("api/sns/")