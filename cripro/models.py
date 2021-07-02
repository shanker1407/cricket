from django.db import models



class Team(models.Model):
    """Model class for the cripro apps Teams
       """
    team_name = models.CharField(max_length=100)
    team_logo = models.ImageField(upload_to='media/')
    club_state = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name


class Players(models.Model):
    """Model class for the cripro apps Players
       """
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_fname = models.CharField(max_length=100)
    player_lname = models.CharField(max_length=100)
    player_image = models.ImageField(upload_to='media/')
    jersey_number = models.IntegerField(null=False, blank=False)
    player_country = models.CharField(max_length=100)
    total_matches = models.IntegerField(default=0)
    total_runs = models.IntegerField(default=0)
    hundreds = models.IntegerField(default=0)
    half_centuries = models.IntegerField(default=0)
    highest_score = models.IntegerField(default=0)
    total_wickets = models.IntegerField(default=0)
    highest_wickets = models.IntegerField(default=0)

    def __str__(self):
        return self.player_fname


class Matches(models.Model):
    """Model class for the cripro apps Matches
       """
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two')
    result = models.ForeignKey(Team, max_length=50, null=True, blank=True, on_delete=models.CASCADE)


class Points(models.Model):
    """Model class for the cripro apps Points
       """
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return str(self.team)
