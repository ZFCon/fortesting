from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    html = render(request, template_name)
    print(html.content)

    return html
