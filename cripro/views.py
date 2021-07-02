import random
from django.db import connection
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PlayersForm
from .models import Players, Team, Matches, Points


def teams_list(request):
    """View method for 'cripro' app's team' list page.
        :return: HttpResponse
        """
    cursor = connection.cursor()
    cursor.execute('''select * from cripro_team''')
    teams = cursor.fetchall()
    return render(request, 'cripro/teams_list.html', {'teams': teams})


def add_player(request):
    """View method for 'cripro' app's  add_players'list page.
        :return: HttpResponse
        """
    cursor = connection.cursor()
    cursor.execute('''select * from cripro_team''')
    team = cursor.fetchall()
    form = PlayersForm()
    return render(request, 'cripro/add_player.html', {'form': form, 'team': team})


def save_player(request):
    """View method for 'cricpro' app's save_player' save_details page.
        :return: HttpResponse
        """
    if request.method == 'POST':
        form_obj = PlayersForm(request.POST, request.FILES)
        if form_obj.is_valid():
            form_obj.save()

            return HttpResponseRedirect('/cripro/')

    return HttpResponseRedirect('/cripro/')


def team_players(request):
    """View method for 'cricpro' app's team_players' players_list page.
        :return: HttpResponse
        """
    cursor=connection.cursor()
    cursor.execute(f''' select *
    from cripro_team
    join cripro_players
    on cripro_team.id = cripro_players.team_id
    where cripro_team.id = {id}''')
    list1=cursor.fetchall()
    return render(request, 'cripro/player_list.html', {'list': list1})


def player_info(request):
    """View method for 'cricpro' app's player_info' players_details page.
        turn: HttpResponse
        """
    player=Players.objects.get(id=id)
    return render(request, 'cripro/player_info.html', {'player': player})


def matches(request):
    """View method for 'cricpro' app's matches' create page.
        :return: HttpResponse
        """
    teams = Team.objects.all()
    team1 = random.choice(teams)
    ex = teams.exclude(team_name=team1.team_name)
    team2 = random.choice(ex)
    winner = random.choice((team1, team2))
    win_tm = Points.objects.get_or_create(team=winner)
    Matches.objects.create(team1=team1, team2=team2, result=winner)
    win_tm.played += 1
    win_tm.won += 1
    win_tm.points += 2
    win_tm.save()
    if team1.team_name == win_tm.team.team_name:
        l_team = team2
    else:
        l_team = team1
    loss_tm = Points.objects.get_or_create(team=l_team)
    loss_tm.played += 1
    loss_tm.lost += 1
    loss_tm.points += 0
    loss_tm.save()
    return render(request, "cripro/points_table.html",
                  {"win": win_tm, "loss": loss_tm, "teams": teams})


def points(request):
    """View method for 'cricpro' app's points' points_table page.
        :return: HttpResponse
        """
    point=Points.objects.all
    return render(request, 'cripro/points.html',
                  {'point': point})


def match_history(request):
    """View method for 'cricpro' app's match_history' match_details page.
        :return: HttpResponse
        """
    match = Matches.objects.all
    return render(request, 'cripro/history.html',
                  {"match": match})


