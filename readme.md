# DjangoUrban

## Обзор проекта

`DjangoUrban` — это простое приложение (шаблонное) на джанго, с наследуемым меню, формой регистрации,блоком навигации и кнопками. Без стилей. Может быть использован, как рыба при написании приложений

## Почему это важно?

Этот инструмент позволяет быстро заполнить нужные файлы для последующей реализации какого-либо приложения.

## Установка

1. Убедитесь, что у вас установлен Python 3.6 или выше.

2. Клонируйте репозиторий или загрузите файлы проекта:

    ```sh
    git clone <URL-вашего-репозитория>
    cd <папка-проекта>
    ```

3. Установите необходимые библиотеки (если таковые имеются) с помощью pip:

    ```sh
    pip install -r requirements.txt
    ```

## Использование

1. Создайте проект с venv, в нем приложение <имя>.Скопируйте все необходимые файлы, создав не достающие папки.

2. Запустите программу:

    ```sh
    активируем виртуальное окружение в консоли: venv/Scripts/activate
    активируем приложение в консоли: cd <имя>
    запускаем в консоли: python manage.py runserver
    ```



Приложение содержит:

    ```
    task1 содержит: модели покупателя и игры, миграции и записи в БД с условиями и без, дополненные представления QuerySet-запросами
    task2 содержит: шаблоны и маршруты классового и функционального представления
    task4 содержит: меню (родительский шаблон)
    task1 содержит: представления (джанго-форма и html-форма, POST-запрос), шаблон регистрации (имя, пароль, возраст)
    
    ```


## Внесение вклада

Если вы хотите внести свой вклад в проект, пожалуйста, создайте запрос на извлечение (pull request) с описанием изменений. Обязательно добавьте тесты и убедитесь, что все существующие тесты проходят успешно.

## Лицензия

Этот проект лицензируется под MIT License. См. файл [LICENSE](LICENSE) для подробностей.

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с [sofyamilich@gmail.com]

