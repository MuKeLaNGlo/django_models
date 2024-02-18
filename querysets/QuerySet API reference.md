### QuerySet API (API запросов)

#### Methods that return new QuerySets (Методы, возвращающие новые QuerySets)

##### filter() (Фильтрация)
```python
tasks_todo = Task.objects.filter(status='todo')
```

##### exclude() (Исключение)
```python
tasks_not_done = Task.objects.exclude(status='done')
```

##### annotate() (Аннотация)
```python
projects_with_task_count = Project.objects.annotate(task_count=models.Count('task'))
```

##### alias() (Псевдоним)
```python
tasks_due_soon = Task.objects.alias(due_date__lt=models.functions.Now() + models.Duration(days=7))
```

##### order_by() (Сортировка)
```python
tasks_ordered_by_priority = Task.objects.order_by('-priority')
```

##### reverse() (Реверс)
```python
reversed_tasks = Task.objects.reverse()
```

##### distinct() (Уникальные значения)
```python
unique_priorities = Task.objects.values('priority').distinct()
```

##### values() (Выборка значений)
```python
project_names = Project.objects.values('name')
```

##### values_list() (Выборка значений в виде списка)
```python
task_titles = Task.objects.values_list('title', flat=True)
```

##### dates() (Даты)
```python
task_due_dates = Task.objects.dates('due_date', 'month')
```

##### datetimes() (Дата и время)
```python
task_created_datetimes = Task.objects.datetimes('created_at', 'hour')
```

##### none() (Пустой QuerySet)
```python
empty_queryset = Task.objects.none()
```

##### all() (Все объекты)
```python
all_tasks = Task.objects.all()
```

##### union() (Объединение QuerySets)
```python
union_result = Task.objects.filter(status='todo').union(Task.objects.filter(status='in_progress'))
```

##### intersection() (Пересечение QuerySets)
```python
intersection_result = Task.objects.filter(status='todo').intersection(Task.objects.filter(priority='high'))
```

##### difference() (Разность QuerySets)
```python
difference_result = Task.objects.filter(status='todo').difference(Task.objects.filter(priority='high'))
```

##### select_related() (Выбор связанных объектов)
```python
tasks_with_project = Task.objects.select_related('project')
```

##### prefetch_related() (Предварительная выборка связанных объектов)
```python
projects_with_tasks = Project.objects.prefetch_related('task_set')
```

##### extra() (Дополнительные условия)
```python
tasks_with_extra_condition = Task.objects.extra(where=["due_date > '2022-01-01'"])
```

##### defer() (Отложенная загрузка полей)
```python
tasks_deferred_description = Task.objects.defer('description')
```

##### only() (Загрузка только определенных полей)
```python
tasks_only_title = Task.objects.only('title')
```

##### using() (Использование определенной базы данных)
```python
tasks_from_another_database = Task.objects.using('another_database')
```

##### select_for_update() (Выбор для обновления)
```python
selected_tasks_for_update = Task.objects.select_for_update().filter(status='todo')
```

##### raw() (Использование SQL-запроса)
```python
raw_queryset = Task.objects.raw('SELECT * FROM tasks_task WHERE status = %s', ['todo'])
```

#### Operators that return new QuerySets (Операторы, возвращающие новые QuerySets)

##### AND (&) (И)
```python
high_priority_todo_tasks = Task.objects.filter(priority='high') & Task.objects.filter(status='todo')
```

##### OR (|) (ИЛИ)
```python
high_priority_or_todo_tasks = Task.objects.filter(priority='high') | Task.objects.filter(status='todo')
```

##### XOR (^) (Исключающее ИЛИ)
```python
high_priority_xor_todo_tasks = Task.objects.filter(priority='high') ^ Task.objects.filter(status='todo')
```

#### Methods that do not return QuerySets (Методы, не возвращающие новые QuerySets)

##### get() (Получение одного объекта)
```python
specific_task = Task.objects.get(title='Конкретная задача')
```

##### create() (Создание объекта)
```python
new_project = Project.objects.create(name='Новый проект', description='Описание')
```

##### get_or_create() (Получение или создание объекта)
```python
existing_project, created = Project.objects.get_or_create(name='Существующий проект', defaults={'description': 'Описание'})
```

##### update_or_create() (Обновление или создание объекта)
```python
updated_project, created = Project.objects.update_or_create(name='Существующий проект', defaults={'description': 'Новое описание'})
```

##### bulk_create() (Массовое создание объектов)
```python
tasks_to_create = [Task(title=f'Задача {i}') for i in range(10)]
Task.objects.bulk_create(tasks_to_create)
```

##### bulk_update() (Массовое обновление объектов)
```python
tasks_to_update = Task.objects.filter(status='todo')
tasks_to_update.update(status='in_progress')
```

##### count() (Количество объектов)
```python
task_count = Task.objects.count()
```

##### in_bulk() (Получение объектов по списку ключей)
```python
tasks_by_ids = Task.objects.in_bulk([1, 2, 3])
```

##### iterator() (Итератор по объектам)
```python
tasks_iterator = Task.objects.iterator()
```

###### With server-side cursors (С курсорами на стороне сервера)
```python
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM tasks_task;")
    for row in cursor.fetchall():
        print(row)
```

###### Without server-side cursors (Без курсоров на стороне сервера)
```python
for task in Task.objects.iterator(chunk_size=100):
    print(task)
```

##### latest() (Последний объект)
```python
latest_task = Task.objects.latest('created_at')
```

##### earliest() (Первый объект)
```python
earliest_task = Task.objects.earliest('created_at')
```

##### first() (Первый объект)
```python
first_task = Task.objects.first()
```

##### last() (Последний объект)
```python
last_task = Task.objects.last()
```

##### aggregate() (Агрегация)
```python
from django.db.models import Avg, Count, Max, Min, StdDev, Sum, Variance

project_stats = Project.objects.aggregate(
    avg_tasks=Avg('task__priority'),
    total_tasks=Count('task'),
    latest_task=Max('task__created_at'),
    earliest_task=Min('task

__created_at'),
    task_count_by_status=Count('task', filter=models.Q(task__status='todo')),
    total_task_duration=Sum(models.F('task__due_date') - models.F('task__created_at')),
    priority_variance=Variance('task__priority')
)
```

##### exists() (Проверка наличия объектов)
```python
tasks_exist = Task.objects.filter(status='todo').exists()
```

##### contains() (Проверка наличия значения в поле)
```python
value_exists = Task.objects.filter(description__contains='important').exists()
```

##### update() (Обновление объектов)
```python
Task.objects.filter(status='todo').update(status='in_progress')
```

###### Ordered queryset (Упорядоченный QuerySet)
```python
Task.objects.filter(status='todo').order_by('due_date').update(status='in_progress')
```

##### delete() (Удаление объектов)
```python
Task.objects.filter(status='done').delete()
```

##### as_manager() (Преобразование QuerySet в менеджер)
```python
tasks_manager = Task.objects.filter(status='todo').as_manager()
```

##### explain() (Получение плана выполнения запроса)
```python
query_plan = Task.objects.filter(status='todo').explain()
```

### Field lookups (Поиск по полям)

#### exact (Точное совпадение)
```python
exact_match = Task.objects.filter(title__exact='Точное совпадение')
```

#### iexact (Точное совпадение без учета регистра)
```python
case_insensitive_exact_match = Task.objects.filter(title__iexact='Точное совпадение без учета регистра')
```

#### contains (Содержит подстроку)
```python
contains_substr = Task.objects.filter(description__contains='подстрока')
```

#### icontains (Содержит подстроку без учета регистра)
```python
case_insensitive_contains_substr = Task.objects.filter(description__icontains='подстрока без учета регистра')
```

#### in (В списке)
```python
tasks_in_list = Task.objects.filter(priority__in=['low', 'medium'])
```

#### startswith (Начинается с)
```python
tasks_starting_with = Task.objects.filter(title__startswith='Начинается с')
```

#### istartswith (Начинается с без учета регистра)
```python
case_insensitive_startswith = Task.objects.filter(title__istartswith='начинается с без учета регистра')
```

#### endswith (Заканчивается на)
```python
tasks_ending_with = Task.objects.filter(title__endswith='Заканчивается на')
```

#### iendswith (Заканчивается на без учета регистра)
```python
case_insensitive_ending_with = Task.objects.filter(title__iendswith='заканчивается на без учета регистра')
```

#### range (В диапазоне)
```python
tasks_in_range = Task.objects.filter(priority__range=('low', 'medium'))
```

#### date (По дате)
```python
tasks_on_date = Task.objects.filter(created_at__date='2022-01-01')
```

#### year (По году)
```python
tasks_in_year = Task.objects.filter(created_at__year=2022)
```

#### iso_year (По ISO году)
```python
tasks_in_iso_year = Task.objects.filter(created_at__iso_year=2022)
```

#### month (По месяцу)
```python
tasks_in_month = Task.objects.filter(created_at__month=1)
```

#### day (По дню месяца)
```python
tasks_in_day = Task.objects.filter(created_at__day=1)
```

#### week (По неделе года)
```python
tasks_in_week = Task.objects.filter(created_at__week=1)
```

#### week_day (По дню недели)
```python
tasks_on_week_day = Task.objects.filter(created_at__week_day=1)
```

#### iso_week_day (По ISO дню недели)
```python
tasks_on_iso_week_day = Task.objects.filter(created_at__iso_week_day=1)
```

#### quarter (По кварталу)
```python
tasks_in_quarter = Task.objects.filter(created_at__quarter=1)
```

#### time (По времени)
```python
tasks_at_time = Task.objects.filter(created_at__time='12:00:00')
```

#### hour (По часу)
```python
tasks_in_hour = Task.objects.filter(created_at__hour=12)
```

#### minute (По минуте)
```python
tasks_in_minute = Task.objects.filter(created_at__minute=30)
```

#### second (По секунде)
```python
tasks_in_second = Task.objects.filter(created_at__second=45)
```

#### isnull (Пустое значение)
```python
tasks_with_null_description = Task.objects.filter(description__isnull=True)
```

#### regex (Регулярное выражение)
```python
tasks_with_regex_pattern = Task.objects.filter(title__regex=r'^[0-9]+$')
```

#### iregex (Регулярное выражение без учета регистра)
```python
tasks_with_case_insensitive_regex_pattern = Task.objects.filter(title__iregex=r'^[a-z]+$')
```

### Aggregation functions (Функции агрегации)

#### Avg (Среднее значение)
```python
average_priority = Task.objects.aggregate(average_priority=models.Avg('priority'))
```

#### Count (Количество)
```python
total_projects = Project.objects.aggregate(total_projects=models.Count('id'))
```

#### Max (Максимальное значение)
```python
latest_due_date = Task.objects.aggregate(latest_due_date=models.Max('due_date'))
```

#### Min (Минимальное значение)
```python
earliest_due_date = Task.objects.aggregate(earliest_due_date=models.Min('due_date'))
```

#### StdDev (Стандартное отклонение)
```python
priority_deviation = Task.objects.aggregate(priority_deviation=models.StdDev('priority'))
```

#### Sum (Сумма)
```

python
total_task_priority = Task.objects.aggregate(total_task_priority=models.Sum('priority'))
```

#### Variance (Дисперсия)
```python
priority_variance = Task.objects.aggregate(priority_variance=models.Variance('priority'))
```

### Query-related tools (Инструменты, связанные с запросами)

#### Q() objects (Объекты Q)
```python
from django.db.models import Q

tasks_with_high_priority_or_todo_status = Task.objects.filter(Q(priority='high') | Q(status='todo'))
```

#### Prefetch() objects (Объекты Prefetch)
```python
from django.db.models import Prefetch

projects_with_prefetched_tasks = Project.objects.prefetch_related(Prefetch('task_set', queryset=Task.objects.filter(status='todo')))
```

#### prefetch_related_objects() (Предварительная выборка связанных объектов)
```python
from django.db.models.query import prefetch_related_objects

tasks = Task.objects.all()
prefetch_related_objects(tasks, 'project')
```

#### FilteredRelation() objects (Объекты FilteredRelation)
```python
from django.db.models import FilteredRelation

tasks_with_filtered_project = Task.objects.annotate(
    filtered_project=FilteredRelation('project', condition=models.Q(project__status='active'))
)
```