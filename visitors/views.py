from django.contrib import messages
from django.shortcuts import render, redirect
from visitors.forms import VisitorsForm

def visitor_register(request):
    form = VisitorsForm()
    
    if request.method == "POST":
        form = VisitorsForm(request.POST)
        
        if form.is_valid():
            visitor = form.save(commit=False)
            visitor.registered_by = request.user
            visitor.save()
            
            messages.success(
                request,
                "Visitor successfully registered"
            )
            
            return redirect("index")
            
    context = {
        "page_name": "Visitor Register",
        "form": form
    }
    
    return render(request, "visitors_register.html", context)
