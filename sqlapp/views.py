#from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Avg

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    View,
)

from .consts import ITEM_PER_PAGE

from .models import Practice, TestRoutine, TestRoutine10, Book, PracticeChoice, Codepractice, Category, Quota

import random

from .forms import QuestionForm, FindForm, QuestionChoiceForm, CodePracticeForm, QuotaForm, CodePracticeSlickForm1, CodePracticeSlickForm2, CodePracticeSlickForm3

import os

from django_pandas.io import read_frame

#ストップウォッチ
import time

from datetime import date, timedelta, datetime

from django.contrib.auth.decorators import login_required

from django.db import IntegrityError, transaction

#from book import dataframe
from django.http import HttpResponse

from django_pandas.io import read_frame

from django.http import JsonResponse

from django.utils.translation import gettext as _


from .forms import SQLForm
import pandas as pd
from django.db import connection

from django.utils import timezone


def questionRandom30(request):
    object_list = Practice.objects.all()
    if (request.method == 'POST'):
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)

    else:
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)

    dQ = Practice.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3

    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9

    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category
   
    
    d4allshuf1 = Practice.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Practice.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Practice.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Practice.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Practice.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer 

    d4allshuf6 = Practice.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer 

    d4allshuf7 = Practice.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer 

    d4allshuf8 = Practice.objects.get(id=data4allshuffle[7])
    data8Answer = d4allshuf8.answer 

    d4allshuf9 = Practice.objects.get(id=data4allshuffle[8])
    data9Answer = d4allshuf9.answer 

    d4allshuf10 = Practice.objects.get(id=data4allshuffle[9])
    data10Answer = d4allshuf10.answer 

    d4allshuf11 = Practice.objects.get(id=data4allshuffle[10])
    data11Answer = d4allshuf11.answer 

    d4allshuf12 = Practice.objects.get(id=data4allshuffle[11])
    data12Answer = d4allshuf12.answer 

    d4allshuf13 = Practice.objects.get(id=data4allshuffle[12])
    data13Answer = d4allshuf13.answer 

    d4allshuf14 = Practice.objects.get(id=data4allshuffle[13])
    data14Answer = d4allshuf14.answer 

    d4allshuf15 = Practice.objects.get(id=data4allshuffle[14])
    data15Answer = d4allshuf15.answer 

    d4allshuf16 = Practice.objects.get(id=data4allshuffle[15])
    data16Answer = d4allshuf16.answer 

    d4allshuf17 = Practice.objects.get(id=data4allshuffle[16])
    data17Answer = d4allshuf17.answer


    d4allshuf18 = Practice.objects.get(id=data4allshuffle[17])
    data18Answer = d4allshuf18.answer 

    d4allshuf19 = Practice.objects.get(id=data4allshuffle[18])
    data19Answer = d4allshuf19.answer 

    d4allshuf20 = Practice.objects.get(id=data4allshuffle[19])
    data20Answer = d4allshuf20.answer 

    d4allshuf21 = Practice.objects.get(id=data4allshuffle[20])
    data21Answer = d4allshuf21.answer


    d4allshuf22 = Practice.objects.get(pk=data4allshuffle[21])
    if dQ.wronganswer4 is str and d4allshuf22.answer != dQ.answer:
        data22Answer = dataWrongAnswer4
    else:   
        data22Answer = d4allshuf22.answer

    d4allshuf23 = Practice.objects.get(pk=data4allshuffle[22])
    if dQ.wronganswer5 is str and d4allshuf23.answer != dQ.answer:
        data23Answer = dataWrongAnswer5
    else:
        data23Answer = d4allshuf23.answer 

    d4allshuf24 = Practice.objects.get(pk=data4allshuffle[23])
    if dQ.wronganswer6 is str and d4allshuf24.answer != dQ.answer:
        data24Answer = dataWrongAnswer6
    else:
        data24Answer = d4allshuf24.answer 

    d4allshuf25 = Practice.objects.get(pk=data4allshuffle[24])
    if dQ.wronganswer7 is str and d4allshuf25.answer != dQ.answer:
        data25Answer = dataWrongAnswer7
    else:
        data25Answer = d4allshuf25.answer 

    d4allshuf26 = Practice.objects.get(pk=data4allshuffle[25])
    if dQ.wronganswer8 is str and d4allshuf26.answer != dQ.answer:
        data26Answer = dataWrongAnswer8
    else:
        data26Answer = d4allshuf26.answer 

    d4allshuf27 = Practice.objects.get(pk=data4allshuffle[26])
    if dQ.wronganswer9 is str and d4allshuf27.answer != dQ.answer:
        data27Answer = dataWrongAnswer9
    else:     
        data27Answer = d4allshuf27.answer

    

    data28Answer = dataWrongAnswer1 
    data29Answer = dataWrongAnswer2
    data30Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer, data11Answer, data12Answer, data13Answer, data14Answer, data15Answer, data16Answer, data17Answer, data18Answer, data19Answer, data20Answer, data21Answer, data22Answer, data23Answer, data24Answer, data25Answer, data26Answer, data27Answer, data28Answer, data29Answer, data30Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,30)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]
    d7_11_Answer = dataAnsList7shuffle[10]
    d7_12_Answer = dataAnsList7shuffle[11]
    d7_13_Answer = dataAnsList7shuffle[12]
    d7_14_Answer = dataAnsList7shuffle[13]
    d7_15_Answer = dataAnsList7shuffle[14]
    d7_16_Answer = dataAnsList7shuffle[15]
    d7_17_Answer = dataAnsList7shuffle[16]
    d7_18_Answer = dataAnsList7shuffle[17]
    d7_19_Answer = dataAnsList7shuffle[18]
    d7_20_Answer = dataAnsList7shuffle[19]

    d7_21_Answer = dataAnsList7shuffle[20]
    d7_22_Answer = dataAnsList7shuffle[21]
    d7_23_Answer = dataAnsList7shuffle[22]
    d7_24_Answer = dataAnsList7shuffle[23]
    d7_25_Answer = dataAnsList7shuffle[24]
    d7_26_Answer = dataAnsList7shuffle[25]
    d7_27_Answer = dataAnsList7shuffle[26]
    d7_28_Answer = dataAnsList7shuffle[27]
    d7_29_Answer = dataAnsList7shuffle[28]
    d7_30_Answer = dataAnsList7shuffle[29]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'd7_11_Answer':d7_11_Answer,
            'd7_12_Answer':d7_12_Answer,
            'd7_13_Answer':d7_13_Answer,
            'd7_14_Answer':d7_14_Answer,
            'd7_15_Answer':d7_15_Answer,
            'd7_16_Answer':d7_16_Answer,
            'd7_17_Answer':d7_17_Answer,
            'd7_18_Answer':d7_18_Answer,
            'd7_19_Answer':d7_19_Answer,
            'd7_20_Answer':d7_20_Answer,

            'd7_21_Answer':d7_21_Answer,
            'd7_22_Answer':d7_22_Answer,
            'd7_23_Answer':d7_23_Answer,
            'd7_24_Answer':d7_24_Answer,
            'd7_25_Answer':d7_25_Answer,
            'd7_26_Answer':d7_26_Answer,
            'd7_27_Answer':d7_27_Answer,
            'd7_28_Answer':d7_28_Answer,
            'd7_29_Answer':d7_29_Answer,
            'd7_30_Answer':d7_30_Answer,
            
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
    }
    return render(request, 'sqlapp/questionRandom_list30.html', params)


def questionRandom20(request):
    object_list = Practice.objects.all()
    if (request.method == 'POST'):
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,16)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,17)

    else:
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,16)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,17)

    dQ = Practice.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3


    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9

    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category
   
    
    d4allshuf1 = Practice.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Practice.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Practice.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Practice.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Practice.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer 

    d4allshuf6 = Practice.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer 

    d4allshuf7 = Practice.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer 

    d4allshuf8 = Practice.objects.get(id=data4allshuffle[7])
    data8Answer = d4allshuf8.answer 

    d4allshuf9 = Practice.objects.get(id=data4allshuffle[8])
    data9Answer = d4allshuf9.answer 

    d4allshuf10 = Practice.objects.get(id=data4allshuffle[9])
    data10Answer = d4allshuf10.answer 

    d4allshuf11 = Practice.objects.get(id=data4allshuffle[10])
    data11Answer = d4allshuf11.answer


    d4allshuf12 = Practice.objects.get(id=data4allshuffle[11])
    if dQ.wronganswer4 is str and d4allshuf12.answer != dQ.answer:
        data12Answer = dataWrongAnswer4
    else: 
        data12Answer = d4allshuf12.answer

    d4allshuf13 = Practice.objects.get(pk=data4allshuffle[12])
    if dQ.wronganswer5 is str and d4allshuf13.answer != dQ.answer:
        data13Answer = dataWrongAnswer5
    else:
        data13Answer = d4allshuf13.answer 

    d4allshuf14 = Practice.objects.get(pk=data4allshuffle[13])
    if dQ.wronganswer6 is str and d4allshuf14.answer != dQ.answer:
        data14Answer = dataWrongAnswer6
    else:
        data14Answer = d4allshuf14.answer 

    d4allshuf15 = Practice.objects.get(pk=data4allshuffle[14])
    if dQ.wronganswer7 is str and d4allshuf15.answer != dQ.answer:
        data15Answer = dataWrongAnswer7
    else:
        data15Answer = d4allshuf15.answer 

    d4allshuf16 = Practice.objects.get(pk=data4allshuffle[15])
    if dQ.wronganswer8 is str and d4allshuf16.answer != dQ.answer:
        data16Answer = dataWrongAnswer8
    else:
        data16Answer = d4allshuf16.answer 

    d4allshuf17 = Practice.objects.get(pk=data4allshuffle[16])
    if dQ.wronganswer9 is str and d4allshuf17.answer != dQ.answer:
        data17Answer = dataWrongAnswer9
    else:
        data17Answer = d4allshuf17.answer

    
    data18Answer = dataWrongAnswer1 
    data19Answer = dataWrongAnswer2
    data20Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer, data11Answer, data12Answer, data13Answer, data14Answer, data15Answer, data16Answer, data17Answer, data18Answer, data19Answer, data20Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,20)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]
    d7_11_Answer = dataAnsList7shuffle[10]
    d7_12_Answer = dataAnsList7shuffle[11]
    d7_13_Answer = dataAnsList7shuffle[12]
    d7_14_Answer = dataAnsList7shuffle[13]
    d7_15_Answer = dataAnsList7shuffle[14]
    d7_16_Answer = dataAnsList7shuffle[15]
    d7_17_Answer = dataAnsList7shuffle[16]
    d7_18_Answer = dataAnsList7shuffle[17]
    d7_19_Answer = dataAnsList7shuffle[18]
    d7_20_Answer = dataAnsList7shuffle[19]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'd7_11_Answer':d7_11_Answer,
            'd7_12_Answer':d7_12_Answer,
            'd7_13_Answer':d7_13_Answer,
            'd7_14_Answer':d7_14_Answer,
            'd7_15_Answer':d7_15_Answer,
            'd7_16_Answer':d7_16_Answer,
            'd7_17_Answer':d7_17_Answer,
            'd7_18_Answer':d7_18_Answer,
            'd7_19_Answer':d7_19_Answer,
            'd7_20_Answer':d7_20_Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list
    }
    return render(request, 'sqlapp/questionRandom_list20.html', params)


def questionRandom10(request):
    object_list = Practice.objects.all()
    if (request.method == 'POST'):
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,6)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,7)

    else:
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,6)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,7)

    dQ = Practice.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3
    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category
   
    
    d4allshuf1 = Practice.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Practice.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Practice.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Practice.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Practice.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer

    d4allshuf6 = Practice.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer

    d4allshuf7 = Practice.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer

    data8Answer = dataWrongAnswer1 

    data9Answer = dataWrongAnswer2

    data10Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,10)

    d7_1_Answer = dataAnsList7shuffle[0]

    d7_2_Answer = dataAnsList7shuffle[1]

    d7_3_Answer = dataAnsList7shuffle[2]

    d7_4_Answer = dataAnsList7shuffle[3]

    d7_5_Answer = dataAnsList7shuffle[4]

    d7_6_Answer = dataAnsList7shuffle[5]


    d7_7_Answer = dataAnsList7shuffle[6]

    d7_8_Answer = dataAnsList7shuffle[7]

    d7_9_Answer = dataAnsList7shuffle[8]

    d7_10_Answer = dataAnsList7shuffle[9]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
    }
    return render(request, 'sqlapp/questionRandom_list10.html', params)


def questionRandom(request):
    object_list = Practice.objects.all()
    if (request.method == 'POST'):
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,3)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,4)

    else:
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,3)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,4)

    dQ = Practice.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3
    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category

    dataHint1 = dQ.hint1
    dataHint2 = dQ.hint2

    data4RegAnswer = [dataAnswer, dataWrongAnswer1, dataWrongAnswer2, dataWrongAnswer3]
    data4RegAnswerShuffle = random.sample(data4RegAnswer, 4)
    data1Answer = data4RegAnswerShuffle[0]
    data2Answer = data4RegAnswerShuffle[1]
    data3Answer = data4RegAnswerShuffle[2]
    data4Answer = data4RegAnswerShuffle[3]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'dataHint1': dataHint1,
            'dataHint2': dataHint2,
            'data1Answer':data1Answer,
            'data2Answer':data2Answer,
            'data3Answer':data3Answer,
            'data4Answer':data4Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
    }
    return render(request, 'sqlapp/questionRandom_list.html', params)


def answerResult(request):
    object_list = Practice.objects.all()

    #カテゴリータブの関数を呼び出す
    categories_data = get_categories_data()

    context = {
    'selectedAns':request.POST["name1"],
    'dataAnswer' :request.POST["name0"],
    'dataQuestion' :request.POST["nameQuestion"],
    'dataExplanation' :request.POST["nameEx"],
    'dataThumbnailQ1' :request.POST["nameThuQ1"],
    'dataThumbnailQ2' :request.POST["nameThuQ2"],
    'dataThumbnailQ3' :request.POST["nameThuQ3"],
    'dataThumbnailA1' :request.POST["nameThuA1"],
    'dataThumbnailA2' :request.POST["nameThuA2"],
    'dataThumbnailA3' :request.POST["nameThuA3"],
    'object_list': object_list,
    'dataNumtaku' :request.POST['nameNumtaku'],
    'categories_data': categories_data
    }
    selectedAns = request.POST["name1"]
    dataAnswer = request.POST["name0"]
    dataQuestion = request.POST["nameQuestion"]
    dataThumbnailQ1 = request.POST["nameThuQ1"]
    dataThumbnailQ2 = request.POST["nameThuQ2"]
    dataThumbnailQ3 = request.POST["nameThuQ3"]
    dataThumbnailA1 = request.POST["nameThuA1"]
    dataThumbnailA2 = request.POST["nameThuA2"]
    dataThumbnailA3 = request.POST["nameThuA3"]
    dataNumtaku = request.POST["nameNumtaku"]
    
    if selectedAns == dataAnswer:

        return render(
            request,'book/result_success.html',context
        )
    else:
        return render(
            request,'book/result_fail.html',context
        )


def ListQuestionView(request, num=1):
    if Practice.objects.exists():
        data = Practice.objects.all().order_by('pk').reverse()
        dataFirst = Practice.objects.all().order_by('pk').reverse().first()
    selectColor = ""
    dataFirst1 = ""
    dataFirst2 = ""
    dataFirst3 = ""
    dataFirst4 = ""
    dataFirst1_page = ""
    dataFirst2_page = ""
    dataFirst3_page = ""
    dataFirst4_page = ""
    dataFirst1_shoseki = ""
    dataFirst2_shoseki = ""
    dataFirst3_shoseki = ""
    dataFirst4_shoseki = ""

    data2 = Practice.objects.all().order_by('pk').reverse()
    

    if (request.method == 'POST') and request.POST.get('nameFind'):
            form = FindForm(request.POST)
            find1 = request.POST.get('find1')
            find2 = request.POST.get('find2')
            find3 = request.POST.get('find3')
            #today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).astimezone()
            data = Practice.objects.all().order_by('pk').reverse().filter(question__contains=find1,answer__contains=find2,shoseki__name__contains=find3)
            data2 = Practice.objects.all().order_by('pk').reverse().filter(question__contains=find1,answer__contains=find2,shoseki__name__contains=find3)
            dataFirst1 = Practice.objects.all().order_by('pk').reverse().first()
            dataFirst1_page = dataFirst1.shoseki_page
            dataFirst1_shoseki = dataFirst1.shoseki
            dataFirst2 = Practice.objects.all().order_by('pk').reverse().first()
            dataFirst2_page = dataFirst2.shoseki_page
            dataFirst2_shoseki = dataFirst2.shoseki
            dataFirst3 = Practice.objects.all().order_by('pk').reverse().first()
            dataFirst3_page = dataFirst3.shoseki_page
            dataFirst3_shoseki = dataFirst3.shoseki
            selectColor = ""

            #search_performed = True  # 検索が実行されたことを示すフラグ

    else:
        form = FindForm()
        data = Practice.objects.all().order_by('pk').reverse()

        dataFirst = ""
        dataFirst1 = ""
        dataFirst2 = ""
        dataFirst3 = ""
        dataFirst1_page = ""
        dataFirst2_page = ""
        dataFirst3_page = ""
        
        #today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).astimezone()
        
        #search_performed = False

    
    page = Paginator(data2, 10)

    #カテゴリータブの関数を呼び出す
    categories_data = get_categories_data()
    categories = Category.objects.all()
    
    params = {
            'title': '',
            'form': form,
            'data': data,
            'data2': page.get_page(num),
            'dataFirst': dataFirst,
            'dataFirst1': dataFirst1,
            'dataFirst2': dataFirst2,
            'dataFirst3': dataFirst3,
            'dataFirst1_page': dataFirst1_page,
            'dataFirst2_page': dataFirst2_page,
            'dataFirst3_page': dataFirst3_page,
            'dataFirst1_shoseki': dataFirst1_shoseki,
            'dataFirst2_shoseki': dataFirst2_shoseki,
            'dataFirst3_shoseki': dataFirst3_shoseki,
            'categories_data': categories_data,
            'categories': categories,
            #'search_performed': search_performed
            
    }
    #params['search_performed'] = (request.method == 'POST') and request.POST.get('nameFind')
    return render(request, 'sqlapp/question_list.html', params)



def EachQuestionView30(request, pk):
    object_list = Practice.objects.all()
    if (request.method == 'POST'):
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = [pk]

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)

    else:
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = [pk]

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)

    dQ = Practice.objects.get(pk=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3

    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9


    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category

    
    d4allshuf1 = Practice.objects.get(pk=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Practice.objects.get(pk=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Practice.objects.get(pk=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Practice.objects.get(pk=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Practice.objects.get(pk=data4allshuffle[4])
    data5Answer = d4allshuf5.answer 

    d4allshuf6 = Practice.objects.get(pk=data4allshuffle[5])
    data6Answer = d4allshuf6.answer 

    d4allshuf7 = Practice.objects.get(pk=data4allshuffle[6])
    data7Answer = d4allshuf7.answer 

    d4allshuf8 = Practice.objects.get(pk=data4allshuffle[7])
    data8Answer = d4allshuf8.answer 

    d4allshuf9 = Practice.objects.get(pk=data4allshuffle[8])
    data9Answer = d4allshuf9.answer 

    d4allshuf10 = Practice.objects.get(pk=data4allshuffle[9])
    data10Answer = d4allshuf10.answer 

    d4allshuf11 = Practice.objects.get(pk=data4allshuffle[10])
    data11Answer = d4allshuf11.answer 

    d4allshuf12 = Practice.objects.get(pk=data4allshuffle[11])
    data12Answer = d4allshuf12.answer 

    d4allshuf13 = Practice.objects.get(pk=data4allshuffle[12])
    data13Answer = d4allshuf13.answer 

    d4allshuf14 = Practice.objects.get(pk=data4allshuffle[13])
    data14Answer = d4allshuf14.answer 

    d4allshuf15 = Practice.objects.get(pk=data4allshuffle[14])
    data15Answer = d4allshuf15.answer 

    d4allshuf16 = Practice.objects.get(pk=data4allshuffle[15])
    data16Answer = d4allshuf16.answer 

    d4allshuf17 = Practice.objects.get(pk=data4allshuffle[16])
    data17Answer = d4allshuf17.answer


    d4allshuf18 = Practice.objects.get(pk=data4allshuffle[17])
    data18Answer = d4allshuf18.answer 

    d4allshuf19 = Practice.objects.get(pk=data4allshuffle[18])
    data19Answer = d4allshuf19.answer 

    d4allshuf20 = Practice.objects.get(pk=data4allshuffle[19])
    data20Answer = d4allshuf20.answer 

    
    d4allshuf21 = Practice.objects.get(pk=data4allshuffle[20])
    data21Answer = d4allshuf21.answer


    d4allshuf22 = Practice.objects.get(pk=data4allshuffle[21])
    if dQ.wronganswer4 is str and d4allshuf22.answer != dQ.answer:
        data22Answer = dataWrongAnswer4
    else:   
        data22Answer = d4allshuf22.answer

    d4allshuf23 = Practice.objects.get(pk=data4allshuffle[22])
    if dQ.wronganswer5 is str and d4allshuf23.answer != dQ.answer:
        data23Answer = dataWrongAnswer5
    else:
        data23Answer = d4allshuf23.answer 

    d4allshuf24 = Practice.objects.get(pk=data4allshuffle[23])
    if dQ.wronganswer6 is str and d4allshuf24.answer != dQ.answer:
        data24Answer = dataWrongAnswer6
    else:
        data24Answer = d4allshuf24.answer 

    d4allshuf25 = Practice.objects.get(pk=data4allshuffle[24])
    if dQ.wronganswer7 is str and d4allshuf25.answer != dQ.answer:
        data25Answer = dataWrongAnswer7
    else:
        data25Answer = d4allshuf25.answer 

    d4allshuf26 = Practice.objects.get(pk=data4allshuffle[25])
    if dQ.wronganswer8 is str and d4allshuf26.answer != dQ.answer:
        data26Answer = dataWrongAnswer8
    else:
        data26Answer = d4allshuf26.answer 

    d4allshuf27 = Practice.objects.get(pk=data4allshuffle[26])
    if dQ.wronganswer9 is str and d4allshuf27.answer != dQ.answer:
        data27Answer = dataWrongAnswer9
    else:     
        data27Answer = d4allshuf27.answer


    
    data28Answer = dataWrongAnswer1 
    data29Answer = dataWrongAnswer2
    data30Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer, data11Answer, data12Answer, data13Answer, data14Answer, data15Answer, data16Answer, data17Answer, data18Answer, data19Answer, data20Answer, data21Answer, data22Answer, data23Answer, data24Answer, data25Answer, data26Answer, data27Answer, data28Answer, data29Answer, data30Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,30)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]
    d7_11_Answer = dataAnsList7shuffle[10]
    d7_12_Answer = dataAnsList7shuffle[11]
    d7_13_Answer = dataAnsList7shuffle[12]
    d7_14_Answer = dataAnsList7shuffle[13]
    d7_15_Answer = dataAnsList7shuffle[14]
    d7_16_Answer = dataAnsList7shuffle[15]
    d7_17_Answer = dataAnsList7shuffle[16]
    d7_18_Answer = dataAnsList7shuffle[17]
    d7_19_Answer = dataAnsList7shuffle[18]
    d7_20_Answer = dataAnsList7shuffle[19]

    d7_21_Answer = dataAnsList7shuffle[20]
    d7_22_Answer = dataAnsList7shuffle[21]
    d7_23_Answer = dataAnsList7shuffle[22]
    d7_24_Answer = dataAnsList7shuffle[23]
    d7_25_Answer = dataAnsList7shuffle[24]
    d7_26_Answer = dataAnsList7shuffle[25]
    d7_27_Answer = dataAnsList7shuffle[26]
    d7_28_Answer = dataAnsList7shuffle[27]
    d7_29_Answer = dataAnsList7shuffle[28]
    d7_30_Answer = dataAnsList7shuffle[29]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'd7_11_Answer':d7_11_Answer,
            'd7_12_Answer':d7_12_Answer,
            'd7_13_Answer':d7_13_Answer,
            'd7_14_Answer':d7_14_Answer,
            'd7_15_Answer':d7_15_Answer,
            'd7_16_Answer':d7_16_Answer,
            'd7_17_Answer':d7_17_Answer,
            'd7_18_Answer':d7_18_Answer,
            'd7_19_Answer':d7_19_Answer,
            'd7_20_Answer':d7_20_Answer,

            'd7_21_Answer':d7_21_Answer,
            'd7_22_Answer':d7_22_Answer,
            'd7_23_Answer':d7_23_Answer,
            'd7_24_Answer':d7_24_Answer,
            'd7_25_Answer':d7_25_Answer,
            'd7_26_Answer':d7_26_Answer,
            'd7_27_Answer':d7_27_Answer,
            'd7_28_Answer':d7_28_Answer,
            'd7_29_Answer':d7_29_Answer,
            'd7_30_Answer':d7_30_Answer,
            
            'data2pk3_1':data2pk3_1,
            'object_list':object_list
    }
    return render(request, 'sqlapp/questionEach_list30.html', params)

def EachQuestionView20(request, pk):
    object_list = Practice.objects.all()
    if (request.method == 'POST'):
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = [pk]

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,16)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,17)

    else:
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = [pk]

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,16)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,17)

    dQ = Practice.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3


    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9

    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category
   
    
    d4allshuf1 = Practice.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Practice.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Practice.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Practice.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Practice.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer 

    d4allshuf6 = Practice.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer 

    d4allshuf7 = Practice.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer 

    d4allshuf8 = Practice.objects.get(id=data4allshuffle[7])
    data8Answer = d4allshuf8.answer 

    d4allshuf9 = Practice.objects.get(id=data4allshuffle[8])
    data9Answer = d4allshuf9.answer 

    d4allshuf10 = Practice.objects.get(id=data4allshuffle[9])
    data10Answer = d4allshuf10.answer 

    d4allshuf11 = Practice.objects.get(id=data4allshuffle[10])
    data11Answer = d4allshuf11.answer 


    d4allshuf12 = Practice.objects.get(id=data4allshuffle[11])
    if dQ.wronganswer4 is str and d4allshuf12.answer != dQ.answer:
        data12Answer = dataWrongAnswer4
    else: 
        data12Answer = d4allshuf12.answer

    d4allshuf13 = Practice.objects.get(pk=data4allshuffle[12])
    if dQ.wronganswer5 is str and d4allshuf13.answer != dQ.answer:
        data13Answer = dataWrongAnswer5
    else:
        data13Answer = d4allshuf13.answer 

    d4allshuf14 = Practice.objects.get(pk=data4allshuffle[13])
    if dQ.wronganswer6 is str and d4allshuf14.answer != dQ.answer:
        data14Answer = dataWrongAnswer6
    else:
        data14Answer = d4allshuf14.answer 

    d4allshuf15 = Practice.objects.get(pk=data4allshuffle[14])
    if dQ.wronganswer7 is str and d4allshuf15.answer != dQ.answer:
        data15Answer = dataWrongAnswer7
    else:
        data15Answer = d4allshuf15.answer 

    d4allshuf16 = Practice.objects.get(pk=data4allshuffle[15])
    if dQ.wronganswer8 is str and d4allshuf16.answer != dQ.answer:
        data16Answer = dataWrongAnswer8
    else:
        data16Answer = d4allshuf16.answer 

    d4allshuf17 = Practice.objects.get(pk=data4allshuffle[16])
    if dQ.wronganswer9 is str and d4allshuf17.answer != dQ.answer:
        data17Answer = dataWrongAnswer9
    else:
        data17Answer = d4allshuf17.answer

    data18Answer = dataWrongAnswer1 
    data19Answer = dataWrongAnswer2
    data20Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer, data11Answer, data12Answer, data13Answer, data14Answer, data15Answer, data16Answer, data17Answer, data18Answer, data19Answer, data20Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,20)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]
    d7_11_Answer = dataAnsList7shuffle[10]
    d7_12_Answer = dataAnsList7shuffle[11]
    d7_13_Answer = dataAnsList7shuffle[12]
    d7_14_Answer = dataAnsList7shuffle[13]
    d7_15_Answer = dataAnsList7shuffle[14]
    d7_16_Answer = dataAnsList7shuffle[15]
    d7_17_Answer = dataAnsList7shuffle[16]
    d7_18_Answer = dataAnsList7shuffle[17]
    d7_19_Answer = dataAnsList7shuffle[18]
    d7_20_Answer = dataAnsList7shuffle[19]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'd7_11_Answer':d7_11_Answer,
            'd7_12_Answer':d7_12_Answer,
            'd7_13_Answer':d7_13_Answer,
            'd7_14_Answer':d7_14_Answer,
            'd7_15_Answer':d7_15_Answer,
            'd7_16_Answer':d7_16_Answer,
            'd7_17_Answer':d7_17_Answer,
            'd7_18_Answer':d7_18_Answer,
            'd7_19_Answer':d7_19_Answer,
            'd7_20_Answer':d7_20_Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
    }
    return render(request, 'sqlapp/questionEach_list20.html', params)

def EachQuestionView10(request, pk):
    object_list = Practice.objects.all()
    if (request.method == 'POST'):
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = [pk]

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,6)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,7)

    else:
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = [pk]

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,6)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,7)

    dQ = Practice.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3
    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category
   
    d4allshuf1 = Practice.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Practice.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Practice.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Practice.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Practice.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer

    d4allshuf6 = Practice.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer

    d4allshuf7 = Practice.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer

    data8Answer = dataWrongAnswer1 

    data9Answer = dataWrongAnswer2

    data10Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,10)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
    }
    return render(request, 'sqlapp/questionEach_list10.html', params)

def EachQuestionView(request, pk):
    object_list = Practice.objects.all()
    if (request.method == 'POST'):
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = [pk]
        dataafter = Practice.objects.filter(pk__in=data)

        data2 = Practice.objects.order_by('?')[:3]
        data2after = Practice.objects.filter(pk__in=data2)

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,3)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,4)

        data3 = dataafter | data2after
        data3_list = list(data3)
        if len(data3_list) == 4:
            data3_listtemp = random.sample(data3_list,4)
        else:

            dataadd = Practice.objects.order_by('?')[:1]
            dataaddafter =  Practice.objects.filter(pk__in=dataadd)
            data3 = data3 | dataaddafter
            data3_list = list(data3)

            if len(data3_list) == 4:
                data3_listtemp = random.sample(data3_list,4)
            else:
                dataadd = Practice.objects.order_by('?')[:1]
                dataaddafter =  Practice.objects.filter(pk__in=dataadd)
                data3 = data3 | dataaddafter
                data3_list = list(data3)

                if len(data3_list) == 4:
                    data3_listtemp = random.sample(data3_list,4)
                else:
                    dataadd = Practice.objects.order_by('?')[:1]
                    dataaddafter =  Practice.objects.filter(pk__in=dataadd)
                    data3 = data3 | dataaddafter
                    data3_list = list(data3)

                    if len(data3_list) == 3:
                        data3_listtemp = random.sample(data3_list,3)
                    else:
                        data3_listtemp = random.sample(data3_list,4)

    else:
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = [pk]
        dataafter = Practice.objects.filter(pk__in=data)

        data2 = Practice.objects.order_by('?')[:3]
        data2after = Practice.objects.filter(pk__in=data2)

        pks_list.remove(data[0])
        
        data2pk3_1 = random.sample(pks_list,3)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,4)

        data3 = dataafter | data2after
        data3_list = list(data3)
        if len(data3_list) == 4:
            data3_listtemp = random.sample(data3_list,4)
        else:

            dataadd = Practice.objects.order_by('?')[:1]
            dataaddafter =  Practice.objects.filter(pk__in=dataadd)
            data3 = data3 | dataaddafter
            data3_list = list(data3)

            if len(data3_list) == 4:
                data3_listtemp = random.sample(data3_list,4)
            else:
                dataadd = Practice.objects.order_by('?')[:1]
                dataaddafter =  Practice.objects.filter(pk__in=dataadd)
                data3 = data3 | dataaddafter
                data3_list = list(data3)

                if len(data3_list) == 4:
                    data3_listtemp = random.sample(data3_list,4)
                else:
                    dataadd = Practice.objects.order_by('?')[:1]
                    dataaddafter =  Practice.objects.filter(pk__in=dataadd)
                    data3 = data3 | dataaddafter
                    data3_list = list(data3)

                    if len(data3_list) == 3:
                        data3_listtemp = random.sample(data3_list,3)
                    else:
                        data3_listtemp = random.sample(data3_list,4)

        data4 = Practice.objects.filter(answer__in=data3_listtemp)

    dQ = Practice.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3

    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category

    dataHint1 = dQ.hint1
    dataHint2 = dQ.hint2

    data4RegAnswer = [dataAnswer, dataWrongAnswer1, dataWrongAnswer2, dataWrongAnswer3]   
    data4RegAnswerShuffle = random.sample(data4RegAnswer, 4)
    data1Answer = data4RegAnswerShuffle[0]
    data2Answer = data4RegAnswerShuffle[1]
    data3Answer = data4RegAnswerShuffle[2]
    data4Answer = data4RegAnswerShuffle[3]

    params = {
            'data': data,
            'data2': data2,
            'dataafter': dataafter,
            'data4': data4,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'dataHint1': dataHint1,
            'dataHint2': dataHint2,
            'data1Answer':data1Answer,
            'data2Answer':data2Answer,
            'data3Answer':data3Answer,
            'data4Answer':data4Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
    }
    return render(request, 'sqlapp/questionEach_list.html', params)

def testQuestionView(request):
    test10within10 = Practice.objects.all().count()
    test10within10Choice = PracticeChoice.objects.all().count()
    test10within10Codepractice = Codepractice.objects.all().count()

    if (request.method == 'POST'):
        form = FindForm(request.POST)
        find1 = request.POST.get('find1')
        find2 = request.POST.get('find2')
        answers = request.POST.get('answers')
        if request.POST.get('namePython3test'):
            testCategory = '【テスト対策】Python3　基礎 10問'

        elif request.POST.get('namePython3DBtest'):
            testCategory = '【テスト対策】Python3　データ分析 10問'


    else:
        form = FindForm()
        data = Practice.objects.all().order_by('pk').reverse()
        testCategory = ""
    
    #カテゴリータブの関数を呼び出す
    categories_data = get_categories_data()
    categories = Category.objects.all()

    params = {
            'title': '',
            'form': form,
            'testCategory': testCategory,
            'test10within10': test10within10,
            'test10within10Choice': test10within10Choice,
            'test10within10Codepractice': test10within10Codepractice,
            'categories_data': categories_data,
            'categories': categories
    }
    return render(request, 'sqlapp/question_test.html', params)


def questionRandom50(request):
    object_list = Practice.objects.all()
    if (request.method == 'POST'):
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)

    else:
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)

    dQ = Practice.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3

    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9

    dataExplanation = dQ.explanation

    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3

    dataCategory = dQ.category
   
    
    d4allshuf1 = Practice.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Practice.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Practice.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Practice.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Practice.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer 

    d4allshuf6 = Practice.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer 

    d4allshuf7 = Practice.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer 

    d4allshuf8 = Practice.objects.get(id=data4allshuffle[7])
    data8Answer = d4allshuf8.answer 

    d4allshuf9 = Practice.objects.get(id=data4allshuffle[8])
    data9Answer = d4allshuf9.answer 

    d4allshuf10 = Practice.objects.get(id=data4allshuffle[9])
    data10Answer = d4allshuf10.answer 

    d4allshuf11 = Practice.objects.get(id=data4allshuffle[10])
    data11Answer = d4allshuf11.answer 

    d4allshuf12 = Practice.objects.get(id=data4allshuffle[11])
    data12Answer = d4allshuf12.answer 

    d4allshuf13 = Practice.objects.get(id=data4allshuffle[12])
    data13Answer = d4allshuf13.answer 

    d4allshuf14 = Practice.objects.get(id=data4allshuffle[13])
    data14Answer = d4allshuf14.answer 

    d4allshuf15 = Practice.objects.get(id=data4allshuffle[14])
    data15Answer = d4allshuf15.answer 

    d4allshuf16 = Practice.objects.get(id=data4allshuffle[15])
    data16Answer = d4allshuf16.answer 

    d4allshuf17 = Practice.objects.get(id=data4allshuffle[16])
    data17Answer = d4allshuf17.answer


    d4allshuf18 = Practice.objects.get(id=data4allshuffle[17])
    data18Answer = d4allshuf18.answer 

    d4allshuf19 = Practice.objects.get(id=data4allshuffle[18])
    data19Answer = d4allshuf19.answer 

    d4allshuf20 = Practice.objects.get(id=data4allshuffle[19])
    data20Answer = d4allshuf20.answer 

    d4allshuf21 = Practice.objects.get(id=data4allshuffle[20])
    data21Answer = d4allshuf21.answer



    d4allshuf22 = Practice.objects.get(id=data4allshuffle[21])
    data22Answer = d4allshuf22.answer

    d4allshuf23 = Practice.objects.get(id=data4allshuffle[22])
    data23Answer = d4allshuf23.answer

    d4allshuf24 = Practice.objects.get(id=data4allshuffle[23])
    data24Answer = d4allshuf24.answer

    d4allshuf25 = Practice.objects.get(id=data4allshuffle[24])
    data25Answer = d4allshuf25.answer

    d4allshuf26 = Practice.objects.get(id=data4allshuffle[25])
    data26Answer = d4allshuf26.answer

    d4allshuf27 = Practice.objects.get(id=data4allshuffle[26])
    data27Answer = d4allshuf27.answer

    d4allshuf28 = Practice.objects.get(id=data4allshuffle[27])
    data28Answer = d4allshuf28.answer

    d4allshuf29 = Practice.objects.get(id=data4allshuffle[28])
    data29Answer = d4allshuf29.answer

    d4allshuf30 = Practice.objects.get(id=data4allshuffle[29])
    data30Answer = d4allshuf30.answer

    d4allshuf31 = Practice.objects.get(id=data4allshuffle[30])
    data31Answer = d4allshuf31.answer

    d4allshuf32 = Practice.objects.get(id=data4allshuffle[31])
    data32Answer = d4allshuf32.answer

    d4allshuf33 = Practice.objects.get(id=data4allshuffle[32])
    data33Answer = d4allshuf33.answer

    d4allshuf34 = Practice.objects.get(id=data4allshuffle[33])
    data34Answer = d4allshuf34.answer

    d4allshuf35 = Practice.objects.get(id=data4allshuffle[34])
    data35Answer = d4allshuf35.answer

    d4allshuf36 = Practice.objects.get(id=data4allshuffle[35])
    data36Answer = d4allshuf36.answer

    d4allshuf37 = Practice.objects.get(id=data4allshuffle[36])
    data37Answer = d4allshuf37.answer

    d4allshuf38 = Practice.objects.get(id=data4allshuffle[37])
    data38Answer = d4allshuf38.answer

    d4allshuf39 = Practice.objects.get(id=data4allshuffle[38])
    data39Answer = d4allshuf39.answer

    d4allshuf40 = Practice.objects.get(id=data4allshuffle[39])
    data40Answer = d4allshuf40.answer

    d4allshuf41 = Practice.objects.get(id=data4allshuffle[40])
    data41Answer = d4allshuf41.answer



    d4allshuf42 = Practice.objects.get(pk=data4allshuffle[41])
    if dQ.wronganswer4 is str and d4allshuf42.answer != dQ.answer:
        data42Answer = dataWrongAnswer4
    else:   
        data42Answer = d4allshuf42.answer

    d4allshuf43 = Practice.objects.get(pk=data4allshuffle[42])
    if dQ.wronganswer5 is str and d4allshuf43.answer != dQ.answer:
        data43Answer = dataWrongAnswer5
    else:
        data43Answer = d4allshuf43.answer 

    d4allshuf44 = Practice.objects.get(pk=data4allshuffle[43])
    if dQ.wronganswer6 is str and d4allshuf44.answer != dQ.answer:
        data44Answer = dataWrongAnswer6
    else:
        data44Answer = d4allshuf44.answer 

    d4allshuf45 = Practice.objects.get(pk=data4allshuffle[44])
    if dQ.wronganswer7 is str and d4allshuf45.answer != dQ.answer:
        data45Answer = dataWrongAnswer7
    else:
        data45Answer = d4allshuf45.answer 

    d4allshuf46 = Practice.objects.get(pk=data4allshuffle[45])
    if dQ.wronganswer8 is str and d4allshuf46.answer != dQ.answer:
        data46Answer = dataWrongAnswer8
    else:
        data46Answer = d4allshuf46.answer 

    d4allshuf47 = Practice.objects.get(pk=data4allshuffle[46])
    if dQ.wronganswer9 is str and d4allshuf47.answer != dQ.answer:
        data47Answer = dataWrongAnswer9
    else:     
        data47Answer = d4allshuf47.answer

    data28Answer = dataWrongAnswer1 
    data29Answer = dataWrongAnswer2
    data30Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer, data11Answer, data12Answer, data13Answer, data14Answer, data15Answer, data16Answer, data17Answer, data18Answer, data19Answer, data20Answer, data21Answer, data22Answer, data23Answer, data24Answer, data25Answer, data26Answer, data27Answer, data28Answer, data29Answer, data30Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,30)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]
    d7_11_Answer = dataAnsList7shuffle[10]
    d7_12_Answer = dataAnsList7shuffle[11]
    d7_13_Answer = dataAnsList7shuffle[12]
    d7_14_Answer = dataAnsList7shuffle[13]
    d7_15_Answer = dataAnsList7shuffle[14]
    d7_16_Answer = dataAnsList7shuffle[15]
    d7_17_Answer = dataAnsList7shuffle[16]
    d7_18_Answer = dataAnsList7shuffle[17]
    d7_19_Answer = dataAnsList7shuffle[18]
    d7_20_Answer = dataAnsList7shuffle[19]

    d7_21_Answer = dataAnsList7shuffle[20]
    d7_22_Answer = dataAnsList7shuffle[21]
    d7_23_Answer = dataAnsList7shuffle[22]
    d7_24_Answer = dataAnsList7shuffle[23]
    d7_25_Answer = dataAnsList7shuffle[24]
    d7_26_Answer = dataAnsList7shuffle[25]
    d7_27_Answer = dataAnsList7shuffle[26]
    d7_28_Answer = dataAnsList7shuffle[27]
    d7_29_Answer = dataAnsList7shuffle[28]
    d7_30_Answer = dataAnsList7shuffle[29]

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'd7_11_Answer':d7_11_Answer,
            'd7_12_Answer':d7_12_Answer,
            'd7_13_Answer':d7_13_Answer,
            'd7_14_Answer':d7_14_Answer,
            'd7_15_Answer':d7_15_Answer,
            'd7_16_Answer':d7_16_Answer,
            'd7_17_Answer':d7_17_Answer,
            'd7_18_Answer':d7_18_Answer,
            'd7_19_Answer':d7_19_Answer,
            'd7_20_Answer':d7_20_Answer,

            'd7_21_Answer':d7_21_Answer,
            'd7_22_Answer':d7_22_Answer,
            'd7_23_Answer':d7_23_Answer,
            'd7_24_Answer':d7_24_Answer,
            'd7_25_Answer':d7_25_Answer,
            'd7_26_Answer':d7_26_Answer,
            'd7_27_Answer':d7_27_Answer,
            'd7_28_Answer':d7_28_Answer,
            'd7_29_Answer':d7_29_Answer,
            'd7_30_Answer':d7_30_Answer,
            
            'data2pk3_1':data2pk3_1,
            'object_list':object_list
    }
    return render(request, 'sqlapp/questionRandom_list50.html', params)

def testQuestionView50(request):
    object_list = Practice.objects.all()
    
    test50count = request.POST["test50count"]
    test50seikai = request.POST["test50seikai"]
    testShokai = request.POST["testShokai"]

    if testShokai != 'testShokai':
        context = {
            'test50count' :request.POST["test50count"],
            'test50seikai' :request.POST["test50seikai"],
            'testShokai' :request.POST["testShokai"],
            'selectedAns' :request.POST["name1"],
            'dataAnswer' :request.POST["name0"],
            'dataQuestion' :request.POST["nameQuestion"],
            'dataExplanation' :request.POST["nameEx"],
            'dataThumbnailQ1' :request.POST["nameThuQ1"],
            'dataThumbnailQ2' :request.POST["nameThuQ2"],
            'dataThumbnailQ3' :request.POST["nameThuQ3"],
            'dataThumbnailA1' :request.POST["nameThuA1"],
            'dataThumbnailA2' :request.POST["nameThuA2"],
            'dataThumbnailA3' :request.POST["nameThuA3"],
            'object_list': object_list,
            'dataNumtaku' :request.POST['nameNumtaku'],
            'testId' :request.POST['testId'],
            'testId1' :request.POST['testId1'],
            'testId2' :request.POST['testId2'],
            'testId3' :request.POST['testId3'],
            'testId4':request.POST['testId4'],
            'testId5':request.POST['testId5'],
            'testId6':request.POST['testId6'],
            'testId7':request.POST['testId7'],
            'testId8':request.POST['testId8'],
            'testId9':request.POST['testId9'],
            'testId10':request.POST['testId10'],
            'testId11':request.POST['testId11'],
            'testId12':request.POST['testId12'],
            'testId13':request.POST['testId13'],
            'testId14':request.POST['testId14'],
            'testId15':request.POST['testId15'],
            'testId16':request.POST['testId16'],
            'testId17':request.POST['testId17'],
            'testId18':request.POST['testId18'],
            'testId19':request.POST['testId19'],
            'testId20':request.POST['testId20'],
            'testId21':request.POST['testId21'],
            'testId22':request.POST['testId22'],
            'testId23':request.POST['testId23'],
            'testId24':request.POST['testId24'],
            'testId25':request.POST['testId25'],
            'testId26':request.POST['testId26'],
            'testId27':request.POST['testId27'],
            'testId28':request.POST['testId28'],
            'testId29':request.POST['testId29'],
            'testId30':request.POST['testId30'],
            'testId31':request.POST['testId31'],
            'testId32':request.POST['testId32'],
            'testId33':request.POST['testId33'],
            'testId34':request.POST['testId34'],
            'testId35':request.POST['testId35'],
            'testId36':request.POST['testId36'],
            'testId37':request.POST['testId37'],
            'testId38':request.POST['testId38'],
            'testId39':request.POST['testId39'],
            'testId40':request.POST['testId40'],
            'testId41':request.POST['testId41'],
            'testId42':request.POST['testId42'],
            'testId43':request.POST['testId43'],
            'testId44':request.POST['testId44'],
            'testId45':request.POST['testId45'],
            'testId46':request.POST['testId46'],
            'testId47':request.POST['testId47'],
            'testId48':request.POST['testId48'],
            'testId49':request.POST['testId49'],
            'testId50':request.POST['testId50'],
        }
        selectedAns = request.POST["name1"]
        dataAnswer = request.POST["name0"]
        dataQuestion = request.POST["nameQuestion"]
        dataThumbnailQ1 = request.POST["nameThuQ1"]
        dataThumbnailQ2 = request.POST["nameThuQ2"]
        dataThumbnailQ3 = request.POST["nameThuQ3"]
        dataThumbnailA1 = request.POST["nameThuA1"]
        dataThumbnailA2 = request.POST["nameThuA2"]
        dataThumbnailA3 = request.POST["nameThuA3"]
        dataNumtaku = request.POST["nameNumtaku"]
        test50count = request.POST['test50count']
        test50seikai = request.POST['test50seikai']
        testId = request.POST['testId']
        testId1 = request.POST['testId1']
        testId2 = request.POST['testId2']
        testId3 = request.POST['testId3']
        testId4 = request.POST['testId4']
        testId5 = request.POST['testId5']
        testId6 = request.POST['testId6']
        testId7 = request.POST['testId7']
        testId8 = request.POST['testId8']
        testId9 = request.POST['testId9']
        testId10 = request.POST['testId10']
        testId11 = request.POST['testId11']
        testId12 = request.POST['testId12']
        testId13 = request.POST['testId13']
        testId14 = request.POST['testId14']
        testId15 = request.POST['testId15']
        testId16 = request.POST['testId16']
        testId17 = request.POST['testId17']
        testId18 = request.POST['testId18']
        testId19 = request.POST['testId19']
        testId20 = request.POST['testId20']
        testId21 = request.POST['testId21']
        testId22 = request.POST['testId22']
        testId23 = request.POST['testId23']
        testId24 = request.POST['testId24']
        testId25 = request.POST['testId25']
        testId26 = request.POST['testId26']
        testId27 = request.POST['testId27']
        testId28 = request.POST['testId28']
        testId29 = request.POST['testId29']
        testId30 = request.POST['testId30']
        testId31 = request.POST['testId31']
        testId32 = request.POST['testId32']
        testId33 = request.POST['testId33']
        testId34 = request.POST['testId34']
        testId35 = request.POST['testId35']
        testId36 = request.POST['testId36']
        testId37 = request.POST['testId37']
        testId38 = request.POST['testId38']
        testId39 = request.POST['testId39']
        testId40 = request.POST['testId40']
        testId41 = request.POST['testId41']
        testId42 = request.POST['testId42']
        testId43 = request.POST['testId43']
        testId44 = request.POST['testId44']
        testId45 = request.POST['testId45']
        testId46 = request.POST['testId46']
        testId47 = request.POST['testId47']
        testId48 = request.POST['testId48']
        testId49 = request.POST['testId49']
        testId50 = request.POST['testId50']
    else:
        context = {
            'test50count':request.POST["test50count"],
            'test50seikai':request.POST["test50seikai"],
        }
        selectedAns = "shokaihanai"

    test50count = int(test50count)
    test50count += 1

    test50seikai = int(test50seikai)
    
    if testShokai != 'testShokai' and selectedAns == dataAnswer:
        test50seikai += 1
    
    
    if (request.method == 'POST'):
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)

    else:
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)
   
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)

    dQ = Practice.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3

    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9

    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3
    dataCategory = dQ.category
    
    d4allshuf1 = Practice.objects.get(id=data4allshuffle[0])
    data1Answer = d4allshuf1.answer

    d4allshuf2 = Practice.objects.get(id=data4allshuffle[1])
    data2Answer = d4allshuf2.answer

    d4allshuf3 = Practice.objects.get(id=data4allshuffle[2])
    data3Answer = d4allshuf3.answer

    d4allshuf4 = Practice.objects.get(id=data4allshuffle[3])
    data4Answer = d4allshuf4.answer

    d4allshuf5 = Practice.objects.get(id=data4allshuffle[4])
    data5Answer = d4allshuf5.answer 

    d4allshuf6 = Practice.objects.get(id=data4allshuffle[5])
    data6Answer = d4allshuf6.answer 

    d4allshuf7 = Practice.objects.get(id=data4allshuffle[6])
    data7Answer = d4allshuf7.answer 

    d4allshuf8 = Practice.objects.get(id=data4allshuffle[7])
    data8Answer = d4allshuf8.answer 

    d4allshuf9 = Practice.objects.get(id=data4allshuffle[8])
    data9Answer = d4allshuf9.answer 

    d4allshuf10 = Practice.objects.get(id=data4allshuffle[9])
    data10Answer = d4allshuf10.answer 

    d4allshuf11 = Practice.objects.get(id=data4allshuffle[10])
    data11Answer = d4allshuf11.answer 

    d4allshuf12 = Practice.objects.get(id=data4allshuffle[11])
    data12Answer = d4allshuf12.answer 

    d4allshuf13 = Practice.objects.get(id=data4allshuffle[12])
    data13Answer = d4allshuf13.answer 

    d4allshuf14 = Practice.objects.get(id=data4allshuffle[13])
    data14Answer = d4allshuf14.answer 

    d4allshuf15 = Practice.objects.get(id=data4allshuffle[14])
    data15Answer = d4allshuf15.answer 

    d4allshuf16 = Practice.objects.get(id=data4allshuffle[15])
    data16Answer = d4allshuf16.answer 

    d4allshuf17 = Practice.objects.get(id=data4allshuffle[16])
    data17Answer = d4allshuf17.answer

    d4allshuf18 = Practice.objects.get(id=data4allshuffle[17])
    data18Answer = d4allshuf18.answer 

    d4allshuf19 = Practice.objects.get(id=data4allshuffle[18])
    data19Answer = d4allshuf19.answer 

    d4allshuf20 = Practice.objects.get(id=data4allshuffle[19])
    data20Answer = d4allshuf20.answer 

    d4allshuf21 = Practice.objects.get(id=data4allshuffle[20])
    data21Answer = d4allshuf21.answer

    d4allshuf22 = Practice.objects.get(pk=data4allshuffle[21])
    if dQ.wronganswer4 is str and d4allshuf22.answer != dQ.answer:
        data22Answer = dataWrongAnswer4
    else:   
        data22Answer = d4allshuf22.answer

    d4allshuf23 = Practice.objects.get(pk=data4allshuffle[22])
    if dQ.wronganswer5 is str and d4allshuf23.answer != dQ.answer:
        data23Answer = dataWrongAnswer5
    else:
        data23Answer = d4allshuf23.answer 

    d4allshuf24 = Practice.objects.get(pk=data4allshuffle[23])
    if dQ.wronganswer6 is str and d4allshuf24.answer != dQ.answer:
        data24Answer = dataWrongAnswer6
    else:
        data24Answer = d4allshuf24.answer 

    d4allshuf25 = Practice.objects.get(pk=data4allshuffle[24])
    if dQ.wronganswer7 is str and d4allshuf25.answer != dQ.answer:
        data25Answer = dataWrongAnswer7
    else:
        data25Answer = d4allshuf25.answer 

    d4allshuf26 = Practice.objects.get(pk=data4allshuffle[25])
    if dQ.wronganswer8 is str and d4allshuf26.answer != dQ.answer:
        data26Answer = dataWrongAnswer8
    else:
        data26Answer = d4allshuf26.answer 

    d4allshuf27 = Practice.objects.get(pk=data4allshuffle[26])
    if dQ.wronganswer9 is str and d4allshuf27.answer != dQ.answer:
        data27Answer = dataWrongAnswer9
    else:     
        data27Answer = d4allshuf27.answer


    data28Answer = dataWrongAnswer1 
    data29Answer = dataWrongAnswer2
    data30Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer, data6Answer, data7Answer, data8Answer, data9Answer, data10Answer, data11Answer, data12Answer, data13Answer, data14Answer, data15Answer, data16Answer, data17Answer, data18Answer, data19Answer, data20Answer, data21Answer, data22Answer, data23Answer, data24Answer, data25Answer, data26Answer, data27Answer, data28Answer, data29Answer, data30Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,30)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    d7_5_Answer = dataAnsList7shuffle[4]
    d7_6_Answer = dataAnsList7shuffle[5]
    d7_7_Answer = dataAnsList7shuffle[6]
    d7_8_Answer = dataAnsList7shuffle[7]
    d7_9_Answer = dataAnsList7shuffle[8]
    d7_10_Answer = dataAnsList7shuffle[9]
    d7_11_Answer = dataAnsList7shuffle[10]
    d7_12_Answer = dataAnsList7shuffle[11]
    d7_13_Answer = dataAnsList7shuffle[12]
    d7_14_Answer = dataAnsList7shuffle[13]
    d7_15_Answer = dataAnsList7shuffle[14]
    d7_16_Answer = dataAnsList7shuffle[15]
    d7_17_Answer = dataAnsList7shuffle[16]
    d7_18_Answer = dataAnsList7shuffle[17]
    d7_19_Answer = dataAnsList7shuffle[18]
    d7_20_Answer = dataAnsList7shuffle[19]
    d7_21_Answer = dataAnsList7shuffle[20]
    d7_22_Answer = dataAnsList7shuffle[21]
    d7_23_Answer = dataAnsList7shuffle[22]
    d7_24_Answer = dataAnsList7shuffle[23]
    d7_25_Answer = dataAnsList7shuffle[24]
    d7_26_Answer = dataAnsList7shuffle[25]
    d7_27_Answer = dataAnsList7shuffle[26]
    d7_28_Answer = dataAnsList7shuffle[27]
    d7_29_Answer = dataAnsList7shuffle[28]
    d7_30_Answer = dataAnsList7shuffle[29]

    test50mondaisuu = 3
        
    seikairitsuFloat = (float(test50seikai) / float(test50mondaisuu)) * 100
    seikairitsu = int(seikairitsuFloat)

    #4/19 django-pandas----------------------------------
    df = read_frame(object_list, fieldnames=['answer'])
    #----------------------------------------------------

    dQID = data[0]
    if test50count == 0:
        testId1 = 777
    if test50count <= 1:
        testId2 = 777
    if test50count <= 2:
        testId3 = 777
    if test50count <= 3:
        testId4 = 7777
    if test50count <= 4:
        testId5 = 7777
    if test50count <= 5:
        testId6 = 7777
    if test50count <= 6:
        testId7 = 7777
    if test50count <= 7:
        testId8 = 7777
    if test50count <= 8:
        testId9 = 7777
    if test50count <= 9:
        testId10 = 7777
    if test50count <= 10:
        testId11 = 7777
    if test50count <= 11:
        testId12 = 7777
    if test50count <= 12:
        testId13 = 7777
    if test50count <= 13:
        testId14 = 7777
    if test50count <= 14:
        testId15 = 7777
    if test50count <= 15:
        testId16 = 7777
    if test50count <= 16:
        testId17 = 7777
    if test50count <= 17:
        testId18 = 7777
    if test50count <= 18:
        testId19 = 7777
    if test50count <= 19:
        testId20 = 7777 
    if test50count <= 20:
        testId21 = 7777
    if test50count <= 21:
        testId22 = 7777
    if test50count <= 22:
        testId23 = 7777
    if test50count <= 23:
        testId24 = 7777
    if test50count <= 24:
        testId25 = 7777
    if test50count <= 25:
        testId26 = 7777
    if test50count <= 26:
        testId27 = 7777
    if test50count <= 27:
        testId28 = 7777
    if test50count <= 28:
        testId29 = 7777
    if test50count <= 29:
        testId30 = 7777
    if test50count <= 30:
        testId31 = 7777
    if test50count <= 31:
        testId32 = 7777
    if test50count <= 32:
        testId33 = 7777
    if test50count <= 33:
        testId34 = 7777
    if test50count <= 34:
        testId35 = 7777
    if test50count <= 35:
        testId36 = 7777
    if test50count <= 36:
        testId37 = 7777
    if test50count <= 37:
        testId38 = 7777
    if test50count <= 38:
        testId39 = 7777
    if test50count <= 39:
        testId40 = 7777 
    if test50count <= 40:
        testId41 = 7777
    if test50count <= 41:
        testId42 = 7777
    if test50count <= 42:
        testId43 = 7777
    if test50count <= 43:
        testId44 = 7777
    if test50count <= 44:
        testId45 = 7777
    if test50count <= 45:
        testId46 = 7777
    if test50count <= 46:
        testId47 = 7777
    if test50count <= 47:
        testId48 = 7777
    if test50count <= 48:
        testId49 = 7777
    if test50count <= 49:
        testId50 = 7777 
    if test50count <= 50:
        testId50 = 7777 
    if test50count == 1:
        testId1 = dQID
    if test50count == 2:
        testId2 = dQID
    if test50count == 3:
        testId3 = dQID
    if test50count == 4:
        testId4 = dQID
    if test50count == 5:
        testId5 = dQID
    if test50count == 6:
        testId6 = dQID
    if test50count == 7:
        testId7 = dQID
    if test50count == 8:
        testId8 = dQID
    if test50count == 9:
        testId9 = dQID
    if test50count == 10:
        testId10 = dQID
    if test50count == 11:
        testId11 = dQID
    if test50count == 12:
        testId12 = dQID
    if test50count == 13:
        testId13 = dQID
    if test50count == 14:
        testId14 = dQID
    if test50count == 15:
        testId15 = dQID
    if test50count == 16:
        testId16 = dQID
    if test50count == 17:
        testId17 = dQID
    if test50count == 18:
        testId18 = dQID
    if test50count == 19:
        testId19 = dQID
    if test50count == 20:
        testId20 = dQID
    if test50count == 21:
        testId21 = dQID
    if test50count == 22:
        testId22 = dQID
    if test50count == 23:
        testId23 = dQID
    if test50count == 24:
        testId24 = dQID
    if test50count == 25:
        testId25 = dQID
    if test50count == 26:
        testId26 = dQID
    if test50count == 27:
        testId27 = dQID
    if test50count == 28:
        testId28 = dQID
    if test50count == 29:
        testId29 = dQID
    if test50count == 30:
        testId30 = dQID 
    if test50count == 31:
        testId31 = dQID
    if test50count >= 32:
        testId32 = dQID
    if test50count == 33:
        testId33 = dQID
    if test50count == 34:
        testId34 = dQID
    if test50count == 35:
        testId35 = dQID
    if test50count == 36:
        testId36 = dQID
    if test50count == 37:
        testId37 = dQID
    if test50count == 38:
        testId38 = dQID
    if test50count == 39:
        testId39 = dQID
    if test50count == 40:
        testId40 = dQID
    if test50count == 41:
        testId41 = dQID
    if test50count == 42:
        testId42 = dQID
    if test50count == 43:
        testId43 = dQID
    if test50count == 44:
        testId44 = dQID
    if test50count == 45:
        testId45 = dQID
    if test50count == 46:
        testId46 = dQID
    if test50count == 47:
        testId47 = dQID
    if test50count == 48:
        testId48 = dQID
    if test50count == 49:
        testId49 = dQID
    if test50count == 50:
        testId50 = dQID   

    testId = dQID
    
    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            'd7_6_Answer':d7_6_Answer,
            'd7_7_Answer':d7_7_Answer,
            'd7_8_Answer':d7_8_Answer,
            'd7_9_Answer':d7_9_Answer,
            'd7_10_Answer':d7_10_Answer,
            'd7_11_Answer':d7_11_Answer,
            'd7_12_Answer':d7_12_Answer,
            'd7_13_Answer':d7_13_Answer,
            'd7_14_Answer':d7_14_Answer,
            'd7_15_Answer':d7_15_Answer,
            'd7_16_Answer':d7_16_Answer,
            'd7_17_Answer':d7_17_Answer,
            'd7_18_Answer':d7_18_Answer,
            'd7_19_Answer':d7_19_Answer,
            'd7_20_Answer':d7_20_Answer,
            'd7_21_Answer':d7_21_Answer,
            'd7_22_Answer':d7_22_Answer,
            'd7_23_Answer':d7_23_Answer,
            'd7_24_Answer':d7_24_Answer,
            'd7_25_Answer':d7_25_Answer,
            'd7_26_Answer':d7_26_Answer,
            'd7_27_Answer':d7_27_Answer,
            'd7_28_Answer':d7_28_Answer,
            'd7_29_Answer':d7_29_Answer,
            'd7_30_Answer':d7_30_Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
            'test50count':test50count,
            'test50seikai':test50seikai,
            'testShokai' :"testNandomeka",
            'seikairitsu':seikairitsu,
            'test50mondaisuu':test50mondaisuu,
            'selectedAns':selectedAns,
            'df':df,
            'testId1':testId1,
            'testId2':testId2,
            'testId3':testId3,
            'testId4':testId4,
            'testId5':testId5,
            'testId6':testId6,
            'testId7':testId7,
            'testId8':testId8,
            'testId9':testId9,
            'testId10':testId10,
            'testId11':testId11,
            'testId12':testId12,
            'testId13':testId13,
            'testId14':testId14,
            'testId15':testId15,
            'testId16':testId16,
            'testId17':testId17,
            'testId18':testId18,
            'testId19':testId19,
            'testId20':testId20,
            'testId21':testId21,
            'testId22':testId22,
            'testId23':testId23,
            'testId24':testId24,
            'testId25':testId25,
            'testId26':testId26,
            'testId27':testId27,
            'testId28':testId28,
            'testId29':testId29,
            'testId30':testId30,
            'testId31':testId31,
            'testId32':testId32,
            'testId33':testId33,
            'testId34':testId34,
            'testId35':testId35,
            'testId36':testId36,
            'testId37':testId37,
            'testId38':testId38,
            'testId39':testId39,
            'testId40':testId40,
            'testId41':testId41,
            'testId42':testId42,
            'testId43':testId43,
            'testId44':testId44,
            'testId45':testId45,
            'testId46':testId46,
            'testId47':testId47,
            'testId48':testId48,
            'testId49':testId49,
            'testId50':testId50,
            'testId':testId,
    }

    if test50count == test50mondaisuu + 1 :
        return render(request, 'sqlapp/question_test_result50.html', params)
    else:
        return render(request, 'sqlapp/question_test50.html', params)


def testQuestionView10(request):
    object_list = Practice.objects.all()
    
    test10count = request.POST["test10count"]
    test10seikai = request.POST["test10seikai"]
    testShokai = request.POST["testShokai"]

    if testShokai != 'testShokai':
        context = {
            'test10count' :request.POST["test10count"],
            'test10seikai' :request.POST["test10seikai"],
            'testShokai' :request.POST["testShokai"],

            #テキストボックスに入力した値
            'selectedAns' :request.POST["name1"],


            'dataAnswer' :request.POST["name0"],
            'dataQuestion' :request.POST["nameQuestion"],
            'dataExplanation' :request.POST["nameEx"],
            
            'object_list': object_list,
            'dataNumtaku' :request.POST['nameNumtaku'],
            'testId' :request.POST['testId'],
            'testId1' :request.POST['testId1'],
            'testId2' :request.POST['testId2'],
            'testId3' :request.POST['testId3'],
            'testId4':request.POST['testId4'],
            'testId5':request.POST['testId5'],
            'testId6':request.POST['testId6'],
            'testId7':request.POST['testId7'],
            'testId8':request.POST['testId8'],
            'testId9':request.POST['testId9'],
            'testId10':request.POST['testId10'],

            'testQuestion1' :request.POST['testQuestion1'],
            'testQuestion2' :request.POST['testQuestion2'],
            'testQuestion3' :request.POST['testQuestion3'],
            'testQuestion4':request.POST['testQuestion4'],
            'testQuestion5':request.POST['testQuestion5'],
            'testQuestion6':request.POST['testQuestion6'],
            'testQuestion7':request.POST['testQuestion7'],
            'testQuestion8':request.POST['testQuestion8'],
            'testQuestion9':request.POST['testQuestion9'],
            'testQuestion10':request.POST['testQuestion10'],

            'testAnswer1' :request.POST['testAnswer1'],
            'testAnswer2' :request.POST['testAnswer2'],
            'testAnswer3' :request.POST['testAnswer3'],
            'testAnswer4':request.POST['testAnswer4'],
            'testAnswer5':request.POST['testAnswer5'],
            'testAnswer6':request.POST['testAnswer6'],
            'testAnswer7':request.POST['testAnswer7'],
            'testAnswer8':request.POST['testAnswer8'],
            'testAnswer9':request.POST['testAnswer9'],
            'testAnswer10':request.POST['testAnswer10'],

            'testSelectAns1' :request.POST['testSelectAns1'],
            'testSelectAns2' :request.POST['testSelectAns2'],
            'testSelectAns3' :request.POST['testSelectAns3'],
            'testSelectAns4':request.POST['testSelectAns4'],
            'testSelectAns5':request.POST['testSelectAns5'],
            'testSelectAns6':request.POST['testSelectAns6'],
            'testSelectAns7':request.POST['testSelectAns7'],
            'testSelectAns8':request.POST['testSelectAns8'],
            'testSelectAns9':request.POST['testSelectAns9'],
            'testSelectAns10':request.POST['testSelectAns10'],
            
        }
        selectedAns = request.POST["name1"]
        dataAnswer = request.POST["name0"]
        dataQuestion = request.POST["nameQuestion"]
        dataThumbnailQ1 = request.POST["nameThuQ1"]
        dataThumbnailQ2 = request.POST["nameThuQ2"]
        dataThumbnailQ3 = request.POST["nameThuQ3"]
        dataThumbnailA1 = request.POST["nameThuA1"]
        dataThumbnailA2 = request.POST["nameThuA2"]
        dataThumbnailA3 = request.POST["nameThuA3"]
        dataNumtaku = request.POST["nameNumtaku"]
        test10count = request.POST['test10count']
        test10seikai = request.POST['test10seikai']
        testId = request.POST['testId']
        testId1 = request.POST['testId1']
        testId2 = request.POST['testId2']
        testId3 = request.POST['testId3']
        testId4 = request.POST['testId4']
        testId5 = request.POST['testId5']
        testId6 = request.POST['testId6']
        testId7 = request.POST['testId7']
        testId8 = request.POST['testId8']
        testId9 = request.POST['testId9']
        testId10 = request.POST['testId10']

        testQuestion1 = request.POST['testQuestion1']
        testQuestion2 = request.POST['testQuestion2']
        testQuestion3 = request.POST['testQuestion3']
        testQuestion4 = request.POST['testQuestion4']
        testQuestion5 = request.POST['testQuestion5']
        testQuestion6 = request.POST['testQuestion6']
        testQuestion7 = request.POST['testQuestion7']
        testQuestion8 = request.POST['testQuestion8']
        testQuestion9 = request.POST['testQuestion9']
        testQuestion10 = request.POST['testQuestion10']

        testAnswer1 = request.POST['testAnswer1']
        testAnswer2 = request.POST['testAnswer2']
        testAnswer3 = request.POST['testAnswer3']
        testAnswer4 = request.POST['testAnswer4']
        testAnswer5 = request.POST['testAnswer5']
        testAnswer6 = request.POST['testAnswer6']
        testAnswer7 = request.POST['testAnswer7']
        testAnswer8 = request.POST['testAnswer8']
        testAnswer9 = request.POST['testAnswer9']
        testAnswer10 = request.POST['testAnswer10']

        testSelectAns1 = request.POST['testSelectAns1']
        testSelectAns2 = request.POST['testSelectAns2']
        testSelectAns3 = request.POST['testSelectAns3']
        testSelectAns4 = request.POST['testSelectAns4']
        testSelectAns5 = request.POST['testSelectAns5']
        testSelectAns6 = request.POST['testSelectAns6']
        testSelectAns7 = request.POST['testSelectAns7']
        testSelectAns8 = request.POST['testSelectAns8']
        testSelectAns9 = request.POST['testSelectAns9']
        testSelectAns10 = request.POST['testSelectAns10']
    else:
        context = {
            'test10count':request.POST["test10count"],
            'test10seikai':request.POST["test10seikai"],
            
        }
        selectedAns = "shokaihanai"
        testId = 7777777
        testId1 = 7777777
        testId2 = 7777777
        testId3 = 7777777
        testId4 = 7777777
        testId5 = 7777777
        testId6 = 7777777
        testId7 = 7777777
        testId8 = 7777777
        testId9 = 7777777
        testId10 = 7777777

    test10count = int(test10count)
    test10count += 1

    test10seikai = int(test10seikai)
    
    if testShokai != 'testShokai' and selectedAns == dataAnswer:
        test10seikai += 1
    
    
    if (request.method == 'POST'):
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)

        testId = int(testId)
        testId1 = int(testId1)
        testId2 = int(testId2)
        testId3 = int(testId3)
        testId4 = int(testId4)
        testId5 = int(testId5)
        testId6 = int(testId6)
        testId7 = int(testId7)
        testId8 = int(testId8)
        testId9 = int(testId9)
        testId10 = int(testId10)

        if testShokai != 'testShokai':
            pks_list.remove(testId1)
        
        try:
            pks_list.remove(testId2)
        except:
            pass

        try:
            pks_list.remove(testId3)
        except:
            pass

        try:
            pks_list.remove(testId4)
        except:
            pass

        try:
            pks_list.remove(testId5)
        except:
            pass

        try:
            pks_list.remove(testId6)
        except:
            pass

        try:
            pks_list.remove(testId7)
        except:
            pass

        try:
            pks_list.remove(testId8)
        except:
            pass

        try:
            pks_list.remove(testId9)
        except:
            pass

        try:
            pks_list.remove(testId10)
        except:
            pass
        data = random.sample(pks_list,1)

        pks_list.remove(data[0])

    else:
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)
   
        pks_list.remove(data[0])

    dQ = Practice.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer


    dataExplanation = dQ.explanation
    test10mondaisuu = 10
        
    seikairitsuFloat = (float(test10seikai) / float(test10mondaisuu)) * 100
    seikairitsu = int(seikairitsuFloat)

    df = read_frame(object_list)
    df1 = df.head()

    dQID = data[0]
    dQQuestion = dQ.question
    dQAnswer = dQ.answer
    dQSelectAns = selectedAns


    if test10count == 0:
        testId1 = 777
        testQuestion1 = 7777
        testAnswer1 = 7777
        testSelectAns1 = 7777
    if test10count <= 1:
        testId2 = 777
        testQuestion2 = 7777
        testAnswer2 = 7777
        testSelectAns2 = 7777
    if test10count <= 2:
        testId3 = 777
        testQuestion3 = 7777
        testAnswer3 = 7777
        testSelectAns3 = 7777
    if test10count <= 3:
        testId4 = 7777
        testQuestion4 = 7777
        testAnswer4 = 7777
        testSelectAns4 = 7777
    if test10count <= 4:
        testId5 = 7777
        testQuestion5 = 7777
        testAnswer5 = 7777
        testSelectAns5 = 7777
    if test10count <= 5:
        testId6 = 7777
        testQuestion6 = 7777
        testAnswer6 = 7777
        testSelectAns6 = 7777
    if test10count <= 6:
        testId7 = 7777
        testQuestion7 = 7777
        testAnswer7 = 7777
        testSelectAns7 = 7777
    if test10count <= 7:
        testId8 = 7777
        testQuestion8 = 7777
        testAnswer8 = 7777
        testSelectAns8 = 7777
    if test10count <= 8:
        testId9 = 7777
        testQuestion9 = 7777
        testAnswer9 = 7777
        testSelectAns9 = 7777
    if test10count <= 9:
        testId10 = 7777
        testQuestion10 = 7777
        testAnswer10 = 7777
        testSelectAns10 = 7777
    if test10count == 1:
        testId1 = dQID
        testQuestion1 = dQQuestion
        testAnswer1 = dQAnswer
        testSelectAns1 = dQSelectAns
    if test10count == 2:
        testId2 = dQID
        testQuestion2 = dQQuestion
        testAnswer2 = dQAnswer
        testSelectAns2 = dQSelectAns
    if test10count == 3:
        testId3 = dQID
        testQuestion3 = dQQuestion
        testAnswer3 = dQAnswer
        testSelectAns3 = dQSelectAns
    if test10count == 4:
        testId4 = dQID
        testQuestion4 = dQQuestion
        testAnswer4 = dQAnswer
        testSelectAns4 = dQSelectAns
    if test10count == 5:
        testId5 = dQID
        testQuestion5 = dQQuestion
        testAnswer5 = dQAnswer
        testSelectAns5 = dQSelectAns
    if test10count == 6:
        testId6 = dQID
        testQuestion6 = dQQuestion
        testAnswer6 = dQAnswer
        testSelectAns6 = dQSelectAns
    if test10count == 7:
        testId7 = dQID
        testQuestion7 = dQQuestion
        testAnswer7 = dQAnswer
        testSelectAns7 = dQSelectAns
    if test10count == 8:
        testId8 = dQID
        testQuestion8 = dQQuestion
        testAnswer8 = dQAnswer
        testSelectAns8 = dQSelectAns
    if test10count == 9:
        testId9 = dQID
        testQuestion9 = dQQuestion
        testAnswer9 = dQAnswer
        testSelectAns9 = dQSelectAns
    if test10count == 10:
        testId10 = dQID
        testQuestion10 = dQQuestion
        testAnswer10 = dQAnswer
        testSelectAns10 = dQSelectAns

    testId = dQID

    #カテゴリータブの関数を呼び出す
    categories_data = get_categories_data()

    categories = Category.objects.all()

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataExplanation': dataExplanation,
            
            'object_list':object_list,
            'test10count':test10count,
            'test10seikai':test10seikai,
            'testShokai' :"testNandomeka",
            'seikairitsu':seikairitsu,
            'test10mondaisuu':test10mondaisuu,
            'selectedAns':selectedAns,
            'df':df1,
            'dfHtml': df1.to_html(),
            'testId1':testId1,
            'testId2':testId2,
            'testId3':testId3,
            'testId4':testId4,
            'testId5':testId5,
            'testId6':testId6,
            'testId7':testId7,
            'testId8':testId8,
            'testId9':testId9,
            'testId10':testId10,
            'testId':testId,

            'testQuestion1':testQuestion1,
            'testQuestion2':testQuestion2,
            'testQuestion3':testQuestion3,
            'testQuestion4':testQuestion4,
            'testQuestion5':testQuestion5,
            'testQuestion6':testQuestion6,
            'testQuestion7':testQuestion7,
            'testQuestion8':testQuestion8,
            'testQuestion9':testQuestion9,
            'testQuestion10':testQuestion10,

            'testAnswer1':testAnswer1,
            'testAnswer2':testAnswer2,
            'testAnswer3':testAnswer3,
            'testAnswer4':testAnswer4,
            'testAnswer5':testAnswer5,
            'testAnswer6':testAnswer6,
            'testAnswer7':testAnswer7,
            'testAnswer8':testAnswer8,
            'testAnswer9':testAnswer9,
            'testAnswer10':testAnswer10,

            'testSelectAns1':testSelectAns1,
            'testSelectAns2':testSelectAns2,
            'testSelectAns3':testSelectAns3,
            'testSelectAns4':testSelectAns4,
            'testSelectAns5':testSelectAns5,
            'testSelectAns6':testSelectAns6,
            'testSelectAns7':testSelectAns7,
            'testSelectAns8':testSelectAns8,
            'testSelectAns9':testSelectAns9,
            'testSelectAns10':testSelectAns10,
            'categories_data': categories_data,
            'categories': categories
    }

    if test10count == test10mondaisuu + 1 :
        return render(request, 'sqlapp/question_test_result10.html', params)
    else:
        return render(request, 'sqlapp/question_test10.html', params)


def testQuestionView4taku_10(request):

    object_list = Practice.objects.all()
    
    test10count = request.POST["test10count"]
    test10seikai = request.POST["test10seikai"]
    testShokai = request.POST["testShokai"]
    

    if testShokai != 'testShokai':
        context = {
            'test10count' :request.POST["test10count"],
            'test10seikai' :request.POST["test10seikai"],
            'testShokai' :request.POST["testShokai"],
            'selectedAns' :request.POST["name1"],
            'dataAnswer' :request.POST["name0"],
            'dataQuestion' :request.POST["nameQuestion"],
            'dataExplanation' :request.POST["nameEx"],
            'dataThumbnailQ1' :request.POST["nameThuQ1"],
            'dataThumbnailQ2' :request.POST["nameThuQ2"],
            'dataThumbnailQ3' :request.POST["nameThuQ3"],
            'dataThumbnailA1' :request.POST["nameThuA1"],
            'dataThumbnailA2' :request.POST["nameThuA2"],
            'dataThumbnailA3' :request.POST["nameThuA3"],
            'object_list': object_list,
            'dataNumtaku' :request.POST['nameNumtaku'],
            'testId' :request.POST['testId'],
            'testId1' :request.POST['testId1'],
            'testId2' :request.POST['testId2'],
            'testId3' :request.POST['testId3'],
            'testId4':request.POST['testId4'],
            'testId5':request.POST['testId5'],
            'testId6':request.POST['testId6'],
            'testId7':request.POST['testId7'],
            'testId8':request.POST['testId8'],
            'testId9':request.POST['testId9'],
            'testId10':request.POST['testId10'],

            'testQuestion1' :request.POST['testQuestion1'],
            'testQuestion2' :request.POST['testQuestion2'],
            'testQuestion3' :request.POST['testQuestion3'],
            'testQuestion4':request.POST['testQuestion4'],
            'testQuestion5':request.POST['testQuestion5'],
            'testQuestion6':request.POST['testQuestion6'],
            'testQuestion7':request.POST['testQuestion7'],
            'testQuestion8':request.POST['testQuestion8'],
            'testQuestion9':request.POST['testQuestion9'],
            'testQuestion10':request.POST['testQuestion10'],

            'testAnswer1' :request.POST['testAnswer1'],
            'testAnswer2' :request.POST['testAnswer2'],
            'testAnswer3' :request.POST['testAnswer3'],
            'testAnswer4':request.POST['testAnswer4'],
            'testAnswer5':request.POST['testAnswer5'],
            'testAnswer6':request.POST['testAnswer6'],
            'testAnswer7':request.POST['testAnswer7'],
            'testAnswer8':request.POST['testAnswer8'],
            'testAnswer9':request.POST['testAnswer9'],
            'testAnswer10':request.POST['testAnswer10'],

            'testSelectAns1' :request.POST['testSelectAns1'],
            'testSelectAns2' :request.POST['testSelectAns2'],
            'testSelectAns3' :request.POST['testSelectAns3'],
            'testSelectAns4':request.POST['testSelectAns4'],
            'testSelectAns5':request.POST['testSelectAns5'],
            'testSelectAns6':request.POST['testSelectAns6'],
            'testSelectAns7':request.POST['testSelectAns7'],
            'testSelectAns8':request.POST['testSelectAns8'],
            'testSelectAns9':request.POST['testSelectAns9'],
            'testSelectAns10':request.POST['testSelectAns10'],
            'test10Category': request.POST["test10Category"]
            
        }
        selectedAns = request.POST["name1"]
        dataAnswer = request.POST["name0"]
        dataQuestion = request.POST["nameQuestion"]
        dataThumbnailQ1 = request.POST["nameThuQ1"]
        dataThumbnailQ2 = request.POST["nameThuQ2"]
        dataThumbnailQ3 = request.POST["nameThuQ3"]
        dataThumbnailA1 = request.POST["nameThuA1"]
        dataThumbnailA2 = request.POST["nameThuA2"]
        dataThumbnailA3 = request.POST["nameThuA3"]
        dataNumtaku = request.POST["nameNumtaku"]
        test10count = request.POST['test10count']
        test10seikai = request.POST['test10seikai']
        testId = request.POST['testId']
        testId1 = request.POST['testId1']
        testId2 = request.POST['testId2']
        testId3 = request.POST['testId3']
        testId4 = request.POST['testId4']
        testId5 = request.POST['testId5']
        testId6 = request.POST['testId6']
        testId7 = request.POST['testId7']
        testId8 = request.POST['testId8']
        testId9 = request.POST['testId9']
        testId10 = request.POST['testId10']

        testQuestion1 = request.POST['testQuestion1']
        testQuestion2 = request.POST['testQuestion2']
        testQuestion3 = request.POST['testQuestion3']
        testQuestion4 = request.POST['testQuestion4']
        testQuestion5 = request.POST['testQuestion5']
        testQuestion6 = request.POST['testQuestion6']
        testQuestion7 = request.POST['testQuestion7']
        testQuestion8 = request.POST['testQuestion8']
        testQuestion9 = request.POST['testQuestion9']
        testQuestion10 = request.POST['testQuestion10']

        testAnswer1 = request.POST['testAnswer1']
        testAnswer2 = request.POST['testAnswer2']
        testAnswer3 = request.POST['testAnswer3']
        testAnswer4 = request.POST['testAnswer4']
        testAnswer5 = request.POST['testAnswer5']
        testAnswer6 = request.POST['testAnswer6']
        testAnswer7 = request.POST['testAnswer7']
        testAnswer8 = request.POST['testAnswer8']
        testAnswer9 = request.POST['testAnswer9']
        testAnswer10 = request.POST['testAnswer10']

        testSelectAns1 = request.POST['testSelectAns1']
        testSelectAns2 = request.POST['testSelectAns2']
        testSelectAns3 = request.POST['testSelectAns3']
        testSelectAns4 = request.POST['testSelectAns4']
        testSelectAns5 = request.POST['testSelectAns5']
        testSelectAns6 = request.POST['testSelectAns6']
        testSelectAns7 = request.POST['testSelectAns7']
        testSelectAns8 = request.POST['testSelectAns8']
        testSelectAns9 = request.POST['testSelectAns9']
        testSelectAns10 = request.POST['testSelectAns10']

        test10Category = request.POST["test10Category"]
    else:
        context = {
            'test10count':request.POST["test10count"],
            'test10seikai':request.POST["test10seikai"],
            'test10Category': request.POST["categorybetsu2"]     
        }
        selectedAns = "shokaihanai"
        testId = 7777777
        testId1 = 7777777
        testId2 = 7777777
        testId3 = 7777777
        testId4 = 7777777
        testId5 = 7777777
        testId6 = 7777777
        testId7 = 7777777
        testId8 = 7777777
        testId9 = 7777777
        testId10 = 7777777
        test10Category = request.POST["categorybetsu2"]

    test10count = int(test10count)
    test10count += 1

    test10seikai = int(test10seikai)
    
    if testShokai != 'testShokai' and selectedAns == dataAnswer:
        test10seikai += 1
    
    
    if (request.method == 'POST'):
        selCatKakutei = request.POST.get('selCatKakutei')
        if selCatKakutei == "基本情報技術者試験":
            selCatKakutei = "FE"
        if selCatKakutei == "応用情報技術者試験":
            selCatKakutei = "AP"


        if testShokai == 'testShokai':
            selectCategory = ""
        else:
            selectCategory = request.POST.get('selCatKakutei')
            if selectCategory == "基本情報技術者試験":
                selectCategory = "FE"
            if selectCategory == "応用情報技術者試験":
                selectCategory = "AP"
            
        if request.POST.get('categorybetsu2'):
            selectCategory = request.POST.get('categorybetsu2')
            if selectCategory == "基本情報技術者試験":
                selectCategory = "FE"
            if selectCategory == "応用情報技術者試験":
                selectCategory = "AP"

        if selectCategory == "" or selectCategory == "カテゴリを選択":
            pks = Practice.objects.values_list('pk', flat=True)
            testes = "あ"
        else:
            pks = Practice.objects.filter(category__contains=selectCategory).values_list('pk', flat=True)
            testes = "い"
            if testShokai == 'testShokai':
                selCatKakutei = selectCategory

        pks_list = list(pks)

        testId = int(testId)
        testId1 = int(testId1)
        testId2 = int(testId2)
        testId3 = int(testId3)
        testId4 = int(testId4)
        testId5 = int(testId5)
        testId6 = int(testId6)
        testId7 = int(testId7)
        testId8 = int(testId8)
        testId9 = int(testId9)
        testId10 = int(testId10)

        if testShokai != 'testShokai':
            pks_list.remove(testId1)
        
        try:
            pks_list.remove(testId2)
        except:
            pass

        try:
            pks_list.remove(testId3)
        except:
            pass

        try:
            pks_list.remove(testId4)
        except:
            pass

        try:
            pks_list.remove(testId5)
        except:
            pass

        try:
            pks_list.remove(testId6)
        except:
            pass

        try:
            pks_list.remove(testId7)
        except:
            pass

        try:
            pks_list.remove(testId8)
        except:
            pass

        try:
            pks_list.remove(testId9)
        except:
            pass

        try:
            pks_list.remove(testId10)
        except:
            pass
        data = random.sample(pks_list,1)

        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)

    else:
        pks = Practice.objects.values_list('pk', flat=True)
        pks_list = list(pks)
        data = random.sample(pks_list,1)
   
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,26)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,27)

    dQ = Practice.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3

    if dQ.wronganswer4 is str:
        dataWrongAnswer4 = dQ.wronganswer4
    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9

    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3
    dataCategory = dQ.category
    
    data1Answer = dQ.answer

    data2Answer = dataWrongAnswer1 
    data3Answer = dataWrongAnswer2
    data4Answer = dataWrongAnswer3

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer]
    dataAnsList7shuffle = random.sample(dataAnsList7,4)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]
    
    test10mondaisuu = 10
        
    seikairitsuFloat = (float(test10seikai) / float(test10mondaisuu)) * 100
    seikairitsu = int(seikairitsuFloat)

    dQID = data[0]
    dQQuestion = dQ.question
    dQAnswer = dQ.answer
    dQSelectAns = selectedAns


    if test10count == 0:
        testId1 = 777
        testQuestion1 = 7777
        testAnswer1 = 7777
        testSelectAns1 = 7777
    if test10count <= 1:
        testId2 = 777
        testQuestion2 = 7777
        testAnswer2 = 7777
        testSelectAns2 = 7777
    if test10count <= 2:
        testId3 = 777
        testQuestion3 = 7777
        testAnswer3 = 7777
        testSelectAns3 = 7777
    if test10count <= 3:
        testId4 = 7777
        testQuestion4 = 7777
        testAnswer4 = 7777
        testSelectAns4 = 7777
    if test10count <= 4:
        testId5 = 7777
        testQuestion5 = 7777
        testAnswer5 = 7777
        testSelectAns5 = 7777
    if test10count <= 5:
        testId6 = 7777
        testQuestion6 = 7777
        testAnswer6 = 7777
        testSelectAns6 = 7777
    if test10count <= 6:
        testId7 = 7777
        testQuestion7 = 7777
        testAnswer7 = 7777
        testSelectAns7 = 7777
    if test10count <= 7:
        testId8 = 7777
        testQuestion8 = 7777
        testAnswer8 = 7777
        testSelectAns8 = 7777
    if test10count <= 8:
        testId9 = 7777
        testQuestion9 = 7777
        testAnswer9 = 7777
        testSelectAns9 = 7777
    if test10count <= 9:
        testId10 = 7777
        testQuestion10 = 7777
        testAnswer10 = 7777
        testSelectAns10 = 7777
    if test10count == 1:
        testId1 = dQID
        testQuestion1 = dQQuestion
        testAnswer1 = dQAnswer
        testSelectAns1 = dQSelectAns
    if test10count == 2:
        testId2 = dQID
        testQuestion2 = dQQuestion
        testAnswer2 = dQAnswer
        testSelectAns2 = dQSelectAns
    if test10count == 3:
        testId3 = dQID
        testQuestion3 = dQQuestion
        testAnswer3 = dQAnswer
        testSelectAns3 = dQSelectAns
    if test10count == 4:
        testId4 = dQID
        testQuestion4 = dQQuestion
        testAnswer4 = dQAnswer
        testSelectAns4 = dQSelectAns
    if test10count == 5:
        testId5 = dQID
        testQuestion5 = dQQuestion
        testAnswer5 = dQAnswer
        testSelectAns5 = dQSelectAns
    if test10count == 6:
        testId6 = dQID
        testQuestion6 = dQQuestion
        testAnswer6 = dQAnswer
        testSelectAns6 = dQSelectAns
    if test10count == 7:
        testId7 = dQID
        testQuestion7 = dQQuestion
        testAnswer7 = dQAnswer
        testSelectAns7 = dQSelectAns
    if test10count == 8:
        testId8 = dQID
        testQuestion8 = dQQuestion
        testAnswer8 = dQAnswer
        testSelectAns8 = dQSelectAns
    if test10count == 9:
        testId9 = dQID
        testQuestion9 = dQQuestion
        testAnswer9 = dQAnswer
        testSelectAns9 = dQSelectAns
    if test10count == 10:
        testId10 = dQID
        testQuestion10 = dQQuestion
        testAnswer10 = dQAnswer
        testSelectAns10 = dQSelectAns

    testId = dQID

    if test10count == test10mondaisuu + 1 :
        userid = request.user.id
        TestRoutine10.objects.create(user_id=userid, test_result=seikairitsu, category=test10Category)#seikairitsuは文字列

    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'data2pk3_1':data2pk3_1,
            'object_list':object_list,
            'test10count':test10count,
            'test10seikai':test10seikai,
            'testShokai' :"testNandomeka",
            'seikairitsu':seikairitsu,
            'test10mondaisuu':test10mondaisuu,
            'selectedAns':selectedAns,
            'testId1':testId1,
            'testId2':testId2,
            'testId3':testId3,
            'testId4':testId4,
            'testId5':testId5,
            'testId6':testId6,
            'testId7':testId7,
            'testId8':testId8,
            'testId9':testId9,
            'testId10':testId10,
            'testId':testId,

            'testQuestion1':testQuestion1,
            'testQuestion2':testQuestion2,
            'testQuestion3':testQuestion3,
            'testQuestion4':testQuestion4,
            'testQuestion5':testQuestion5,
            'testQuestion6':testQuestion6,
            'testQuestion7':testQuestion7,
            'testQuestion8':testQuestion8,
            'testQuestion9':testQuestion9,
            'testQuestion10':testQuestion10,

            'testAnswer1':testAnswer1,
            'testAnswer2':testAnswer2,
            'testAnswer3':testAnswer3,
            'testAnswer4':testAnswer4,
            'testAnswer5':testAnswer5,
            'testAnswer6':testAnswer6,
            'testAnswer7':testAnswer7,
            'testAnswer8':testAnswer8,
            'testAnswer9':testAnswer9,
            'testAnswer10':testAnswer10,

            'testSelectAns1':testSelectAns1,
            'testSelectAns2':testSelectAns2,
            'testSelectAns3':testSelectAns3,
            'testSelectAns4':testSelectAns4,
            'testSelectAns5':testSelectAns5,
            'testSelectAns6':testSelectAns6,
            'testSelectAns7':testSelectAns7,
            'testSelectAns8':testSelectAns8,
            'testSelectAns9':testSelectAns9,
            'testSelectAns10':testSelectAns10,
            'testes': testes,
            'selectCategory': selectCategory,
            'selCatKakutei': selCatKakutei,
            'test10Category': test10Category
    }

    if test10count == test10mondaisuu + 1 :

        return render(request, 'sqlapp/question_test4taku_result10.html', params)
    else:
        return render(request, 'sqlapp/question_test4taku_10.html', params)


def testQuestionView5taku_40(request):

    object_list = Practice.objects.all()
    
    test40count = request.POST["test40count"]
    test40seikai = request.POST["test40seikai"]
    testShokai = request.POST["testShokai"]

    if testShokai != 'testShokai':
        context = {
            'test40count' :request.POST["test40count"],
            'test40seikai' :request.POST["test40seikai"],
            'testShokai' :request.POST["testShokai"],
            'selectedAns' :request.POST["name1"],
            'dataAnswer' :request.POST["name0"],
            'dataQuestion' :request.POST["nameQuestion"],
            'dataExplanation' :request.POST["nameEx"],
            'dataThumbnailQ1' :request.POST["nameThuQ1"],
            'dataThumbnailQ2' :request.POST["nameThuQ2"],
            'dataThumbnailQ3' :request.POST["nameThuQ3"],
            'dataThumbnailA1' :request.POST["nameThuA1"],
            'dataThumbnailA2' :request.POST["nameThuA2"],
            'dataThumbnailA3' :request.POST["nameThuA3"],
            'object_list': object_list,
            'dataNumtaku' :request.POST['nameNumtaku'],
            'testId' :request.POST['testId'],
            'testId1' :request.POST['testId1'],
            'testId2' :request.POST['testId2'],
            'testId3' :request.POST['testId3'],
            'testId4':request.POST['testId4'],
            'testId5':request.POST['testId5'],
            'testId6':request.POST['testId6'],
            'testId7':request.POST['testId7'],
            'testId8':request.POST['testId8'],
            'testId9':request.POST['testId9'],
            'testId10':request.POST['testId10'],

            'testId11' :request.POST['testId11'],
            'testId12' :request.POST['testId12'],
            'testId13' :request.POST['testId13'],
            'testId14':request.POST['testId14'],
            'testId15':request.POST['testId15'],
            'testId16':request.POST['testId16'],
            'testId17':request.POST['testId17'],
            'testId18':request.POST['testId18'],
            'testId19':request.POST['testId19'],
            'testId20':request.POST['testId20'],

            'testId21' :request.POST['testId21'],
            'testId22' :request.POST['testId22'],
            'testId23' :request.POST['testId23'],
            'testId24':request.POST['testId24'],
            'testId25':request.POST['testId25'],
            'testId26':request.POST['testId26'],
            'testId27':request.POST['testId27'],
            'testId28':request.POST['testId28'],
            'testId29':request.POST['testId29'],
            'testId30':request.POST['testId30'],

            'testId31' :request.POST['testId31'],
            'testId32' :request.POST['testId32'],
            'testId33' :request.POST['testId33'],
            'testId34':request.POST['testId34'],
            'testId35':request.POST['testId35'],
            'testId36':request.POST['testId36'],
            'testId37':request.POST['testId37'],
            'testId38':request.POST['testId38'],
            'testId39':request.POST['testId39'],
            'testId40':request.POST['testId40'],

            'testQuestion1' :request.POST['testQuestion1'],
            'testQuestion2' :request.POST['testQuestion2'],
            'testQuestion3' :request.POST['testQuestion3'],
            'testQuestion4':request.POST['testQuestion4'],
            'testQuestion5':request.POST['testQuestion5'],
            'testQuestion6':request.POST['testQuestion6'],
            'testQuestion7':request.POST['testQuestion7'],
            'testQuestion8':request.POST['testQuestion8'],
            'testQuestion9':request.POST['testQuestion9'],
            'testQuestion10':request.POST['testQuestion10'],

            'testQuestion11' :request.POST['testQuestion11'],
            'testQuestion12' :request.POST['testQuestion12'],
            'testQuestion13' :request.POST['testQuestion13'],
            'testQuestion14':request.POST['testQuestion14'],
            'testQuestion15':request.POST['testQuestion15'],
            'testQuestion16':request.POST['testQuestion16'],
            'testQuestion17':request.POST['testQuestion17'],
            'testQuestion18':request.POST['testQuestion18'],
            'testQuestion19':request.POST['testQuestion19'],
            'testQuestion20':request.POST['testQuestion20'],

            'testQuestion21' :request.POST['testQuestion21'],
            'testQuestion22' :request.POST['testQuestion22'],
            'testQuestion23' :request.POST['testQuestion23'],
            'testQuestion24':request.POST['testQuestion24'],
            'testQuestion25':request.POST['testQuestion25'],
            'testQuestion26':request.POST['testQuestion26'],
            'testQuestion27':request.POST['testQuestion27'],
            'testQuestion28':request.POST['testQuestion28'],
            'testQuestion29':request.POST['testQuestion29'],
            'testQuestion30':request.POST['testQuestion30'],

            'testQuestion31' :request.POST['testQuestion31'],
            'testQuestion32' :request.POST['testQuestion32'],
            'testQuestion33' :request.POST['testQuestion33'],
            'testQuestion34':request.POST['testQuestion34'],
            'testQuestion35':request.POST['testQuestion35'],
            'testQuestion36':request.POST['testQuestion36'],
            'testQuestion37':request.POST['testQuestion37'],
            'testQuestion38':request.POST['testQuestion38'],
            'testQuestion39':request.POST['testQuestion39'],
            'testQuestion40':request.POST['testQuestion40'],

            'testAnswer1' :request.POST['testAnswer1'],
            'testAnswer2' :request.POST['testAnswer2'],
            'testAnswer3' :request.POST['testAnswer3'],
            'testAnswer4':request.POST['testAnswer4'],
            'testAnswer5':request.POST['testAnswer5'],
            'testAnswer6':request.POST['testAnswer6'],
            'testAnswer7':request.POST['testAnswer7'],
            'testAnswer8':request.POST['testAnswer8'],
            'testAnswer9':request.POST['testAnswer9'],
            'testAnswer10':request.POST['testAnswer10'],

            'testAnswer11' :request.POST['testAnswer11'],
            'testAnswer12' :request.POST['testAnswer12'],
            'testAnswer13' :request.POST['testAnswer13'],
            'testAnswer14':request.POST['testAnswer14'],
            'testAnswer15':request.POST['testAnswer15'],
            'testAnswer16':request.POST['testAnswer16'],
            'testAnswer17':request.POST['testAnswer17'],
            'testAnswer18':request.POST['testAnswer18'],
            'testAnswer19':request.POST['testAnswer19'],
            'testAnswer20':request.POST['testAnswer20'],

            'testAnswer21' :request.POST['testAnswer21'],
            'testAnswer22' :request.POST['testAnswer22'],
            'testAnswer23' :request.POST['testAnswer23'],
            'testAnswer24':request.POST['testAnswer24'],
            'testAnswer25':request.POST['testAnswer25'],
            'testAnswer26':request.POST['testAnswer26'],
            'testAnswer27':request.POST['testAnswer27'],
            'testAnswer28':request.POST['testAnswer28'],
            'testAnswer29':request.POST['testAnswer29'],
            'testAnswer30':request.POST['testAnswer30'],

            'testAnswer31' :request.POST['testAnswer31'],
            'testAnswer32' :request.POST['testAnswer32'],
            'testAnswer33' :request.POST['testAnswer33'],
            'testAnswer34':request.POST['testAnswer34'],
            'testAnswer35':request.POST['testAnswer35'],
            'testAnswer36':request.POST['testAnswer36'],
            'testAnswer37':request.POST['testAnswer37'],
            'testAnswer38':request.POST['testAnswer38'],
            'testAnswer39':request.POST['testAnswer39'],
            'testAnswer40':request.POST['testAnswer40'],

            'testSelectAns1' :request.POST['testSelectAns1'],
            'testSelectAns2' :request.POST['testSelectAns2'],
            'testSelectAns3' :request.POST['testSelectAns3'],
            'testSelectAns4':request.POST['testSelectAns4'],
            'testSelectAns5':request.POST['testSelectAns5'],
            'testSelectAns6':request.POST['testSelectAns6'],
            'testSelectAns7':request.POST['testSelectAns7'],
            'testSelectAns8':request.POST['testSelectAns8'],
            'testSelectAns9':request.POST['testSelectAns9'],
            'testSelectAns10':request.POST['testSelectAns10'],

            'testSelectAns11' :request.POST['testSelectAns11'],
            'testSelectAns12' :request.POST['testSelectAns12'],
            'testSelectAns13' :request.POST['testSelectAns13'],
            'testSelectAns14':request.POST['testSelectAns14'],
            'testSelectAns15':request.POST['testSelectAns15'],
            'testSelectAns16':request.POST['testSelectAns16'],
            'testSelectAns17':request.POST['testSelectAns17'],
            'testSelectAns18':request.POST['testSelectAns18'],
            'testSelectAns19':request.POST['testSelectAns19'],
            'testSelectAns20':request.POST['testSelectAns20'],

            'testSelectAns21' :request.POST['testSelectAns21'],
            'testSelectAns22' :request.POST['testSelectAns22'],
            'testSelectAns23' :request.POST['testSelectAns23'],
            'testSelectAns24':request.POST['testSelectAns24'],
            'testSelectAns25':request.POST['testSelectAns25'],
            'testSelectAns26':request.POST['testSelectAns26'],
            'testSelectAns27':request.POST['testSelectAns27'],
            'testSelectAns28':request.POST['testSelectAns28'],
            'testSelectAns29':request.POST['testSelectAns29'],
            'testSelectAns30':request.POST['testSelectAns30'],

            'testSelectAns31' :request.POST['testSelectAns31'],
            'testSelectAns32' :request.POST['testSelectAns32'],
            'testSelectAns33' :request.POST['testSelectAns33'],
            'testSelectAns34':request.POST['testSelectAns34'],
            'testSelectAns35':request.POST['testSelectAns35'],
            'testSelectAns36':request.POST['testSelectAns36'],
            'testSelectAns37':request.POST['testSelectAns37'],
            'testSelectAns38':request.POST['testSelectAns38'],
            'testSelectAns39':request.POST['testSelectAns39'],
            'testSelectAns40':request.POST['testSelectAns40'],
            
        }
        selectedAns = request.POST["name1"]
        dataAnswer = request.POST["name0"]
        dataQuestion = request.POST["nameQuestion"]
        dataThumbnailQ1 = request.POST["nameThuQ1"]
        dataThumbnailQ2 = request.POST["nameThuQ2"]
        dataThumbnailQ3 = request.POST["nameThuQ3"]
        dataThumbnailA1 = request.POST["nameThuA1"]
        dataThumbnailA2 = request.POST["nameThuA2"]
        dataThumbnailA3 = request.POST["nameThuA3"]
        dataNumtaku = request.POST["nameNumtaku"]
        test40count = request.POST['test40count']
        test40seikai = request.POST['test40seikai']
        testId = request.POST['testId']
        testId1 = request.POST['testId1']
        testId2 = request.POST['testId2']
        testId3 = request.POST['testId3']
        testId4 = request.POST['testId4']
        testId5 = request.POST['testId5']
        testId6 = request.POST['testId6']
        testId7 = request.POST['testId7']
        testId8 = request.POST['testId8']
        testId9 = request.POST['testId9']
        testId10 = request.POST['testId10']
        testId11 = request.POST['testId11']
        testId12 = request.POST['testId12']
        testId13 = request.POST['testId13']
        testId14 = request.POST['testId14']
        testId15 = request.POST['testId15']
        testId16 = request.POST['testId16']
        testId17 = request.POST['testId17']
        testId18 = request.POST['testId18']
        testId19 = request.POST['testId19']
        testId20 = request.POST['testId20']
        testId21 = request.POST['testId21']
        testId22 = request.POST['testId22']
        testId23 = request.POST['testId23']
        testId24 = request.POST['testId24']
        testId25 = request.POST['testId25']
        testId26 = request.POST['testId26']
        testId27 = request.POST['testId27']
        testId28 = request.POST['testId28']
        testId29 = request.POST['testId29']
        testId30 = request.POST['testId30']
        testId31 = request.POST['testId31']
        testId32 = request.POST['testId32']
        testId33 = request.POST['testId33']
        testId34 = request.POST['testId34']
        testId35 = request.POST['testId35']
        testId36 = request.POST['testId36']
        testId37 = request.POST['testId37']
        testId38 = request.POST['testId38']
        testId39 = request.POST['testId39']
        testId40 = request.POST['testId40']

        testQuestion1 = request.POST['testQuestion1']
        testQuestion2 = request.POST['testQuestion2']
        testQuestion3 = request.POST['testQuestion3']
        testQuestion4 = request.POST['testQuestion4']
        testQuestion5 = request.POST['testQuestion5']
        testQuestion6 = request.POST['testQuestion6']
        testQuestion7 = request.POST['testQuestion7']
        testQuestion8 = request.POST['testQuestion8']
        testQuestion9 = request.POST['testQuestion9']
        testQuestion10 = request.POST['testQuestion10']
        testQuestion11 = request.POST['testQuestion11']
        testQuestion12 = request.POST['testQuestion12']
        testQuestion13 = request.POST['testQuestion13']
        testQuestion14 = request.POST['testQuestion14']
        testQuestion15 = request.POST['testQuestion15']
        testQuestion16 = request.POST['testQuestion16']
        testQuestion17 = request.POST['testQuestion17']
        testQuestion18 = request.POST['testQuestion18']
        testQuestion19 = request.POST['testQuestion19']
        testQuestion20 = request.POST['testQuestion20']
        testQuestion21 = request.POST['testQuestion21']
        testQuestion22 = request.POST['testQuestion22']
        testQuestion23 = request.POST['testQuestion23']
        testQuestion24 = request.POST['testQuestion24']
        testQuestion25 = request.POST['testQuestion25']
        testQuestion26 = request.POST['testQuestion26']
        testQuestion27 = request.POST['testQuestion27']
        testQuestion28 = request.POST['testQuestion28']
        testQuestion29 = request.POST['testQuestion29']
        testQuestion30 = request.POST['testQuestion30']
        testQuestion31 = request.POST['testQuestion31']
        testQuestion32 = request.POST['testQuestion32']
        testQuestion33 = request.POST['testQuestion33']
        testQuestion34 = request.POST['testQuestion34']
        testQuestion35 = request.POST['testQuestion35']
        testQuestion36 = request.POST['testQuestion36']
        testQuestion37 = request.POST['testQuestion37']
        testQuestion38 = request.POST['testQuestion38']
        testQuestion39 = request.POST['testQuestion39']
        testQuestion40 = request.POST['testQuestion40']

        testAnswer1 = request.POST['testAnswer1']
        testAnswer2 = request.POST['testAnswer2']
        testAnswer3 = request.POST['testAnswer3']
        testAnswer4 = request.POST['testAnswer4']
        testAnswer5 = request.POST['testAnswer5']
        testAnswer6 = request.POST['testAnswer6']
        testAnswer7 = request.POST['testAnswer7']
        testAnswer8 = request.POST['testAnswer8']
        testAnswer9 = request.POST['testAnswer9']
        testAnswer10 = request.POST['testAnswer10']
        testAnswer11 = request.POST['testAnswer11']
        testAnswer12 = request.POST['testAnswer12']
        testAnswer13 = request.POST['testAnswer13']
        testAnswer14 = request.POST['testAnswer14']
        testAnswer15 = request.POST['testAnswer15']
        testAnswer16 = request.POST['testAnswer16']
        testAnswer17 = request.POST['testAnswer17']
        testAnswer18 = request.POST['testAnswer18']
        testAnswer19 = request.POST['testAnswer19']
        testAnswer20 = request.POST['testAnswer20']
        testAnswer21 = request.POST['testAnswer21']
        testAnswer22 = request.POST['testAnswer22']
        testAnswer23 = request.POST['testAnswer23']
        testAnswer24 = request.POST['testAnswer24']
        testAnswer25 = request.POST['testAnswer25']
        testAnswer26 = request.POST['testAnswer26']
        testAnswer27 = request.POST['testAnswer27']
        testAnswer28 = request.POST['testAnswer28']
        testAnswer29 = request.POST['testAnswer29']
        testAnswer30 = request.POST['testAnswer30']
        testAnswer31 = request.POST['testAnswer31']
        testAnswer32 = request.POST['testAnswer32']
        testAnswer33 = request.POST['testAnswer33']
        testAnswer34 = request.POST['testAnswer34']
        testAnswer35 = request.POST['testAnswer35']
        testAnswer36 = request.POST['testAnswer36']
        testAnswer37 = request.POST['testAnswer37']
        testAnswer38 = request.POST['testAnswer38']
        testAnswer39 = request.POST['testAnswer39']
        testAnswer40 = request.POST['testAnswer40']

        testSelectAns1 = request.POST['testSelectAns1']
        testSelectAns2 = request.POST['testSelectAns2']
        testSelectAns3 = request.POST['testSelectAns3']
        testSelectAns4 = request.POST['testSelectAns4']
        testSelectAns5 = request.POST['testSelectAns5']
        testSelectAns6 = request.POST['testSelectAns6']
        testSelectAns7 = request.POST['testSelectAns7']
        testSelectAns8 = request.POST['testSelectAns8']
        testSelectAns9 = request.POST['testSelectAns9']
        testSelectAns10 = request.POST['testSelectAns10']
        testSelectAns11 = request.POST['testSelectAns11']
        testSelectAns12 = request.POST['testSelectAns12']
        testSelectAns13 = request.POST['testSelectAns13']
        testSelectAns14 = request.POST['testSelectAns14']
        testSelectAns15 = request.POST['testSelectAns15']
        testSelectAns16 = request.POST['testSelectAns16']
        testSelectAns17 = request.POST['testSelectAns17']
        testSelectAns18 = request.POST['testSelectAns18']
        testSelectAns19 = request.POST['testSelectAns19']
        testSelectAns20 = request.POST['testSelectAns20']
        testSelectAns21 = request.POST['testSelectAns21']
        testSelectAns22 = request.POST['testSelectAns22']
        testSelectAns23 = request.POST['testSelectAns23']
        testSelectAns24 = request.POST['testSelectAns24']
        testSelectAns25 = request.POST['testSelectAns25']
        testSelectAns26 = request.POST['testSelectAns26']
        testSelectAns27 = request.POST['testSelectAns27']
        testSelectAns28 = request.POST['testSelectAns28']
        testSelectAns29 = request.POST['testSelectAns29']
        testSelectAns30 = request.POST['testSelectAns30']
        testSelectAns31 = request.POST['testSelectAns31']
        testSelectAns32 = request.POST['testSelectAns32']
        testSelectAns33 = request.POST['testSelectAns33']
        testSelectAns34 = request.POST['testSelectAns34']
        testSelectAns35 = request.POST['testSelectAns35']
        testSelectAns36 = request.POST['testSelectAns36']
        testSelectAns37 = request.POST['testSelectAns37']
        testSelectAns38 = request.POST['testSelectAns38']
        testSelectAns39 = request.POST['testSelectAns39']
        testSelectAns40 = request.POST['testSelectAns40']
    else:
        context = {
            'test40count':request.POST["test40count"],
            'test40seikai':request.POST["test40seikai"],
            
        }
        selectedAns = "shokaihanai"
        testId = 7777777
        testId1 = 7777777
        testId2 = 7777777
        testId3 = 7777777
        testId4 = 7777777
        testId5 = 7777777
        testId6 = 7777777
        testId7 = 7777777
        testId8 = 7777777
        testId9 = 7777777
        testId10 = 7777777
        testId11 = 7777777
        testId12 = 7777777
        testId13 = 7777777
        testId14 = 7777777
        testId15 = 7777777
        testId16 = 7777777
        testId17 = 7777777
        testId18 = 7777777
        testId19 = 7777777
        testId20 = 7777777
        testId21 = 7777777
        testId22 = 7777777
        testId23 = 7777777
        testId24 = 7777777
        testId25 = 7777777
        testId26 = 7777777
        testId27 = 7777777
        testId28 = 7777777
        testId29 = 7777777
        testId30 = 7777777
        testId31 = 7777777
        testId32 = 7777777
        testId33 = 7777777
        testId34 = 7777777
        testId35 = 7777777
        testId36 = 7777777
        testId37 = 7777777
        testId38 = 7777777
        testId39 = 7777777
        testId40 = 7777777

    test40count = int(test40count)
    test40count += 1

    test40seikai = int(test40seikai)
    
    if testShokai != 'testShokai' and selectedAns == dataAnswer:
        test40seikai += 1
    
    
    if (request.method == 'POST'):

        selCatKakutei = request.POST.get('selCatKakutei')
        if testShokai == 'testShokai':
            selectCategory = ""
        else:
            selectCategory = request.POST.get('selCatKakutei')

        if selCatKakutei == "基本情報技術者試験":
            selCatKakutei = "FE"
        if selectCategory == "基本情報技術者試験":
            selectCategory = "FE"
        if selCatKakutei == "応用情報技術者試験":
            selCatKakutei = "AP"
        if selectCategory == "応用情報技術者試験":
            selectCategory = "AP"
 
        if request.POST.get('categorybetsu'):
            selectCategory = request.POST.get('categorybetsu')
            if selectCategory == "基本情報技術者試験":
                selectCategory = "FE"
            if selectCategory == "応用情報技術者試験":
                selectCategory = "AP"

        if request.POST.get('categorybetsu2'):
            selectCategory = request.POST.get('categorybetsu2')
            if selectCategory2 == "基本情報技術者試験":
                selectCategory2 = "FE"
            if selectCategory2 == "応用情報技術者試験":
                selectCategory2 = "AP"


        if selectCategory == "" or selectCategory == "カテゴリを選択": #ここ
            pks = Practice.objects.values_list('pk', flat=True)
            testes = "あ"
        else:
            pks = Practice.objects.filter(category__contains=selectCategory).values_list('pk', flat=True)
            testes = "い"
            if testShokai == 'testShokai':
                selCatKakutei = selectCategory

        pks_list = list(pks)

        testId = int(testId)
        testId1 = int(testId1)
        testId2 = int(testId2)
        testId3 = int(testId3)
        testId4 = int(testId4)
        testId5 = int(testId5)
        testId6 = int(testId6)
        testId7 = int(testId7)
        testId8 = int(testId8)
        testId9 = int(testId9)
        testId10 = int(testId10)
        testId11 = int(testId11)
        testId12 = int(testId12)
        testId13 = int(testId13)
        testId14 = int(testId14)
        testId15 = int(testId15)
        testId16 = int(testId16)
        testId17 = int(testId17)
        testId18 = int(testId18)
        testId19 = int(testId19)
        testId20 = int(testId20)
        testId21 = int(testId21)
        testId22 = int(testId22)
        testId23 = int(testId23)
        testId24 = int(testId24)
        testId25 = int(testId25)
        testId26 = int(testId26)
        testId27 = int(testId27)
        testId28 = int(testId28)
        testId29 = int(testId29)
        testId30 = int(testId30)
        testId31 = int(testId31)
        testId32 = int(testId32)
        testId33 = int(testId33)
        testId34 = int(testId34)
        testId35 = int(testId35)
        testId36 = int(testId36)
        testId37 = int(testId37)
        testId38 = int(testId38)
        testId39 = int(testId39)
        testId40 = int(testId40)

        if testShokai != 'testShokai':
            pks_list.remove(testId1)
            
        try:
            pks_list.remove(testId2)
        except:
            pass
        try:
            pks_list.remove(testId3)
        except:
            pass
        try:
            pks_list.remove(testId4)
        except:
            pass
        try:
            pks_list.remove(testId5)
        except:
            pass
        try:
            pks_list.remove(testId6)
        except:
            pass
        try:
            pks_list.remove(testId7)
        except:
            pass
        try:
            pks_list.remove(testId8)
        except:
            pass
        try:
            pks_list.remove(testId9)
        except:
            pass
        try:
            pks_list.remove(testId10)
        except:
            pass
        try:
            pks_list.remove(testId11)
        except:
            pass       
        try:
            pks_list.remove(testId12)
        except:
            pass
        try:
            pks_list.remove(testId13)
        except:
            pass
        try:
            pks_list.remove(testId14)
        except:
            pass
        try:
            pks_list.remove(testId15)
        except:
            pass
        try:
            pks_list.remove(testId16)
        except:
            pass
        try:
            pks_list.remove(testId17)
        except:
            pass
        try:
            pks_list.remove(testId18)
        except:
            pass
        try:
            pks_list.remove(testId19)
        except:
            pass
        try:
            pks_list.remove(testId20)
        except:
            pass
        try:
            pks_list.remove(testId21)
        except:
            pass

        try:
            pks_list.remove(testId22)
        except:
            pass
        try:
            pks_list.remove(testId23)
        except:
            pass
        try:
            pks_list.remove(testId24)
        except:
            pass
        try:
            pks_list.remove(testId25)
        except:
            pass
        try:
            pks_list.remove(testId26)
        except:
            pass
        try:
            pks_list.remove(testId27)
        except:
            pass
        try:
            pks_list.remove(testId28)
        except:
            pass
        try:
            pks_list.remove(testId29)
        except:
            pass
        try:
            pks_list.remove(testId30)
        except:
            pass
        try:
            pks_list.remove(testId31)
        except:
            pass
        try:
            pks_list.remove(testId32)
        except:
            pass
        try:
            pks_list.remove(testId33)
        except:
            pass
        try:
            pks_list.remove(testId34)
        except:
            pass
        try:
            pks_list.remove(testId35)
        except:
            pass

        try:
            pks_list.remove(testId36)
        except:
            pass
        try:
            pks_list.remove(testId37)
        except:
            pass
        try:
            pks_list.remove(testId38)
        except:
            pass
        try:
            pks_list.remove(testId39)
        except:
            pass
        try:
            pks_list.remove(testId40)
        except:
            pass
        
        data = random.sample(pks_list,1)     
        
        pks_list.remove(data[0])
        data2pk3_1 = random.sample(pks_list,35)
        data4all = data + data2pk3_1
        data4allshuffle = random.sample(data4all,36)


    dQ = Practice.objects.get(id=data[0])
    dataQuestion = dQ.question
    dataAnswer = dQ.answer
    dataWrongAnswer1 = dQ.wronganswer1
    dataWrongAnswer2 = dQ.wronganswer2
    dataWrongAnswer3 = dQ.wronganswer3

    if dQ.wronganswer4 :
        dataWrongAnswer4 = dQ.wronganswer4
    else:
        dataWrongAnswer4 = ""


    if dQ.wronganswer5 is str:
        dataWrongAnswer5 = dQ.wronganswer5
    if dQ.wronganswer6 is str:
        dataWrongAnswer6 = dQ.wronganswer6
    if dQ.wronganswer7 is str:
        dataWrongAnswer7 = dQ.wronganswer7
    if dQ.wronganswer8 is str:
        dataWrongAnswer8 = dQ.wronganswer8
    if dQ.wronganswer9 is str:
        dataWrongAnswer9 = dQ.wronganswer9

    dataExplanation = dQ.explanation
    dataThumbnailQ1 = dQ.thumbnailQ1
    dataThumbnailQ2 = dQ.thumbnailQ2
    dataThumbnailQ3 = dQ.thumbnailQ3
    dataThumbnailA1 = dQ.thumbnailA1
    dataThumbnailA2 = dQ.thumbnailA2
    dataThumbnailA3 = dQ.thumbnailA3
    dataCategory = dQ.category
  
    data1Answer = dQ.answer

    data2Answer = dataWrongAnswer1 
    data3Answer = dataWrongAnswer2
    data4Answer = dataWrongAnswer3

    data5Answer = dataWrongAnswer4

    dataAnsList7 = [data1Answer, data2Answer, data3Answer, data4Answer, data5Answer]

    dataAnsList7shuffle = random.sample(dataAnsList7,5)

    d7_1_Answer = dataAnsList7shuffle[0]
    d7_2_Answer = dataAnsList7shuffle[1]
    d7_3_Answer = dataAnsList7shuffle[2]
    d7_4_Answer = dataAnsList7shuffle[3]

    d7_5_Answer = dataAnsList7shuffle[4]
    
    test40mondaisuu = 40
        
    seikairitsuFloat = (float(test40seikai) / float(test40mondaisuu)) * 100
    seikairitsu = int(seikairitsuFloat)

    dQID = data[0]
    dQQuestion = dQ.question
    dQAnswer = dQ.answer
    dQSelectAns = selectedAns


    if test40count == 0:
        testId1 = 777
        testQuestion1 = 7777
        testAnswer1 = 7777
        testSelectAns1 = 7777
    if test40count <= 1:
        testId2 = 777
        testQuestion2 = 7777
        testAnswer2 = 7777
        testSelectAns2 = 7777
    if test40count <= 2:
        testId3 = 777
        testQuestion3 = 7777
        testAnswer3 = 7777
        testSelectAns3 = 7777
    if test40count <= 3:
        testId4 = 7777
        testQuestion4 = 7777
        testAnswer4 = 7777
        testSelectAns4 = 7777
    if test40count <= 4:
        testId5 = 7777
        testQuestion5 = 7777
        testAnswer5 = 7777
        testSelectAns5 = 7777
    if test40count <= 5:
        testId6 = 7777
        testQuestion6 = 7777
        testAnswer6 = 7777
        testSelectAns6 = 7777
    if test40count <= 6:
        testId7 = 7777
        testQuestion7 = 7777
        testAnswer7 = 7777
        testSelectAns7 = 7777
    if test40count <= 7:
        testId8 = 7777
        testQuestion8 = 7777
        testAnswer8 = 7777
        testSelectAns8 = 7777
    if test40count <= 8:
        testId9 = 7777
        testQuestion9 = 7777
        testAnswer9 = 7777
        testSelectAns9 = 7777
    if test40count <= 9:
        testId10 = 7777
        testQuestion10 = 7777
        testAnswer10 = 7777
        testSelectAns10 = 7777

    if test40count <= 10:
        testId11 = 777
        testQuestion11 = 7777
        testAnswer11 = 7777
        testSelectAns11 = 7777
    if test40count <= 11:
        testId12 = 777
        testQuestion12 = 7777
        testAnswer12 = 7777
        testSelectAns12 = 7777
    if test40count <= 12:
        testId13 = 777
        testQuestion13 = 7777
        testAnswer13 = 7777
        testSelectAns13 = 7777
    if test40count <= 13:
        testId14 = 7777
        testQuestion14 = 7777
        testAnswer14 = 7777
        testSelectAns14 = 7777
    if test40count <= 14:
        testId15 = 7777
        testQuestion15 = 7777
        testAnswer15 = 7777
        testSelectAns15 = 7777
    if test40count <= 15:
        testId16 = 7777
        testQuestion16 = 7777
        testAnswer16 = 7777
        testSelectAns16 = 7777
    if test40count <= 16:
        testId17 = 7777
        testQuestion17 = 7777
        testAnswer17 = 7777
        testSelectAns17 = 7777
    if test40count <= 17:
        testId18 = 7777
        testQuestion18 = 7777
        testAnswer18 = 7777
        testSelectAns18 = 7777
    if test40count <= 18:
        testId19 = 7777
        testQuestion19 = 7777
        testAnswer19 = 7777
        testSelectAns19 = 7777
    if test40count <= 19:
        testId20 = 7777
        testQuestion20 = 7777
        testAnswer20 = 7777
        testSelectAns20 = 7777

    if test40count <= 20:
        testId21 = 777
        testQuestion21 = 7777
        testAnswer21 = 7777
        testSelectAns21 = 7777
    if test40count <= 21:
        testId22 = 777
        testQuestion22 = 7777
        testAnswer22 = 7777
        testSelectAns22 = 7777
    if test40count <= 22:
        testId23 = 777
        testQuestion23 = 7777
        testAnswer23 = 7777
        testSelectAns23 = 7777
    if test40count <= 23:
        testId24 = 7777
        testQuestion24 = 7777
        testAnswer24 = 7777
        testSelectAns24 = 7777
    if test40count <= 24:
        testId25 = 7777
        testQuestion25 = 7777
        testAnswer25 = 7777
        testSelectAns25 = 7777
    if test40count <= 25:
        testId26 = 7777
        testQuestion26 = 7777
        testAnswer26 = 7777
        testSelectAns26 = 7777
    if test40count <= 26:
        testId27 = 7777
        testQuestion27 = 7777
        testAnswer27 = 7777
        testSelectAns27 = 7777
    if test40count <= 27:
        testId28 = 7777
        testQuestion28 = 7777
        testAnswer28 = 7777
        testSelectAns28 = 7777
    if test40count <= 28:
        testId29 = 7777
        testQuestion29 = 7777
        testAnswer29 = 7777
        testSelectAns29 = 7777
    if test40count <= 29:
        testId30 = 7777
        testQuestion30 = 7777
        testAnswer30 = 7777
        testSelectAns30 = 7777

    if test40count <= 30:
        testId31 = 777
        testQuestion31 = 7777
        testAnswer31 = 7777
        testSelectAns31 = 7777
    if test40count <= 31:
        testId32 = 777
        testQuestion32 = 7777
        testAnswer32 = 7777
        testSelectAns32 = 7777
    if test40count <= 32:
        testId33 = 777
        testQuestion33 = 7777
        testAnswer33 = 7777
        testSelectAns33 = 7777
    if test40count <= 33:
        testId34 = 7777
        testQuestion34 = 7777
        testAnswer34 = 7777
        testSelectAns34 = 7777
    if test40count <= 34:
        testId35 = 7777
        testQuestion35 = 7777
        testAnswer35 = 7777
        testSelectAns35 = 7777
    if test40count <= 35:
        testId36 = 7777
        testQuestion36 = 7777
        testAnswer36 = 7777
        testSelectAns36 = 7777
    if test40count <= 36:
        testId37 = 7777
        testQuestion37 = 7777
        testAnswer37 = 7777
        testSelectAns37 = 7777
    if test40count <= 37:
        testId38 = 7777
        testQuestion38 = 7777
        testAnswer38 = 7777
        testSelectAns38 = 7777
    if test40count <= 38:
        testId39 = 7777
        testQuestion39 = 7777
        testAnswer39 = 7777
        testSelectAns39 = 7777
    if test40count <= 39:
        testId40 = 7777
        testQuestion40 = 7777
        testAnswer40 = 7777
        testSelectAns40 = 7777

    if test40count == 1:
        testId1 = dQID
        testQuestion1 = dQQuestion
        testAnswer1 = dQAnswer
        testSelectAns1 = dQSelectAns
    if test40count == 2:
        testId2 = dQID
        testQuestion2 = dQQuestion
        testAnswer2 = dQAnswer
        testSelectAns2 = dQSelectAns
    if test40count == 3:
        testId3 = dQID
        testQuestion3 = dQQuestion
        testAnswer3 = dQAnswer
        testSelectAns3 = dQSelectAns
    if test40count == 4:
        testId4 = dQID
        testQuestion4 = dQQuestion
        testAnswer4 = dQAnswer
        testSelectAns4 = dQSelectAns
    if test40count == 5:
        testId5 = dQID
        testQuestion5 = dQQuestion
        testAnswer5 = dQAnswer
        testSelectAns5 = dQSelectAns
    if test40count == 6:
        testId6 = dQID
        testQuestion6 = dQQuestion
        testAnswer6 = dQAnswer
        testSelectAns6 = dQSelectAns
    if test40count == 7:
        testId7 = dQID
        testQuestion7 = dQQuestion
        testAnswer7 = dQAnswer
        testSelectAns7 = dQSelectAns
    if test40count == 8:
        testId8 = dQID
        testQuestion8 = dQQuestion
        testAnswer8 = dQAnswer
        testSelectAns8 = dQSelectAns
    if test40count == 9:
        testId9 = dQID
        testQuestion9 = dQQuestion
        testAnswer9 = dQAnswer
        testSelectAns9 = dQSelectAns
    if test40count == 10:
        testId10 = dQID
        testQuestion10 = dQQuestion
        testAnswer10 = dQAnswer
        testSelectAns10 = dQSelectAns

    if test40count == 11:
        testId11 = dQID
        testQuestion11 = dQQuestion
        testAnswer11 = dQAnswer
        testSelectAns11 = dQSelectAns
    if test40count == 12:
        testId12 = dQID
        testQuestion12 = dQQuestion
        testAnswer12 = dQAnswer
        testSelectAns12 = dQSelectAns
    if test40count == 13:
        testId13 = dQID
        testQuestion13 = dQQuestion
        testAnswer13 = dQAnswer
        testSelectAns13 = dQSelectAns
    if test40count == 14:
        testId14 = dQID
        testQuestion14 = dQQuestion
        testAnswer14 = dQAnswer
        testSelectAns14 = dQSelectAns
    if test40count == 15:
        testId15 = dQID
        testQuestion15 = dQQuestion
        testAnswer15 = dQAnswer
        testSelectAns15 = dQSelectAns
    if test40count == 16:
        testId16 = dQID
        testQuestion16 = dQQuestion
        testAnswer16 = dQAnswer
        testSelectAns16 = dQSelectAns
    if test40count == 17:
        testId17 = dQID
        testQuestion17 = dQQuestion
        testAnswer17 = dQAnswer
        testSelectAns17 = dQSelectAns
    if test40count == 18:
        testId18 = dQID
        testQuestion18 = dQQuestion
        testAnswer18 = dQAnswer
        testSelectAns18 = dQSelectAns
    if test40count == 19:
        testId19 = dQID
        testQuestion19 = dQQuestion
        testAnswer19 = dQAnswer
        testSelectAns19 = dQSelectAns
    if test40count == 20:
        testId20 = dQID
        testQuestion20 = dQQuestion
        testAnswer20 = dQAnswer
        testSelectAns20 = dQSelectAns

    if test40count == 21:
        testId21 = dQID
        testQuestion21 = dQQuestion
        testAnswer21 = dQAnswer
        testSelectAns21 = dQSelectAns
    if test40count == 22:
        testId22 = dQID
        testQuestion22 = dQQuestion
        testAnswer22 = dQAnswer
        testSelectAns22 = dQSelectAns
    if test40count == 23:
        testId23 = dQID
        testQuestion23 = dQQuestion
        testAnswer23 = dQAnswer
        testSelectAns23 = dQSelectAns
    if test40count == 24:
        testId24 = dQID
        testQuestion24 = dQQuestion
        testAnswer24 = dQAnswer
        testSelectAns24 = dQSelectAns
    if test40count == 25:
        testId25 = dQID
        testQuestion25 = dQQuestion
        testAnswer25 = dQAnswer
        testSelectAns25 = dQSelectAns
    if test40count == 26:
        testId26 = dQID
        testQuestion26 = dQQuestion
        testAnswer26 = dQAnswer
        testSelectAns26 = dQSelectAns
    if test40count == 27:
        testId27 = dQID
        testQuestion27 = dQQuestion
        testAnswer27 = dQAnswer
        testSelectAns27 = dQSelectAns
    if test40count == 28:
        testId28 = dQID
        testQuestion28 = dQQuestion
        testAnswer28 = dQAnswer
        testSelectAns28 = dQSelectAns
    if test40count == 29:
        testId29 = dQID
        testQuestion29 = dQQuestion
        testAnswer29 = dQAnswer
        testSelectAns29 = dQSelectAns
    if test40count == 30:
        testId30 = dQID
        testQuestion30 = dQQuestion
        testAnswer30 = dQAnswer
        testSelectAns30 = dQSelectAns

    if test40count == 31:
        testId31 = dQID
        testQuestion31 = dQQuestion
        testAnswer31 = dQAnswer
        testSelectAns31 = dQSelectAns
    if test40count == 32:
        testId32 = dQID
        testQuestion32 = dQQuestion
        testAnswer32 = dQAnswer
        testSelectAns32 = dQSelectAns
    if test40count == 33:
        testId33 = dQID
        testQuestion33 = dQQuestion
        testAnswer33 = dQAnswer
        testSelectAns33 = dQSelectAns
    if test40count == 34:
        testId34 = dQID
        testQuestion34 = dQQuestion
        testAnswer34 = dQAnswer
        testSelectAns34 = dQSelectAns
    if test40count == 35:
        testId35 = dQID
        testQuestion35 = dQQuestion
        testAnswer35 = dQAnswer
        testSelectAns35 = dQSelectAns
    if test40count == 36:
        testId36 = dQID
        testQuestion36 = dQQuestion
        testAnswer36 = dQAnswer
        testSelectAns36 = dQSelectAns
    if test40count == 37:
        testId37 = dQID
        testQuestion37 = dQQuestion
        testAnswer37 = dQAnswer
        testSelectAns37 = dQSelectAns
    if test40count == 38:
        testId38 = dQID
        testQuestion38 = dQQuestion
        testAnswer38 = dQAnswer
        testSelectAns38 = dQSelectAns
    if test40count == 39:
        testId39 = dQID
        testQuestion39 = dQQuestion
        testAnswer39 = dQAnswer
        testSelectAns39 = dQSelectAns
    if test40count == 40:
        testId40 = dQID
        testQuestion40 = dQQuestion
        testAnswer40 = dQAnswer
        testSelectAns40 = dQSelectAns

    testId = dQID

    if test40count == test40mondaisuu + 1 :
        userid = request.user.id
        TestRoutine.objects.create(user_id=userid, test_result=seikairitsu)#seikairitsuは文字列

     
    params = {
            'data': data,
            'dataQuestion': dataQuestion,
            'dataAnswer': dataAnswer,
            'dataWrongAnswer1': dataWrongAnswer1,
            'dataWrongAnswer2': dataWrongAnswer2,
            'dataWrongAnswer3': dataWrongAnswer3,
            'dataWrongAnswer4': dataWrongAnswer4,
            'dataExplanation': dataExplanation,
            'dataThumbnailQ1': dataThumbnailQ1,
            'dataThumbnailQ2': dataThumbnailQ2,
            'dataThumbnailQ3': dataThumbnailQ3,
            'dataThumbnailA1': dataThumbnailA1,
            'dataThumbnailA2': dataThumbnailA2,
            'dataThumbnailA3': dataThumbnailA3,
            'dataCategory': dataCategory,
            'd7_1_Answer':d7_1_Answer,
            'd7_2_Answer':d7_2_Answer,
            'd7_3_Answer':d7_3_Answer,
            'd7_4_Answer':d7_4_Answer,
            'd7_5_Answer':d7_5_Answer,
            #'data2pk3_1':data2pk3_1,
            'object_list':object_list,
            'test40count':test40count,
            'test40seikai':test40seikai,
            'testShokai' :"testNandomeka",
            'seikairitsu':seikairitsu,
            'test40mondaisuu':test40mondaisuu,
            'selectedAns':selectedAns,
            'testId1':testId1,
            'testId2':testId2,
            'testId3':testId3,
            'testId4':testId4,
            'testId5':testId5,
            'testId6':testId6,
            'testId7':testId7,
            'testId8':testId8,
            'testId9':testId9,
            'testId10':testId10,
            'testId':testId,

            'testId11':testId11,
            'testId12':testId12,
            'testId13':testId13,
            'testId14':testId14,
            'testId15':testId15,
            'testId16':testId16,
            'testId17':testId17,
            'testId18':testId18,
            'testId19':testId19,
            'testId20':testId20,

            'testId21':testId21,
            'testId22':testId22,
            'testId23':testId23,
            'testId24':testId24,
            'testId25':testId25,
            'testId26':testId26,
            'testId27':testId27,
            'testId28':testId28,
            'testId29':testId29,
            'testId30':testId30,

            'testId31':testId31,
            'testId32':testId32,
            'testId33':testId33,
            'testId34':testId34,
            'testId35':testId35,
            'testId36':testId36,
            'testId37':testId37,
            'testId38':testId38,
            'testId39':testId39,
            'testId40':testId40,

            'testQuestion1':testQuestion1,
            'testQuestion2':testQuestion2,
            'testQuestion3':testQuestion3,
            'testQuestion4':testQuestion4,
            'testQuestion5':testQuestion5,
            'testQuestion6':testQuestion6,
            'testQuestion7':testQuestion7,
            'testQuestion8':testQuestion8,
            'testQuestion9':testQuestion9,
            'testQuestion10':testQuestion10,

            'testQuestion11':testQuestion11,
            'testQuestion12':testQuestion12,
            'testQuestion13':testQuestion13,
            'testQuestion14':testQuestion14,
            'testQuestion15':testQuestion15,
            'testQuestion16':testQuestion16,
            'testQuestion17':testQuestion17,
            'testQuestion18':testQuestion18,
            'testQuestion19':testQuestion19,
            'testQuestion20':testQuestion20,

            'testQuestion21':testQuestion21,
            'testQuestion22':testQuestion22,
            'testQuestion23':testQuestion23,
            'testQuestion24':testQuestion24,
            'testQuestion25':testQuestion25,
            'testQuestion26':testQuestion26,
            'testQuestion27':testQuestion27,
            'testQuestion28':testQuestion28,
            'testQuestion29':testQuestion29,
            'testQuestion30':testQuestion30,

            'testQuestion31':testQuestion31,
            'testQuestion32':testQuestion32,
            'testQuestion33':testQuestion33,
            'testQuestion34':testQuestion34,
            'testQuestion35':testQuestion35,
            'testQuestion36':testQuestion36,
            'testQuestion37':testQuestion37,
            'testQuestion38':testQuestion38,
            'testQuestion39':testQuestion39,
            'testQuestion40':testQuestion40,

            'testAnswer1':testAnswer1,
            'testAnswer2':testAnswer2,
            'testAnswer3':testAnswer3,
            'testAnswer4':testAnswer4,
            'testAnswer5':testAnswer5,
            'testAnswer6':testAnswer6,
            'testAnswer7':testAnswer7,
            'testAnswer8':testAnswer8,
            'testAnswer9':testAnswer9,
            'testAnswer10':testAnswer10,

            'testAnswer11':testAnswer11,
            'testAnswer12':testAnswer12,
            'testAnswer13':testAnswer13,
            'testAnswer14':testAnswer14,
            'testAnswer15':testAnswer15,
            'testAnswer16':testAnswer16,
            'testAnswer17':testAnswer17,
            'testAnswer18':testAnswer18,
            'testAnswer19':testAnswer19,
            'testAnswer20':testAnswer20,

            'testAnswer21':testAnswer21,
            'testAnswer22':testAnswer22,
            'testAnswer23':testAnswer23,
            'testAnswer24':testAnswer24,
            'testAnswer25':testAnswer25,
            'testAnswer26':testAnswer26,
            'testAnswer27':testAnswer27,
            'testAnswer28':testAnswer28,
            'testAnswer29':testAnswer29,
            'testAnswer30':testAnswer30,

            'testAnswer31':testAnswer31,
            'testAnswer32':testAnswer32,
            'testAnswer33':testAnswer33,
            'testAnswer34':testAnswer34,
            'testAnswer35':testAnswer35,
            'testAnswer36':testAnswer36,
            'testAnswer37':testAnswer37,
            'testAnswer38':testAnswer38,
            'testAnswer39':testAnswer39,
            'testAnswer40':testAnswer40,

            'testSelectAns1':testSelectAns1,
            'testSelectAns2':testSelectAns2,
            'testSelectAns3':testSelectAns3,
            'testSelectAns4':testSelectAns4,
            'testSelectAns5':testSelectAns5,
            'testSelectAns6':testSelectAns6,
            'testSelectAns7':testSelectAns7,
            'testSelectAns8':testSelectAns8,
            'testSelectAns9':testSelectAns9,
            'testSelectAns10':testSelectAns10,

            'testSelectAns11':testSelectAns11,
            'testSelectAns12':testSelectAns12,
            'testSelectAns13':testSelectAns13,
            'testSelectAns14':testSelectAns14,
            'testSelectAns15':testSelectAns15,
            'testSelectAns16':testSelectAns16,
            'testSelectAns17':testSelectAns17,
            'testSelectAns18':testSelectAns18,
            'testSelectAns19':testSelectAns19,
            'testSelectAns20':testSelectAns20,

            'testSelectAns21':testSelectAns21,
            'testSelectAns22':testSelectAns22,
            'testSelectAns23':testSelectAns23,
            'testSelectAns24':testSelectAns24,
            'testSelectAns25':testSelectAns25,
            'testSelectAns26':testSelectAns26,
            'testSelectAns27':testSelectAns27,
            'testSelectAns28':testSelectAns28,
            'testSelectAns29':testSelectAns29,
            'testSelectAns30':testSelectAns30,

            'testSelectAns31':testSelectAns31,
            'testSelectAns32':testSelectAns32,
            'testSelectAns33':testSelectAns33,
            'testSelectAns34':testSelectAns34,
            'testSelectAns35':testSelectAns35,
            'testSelectAns36':testSelectAns36,
            'testSelectAns37':testSelectAns37,
            'testSelectAns38':testSelectAns38,
            'testSelectAns39':testSelectAns39,
            'testSelectAns40':testSelectAns40,
            'testes': testes,
            'selectCategory': selectCategory,
            'selCatKakutei': selCatKakutei,
            'pks_list': pks_list,
    }

    if test40count == test40mondaisuu + 1 :
        return render(request, 'sqlapp/question_test5taku_result40.html', params)
    else:
        return render(request, 'sqlapp/question_test5taku_40.html', params)


class DetailQuestionView(DetailView):
    object_list = Practice.objects.all()
    template_name = 'sqlapp/question_detail.html'
    model = Practice

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Practice.objects.all()

        #カテゴリータブの関数を呼び出す
        categories_data = get_categories_data()
        context['categories_data'] = categories_data

        categories = Category.objects.all()
        context['categories'] = categories

        return context



class CreateQuestionView(CreateView):
    object_list = Practice.objects.all()
    template_name = 'sqlapp/question_create.html'
    form_class = QuestionForm
    model = Practice
    success_url = reverse_lazy('create-question')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Practice.objects.all()
        shoseki_list = Practice.objects.values_list('shoseki', flat=True)
        context['shoseki'] = Book.objects.all()
        
        """
        touroku1tsumae = Practice.objects.all().last()
        if touroku1tsumae:
            touroku1tsumaeShoseki = touroku1tsumae.shoseki
            touroku1tsumaeQuestion = touroku1tsumae.question
            touroku1tsumaeAnswer = touroku1tsumae.answer
            touroku1tsumaePage = touroku1tsumae.shoseki_page
            touroku1tsumaeId = touroku1tsumae.id
            context['touroku1tsumaeShoseki'] = touroku1tsumaeShoseki
            context['touroku1tsumaeQuestion'] = touroku1tsumaeQuestion
            context['touroku1tsumaeAnswer'] = touroku1tsumaeAnswer
            context['touroku1tsumaePage'] = touroku1tsumaePage
            context['touroku1tsumaeId'] = touroku1tsumaeId 
            """


        # 各モデルから最新のレコードを取得
        latest_practice = Practice.objects.order_by('-created_at').first()
        latest_practice_choice = PracticeChoice.objects.order_by('-created_at').first()
        latest_code_practice = Codepractice.objects.order_by('-created_at').first()
        # 最新のレコードを見つける
        latest_record = max(
            (latest_practice, latest_practice_choice, latest_code_practice),
            key=lambda x: x.created_at if x else None
        )
        # 最新のレコードに基づいてコンテキストを更新
        if latest_record:
            context['touroku1tsumaeShoseki'] = latest_record.shoseki
            context['touroku1tsumaePage'] = latest_record.shoseki_page
            # PracticeChoiceとCodepracticeの処理
            if isinstance(latest_record, Codepractice):
                context['touroku1tsumaeQuestion'] = latest_record.question1
            else:
                context['touroku1tsumaeQuestion'] = latest_record.question
            context['touroku1tsumaeId'] = latest_record.id
        else:
            context['touroku1tsumaeShoseki'] = None
            context['touroku1tsumaeQuestion'] = None
            context['touroku1tsumaePage'] = None
            context['touroku1tsumaeId'] = None



        context['tourokugoNew'] = ""
        #today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).astimezone()

        #カテゴリータブの関数を呼び出す
        categories_data = get_categories_data()
        categories = Category.objects.all()
        context['categories_data'] = categories_data
        context['categories'] = categories


        return context
    
    
    
    def get(self, request, *args, **kwargs):
        self.object = Practice()

        context = self.get_context_data(**kwargs)

        
        dataFirst1 = ""
        dataFirst1_page = ""
        dataFirst1_shoseki = ""

        dataFirst2 = ""
        dataFirst2_page = ""
        dataFirst2_shoseki = ""   

        dataFirst3 = ""
        dataFirst3_page = ""
        dataFirst3_shoseki = ""

        dataFirst4 = ""
        dataFirst4_page = ""
        dataFirst4_shoseki = ""
        context['kategory'] = ""

        nextReg = ""
        nextShoseki = ""
        nextQuestion = ""
        nextCategory = ""
        nextSho_page = ""
        
        if request.GET.get('nameFind'):
            data = Practice.objects.all().order_by('pk').reverse().filter(question__contains=find1,answer__contains=find2)
            dataFirst1 = Practice.objects.all().order_by('pk').reverse().first()
            dataFirst1_page = dataFirst1.shoseki_page
            dataFirst1_shoseki = dataFirst1.shoseki
            dataFirst2 = Practice.objects.all().order_by('pk').reverse().first()
            dataFirst2_page = dataFirst2.shoseki_page
            dataFirst2_shoseki = dataFirst2.shoseki
            dataFirst3 = Practice.objects.all().order_by('pk').reverse().first()
            dataFirst3_page = dataFirst3.shoseki_page
            dataFirst3_shoseki = dataFirst3.shoseki
            selectColor = ""

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki

            context['dataFirst4'] = dataFirst4
            context['dataFirst4_page'] = dataFirst4_page
            context['dataFirst4_shoseki'] = dataFirst4_shoseki
        
            
        else:
            dataFirst1 = Practice.objects.all().order_by('pk').reverse().first()
            dataFirst1_page = ""
            dataFirst1_shoseki = ""
            dataFirst2 = Practice.objects.all().order_by('pk').reverse().first()
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = Practice.objects.all().order_by('pk').reverse().first()
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            dataFirst4 = Practice.objects.all().order_by('pk').reverse().first()
            dataFirst4_page = ""
            dataFirst4_shoseki = ""
       
        context['shosekiSakuseigo'] = ""
        context['kateSakuseigo'] = ""
        context['tourokugoNew'] = "tourokumae"
        
        
        return self.render_to_response(context)
  
    def form_valid(self, form, **kwargs):
        form.instance.user = self.request.user

        new_shoseki_name = form.cleaned_data.get('new_shoseki')
        if new_shoseki_name:
            shoseki, created = Book.objects.get_or_create(name=new_shoseki_name)
            form.instance.shoseki = shoseki

        return super().form_valid(form)



def get_previous_registration_data(request):
    shoseki_id = request.GET.get('shoseki')
    if shoseki_id:
        touroku1tsumae = Practice.objects.filter(shoseki_id=shoseki_id).order_by('-id').first()
        #touroku1tsumaeChoice = PracticeChoice.objects.filter(shoseki_id=shoseki_id).order_by('-id').first()
        if touroku1tsumae:
            data = {
                'touroku1tsumaeShoseki': touroku1tsumae.shoseki.name,  # または適切な属性
                'touroku1tsumaeQuestion': touroku1tsumae.question,
                'touroku1tsumaePage': touroku1tsumae.shoseki_page,
                'touroku1tsumaeId': touroku1tsumae.id
            }
        else:
            data = {'message': 'No data found for the selected shoseki'}
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'No shoseki provided'})
       

class DeleteQuestionView(DeleteView):
    object_list = Practice.objects.all()
    template_name = 'sqlapp/question_confirm_delete.html'
    model = Practice
    success_url = reverse_lazy('list-question')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_data = get_categories_data()
        context['categories_data'] = categories_data
        categories = Category.objects.all()
        context['categories'] = categories
        return context


class UpdateQuestionView(UpdateView):
    model = Practice
    template_name = 'sqlapp/question_update.html'
    form_class = QuestionForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        return obj

    def get_success_url(self):
        return reverse('detail-question', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_data = get_categories_data()
        context['categories_data'] = categories_data
        categories = Category.objects.all()
        context['categories'] = categories
        return context


import pandas as pd

def ListDataframeView(request):
    object_list = Practice.objects.order_by('-id')

    if (request.method == 'POST'):

        allList = pd.DataFrame(Practice.objects.all().values()).head().to_html()
        result=ataframe.kkkk(request)

        params = {
            'allList': allList,
            'result': result
        }
        return render(request, 'sqlapp/dataframe.html', params)

    if (request.method == 'GET'):

        allList = pd.DataFrame(Practice.objects.all()[:5].values()).to_html()
        
        params = {
            'allList': allList
        }
        return render(request, 'sqlapp/dataframe.html', params)


#12/30
def ListQuestionChoiceView(request, num=1):

    data = PracticeChoice.objects.all().order_by('pk').reverse()
    dataFirst = PracticeChoice.objects.all().order_by('pk').reverse().first()



    data2 = PracticeChoice.objects.all().order_by('pk').reverse()
   
    
    page = Paginator(data2, 10)

    #カテゴリータブの関数を呼び出す
    categories_data = get_categories_data()
    categories = Category.objects.all()
    
    params = {
            'title': '',
            #'form': form,
            'data': data,
            'data2': page.get_page(num),
            'dataFirst': dataFirst,
            'categories_data': categories_data,
            'categories': categories
    }
    return render(request, 'sqlapp/question_choice_list.html', params)


class CreateQuestionChoiceView(CreateView):
    object_list = PracticeChoice.objects.all()
    template_name = 'sqlapp/question_choice_create.html'
    form_class = QuestionChoiceForm
    model = PracticeChoice
    success_url = reverse_lazy('create-question-choice')

    categories = Category.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = PracticeChoice.objects.all()

        # PracticeChoiceのデータの有無をチェック
        if not data.exists():
            context['no_data_message'] = _("選択問題のデータの登録がありません")
        else:
            context['data'] = data

        context['data'] = PracticeChoice.objects.all()
        shoseki_list = PracticeChoice.objects.values_list('shoseki', flat=True)
        context['shoseki'] = Book.objects.all()
        
        """
        touroku1tsumae = PracticeChoice.objects.all().last()
        if touroku1tsumae:
            touroku1tsumaeShoseki = touroku1tsumae.shoseki
            touroku1tsumaeQuestion = touroku1tsumae.question
            touroku1tsumaeAnswer = touroku1tsumae.answer
            touroku1tsumaePage = touroku1tsumae.shoseki_page
            touroku1tsumaeId = touroku1tsumae.id
            context['touroku1tsumaeShoseki'] = touroku1tsumaeShoseki
            context['touroku1tsumaeQuestion'] = touroku1tsumaeQuestion
            context['touroku1tsumaeAnswer'] = touroku1tsumaeAnswer
            context['touroku1tsumaePage'] = touroku1tsumaePage
            context['touroku1tsumaeId'] = touroku1tsumaeId 
            """

        # 各モデルから最新のレコードを取得
        latest_practice = Practice.objects.order_by('-created_at').first()
        latest_practice_choice = PracticeChoice.objects.order_by('-created_at').first()
        latest_code_practice = Codepractice.objects.order_by('-created_at').first()
        # 最新のレコードを見つける
        latest_record = max(
            (latest_practice, latest_practice_choice, latest_code_practice),
            key=lambda x: x.created_at if x else None
        )
        # 最新のレコードに基づいてコンテキストを更新
        if latest_record:
            context['touroku1tsumaeShoseki'] = latest_record.shoseki
            context['touroku1tsumaePage'] = latest_record.shoseki_page
            # PracticeChoiceとCodepracticeの処理
            if isinstance(latest_record, Codepractice):
                context['touroku1tsumaeQuestion'] = latest_record.question1
            else:
                context['touroku1tsumaeQuestion'] = latest_record.question
            context['touroku1tsumaeId'] = latest_record.id
        else:
            context['touroku1tsumaeShoseki'] = None
            context['touroku1tsumaeQuestion'] = None
            context['touroku1tsumaePage'] = None
            context['touroku1tsumaeId'] = None

        context['tourokugoNew'] = ""
        #today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).astimezone()
        
        return context
  
    def get(self, request, *args, **kwargs):
        self.object = PracticeChoice()

        context = self.get_context_data(**kwargs)

        categories = Category.objects.all()
        
        #カテゴリータブの関数を呼び出す
        categories_data = get_categories_data()
        categories = Category.objects.all()

        context['categories_data'] = categories_data
        context['categories'] = categories

        #context['categories'] = categories
        
        
        return self.render_to_response(context)
    


    def form_valid(self, form, **kwargs):
        #form.instance.user = self.request.user
        return super().form_valid(form) 


class UpdateQuestionChoiceView(UpdateView):
    model = PracticeChoice
    template_name = 'sqlapp/question_choice_update.html'
    form_class = QuestionChoiceForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        return obj

    def get_success_url(self):
        return reverse('detail-question-choice', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_data = get_categories_data()
        context['categories_data'] = categories_data
        categories = Category.objects.all()
        context['categories'] = categories
        return context


class DeleteQuestionChoiceView(DeleteView):
    object_list = PracticeChoice.objects.all()
    template_name = 'sqlapp/question_choice_confirm_delete.html'
    model = PracticeChoice
    success_url = reverse_lazy('list-question-choice')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_data = get_categories_data()
        context['categories_data'] = categories_data
        categories = Category.objects.all()
        context['categories'] = categories
        return context


class DetailQuestionChoiceView(DetailView):
    object_list = PracticeChoice.objects.all()
    template_name = 'sqlapp/question_choice_detail.html'
    model = PracticeChoice

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = PracticeChoice.objects.all()

        #カテゴリータブの関数を呼び出す
        categories_data = get_categories_data()
        context['categories_data'] = categories_data

        categories = Category.objects.all()
        context['categories'] = categories

        return context




#1/2 memopractice
def ListCodepracticeView(request, num=1):
    if Codepractice.objects.exists():
        data = Codepractice.objects.all().order_by('pk').reverse()
        dataFirst = Codepractice.objects.all().order_by('pk').reverse().first()
    selectColor = ""
    dataFirst1 = ""
    dataFirst2 = ""
    dataFirst3 = ""
    dataFirst4 = ""
    dataFirst1_page = ""
    dataFirst2_page = ""
    dataFirst3_page = ""
    dataFirst4_page = ""
    dataFirst1_shoseki = ""
    dataFirst2_shoseki = ""
    dataFirst3_shoseki = ""
    dataFirst4_shoseki = ""

    data2 = Codepractice.objects.all().order_by('pk').reverse()
    

    if (request.method == 'POST') and request.POST.get('nameFind'):
            form = FindForm(request.POST)
            find1 = request.POST.get('find1')
            find2 = request.POST.get('find2')
            find3 = request.POST.get('find3')
            #today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).astimezone()
            data = Practice.objects.all().order_by('pk').reverse().filter(question__contains=find1,answer__contains=find2,shoseki__name__contains=find3)
            data2 = Practice.objects.all().order_by('pk').reverse().filter(question__contains=find1,answer__contains=find2,shoseki__name__contains=find3)
            dataFirst1 = Practice.objects.all().order_by('pk').reverse().first()
            dataFirst1_page = dataFirst1.shoseki_page
            dataFirst1_shoseki = dataFirst1.shoseki
            dataFirst2 = Practice.objects.all().order_by('pk').reverse().first()
            dataFirst2_page = dataFirst2.shoseki_page
            dataFirst2_shoseki = dataFirst2.shoseki
            dataFirst3 = Practice.objects.all().order_by('pk').reverse().first()
            dataFirst3_page = dataFirst3.shoseki_page
            dataFirst3_shoseki = dataFirst3.shoseki
            selectColor = ""
    else:
        form = FindForm()
        data = Codepractice.objects.all().order_by('pk').reverse()

        dataFirst = ""
        dataFirst1 = ""
        dataFirst2 = ""
        dataFirst3 = ""
        dataFirst1_page = ""
        dataFirst2_page = ""
        dataFirst3_page = ""
        
        #today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).astimezone()
        

    
    page = Paginator(data2, 10)

    #カテゴリータブの関数を呼び出す
    categories_data = get_categories_data()
    categories = Category.objects.all()
    
    params = {
            'title': '',
            'form': form,
            'data': data,
            'data2': page.get_page(num),
            'dataFirst': dataFirst,
            'dataFirst1': dataFirst1,
            'dataFirst2': dataFirst2,
            'dataFirst3': dataFirst3,
            'dataFirst1_page': dataFirst1_page,
            'dataFirst2_page': dataFirst2_page,
            'dataFirst3_page': dataFirst3_page,
            'dataFirst1_shoseki': dataFirst1_shoseki,
            'dataFirst2_shoseki': dataFirst2_shoseki,
            'dataFirst3_shoseki': dataFirst3_shoseki,
            'categories_data': categories_data,
            'categories': categories
            
    }
    return render(request, 'sqlapp/codepractice_list.html', params)


class DetailCodepracticeView(DetailView):
    object_list = Codepractice.objects.all()
    template_name = 'sqlapp/codepractice_detail.html'
    model = Codepractice

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.object
        context['data'] = Codepractice.objects.all()
        context['range1_4'] = range(1, 4)
        context['range1_6'] = range(1, 6)
        context['range1_11'] = range(1, 11)
        questions = [getattr(obj, f'question{i}', None) for i in range(1, 4)]
        reqs = [getattr(obj, f'req{i}', None) for i in range(1, 4)]
        answers = [getattr(obj, f'answer{i}', None) for i in range(1, 6)]
        thumbnailsQ = [getattr(obj, f'thumbnailQ{i}', None) for i in range(1, 12)]
        thumbnailsQ = [getattr(obj, f'thumbnailA{i}', None) for i in range(1, 12)]
        context['questions'] = questions
        context['reqs'] = reqs
        context['answers'] = answers
        context['thumbnailsQ'] = thumbnailsQ
        context['thumbnailsQ'] = thumbnailsQ

        #カテゴリータブの関数を呼び出す
        categories_data = get_categories_data()
        context['categories_data'] = categories_data

        categories = Category.objects.all()
        context['categories'] = categories

        return context



class CreateCodepracticeView(CreateView):
    object_list = Codepractice.objects.all()
    template_name = 'sqlapp/codepractice_create.html'
    form_class = CodePracticeForm
    model = Codepractice
    success_url = reverse_lazy('create-codepractice')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Codepractice.objects.all()
        shoseki_list = Codepractice.objects.values_list('shoseki', flat=True)
        context['shoseki'] = Book.objects.all()
        
        """
        touroku1tsumae = Codepractice.objects.all().last()
        if touroku1tsumae:
            touroku1tsumaeShoseki = touroku1tsumae.shoseki
            touroku1tsumaeQuestion1 = touroku1tsumae.question1
            touroku1tsumaeQuestion2 = touroku1tsumae.question2
            touroku1tsumaeQuestion3 = touroku1tsumae.question3
            touroku1tsumaeAnswer1 = touroku1tsumae.answer1
            touroku1tsumaeAnswer2 = touroku1tsumae.answer2
            touroku1tsumaeAnswer3 = touroku1tsumae.answer3
            touroku1tsumaeAnswer4 = touroku1tsumae.answer4
            touroku1tsumaeAnswer5 = touroku1tsumae.answer5
            touroku1tsumaePage = touroku1tsumae.shoseki_page
            touroku1tsumaeId = touroku1tsumae.id
            context['touroku1tsumaeShoseki'] = touroku1tsumaeShoseki
            context['touroku1tsumaeQuestion1'] = touroku1tsumaeQuestion1
            context['touroku1tsumaeQuestion2'] = touroku1tsumaeQuestion2
            context['touroku1tsumaeQuestion3'] = touroku1tsumaeQuestion3
            context['touroku1tsumaeAnswer1'] = touroku1tsumaeAnswer1
            context['touroku1tsumaeAnswer2'] = touroku1tsumaeAnswer2
            context['touroku1tsumaeAnswer3'] = touroku1tsumaeAnswer3
            context['touroku1tsumaeAnswer4'] = touroku1tsumaeAnswer4
            context['touroku1tsumaeAnswer5'] = touroku1tsumaeAnswer5
            context['touroku1tsumaePage'] = touroku1tsumaePage
            context['touroku1tsumaeId'] = touroku1tsumaeId 
            """

        # 各モデルから最新のレコードを取得
        latest_practice = Practice.objects.order_by('-created_at').first()
        latest_practice_choice = PracticeChoice.objects.order_by('-created_at').first()
        latest_code_practice = Codepractice.objects.order_by('-created_at').first()
        # 最新のレコードを見つける
        latest_record = max(
            (latest_practice, latest_practice_choice, latest_code_practice),
            key=lambda x: x.created_at if x else None
        )
        # 最新のレコードに基づいてコンテキストを更新
        if latest_record:
            context['touroku1tsumaeShoseki'] = latest_record.shoseki
            context['touroku1tsumaePage'] = latest_record.shoseki_page
            # PracticeChoiceとCodepracticeの処理
            if isinstance(latest_record, Codepractice):
                context['touroku1tsumaeQuestion'] = latest_record.question1
            else:
                context['touroku1tsumaeQuestion'] = latest_record.question
            context['touroku1tsumaeId'] = latest_record.id
        else:
            context['touroku1tsumaeShoseki'] = None
            context['touroku1tsumaeQuestion'] = None
            context['touroku1tsumaePage'] = None
            context['touroku1tsumaeId'] = None
        
        context['tourokugoNew'] = ""
        #today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).astimezone()
        
        #カテゴリータブの関数を呼び出す
        categories_data = get_categories_data()
        categories = Category.objects.all()
        context['categories_data'] = categories_data
        context['categories'] = categories

        return context
    
    
    
    def get(self, request, *args, **kwargs):
        self.object = Codepractice()

        context = self.get_context_data(**kwargs)

        
        dataFirst1 = ""
        dataFirst1_page = ""
        dataFirst1_shoseki = ""

        dataFirst2 = ""
        dataFirst2_page = ""
        dataFirst2_shoseki = ""   

        dataFirst3 = ""
        dataFirst3_page = ""
        dataFirst3_shoseki = ""

        dataFirst4 = ""
        dataFirst4_page = ""
        dataFirst4_shoseki = ""
        context['kategory'] = ""

        nextReg = ""
        nextShoseki = ""
        nextQuestion = ""
        nextCategory = ""
        nextSho_page = ""
        
        if request.GET.get('nameFind'):
            data = Codepractice.objects.all().order_by('pk').reverse().filter(question1__contains=find1,answer1__contains=find2)
            dataFirst1 = Codepractice.objects.all().order_by('pk').reverse().first()
            dataFirst1_page = dataFirst1.shoseki_page
            dataFirst1_shoseki = dataFirst1.shoseki
            dataFirst2 = Codepractice.objects.all().order_by('pk').reverse().first()
            dataFirst2_page = dataFirst2.shoseki_page
            dataFirst2_shoseki = dataFirst2.shoseki
            dataFirst3 = Codepractice.objects.all().order_by('pk').reverse().first()
            dataFirst3_page = dataFirst3.shoseki_page
            dataFirst3_shoseki = dataFirst3.shoseki
            selectColor = ""

            context['fromList'] = "nashi"
            context['dataFirst1'] = dataFirst1
            context['dataFirst1_page'] = dataFirst1_page
            context['dataFirst1_shoseki'] = dataFirst1_shoseki
            
            context['dataFirst2'] = dataFirst2
            context['dataFirst2_page'] = dataFirst2_page
            context['dataFirst2_shoseki'] = dataFirst2_shoseki
            
            context['dataFirst3'] = dataFirst3
            context['dataFirst3_page'] = dataFirst3_page
            context['dataFirst3_shoseki'] = dataFirst3_shoseki

            context['dataFirst4'] = dataFirst4
            context['dataFirst4_page'] = dataFirst4_page
            context['dataFirst4_shoseki'] = dataFirst4_shoseki
        
            
        else:
            dataFirst1 = Codepractice.objects.all().order_by('pk').reverse().first()
            dataFirst1_page = ""
            dataFirst1_shoseki = ""
            dataFirst2 = Codepractice.objects.all().order_by('pk').reverse().first()
            dataFirst2_page = ""
            dataFirst2_shoseki = ""
            dataFirst3 = Codepractice.objects.all().order_by('pk').reverse().first()
            dataFirst3_page = ""
            dataFirst3_shoseki = ""
            dataFirst4 = Codepractice.objects.all().order_by('pk').reverse().first()
            dataFirst4_page = ""
            dataFirst4_shoseki = ""
       
        context['shosekiSakuseigo'] = ""
        context['kateSakuseigo'] = ""
        context['tourokugoNew'] = "tourokumae"
        
        
        return self.render_to_response(context)
  
    def form_valid(self, form, **kwargs):
        form.instance.user = self.request.user

        new_shoseki_name = form.cleaned_data.get('new_shoseki')
        if new_shoseki_name:
            shoseki, created = Book.objects.get_or_create(name=new_shoseki_name)
            form.instance.shoseki = shoseki

        return super().form_valid(form)



def get_previous_registration_data(request):
    shoseki_id = request.GET.get('shoseki')
    if shoseki_id:
        touroku1tsumae = Practice.objects.filter(shoseki_id=shoseki_id).order_by('-id').first()
        touroku1tsumaeChoice = PracticeChoice.objects.filter(shoseki_id=shoseki_id).order_by('-id').first()
        touroku1tsumaeCodepractice = Codepractice.objects.filter(shoseki_id=shoseki_id).order_by('-id').first()
        if touroku1tsumae:
            data = {
                'touroku1tsumaeShoseki': touroku1tsumae.shoseki.name,  # または適切な属性
                'touroku1tsumaeQuestion': touroku1tsumae.question,
                'touroku1tsumaePage': touroku1tsumae.shoseki_page,
                'touroku1tsumaeId': touroku1tsumae.id
            }
        else:
            data = {}
        return JsonResponse(data)

        if touroku1tsumaeChoice:
            dataChoice = {
                'touroku1tsumaeShosekiChoice': touroku1tsumaeChoice.shoseki.name,  # または適切な属性
                'touroku1tsumaeQuestionChoice': touroku1tsumaeChoice.question,
                'touroku1tsumaePageChoice': touroku1tsumaeChoice.shoseki_page,
                'touroku1tsumaeIdChoice': touroku1tsumaeChoice.id
            }
        else:
            dataChoice = {}
        return JsonResponse(dataChoice)

    else:
        return JsonResponse({'error': 'No shoseki provided'}, status=400)



class DeleteCodepracticeView(DeleteView):
    object_list = Codepractice.objects.all()
    template_name = 'sqlapp/codepractice_confirm_delete.html'
    model = Codepractice
    success_url = reverse_lazy('list-codepractice')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_data = get_categories_data()
        context['categories_data'] = categories_data
        categories = Category.objects.all()
        context['categories'] = categories
        return context


class UpdateCodepracticeView(UpdateView):
    model = Codepractice
    template_name = 'sqlapp/codepractice_update.html'
    form_class = CodePracticeForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        return obj

    def get_success_url(self):
        return reverse('detail-codepractice', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_data = get_categories_data()
        context['categories_data'] = categories_data
        categories = Category.objects.all()
        context['categories'] = categories
        return context




def execute_pandas_code(code):
    # 安全でないため、本番環境では絶対に使用しないでください。
    locals = {}
    exec(code, globals(), locals)
    return locals['result']  # 'result'変数に結果を格納することを期待


def sql_view(request):
    form = SQLForm()
    data = None
    html_data = None  # HTML形式のデータを保持する変数

    #カテゴリータブの関数を呼び出す
    categories_data = get_categories_data()
    categories = Category.objects.all()

    if request.method == 'POST':
        form = SQLForm(request.POST)
        if form.is_valid():
            mode = form.cleaned_data['mode']
            #query = form.cleaned_data['query']
            user_code = form.cleaned_data['query']
            try:
                if mode == 'sql':
                    #data = pd.read_sql_query(query, connection)
                    df = pd.read_sql_query(user_code, connection)
                    #html_data = data.to_html()  # DataFrameをHTMLに変換
                    html_data = df.to_html()  # DataFrameをHTMLに変換
                elif mode == 'pandas':
                    #exec(query)
                    #data = locals()['result']
                    #html_data = data.to_html() if isinstance(data, pd.DataFrame) else str(data)

                    # Pandas DataFrameモードの場合の処理
                    data2 = pd.DataFrame(Practice.objects.all().values())
                    df = pd.DataFrame(data2)


                    dataPractice = pd.DataFrame(Practice.objects.all().values())
                    sqlapp_practice = pd.DataFrame(dataPractice)
                    dataPracticeChoice = pd.DataFrame(PracticeChoice.objects.all().values())
                    sqlapp_practicechoice = pd.DataFrame(dataPracticeChoice)
                    dataCodepractice = pd.DataFrame(Codepractice.objects.all().values())
                    sqlapp_codepractice = pd.DataFrame(dataCodepractice)


                    inputCode = eval(user_code)  # ユーザーが入力したコードの実行
                    html_data = inputCode.to_html()  # DataFrameをHTMLに変換
            
            
            except Exception as e:
                #data = str(e)
                html_data = f'エラーが発生しました: {e}'
    return render(request, 'sqlapp/sql_view.html', {'form': form, 'data': html_data, 'categories_data': categories_data, 'categories': categories})



def update_quota(request, category_id):
    if request.method == 'POST':
        form = QuotaForm(request.POST)
        if form.is_valid():
            quota = form.save(commit=False)
            quota.category_id = category_id
            quota.save()
    return redirect('create-question-choice')


# 1/8 カテゴリータブ
def get_categories_data():
    categories = Category.objects.all()
    today = timezone.now().date()
    categories_data = []

    for category in categories:
        today_count_practice = Practice.objects.filter(
            category=category,
            created_at__date=today
        ).count()

        today_count_practicechoice = PracticeChoice.objects.filter(
            category=category,
            created_at__date=today
        ).count()

        today_count_codepractice = Codepractice.objects.filter(
            category=category,
            created_at__date=today
        ).count()

        today_count = today_count_practice + today_count_practicechoice + today_count_codepractice

        quota = Quota.objects.filter(category=category).first()
        target_count = quota.target_count if quota else 0

        categories_data.append({
            'category': category,
            'today_count': today_count,
            'target_count': target_count
        })

    return categories_data


def quiz_view(request):
    # 最新の問題を取得
    latest_question = Codepractice.objects.latest('created_at')

    categories_data = get_categories_data()
    categories = Category.objects.all()

    # question1からquestion3までのデータを取得
    questions_data = {
        'question1': latest_question.question1,
        'question2': latest_question.question2,
        'question3': latest_question.question3,
        'answer1': latest_question.answer1,
        'answer2': latest_question.answer2,
        'answer3': latest_question.answer3,
        'answer4': latest_question.answer4,
        'answer5': latest_question.answer5,

        'answerTitle1': latest_question.answerTitle1,
        'answerTitle2': latest_question.answerTitle2,
        'answerTitle3': latest_question.answerTitle3,
        'answerTitle4': latest_question.answerTitle4,
        'answerTitle5': latest_question.answerTitle5,
        

    }

    form1 = CodePracticeSlickForm1(instance=latest_question)
    form2 = CodePracticeSlickForm2(instance=latest_question)
    form3 = CodePracticeSlickForm3(instance=latest_question)
    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'questions': questions_data,
        'answer_range': range(1, 6),
        'categories_data': categories_data,
        'categories': categories
    }
    return render(request, 'sqlapp/codepractice_test.html', context)  # テンプレートのパスを調整
