from django.shortcuts import render, redirect


# ===============================
# Index View
# ===============================
def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'index.html')
        
