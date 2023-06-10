import json

import pandas as pd
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Players, Lineup, Clubs, Championships, Matches, Hit
from .apps import compose
from .serializer import HitSerializer


@api_view(['GET'])
def all_matches(request):
    if request.method == 'GET':
        m = Matches.objects.all()
        print(m[0].tour.championship)
    return Response({})


@api_view(['POST'])
def post_predicted_hit(request):
    if request.method == "POST":
        data = dict(request.data)
        player = Players.objects.get(pk=int(data['playerId'][0]))
        match = Matches.objects.get(pk=int(data['match_id'][0]))
        club = Clubs.objects.get(pk=int(data['team_id'][0]))
        data['footed'] = player.footed
        # match = models.ForeignKey(Matches, on_delete=models.CASCADE, default=None, related_name="hits")
        # player = models.ForeignKey(Players, on_delete=models.CASCADE, default=None)
        # club = models.ForeignKey(Clubs, on_delete=models.CASCADE, default=None)
        # xPos = models.FloatField(default=None, verbose_name="X")
        # yPos = models.FloatField(default=None, verbose_name="Y")
        # distance = models.FloatField(default=None, verbose_name="Расстояние")
        # angle = models.FloatField(default=90, verbose_name='Угол')
        # passes_before = models.IntegerField(default=0, verbose_name='Пасы до удара')
        # shots_before = models.IntegerField(default=0, verbose_name='Удары до удара')
        # shots_by_team_before = models.IntegerField(default=0, verbose_name='Удары всей команды до удара')
        # shooted_by = models.CharField(max_length=15, verbose_name='Чем ударил', default="Head")
        # isGoal = models.BooleanField(default=False, verbose_name="Гол")
        #
        # PG = models.FloatField(default=0.5, verbose_name='predicted goal')

        hit = {'match': match, 'player': player,
               'club': club, 'xPos': float(data['x'][0]), 'yPos': float(data['y'][0]),
               'distance': float(data['distance'][0]), 'angle': float(data['angle'][0]),
               'passes_before': int(data['passes_before'][0]), 'shots_before': int(data['shots_before'][0]),
               'shots_by_team_before': int(data['shots_by_team_before'][0]), 'shooted_by': data['shootedBy'][0],
               }
        if data['isGoal'][0] == "False":
            hit['isGoal'] = False
        else:
            hit['isGoal'] = True
        df = pd.DataFrame(data)
        hit['PG'] = compose.predict_proba(df.drop('isGoal', axis=1))[:, 1][0]
        #print(compose.predict_proba(df.drop('isGoal', axis=1))[0])
        predicted_hit = Hit(**hit)
        predicted_hit.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)
