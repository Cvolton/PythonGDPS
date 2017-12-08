from django.http import HttpResponse
from django.template import Context, Template

def hello(request):
    t = Template("Sakuješ {{count}} špeků")
    c = Context({'count': str(randint(69,420))})
    return HttpResponse(t.render(c))
