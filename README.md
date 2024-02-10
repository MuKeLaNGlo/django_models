# Листинг №1 по моделям


### Проект содержит в себе Систему управления проектами с задачами и командами. <br> Похоже на тот же Gitlab.

<hr>

## Установка проекта
-   ```bash
    python3.10 -m venv venv
    ```
-   ```bash
    source venv/bin/activate
    ```
-   ```bash
    pip install -r requirements.txt
    ```
-   ```bash
    python3 manage.py migrate
    ```
Загружаем фикстуры
-   `По одной/разом все` из папки `fixtures`
-   Все разом + пользователь admin 
```bash
python3 manage.py loaddata db_fixture.json
```

## Основные моменты

### Multi-Inheritance, Abstract model, Proxy model

- **`CustomUser`**: Множественное наследование (Multi-Inheritance) - наследуется от `AbstractUser`. Переопределен метод `__str__` для отображения полного имени пользователя.

- **`TimeStampedModel`**: Абстрактная модель (Abstract model) - содержит поля `created_at` и `updated_at` для отслеживания времени создания и обновления записи.

- **`AdminProfileProxy`**: Прокси-модель (Proxy model) - создана на базе `UserProfile`. Дает возможность предоставлять и отзывать права администратора.

### Работа с M2M, FK, One-to-One

- **`UserProfile`**: Одна к одной (One-to-One) связь с пользовательской моделью (`CustomUser`). Также есть многие ко многим (M2M) связь с `SocialLink`.

- **`SocialLink`**: Внешний ключ (FK) на `UserProfile` для связи с конкретным пользователем.

- **`Project` и `CustomUser`**: M2M связь через модель промежуточного уровня `ProjectMembership` для отслеживания ролей участников проекта.

- **`Task`**: Внешний ключ (FK) на `Project` и `CustomUser` для определения проекта, ответственного и дополнительных сотрудников.

- **`TaskComment`**: Ссылка на саму себя через внешний ключ (FK) для родительского комментария.

### Использование медиа-файлов (фото)

- **`UserProfile` и `TaskMedia`**: Используют `ImageField` для хранения аватара пользователя и изображений задач соответственно.

<hr>

# P.S.
Не придумал как использовать `прокси модель`, поэтому выпилил из админки.