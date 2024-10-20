from django.shortcuts import render
from custom_admin.views import Tournament
# Create your views here.




def tournaments(request):
    tournaments = [
        Tournament(1, 'Tournament 1', '2021-10-01', 10),
        Tournament(2, 'Tournament 2', '2021-10-02', 20),
        Tournament(3, 'Tournament 3', '2021-10-03', 30),
    ]

    return render(request, 'tournaments.html', {'tournaments': tournaments})
