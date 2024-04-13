from django.urls import path

from .views import get_previous_registration_data

from . import views

urlpatterns = [
    path('random/', views.questionRandom, name='questionRandom'),
    path('random10/', views.questionRandom10, name='questionRandom10'),
    path('random20/', views.questionRandom20, name='questionRandom20'),
    path('random30/', views.questionRandom30, name='questionRandom30'),
    path('random/result/', views.answerResult, name='answer-result'),

    path('<int:pk>/each/', views.EachQuestionView, name='each-question'),
    path('<int:pk>/each10/', views.EachQuestionView10, name='each-question10'),
    path('<int:pk>/each20/', views.EachQuestionView20, name='each-question20'),
    path('<int:pk>/each30/', views.EachQuestionView30, name='each-question30'),


    path('', views.ListQuestionView, name='list-question'),
    #path('<int:num>', views.ListQuestionView, name='list-question'),

    path('test/', views.testQuestionView, name='test-question'),
    path('test/50/', views.testQuestionView50, name='test-question50'),
    path('test/10/', views.testQuestionView10, name='test-question10'),
    path('test/4_10/', views.testQuestionView4taku_10, name='test-question4-10'),
    path('test/5_40/', views.testQuestionView5taku_40, name='test-question5-40'),

    path('<int:pk>/detail/', views.DetailQuestionView.as_view(), name='detail-question'),
    path('create/', views.CreateQuestionView.as_view(), name='create-question'),
    path('<int:pk>/delete/', views.DeleteQuestionView.as_view(), name='delete-question'), 
    path('<int:pk>/update/', views.UpdateQuestionView.as_view(), name='update-question'),

    path('get-previous-registration-data/', get_previous_registration_data, name='get_previous_registration_data'),

    path('dataframe/', views.ListDataframeView, name='appear-dataframe'),

    path('choice/<int:pk>/detail/', views.DetailQuestionChoiceView.as_view(), name='detail-question-choice'),
    path('choice/create/', views.CreateQuestionChoiceView.as_view(), name='create-question-choice'),
    path('choice/<int:pk>/delete/', views.DeleteQuestionChoiceView.as_view(), name='delete-question-choice'), 
    path('choice/<int:pk>/update/', views.UpdateQuestionChoiceView.as_view(), name='update-question-choice'),
    path('choice/', views.ListQuestionChoiceView, name='list-question-choice'),

    path('codepractice/<int:pk>/detail/', views.DetailCodepracticeView.as_view(), name='detail-codepractice'),
    path('codepractice/create/', views.CreateCodepracticeView.as_view(), name='create-codepractice'),
    path('codepractice/<int:pk>/delete/', views.DeleteCodepracticeView.as_view(), name='delete-codepractice'), 
    path('codepractice/<int:pk>/update/', views.UpdateCodepracticeView.as_view(), name='update-codepractice'),
    path('codepractice/', views.ListCodepracticeView, name='list-codepractice'),

    path('sql/', views.sql_view, name='sql_view'),

    path('quota-update/<int:category_id>/', views.update_quota, name='quota_update_url'),

    path('codepractice/test/', views.quiz_view, name='test-codepractice10')
]