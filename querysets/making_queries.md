### Creating objects (Создание объектов)

#### Создание нового проекта:
```python
from core.models import *
project = Project.objects.create(name='Новый проект', description='Описание проекта', creator=CustomUser.objects.first())
```

#### Добавление нового участника в проект:
```python
project = Project.objects.get(name='Новый проект')
user = CustomUser.objects.create(username='НовыйУчастник', first_name='Имя', last_name='Фамилия')
membership = ProjectMembership.objects.create(user=user, project=project, role='developer')
```

### Saving changes to objects (Сохранение изменений объектов)

#### Изменение описания проекта и сохранение:
```python
project = Project.objects.get(name='Новый проект')
project.description = 'Новое описание проекта'
project.save()
```

### Retrieving objects (Получение объектов)

#### Получение всех пользователей:
```python
users = CustomUser.objects.all()
```

#### Получение всех проектов с их создателями:
```python
projects_with_creators = Project.objects.select_related('creator').all()
```

### Retrieving specific objects with filters (Получение конкретных объектов с использованием фильтров)

#### Получение проекта с определенным именем:
```python
project = Project.objects.get(name='Новый проект')
```

### Retrieving a single object with get() (Получение одного объекта с использованием get())

#### Получение пользователя с определенным именем:
```python
user = CustomUser.objects.get(username='НовыйУчастник')
```

### Other QuerySet methods (Другие методы QuerySet)

#### Получение количества проектов:
```python
project_count = Project.objects.count()
```

#### Получение всех проектов, созданных конкретным пользователем:
```python
user_projects = Project.objects.filter(creator__username='ИмяПользователя')
```

### Limiting QuerySets (Ограничение QuerySets)

#### Получение первых 5 проектов:
```python
first_five_projects = Project.objects.all()[:5]
```

#### Получение последних 3 пользователей:
```python
last_three_users = CustomUser.objects.all().order_by('-id')[:3]
```

### Field lookups (Поиск по полям)

#### Получение всех пользователей, чьи имена начинаются с "И":
```python
users_starting_with_i = CustomUser.objects.filter(first_name__startswith='И')
```

### Lookups that span relationships (Поиск, охватывающий отношения)

#### Получение всех участников проекта с ролью "developer":
```python
developers_in_project = ProjectMembership.objects.filter(role='developer').select_related('user')
```

### Filters can reference fields on the model (Фильтры могут ссылаться на поля модели)

#### Получение задач, у которых срок выполнения больше текущей даты:
```python
tasks_due_later = Task.objects.filter(due_date__gt=models.functions.Now())
```

### Expressions can reference transforms (Выражения могут ссылаться на преобразования)

#### Получение задач с приоритетом "High" или "Medium":
```python
high_medium_priority_tasks = Task.objects.filter(priority__in=['High', 'Medium'])
```

### The pk lookup shortcut (Сокращение поиска по ключу)

#### Получение проекта с определенным идентификатором:
```python
project = Project.objects.get(pk=1)
```

### Escaping percent signs and underscores in LIKE statements (Экранирование знаков процента и подчеркивания в операторах LIKE)

#### Получение всех проектов, содержащих в названии "django":
```python
django_projects = Project.objects.filter(name__icontains='django')
```

### Caching and QuerySets (Кеширование и QuerySets)

#### Получение всех проектов из кеша, если они там есть:
```python
cached_projects = Project.objects.all().using('cache_alias')
```

### Asynchronous queries (Асинхронные запросы)

#### Асинхронное получение всех проектов:
```python
import asyncio
async def get_projects():
    projects = await asyncio.gather(*[project.async for project in Project.objects.all()])
```

### QuerySet and manager methods (Методы QuerySet и менеджера)

#### Получение всех проектов, созданных в течение последних 30 дней:
```python
recent_projects = Project.objects.created_last_30_days()
```

### Transactions (Транзакции)

#### Использование транзакции при создании пользователя и профиля:
```python
from django.db import transaction

with transaction.atomic():
    user = CustomUser.objects.create(username='НовыйПользователь')
    profile = UserProfile.objects.create(user=user, bio='Новая биография')
```

### Querying JSONField (Запросы к JSONField)

#### Получение всех задач с определенным ключом в JSONField:
```python
tasks_with_key = Task.objects.filter(description__contains='{"key": "value"}')
```

### Key, index, and path transforms (Преобразования ключа, индекса и пути)

#### Получение всех задач с изображениями:
```python
tasks_with_images = Task.objects.filter(taskmedia__image__isnull=False)
```

### Containment and key lookups (Поиск по вхождению и ключевым запросам)

#### Получение задач с приоритетом "High" и "Medium":
```python
high_medium_priority_tasks = Task.objects.filter(priority__in=['High', 'Medium'])
```

### Complex lookups with Q objects (запросы с использованием объектов Q)

#### Получение задач, у которых статус "To Do" и приоритет "High":
```python
from django.db.models import Q

tasks_todo_high_priority = Task.objects.filter(Q(status='todo') & Q(priority='high'))
```

### Comparing objects (Сравнение объектов)

#### Сравнение даты создания двух проектов:
```python
project1 = Project.objects.get(name='Проект1')
project2 = Project.objects.get(name='Проект2')

if project1.created_at > project2.created_at:
    print(f'{project1.name} создан раньше {project2.name}')
```

### Deleting objects (Удаление объектов)

#### Удаление пользователя с определенным именем:
```python
CustomUser.objects.filter(username='УдаляемыйПользователь').delete()
```

### Copying model instances (Копирование экземпляров модели)

#### Копирование задачи и изменение названия:
```python
original_task = Task.objects.get(title='ОригинальнаяЗадача')
copied_task = original_task.copy()
copied_task.title = 'КопияЗадачи'
copied_task.save()
```

### Updating multiple objects at once (Обновление нескольких объектов одновременно)

#### Обновление статуса всех задач с "To Do" на "In Progress":
```python
Task.objects.filter(status='todo').update(status='in_progress')
```

### Related objects (Связанные объекты)

#### Получение всех задач, назначенных конкретному пользователю:
```python
user_assigned_tasks = CustomUser.objects.get(username='ИмяПользователя').assigned_tasks.all()
```

### One-to-one relationships (Отношения один к одному)

#### Получение профиля пользователя по пользователю:
```python
user_profile = UserProfile.objects.get(user__username='ИмяПользователя')
```

### Queries over related objects (Запросы по связанным объектам)

#### Получение всех комментариев к задаче:
```python
task_comments = Task.objects.get(title='Название Задачи').taskcomment_set.all()
```

### F expressions (Выражения F)

#### Увеличение приоритета всех задач "Medium" на 1:
```python
Task.objects.filter(priority='medium').update(priority=models.F('priority') + 1)
```

### Combining multiple queries with Q objects (Сочетание нескольких запросов с объектами Q)

#### Получение всех задач, у которых статус "To Do" или "In Progress":
```python
tasks_todo_in_progress = Task.objects.filter(Q(status='todo') | Q(status='in_progress'))
```

### Bulk create (Массовое создание объектов)

#### Массовое создание нескольких задач для проекта:
```python
tasks = [Task(title=f'Задача {i}', description=f'Описание {i}', project=project) for i in range(5)]
Task.objects.bulk_create(tasks)
```