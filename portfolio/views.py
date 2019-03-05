from django.shortcuts import render, get_object_or_404
from .models import Portfolio
# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios':portfolios})

def p_detail(request, portfolio_id):
    p_details = get_object_or_404(Portfolio, pk = portfolio_id)
    #몇번객체애 담아 pk 는 프라이머리 키 이거 기준찾아가라
    return render(request, 'p_detail.html', {'p_details':p_details})# 이거 왜쓰는거임?

