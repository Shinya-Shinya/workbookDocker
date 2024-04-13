from django import forms
from django.forms import ModelForm
from .models import Practice, Book, PracticeChoice, Category, Codepractice, Quota
from betterforms.multiform import MultiModelForm
from django.utils.html import format_html
from django.db import transaction
from django.core.exceptions import ValidationError
from django.contrib import messages


class QuestionForm(ModelForm):
    new_shoseki = forms.CharField(
        label='新しい書籍名',
        required=False,
        #help_text='※「書籍」にない場合、新しい書籍として追加されます'
        help_text=format_html("<span class='help-text'>↑「書籍」にない場合、新しい書籍として追加されます</span>")
    )
    new_category = forms.CharField(
        label='新しいカテゴリ名',
        required=False,
        help_text=format_html("<span class='help-text'>↑「カテゴリ」にない場合、新しいカテゴリとして追加されます</span>")
    )

    class Meta:
        model = Practice
        fields = ['shoseki', 'new_shoseki', 'shoseki_page','question','thumbnail', 'answer', 'hint','explanation', 'category', 'new_category']
        widgets = {
            'question': forms.Textarea(attrs={'rows':3, 'cols':45}),
            'answer': forms.Textarea(attrs={'rows':1, 'cols':45}),

            'explanation': forms.Textarea(attrs={'rows':1, 'cols':45}),
            'hint': forms.Textarea(attrs={'rows':1, 'cols':43}),
          
            #'shoseki': forms.CharField(attrs={'rows':1, 'cols':45}),
        }

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['shoseki'].queryset = Book.objects.all()
        self.fields['shoseki'].required = False 
        self.order_fields(['shoseki', 'new_shoseki', 'shoseki_page', 'question', 'thumbnail', 'answer', 'hint', 'explanation', 'category', 'new_category'])
        self.fields['shoseki'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['new_shoseki'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['shoseki_page'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['question'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['answer'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['hint'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['explanation'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].required = False 
        self.fields['category'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['new_category'].widget.attrs.update({'class': 'form-label form-height'})


    def clean(self):
        cleaned_data = super().clean()
        shoseki = cleaned_data.get("shoseki")
        new_shoseki = cleaned_data.get("new_shoseki")
        category = cleaned_data.get("category")
        new_category = cleaned_data.get("new_category")

        if not shoseki and not new_shoseki:
            messages.error(self.request, "書籍を選択するか、新しい書籍名を入力してください。")
            raise ValidationError("書籍を選択するか、新しい書籍名を入力してください。")

        if not category and not new_category:
            messages.error(self.request, "カテゴリを選択するか、新しいカテゴリ名を入力してください。")
            raise ValidationError("既存のカテゴリを選択するか、新しいカテゴリを入力するかのいずれかを選択してください。")

        return cleaned_data

    def save(self, commit=True):
        with transaction.atomic():
            instance = super().save(commit=False)
            new_shoseki = self.cleaned_data.get("new_shoseki")
            new_category = self.cleaned_data.get("new_category")
            
            if new_shoseki:
                # 新しい書籍名が提供された場合、Bookモデルに保存
                shoseki_instance = Book.objects.create(name=new_shoseki)
                instance.shoseki = shoseki_instance

            if new_category:
                # 新しいカテゴリ名が提供された場合、Categoryモデルを検索または作成
                category_instance, created = Category.objects.get_or_create(name=new_category)
                instance.category = category_instance

            if commit:
                instance.save()
                self.save_m2m()  # ManyToManyフィールドがある場合に必要

        return instance


class QuestionChoiceForm(ModelForm):
    new_shoseki = forms.CharField(
        label='新しい書籍名',
        required=False,
        #help_text='※「書籍」にない場合、新しい書籍として追加されます'
        help_text=format_html("<span class='help-text'>↑「書籍」にない場合、新しい書籍として追加されます</span>")
    )
    new_category = forms.CharField(
        label='新しいカテゴリ名',
        required=False,
        help_text=format_html("<span class='help-text'>↑「カテゴリ」にない場合、新しいカテゴリとして追加されます</span>")
    )

    class Meta:
        model = PracticeChoice
        fields = ['shoseki', 'new_shoseki', 'shoseki_page','question', 'thumbnailQ1', 'thumbnailQ2', 'thumbnailQ3', 'answer','wronganswer1','wronganswer2','wronganswer3','wronganswer4','wronganswer5','wronganswer6','wronganswer7','wronganswer8','wronganswer9','hint1','hint2','explanation', 'category', 'new_category', 'thumbnailA1', 'thumbnailA2', 'thumbnailA3']
        widgets = {
            
            'question': forms.Textarea(attrs={'rows':3, 'cols':45}),
            #'answer': forms.Textarea(attrs={'rows':3, 'cols':45})
        }

    def __init__(self, *args, **kwargs):
        super(QuestionChoiceForm, self).__init__(*args, **kwargs)
        self.fields['shoseki'].queryset = Book.objects.all()
        self.fields['shoseki'].required = False 
        self.order_fields(['shoseki', 'new_shoseki', 'shoseki_page','question', 'thumbnailQ1', 'thumbnailQ2', 'thumbnailQ3', 'answer','wronganswer1','wronganswer2','wronganswer3','wronganswer4','wronganswer5','wronganswer6','wronganswer7','wronganswer8','wronganswer9','hint1','hint2','explanation', 'category', 'new_category', 'thumbnailA1', 'thumbnailA2', 'thumbnailA3'])
        self.fields['shoseki'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['shoseki_page'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['new_shoseki'].widget.attrs.update({'class': 'form-label'})
        self.fields['question'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['answer'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['hint1'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['hint2'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['explanation'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].required = False 
        self.fields['category'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['new_category'].widget.attrs.update({'class': 'form-label form-height'})

        self.fields['wronganswer1'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['wronganswer2'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['wronganswer3'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['wronganswer4'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['wronganswer5'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['wronganswer6'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['wronganswer7'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['wronganswer8'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['wronganswer9'].widget.attrs.update({'class': 'form-label form-height'})



    def clean(self):
        cleaned_data = super().clean()
        shoseki = cleaned_data.get("shoseki")
        new_shoseki = cleaned_data.get("new_shoseki")
        category = cleaned_data.get("category")
        new_category = cleaned_data.get("new_category")

        if not shoseki and not new_shoseki:
            messages.error(self.request, "書籍を選択するか、新しい書籍名を入力してください。")
            raise ValidationError("書籍を選択するか、新しい書籍名を入力してください。")

        if not category and not new_category:
            messages.error(self.request, "カテゴリを選択するか、新しいカテゴリ名を入力してください。")
            raise ValidationError("既存のカテゴリを選択するか、新しいカテゴリを入力するかのいずれかを選択してください。")

        return cleaned_data

    def save(self, commit=True):
        with transaction.atomic():
            instance = super().save(commit=False)
            new_shoseki = self.cleaned_data.get("new_shoseki")
            new_category = self.cleaned_data.get("new_category")

            if new_shoseki:
                # 新しい書籍名が提供された場合、Bookモデルに保存
                shoseki_instance = Book.objects.create(name=new_shoseki)
                instance.shoseki = shoseki_instance

            if new_category:
                # 新しいカテゴリ名が提供された場合、Categoryモデルに保存
                category_instance = Category.objects.create(name=new_category)
                instance.category = category_instance

            if commit:
                instance.save()
                self.save_m2m()  # ManyToManyフィールドがある場合に必要

        return instance

class FindForm(forms.Form):
        find1 = forms.CharField(label='問題', widget=forms.TextInput(attrs={'class':'form-control1'}),max_length=30, required=False)
        find2 = forms.CharField(label='答え', widget=forms.TextInput(attrs={'class':'form-control2'}),max_length=30,required=False)
        find3 = forms.CharField(label='書籍・HP', widget=forms.TextInput(attrs={'class':'form-control3'}),max_length=30,required=False)
        

class FindForm2(forms.Form):
        find1 = forms.CharField(label='問題', widget=forms.TextInput(attrs={'class':'form-control1'}),max_length=15, required=False)
        answers = forms.fields.ChoiceField(
            choices = (
              ('','全ての項目'), ('JAVA', 'JAVA'), ('Linux', 'Linux'), ('LinuC1', 'LinuC1'),('LPIC1', 'LPIC1'),('ディープラーニングE資格', 'ディープラーニングE資格'),('G検定', 'G検定'),('Python(全般)', 'Python(All)'), ('Python(Django)', 'Python(Django)'), ('Python(Machine Learning)', 'Python(機械学習)'), ('Python(Pandas)', 'Python(Pandas)'),('Python3エンジニア認定基礎試験', 'Python3エンジニア認定基礎試験'),('Python3エンジニア認定データ分析試験', 'Python3エンジニア認定データ分析試験'),('Python3エンジニア認定実践試験','Python3エンジニア認定実践試験'),('Javascript(All)', 'Javascript(全般)'), ('Javascript(Vue.js)', 'Javascript(vue.js)'), ('DATA SCIENTIST', 'データ　サイエンティスト'),('DATABASE SPECIALIST', 'データベース　スペシャリスト'),('Bronze 12c SQL基礎', 'Bronze 12c SQL基礎'),('NETWORK SPECIALIST', 'ネットワークスペシャリスト'),('AP', '応用情報技術者試験'),('FE', '基本情報技術者試験'),('情報セキュリティマネジメント', '情報セキュリティマネジメント'),('PHP', 'PHP'), ('SEO検定', 'SEO検定'),('Access VBA', 'Access VBA'), ('Excel VBA', 'Excel VBA'), ('統計検定2級', '統計検定2級'), ('統計検定3級', '統計検定3級'),('statistics', '統計学'), ('簿記2級', '簿記2級'),('TOEIC','TOEIC'),('trivia','雑学'),('other','その他'),('other','その他')
            ),
            initial='',
            label='カテゴリ',
            required=False,
            widget=forms.widgets.Select()
        )



class CodePracticeForm(ModelForm):
    new_shoseki = forms.CharField(
        label='新しい書籍名',
        required=False,
        #help_text='※「書籍・HP」にない場合、新しい書籍として追加されます'
        help_text=format_html("<span class='help-text'>↑「書籍」にない場合、新しい書籍として追加されます</span>")
    )
    new_category = forms.CharField(
        label='新しいカテゴリ名',
        required=False,
        help_text=format_html("<span class='help-text'>↑「カテゴリ」にない場合、新しいカテゴリとして追加されます</span>")
    )

    class Meta:
        model = Codepractice
        fields = ['shoseki', 'new_shoseki', 'shoseki_page', 'question1', 'question2', 'question3', 'req1', 'req2', 'req3', 'thumbnailQ1', 'thumbnailQ2', 'thumbnailQ3', 'thumbnailQ4', 'thumbnailQ5', 'thumbnailQ6', 'thumbnailQ7', 'thumbnailQ8', 'thumbnailQ9', 'thumbnailQ10', 'thumbnailQ11', 'thumbnailQ12', 'thumbnailQ13', 'thumbnailQ14', 'thumbnailQ15', 'thumbnailQ16', 'thumbnailQ17', 'thumbnailQ18', 'thumbnailQ19', 'thumbnailQ20', 'thumbnailQ21', 'thumbnailQ22', 'thumbnailQ23', 'thumbnailQ24', 'thumbnailQ25', 'thumbnailQ26', 'thumbnailQ27', 'thumbnailQ28', 'thumbnailQ29', 'thumbnailQ30', 'explanation',  'answerTitle1',  'answer1', 'answerTitle2', 'answer2', 'answerTitle3', 'answer3', 'answerTitle4', 'answer4', 'answerTitle5', 'answer5', 'thumbnailA1', 'thumbnailA2', 'thumbnailA3', 'thumbnailA4', 'thumbnailA5','category', 'new_category']
        widgets = {
            'question1': forms.Textarea(attrs={'rows':3, 'cols':45}),
            'question2': forms.Textarea(attrs={'rows':3, 'cols':45}),
            'question3': forms.Textarea(attrs={'rows':3, 'cols':45}),
            'req1': forms.Textarea(attrs={'rows':3, 'cols':45}),
            'req2': forms.Textarea(attrs={'rows':3, 'cols':45}),
            'req3': forms.Textarea(attrs={'rows':3, 'cols':45}),
            'answer1': forms.Textarea(attrs={'rows':1, 'cols':45}),
            'answer2': forms.Textarea(attrs={'rows':1, 'cols':45}),
            'answer3': forms.Textarea(attrs={'rows':1, 'cols':45}),
            'answer4': forms.Textarea(attrs={'rows':1, 'cols':45}),
            'answer5': forms.Textarea(attrs={'rows':1, 'cols':45}),

            'explanation': forms.Textarea(attrs={'rows':1, 'cols':45})
        }

    def __init__(self, *args, **kwargs):
        super(CodePracticeForm, self).__init__(*args, **kwargs)
        self.fields['shoseki'].queryset = Book.objects.all()
        self.fields['shoseki'].required = False 
        self.order_fields(['shoseki', 'new_shoseki', 'shoseki_page', 'question1', 'question2', 'question3', 'req1', 'req2', 'req3', 'thumbnailQ1', 'thumbnailQ2', 'thumbnailQ3', 'thumbnailQ4', 'thumbnailQ5', 'thumbnailQ6', 'thumbnailQ7', 'thumbnailQ8', 'thumbnailQ9', 'thumbnailQ10', 'thumbnailQ11', 'thumbnailQ12', 'thumbnailQ13', 'thumbnailQ14', 'thumbnailQ15', 'thumbnailQ16', 'thumbnailQ17', 'thumbnailQ18', 'thumbnailQ19', 'thumbnailQ20', 'thumbnailQ21', 'thumbnailQ22', 'thumbnailQ23', 'thumbnailQ24', 'thumbnailQ25', 'thumbnailQ26', 'thumbnailQ27', 'thumbnailQ28', 'thumbnailQ29', 'thumbnailQ30', 'explanation',  'answerTitle1',  'answer1', 'answerTitle2', 'answer2', 'answerTitle3', 'answer3', 'answerTitle4', 'answer4', 'answerTitle5', 'answer5', 'thumbnailA1', 'thumbnailA2', 'thumbnailA3', 'thumbnailA4', 'thumbnailA5','category', 'new_category'])
        self.fields['shoseki'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['new_shoseki'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['shoseki_page'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['question1'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['question2'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['question3'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['req1'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['req2'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['req3'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['answer1'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['answer2'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['answer3'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['answer4'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['answer5'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['explanation'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].required = False 
        self.fields['category'].widget.attrs.update({'class': 'form-label form-height'})
        self.fields['new_category'].widget.attrs.update({'class': 'form-label form-height'})


    def clean(self):
        cleaned_data = super().clean()
        shoseki = cleaned_data.get("shoseki")
        new_shoseki = cleaned_data.get("new_shoseki")
        category = cleaned_data.get("category")
        new_category = cleaned_data.get("new_category")

        if not shoseki and not new_shoseki:
            messages.error(self.request, "書籍を選択するか、新しい書籍名を入力してください。")
            raise ValidationError("書籍を選択するか、新しい書籍名を入力してください。")

        if not category and not new_category:
            messages.error(self.request, "カテゴリを選択するか、新しいカテゴリ名を入力してください。")
            raise ValidationError("既存のカテゴリを選択するか、新しいカテゴリを入力するかのいずれかを選択してください。")

        return cleaned_data

    def save(self, commit=True):
        with transaction.atomic():
            instance = super().save(commit=False)
            new_shoseki = self.cleaned_data.get("new_shoseki")
            new_category = self.cleaned_data.get("new_category")
            
            if new_shoseki:
                # 新しい書籍名が提供された場合、Bookモデルに保存
                #shoseki_instance = Book.objects.create(name=new_shoseki)
                shoseki_instance = Book.objects.get_or_create(name=new_shoseki)
                instance.shoseki = shoseki_instance

            if new_category:
                # 新しいカテゴリ名が提供された場合、Categoryモデルを検索または作成
                category_instance, created = Category.objects.get_or_create(name=new_category)
                instance.category = category_instance

            if commit:
                instance.save()
                self.save_m2m()  # ManyToManyフィールドがある場合に必要

        return instance


class CodePracticeSlickForm1(forms.ModelForm):
    class Meta:
        model = Codepractice
        fields = ['question1', 'question2', 'question3', 'req1', 'req2', 'req3']


class CodePracticeSlickForm2(forms.ModelForm):
    class Meta:
        model = Codepractice
        fields = ['thumbnailQ1', 'thumbnailQ2', 'thumbnailQ3', 'thumbnailQ4', 'thumbnailQ5', 'thumbnailQ6', 'thumbnailQ7', 'thumbnailQ8', 'thumbnailQ9', 'thumbnailQ10']

class CodePracticeSlickForm3(forms.ModelForm):
    class Meta:
        model = Codepractice
        fields = ['explanation', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'thumbnailA1', 'thumbnailA2', 'thumbnailA3', 'thumbnailA4', 'thumbnailA5']


class SQLForm(forms.Form):
    MODE_CHOICES = (
        ('sql', 'SQL'),
        ('pandas', 'Pandas DataFrame')
    )

    mode = forms.ChoiceField(choices=MODE_CHOICES, label='モード')
    #query = forms.CharField(widget=forms.Textarea, label='クエリ', help_text="SQLまたはPandas DataFrameのPythonコードを入力してください。")
    query = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), label='クエリ', help_text="SQLまたはPandas DataFrameのPythonコードを入力してください。")


class QuotaForm(forms.ModelForm):
    class Meta:
        model = Quota
        fields = ['target_count']

    def __init__(self, *args, **kwargs):
        super(QuotaForm, self).__init__(*args, **kwargs)
        self.fields['target_count'].widget.attrs.update({'class': 'quota-input'})