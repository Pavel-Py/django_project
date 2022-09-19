from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Row, Column, Layout, HTML
from django import forms

from jum.models import Company, Vacancy, Application, Resume


class CompanyForm(forms.ModelForm):
    logo = forms.ImageField()

    class Meta:
        model = Company
        fields = ['title', 'location', 'logo', 'description', 'employee_count']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.fields['title'].label = 'Название'
        self.fields['location'].label = 'Находимся'
        self.fields['logo'].label = 'Эмблема'
        self.fields['logo'].widget = forms.FileInput()
        self.fields['logo'].required = False
        self.fields['description'].label = 'Описание'
        self.fields['employee_count'].label = 'Количество сотрудников'
        self.helper.layout = Layout(
            Row(
                Column('title'),
                Column('logo', HTML("{% if form.logo.value %}<img width='150' class='img-responsive' \
                src='{{ object.logo.url }}'>{% endif %}")),
            ),
            Row(Column('employee_count'), Column('location')),
            'description'
        )


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'skills', 'description', 'salary_min', 'salary_max']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Добавить'))
        self.fields['title'].label = 'Название'
        self.fields['specialty'].label = 'Специализация'
        self.fields['skills'].label = 'Скилы'
        self.fields['description'].label = 'Описание'
        self.fields['salary_min'].label = 'Зарплата от'
        self.fields['salary_max'].label = 'Зарплата до'
        self.helper.layout = Layout(
            Row(Column('title'), Column('specialty')),
            Row(Column('salary_min'), Column('salary_max')),
            'skills',
            'description'
        )


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Добавить'))
        self.helper.form_class = 'form-horizontal'


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'surname', 'status', 'salary', 'specialty', 'grade', 'education', 'experience', 'portfolio']

    def __init__(self, *args, **kwargs):
        rus_labels = [
            'Имя',
            'Фамилия',
            'Готовность к работе',
            'Ожидаемое вознаграждение',
            'Специализация',
            'Квалификация',
            'Образование',
            'Опыт работы',
            'Портфолио'
        ]
        super().__init__(*args, **kwargs)
        for form_obj, new_label in zip(self.fields.values(), rus_labels):
            form_obj.label = new_label
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Создать'))
        self.helper.form_class = 'form-label'
        self.helper.layout = Layout(
            Row(Column('name'), Column('surname')),
            Row(Column('status'), Column('salary')),
            Row(Column('specialty'), Column('grade')),
            'education',
            'experience',
            'portfolio'
        )
