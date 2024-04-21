from django.db import models

from .consts import MAX_RATE

from django.conf import settings

from django_pandas.io import read_frame

from datetime import datetime
from datetime import date, timedelta

from django.utils import timezone

from django.core.exceptions import ValidationError

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]


CATEGORY = (('business', 'ビジネス'), ('life','生活'),('other','その他'))
CATEGORY2 = (('JAVA', 'JAVA'), ('Linux', 'Linux'), ('LinuC1', 'LinuC1'),('LPIC1', 'LPIC1'),('ディープラーニングE資格', 'ディープラーニングE資格'),('G検定', 'G検定'),('Python(全般)', 'Python(All)'), ('Python(Django)', 'Python(Django)'), ('Python(Machine Learning)', 'Python(機械学習)'), ('Python(Pandas)', 'Python(Pandas)'),('Python3エンジニア認定基礎試験', 'Python3エンジニア認定基礎試験'),('Python3エンジニア認定データ分析試験', 'Python3エンジニア認定データ分析試験'),('Python3エンジニア認定実践試験','Python3エンジニア認定実践試験'),('Javascript(All)', 'Javascript(全般)'), ('Javascript(Vue.js)', 'Javascript(vue.js)'), ('DATA SCIENTIST', 'データ　サイエンティスト'),('DATABASE SPECIALIST', 'データベース　スペシャリスト'),('Bronze 12c SQL基礎', 'Bronze 12c SQL基礎'),('NETWORK SPECIALIST', 'ネットワークスペシャリスト'),('AP', '応用情報技術者試験'),('FE', '基本情報技術者試験'),('情報セキュリティマネジメント', '情報セキュリティマネジメント'),('PHP', 'PHP'), ('SEO検定', 'SEO検定'),('Access VBA', 'Access VBA'), ('Excel VBA', 'Excel VBA'), ('統計検定2級', '統計検定2級'), ('統計検定3級', '統計検定3級'),('statistics', '統計学'), ('簿記2級', '簿記2級'), ('TOEIC', 'TOEIC'), ('trivia','雑学'),('other','その他'))
CATEGORY3 = (('Excel VBA','Excel VBA'), ('LINE stickers','LINEスタンプ'),('other', 'その他'))
CATEGORY4 = ( ('laugher','笑い'),('impressed','感動'),('other','その他'))
SHOSEKILIST = (('徹底攻略 Java SE Bronze 問題集','徹底攻略 Java SE Bronze 問題集'),('スッキリわかるJava入門第3版','スッキリわかるJava入門第3版'),('キタミ式ITイラスト塾　応用情報技術者　令和03年','キタミ式ITイラスト塾　応用情報技術者　令和03年'),('令和04年【春期】　応用情報技術者　過去問題集','令和04年【春期】　応用情報技術者　過去問題集'),('応用情報技術者　試験によくでる問題集【午後】','応用情報技術者　試験によくでる問題集【午後】'),('応用情報技術者テキスト&問題集2020年版','応用情報技術者テキスト&問題集2020年版'),('LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応','LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応'),('Python3エンジニア認定実践試験Web問題','Python3エンジニア認定実践試験Web問題'),('Python3エンジニア認定データ分析試験Web問題','Python3エンジニア認定データ分析試験Web問題'),('Python3エンジニア認定基礎試験Web問題','Python3エンジニア認定基礎試験Web問題'),('Python3エンジニア認定基礎試験問題集','Python3エンジニア認定基礎試験問題集'),('基本情報技術者　らくらく突破PYTHON情報処理技術者試験','基本情報技術者　らくらく突破PYTHON情報処理技術者試験'),('徹底攻略データサイエンティスト検定リテラシーレベル問題集','徹底攻略データサイエンティスト検定リテラシーレベル問題集'),('データベーススペシャリスト教科書令和4年度','データベーススペシャリスト教科書令和4年度'),('Bronze 12c SQL 基礎問題集','Bronze 12c SQL 基礎問題集'),('シェルワンライナー100本ノック','シェルワンライナー100本ノック'),('【新試験対応】　VBAエキスパート試験　対策問題集　Access VBA スタンダード<1-5章>','【新試験対応】　VBAエキスパート試験　対策問題集　Access VBA スタンダード<1-5章>'),('Access VBA スタンダード','Access VBA スタンダード'),('Access VBA ベーシック','Access VBA ベーシック'),('Excel VBA スタンダード','Excel VBA スタンダード'),('Excel VBA ベーシック','Excel VBA ベーシック'), ('統計検定2級公式問題集CBT対応板','統計検定2級公式問題集CBT対応板'), ('統計検定2級　模擬問題集1', '統計検定2級　模擬問題集1'), ('統計検定2級　模擬問題集2', '統計検定2級　模擬問題集2'), ('統計検定2級　模擬問題集3', '統計検定2級　模擬問題集3'),('キタミ式ITイラスト塾　基本情報技術者　令和02年','キタミ式ITイラスト塾　基本情報技術者　令和02年'),('かんたん合格基本情報技術者過去問題集　令和元年度秋期かんたん合格シリーズ','かんたん合格基本情報技術者過去問題集　令和元年度秋期かんたん合格シリーズ'),('かんたん合格基本情報技術者過去問題集　令和2年度春期かんたん合格シリーズ','かんたん合格基本情報技術者過去問題集　令和2年度春期かんたん合格シリーズ'),('令和03年イメージ&クレバー方式でよくわかる栢木先生の基本情報技術者教室　情報処理技術者試験','令和03年イメージ&クレバー方式でよくわかる栢木先生の基本情報技術者教室　情報処理技術者試験'),('情報セキュリティマネジメント教科書令和2年度','情報セキュリティマネジメント教科書令和2年度'),('LPICレベル1スピードマスター問題集','LPICレベル1スピードマスター問題集'),('ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集','ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集'),('徹底攻略ディープラーニングE資格エンジニア問題集', '徹底攻略ディープラーニングE資格エンジニア問題集'),('Linuxコマンド200本ノック','Linuxコマンド200本ノック'),('パブロフ流でみんな合格　日商簿記２級　商業簿記　テキスト＆問題集','パブロフ流でみんな合格　日商簿記２級　商業簿記　テキスト＆問題集'),('新TOEIC TEST 頻出1200語','新TOEIC TEST 頻出1200語'))
SHOSEKILIST2 = (('徹底攻略 Java SE Bronze 問題集','徹底攻略 Java SE Bronze 問題集'),('スッキリわかるJava入門第3版','スッキリわかるJava入門第3版'),('キタミ式ITイラスト塾　応用情報技術者　令和03年','キタミ式ITイラスト塾　応用情報技術者　令和03年'),('令和04年【春期】　応用情報技術者　過去問題集','令和04年【春期】　応用情報技術者　過去問題集'),('応用情報技術者　試験によくでる問題集【午後】','応用情報技術者　試験によくでる問題集【午後】'),('応用情報技術者テキスト&問題集2020年版','応用情報技術者テキスト&問題集2020年版'),('LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応','LINUC教科書LINUCレベル1スピードマスター問題集 VERSION10.0対応'),('Python3エンジニア認定実践試験Web問題','Python3エンジニア認定実践試験Web問題'),('Python3エンジニア認定データ分析試験Web問題','Python3エンジニア認定データ分析試験Web問題'),('Python3エンジニア認定基礎試験Web問題','Python3エンジニア認定基礎試験Web問題'),('Python3エンジニア認定基礎試験問題集','Python3エンジニア認定基礎試験問題集'),('基本情報技術者　らくらく突破PYTHON情報処理技術者試験','基本情報技術者　らくらく突破PYTHON情報処理技術者試験'),('徹底攻略データサイエンティスト検定リテラシーレベル問題集','徹底攻略データサイエンティスト検定リテラシーレベル問題集'),('データベーススペシャリスト教科書令和4年度','データベーススペシャリスト教科書令和4年度'),('Bronze 12c SQL 基礎問題集','Bronze 12c SQL 基礎問題集'),('シェルワンライナー100本ノック','シェルワンライナー100本ノック'),('【新試験対応】　VBAエキスパート試験　対策問題集　Access VBA スタンダード<1-5章>','【新試験対応】　VBAエキスパート試験　対策問題集　Access VBA スタンダード<1-5章>'),('Access VBA スタンダード','Access VBA スタンダード'),('Access VBA ベーシック','Access VBA ベーシック'),('Excel VBA スタンダード','Excel VBA スタンダード'),('Excel VBA ベーシック','Excel VBA ベーシック'), ('統計検定2級公式問題集CBT対応板','統計検定2級公式問題集CBT対応板'), ('統計検定2級　模擬問題集1', '統計検定2級　模擬問題集1'), ('統計検定2級　模擬問題集2', '統計検定2級　模擬問題集2'), ('統計検定2級　模擬問題集3', '統計検定2級　模擬問題集3'),('キタミ式ITイラスト塾　基本情報技術者　令和02年','キタミ式ITイラスト塾　基本情報技術者　令和02年'),('かんたん合格基本情報技術者過去問題集　令和元年度秋期かんたん合格シリーズ','かんたん合格基本情報技術者過去問題集　令和元年度秋期かんたん合格シリーズ'),('かんたん合格基本情報技術者過去問題集　令和2年度春期かんたん合格シリーズ','かんたん合格基本情報技術者過去問題集　令和2年度春期かんたん合格シリーズ'),('令和03年イメージ&クレバー方式でよくわかる栢木先生の基本情報技術者教室　情報処理技術者試験','令和03年イメージ&クレバー方式でよくわかる栢木先生の基本情報技術者教室　情報処理技術者試験'),('情報セキュリティマネジメント教科書令和2年度','情報セキュリティマネジメント教科書令和2年度'),('LPICレベル1スピードマスター問題集','LPICレベル1スピードマスター問題集'),('ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集','ディープラーニングG検定ジェネラリスト要点整理テキスト&問題集'),('徹底攻略ディープラーニングE資格エンジニア問題集', '徹底攻略ディープラーニングE資格エンジニア問題集'),('Linuxコマンド200本ノック','Linuxコマンド200本ノック'),('パブロフ流でみんな合格　日商簿記２級　商業簿記　テキスト＆問題集','パブロフ流でみんな合格　日商簿記２級　商業簿記　テキスト＆問題集'),('新TOEIC TEST 頻出1200語','新TOEIC TEST 頻出1200語'))
CATEGORYTEST = (('40問','40問'),('10問','10問'))
CATEGORYFETEST = (('未','未'),('済','済'))
CATEGORYKUNRENBOOK = (('JAVA','JAVA'),('Python','Python'),('サーブレット&JSP','サーブレット&JSP'))


class Book(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Quota(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    target_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.category.name} - {self.target_count}"


class Practice(models.Model):
    question = models.TextField(verbose_name="問題")
    answer = models.TextField(verbose_name="正解")
    explanation = models.TextField(verbose_name="解説", null=True,  blank=True)
    thumbnail = models.ImageField(verbose_name="画像", null=True, blank= True)
    hint = models.TextField(verbose_name="ヒント", null=True,  blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="カテゴリ", null=True,  blank=True)
    shoseki = models.ForeignKey(Book, on_delete=models.CASCADE,verbose_name="書籍・HP", null=True,  blank=True)
    
    shoseki_page = models.CharField(verbose_name="書籍ページ・HP何問目", max_length=255, null=True,  blank=True)

    
    def __str__(self):
        return str(self.id)



        

class TestRoutine(models.Model):
    #text = models.TextField(verbose_name="内容")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    which_test = models.CharField(
        verbose_name="テストの種類", 
        max_length=100,
        choices = CATEGORYTEST
        )

    test_result = models.TextField()


class TestRoutine10(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    which_test = models.CharField(
        verbose_name="テストの種類", 
        max_length=100,
        choices = CATEGORYTEST
        )

    category = models.TextField()

    test_result = models.TextField()


class PracticeChoice(models.Model):
    question = models.TextField(verbose_name="問題")
    thumbnailQ1 = models.ImageField(verbose_name="画像1 (問題用)", null=True, blank= True)
    thumbnailQ2 = models.ImageField(verbose_name="画像2 (問題用)", null=True, blank= True)
    thumbnailQ3 = models.ImageField(verbose_name="画像3 (問題用)", null=True, blank= True)
    answer = models.TextField(verbose_name="正解")
    wronganswer1 = models.TextField(verbose_name="誤回答1", null=True, blank= True)
    wronganswer2 = models.TextField(verbose_name="誤回答2", null=True, blank= True)
    wronganswer3 = models.TextField(verbose_name="誤回答3", null=True, blank= True)

    wronganswer4 = models.TextField(verbose_name="誤回答4", null=True, blank= True)
    wronganswer5 = models.TextField(verbose_name="誤回答5", null=True, blank= True)
    wronganswer6 = models.TextField(verbose_name="誤回答6", null=True, blank= True)
    wronganswer7 = models.TextField(verbose_name="誤回答7", null=True, blank= True)
    wronganswer8 = models.TextField(verbose_name="誤回答8", null=True, blank= True)
    wronganswer9 = models.TextField(verbose_name="誤回答9", null=True, blank= True)

    explanation = models.TextField(verbose_name="解説", null=True,  blank=True,)
    thumbnailA1 = models.ImageField(verbose_name="画像1 (正解用)", null=True, blank= True)
    thumbnailA2 = models.ImageField(verbose_name="画像2 (正解用)", null=True, blank= True)
    thumbnailA3 = models.ImageField(verbose_name="画像3 (正解用)", null=True, blank= True)
    hint1 = models.TextField(verbose_name="ヒント1", null=True,  blank=True,)
    hint2 = models.TextField(verbose_name="ヒント2", null=True,  blank=True,)
  
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="カテゴリ", null=True,  blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    shoseki = models.ForeignKey(Book, on_delete=models.CASCADE,verbose_name="書籍・HP", null=True,  blank=True)
    shoseki_page = models.CharField(verbose_name="書籍ページ", max_length=255, null=True,  blank=True)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.shoseki_page)


class Codepractice(models.Model):
    question1 = models.TextField(verbose_name="問題")
    question2 = models.TextField(verbose_name="問題", null=True, blank= True)
    question3 = models.TextField(verbose_name="問題", null=True, blank= True)
    req1 = models.TextField(verbose_name="要件", null=True, blank= True)
    req2 = models.TextField(verbose_name="要件", null=True, blank= True)
    req3 = models.TextField(verbose_name="要件", null=True, blank= True)
    answerTitle1 = models.CharField(verbose_name="モジュール名1", max_length=255)
    answerTitle2 = models.CharField(verbose_name="モジュール名2", max_length=255, null=True,  blank=True)
    answerTitle3 = models.CharField(verbose_name="モジュール名3", max_length=255, null=True,  blank=True)
    answerTitle4 = models.CharField(verbose_name="モジュール名4", max_length=255, null=True,  blank=True)
    answerTitle5 = models.CharField(verbose_name="モジュール名5", max_length=255, null=True,  blank=True)
    answerTitle6 = models.CharField(verbose_name="モジュール名6", max_length=255, null=True,  blank=True)
    answerTitle7 = models.CharField(verbose_name="モジュール名7", max_length=255, null=True,  blank=True)


    answer1 = models.TextField(verbose_name="正解コード1")
    answer2 = models.TextField(verbose_name="正解コード2", null=True, blank= True)
    answer3 = models.TextField(verbose_name="正解コード3", null=True, blank= True)
    answer4 = models.TextField(verbose_name="正解コード4", null=True, blank= True)
    answer5 = models.TextField(verbose_name="正解コード5", null=True, blank= True)
    answer6 = models.TextField(verbose_name="正解コード6", null=True, blank= True)
    answer7 = models.TextField(verbose_name="正解コード7", null=True, blank= True)
    
    thumbnailQ1 = models.ImageField(verbose_name="画像1 (問題用)", null=True, blank= True)
    thumbnailQ2 = models.ImageField(verbose_name="画像2 (問題用)", null=True, blank= True)
    thumbnailQ3 = models.ImageField(verbose_name="画像3 (問題用)", null=True, blank= True)
    thumbnailQ4 = models.ImageField(verbose_name="画像4 (問題用)", null=True, blank= True)
    thumbnailQ5 = models.ImageField(verbose_name="画像5 (問題用)", null=True, blank= True)
    thumbnailQ6 = models.ImageField(verbose_name="画像6 (問題用)", null=True, blank= True)
    thumbnailQ7 = models.ImageField(verbose_name="画像7 (問題用)", null=True, blank= True)
    thumbnailQ8 = models.ImageField(verbose_name="画像8 (問題用)", null=True, blank= True)
    thumbnailQ9 = models.ImageField(verbose_name="画像9 (問題用)", null=True, blank= True)
    thumbnailQ10 = models.ImageField(verbose_name="画像10 (問題用)", null=True, blank= True)

    thumbnailQ11 = models.ImageField(verbose_name="画像11 (問題用)", null=True, blank= True)
    thumbnailQ12 = models.ImageField(verbose_name="画像12 (問題用)", null=True, blank= True)
    thumbnailQ13 = models.ImageField(verbose_name="画像13 (問題用)", null=True, blank= True)
    thumbnailQ14 = models.ImageField(verbose_name="画像14 (問題用)", null=True, blank= True)
    thumbnailQ15 = models.ImageField(verbose_name="画像15 (問題用)", null=True, blank= True)
    thumbnailQ16 = models.ImageField(verbose_name="画像16 (問題用)", null=True, blank= True)
    thumbnailQ17 = models.ImageField(verbose_name="画像17 (問題用)", null=True, blank= True)
    thumbnailQ18 = models.ImageField(verbose_name="画像18 (問題用)", null=True, blank= True)
    thumbnailQ19 = models.ImageField(verbose_name="画像19 (問題用)", null=True, blank= True)
    thumbnailQ20 = models.ImageField(verbose_name="画像20 (問題用)", null=True, blank= True)

    thumbnailQ21 = models.ImageField(verbose_name="画像21 (問題用)", null=True, blank= True)
    thumbnailQ22 = models.ImageField(verbose_name="画像22 (問題用)", null=True, blank= True)
    thumbnailQ23 = models.ImageField(verbose_name="画像23 (問題用)", null=True, blank= True)
    thumbnailQ24 = models.ImageField(verbose_name="画像24 (問題用)", null=True, blank= True)
    thumbnailQ25 = models.ImageField(verbose_name="画像25 (問題用)", null=True, blank= True)
    thumbnailQ26 = models.ImageField(verbose_name="画像26 (問題用)", null=True, blank= True)
    thumbnailQ27 = models.ImageField(verbose_name="画像27 (問題用)", null=True, blank= True)
    thumbnailQ28 = models.ImageField(verbose_name="画像28 (問題用)", null=True, blank= True)
    thumbnailQ29 = models.ImageField(verbose_name="画像29 (問題用)", null=True, blank= True)
    thumbnailQ30 = models.ImageField(verbose_name="画像30 (問題用)", null=True, blank= True)

    explanation = models.TextField(verbose_name="解説", null=True,  blank=True)
    thumbnailA1 = models.ImageField(verbose_name="画像1 (正解用)", null=True, blank= True)
    thumbnailA2 = models.ImageField(verbose_name="画像2 (正解用)", null=True, blank= True)
    thumbnailA3 = models.ImageField(verbose_name="画像3 (正解用)", null=True, blank= True)
    thumbnailA4 = models.ImageField(verbose_name="画像4 (正解用)", null=True, blank= True)
    thumbnailA5 = models.ImageField(verbose_name="画像5 (正解用)", null=True, blank= True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="カテゴリ", null=True,  blank=True)
    shoseki = models.ForeignKey(Book, on_delete=models.CASCADE,verbose_name="書籍・HP", null=True, blank= True)
    
    shoseki_page = models.CharField(verbose_name="書籍ページ・HP何問目", max_length=255, null=True,  blank=True)

    """
    def __str__(self):
        return str(self.id)
        """