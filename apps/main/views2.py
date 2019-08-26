from django.shortcuts import render

from apps.main.utils import group_required


@group_required("group2")
def main(request):
    template = 'main2/main.html'
    return render(request, template)
