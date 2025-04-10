from django.shortcuts import render
from .models import Country, MinimumRequirement, TopUniversityStat, PopularUniversity
# Create your views here.
def unipage(request):
    return render(request, "unipage/main.html")

def land(request):
    return render(request, "unipage/landing.html")





def country_detail_view(request):
    countries = Country.objects.all().prefetch_related(
        'mininum_requirements', 'top_university_stats', 'popular_universities'
    )
    return render(request, 'landing.html', {'countries': countries})
