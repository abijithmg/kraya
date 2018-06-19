from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Index(TemplateView):
    template_name = "index.html"


def product(request):
    import pdb
    pdb.set_trace()
    if request.method == "POST":
        pass
    template_name = "product.html"
    context = {}
    return render(request, template_name, context)
