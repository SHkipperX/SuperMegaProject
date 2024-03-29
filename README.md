[клёвое-местечко.beta](https://www.klevoemestechko.store/)
## Для запуска проекта "Клёвое место" из репозитория GitLab выполните следующие шаги

### Клонирование репозитория

Убедитесь, что на вашем компьютере установлен Git. Если нет, установите его, следуя инструкциям на официальном сайте.

Откройте командную строку (терминал) на вашем компьютере.

Перейдите в каталог, в котором вы хотите разместить проект Django. Используйте команду cd для навигации. Например:

```Bash
cd Documents
```

Клонирование репозитория:

```Bash
git clone https://github.com/SHkipperX/SuperMegaProject.git
```

#### Настройка виртуальной среды (virtual environment)

Создайте виртуальную среду Python. Если у вас установлен модуль virtualenv, используйте следующую команду:

```Bash
virtualenv venv
```

Если virtualenv не установлен, вы можете использовать

```Bash
python -m venv venv
```

Активируйте виртуальную среду:

В Windows:

```Bash
venv\Scripts\activate
```

В macOS и Linux:

```Bash
source venv/bin/activate
```

##### Установка зависимостей

Убедитесь, что виртуальная среда активирована (в приглашении командной строки должно быть указано имя вашей виртуальной
среды, например, (venv)).

Для перехода по каталогам используйте команду ```cd```

Установите зависимости проекта, перейдя в каталог проекта, и выполните следующие команды:

Установка зависимостей

```Bash
pip install -r requirements/prod.txt
```

Для разработки необходимо дополнительно установить зависимости из

```Bash
pip install -r requirements/dev.txt
```

Для запуска тестов зависимости перечислены в:

```Bash
pip install -r requirements/test.txt
```

Для телеграм бота зависимости перечислены в:

```Bash
pip install -r requirements/bot.txt
```

##### Настройка переменных окружения

Скопируйте файл `.env.template` в `.env`

```Bash
cp .env.template .env
```

Откройте файл .env в текстовом редакторе и установите необходимые переменные окружения. Вот пример:

```Bash
DJANGO_SECRET_KEY=django-insecure-*kd#mnmzdmfzd
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

Перейдите в каталог проекта Django:

```Bash
cd OnTheHook
```

##### Применение миграций

В активированной виртуальной среде выполните команду для применения миграций:

```Bash
python manage.py migrate
```

##### Установка фикстур

```Bash
python manage.py loaddata fixtures/data.json
```

Выполните команду для запуска встроенного сервера Django:

```Bash
python manage.py runserver
```

##### Проверка работоспособности

Откройте веб-браузер и перейдите по адресу ```http://127.0.0.1:8000/``` (или ```http://localhost:8000/```). Вы должны
увидеть
страницу приветствия Django.

##### Работа с проектом

Теперь вы можете работать с проектом, вносить изменения, создавать приложения и т. д. Ваши изменения будут автоматически
обновляться при использовании встроенного сервера в режиме разработки.

##### Завершение работы

Для остановки сервера разработки нажмите Ctrl+C в командной строке.
> feat. EgorDikanskiy 
