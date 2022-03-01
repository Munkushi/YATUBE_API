API для проекта **yatube_project**

**Как запустить проект:**

Клонировать репозиторий и перейти в него в командной строке:

https://github.com/Munkushi/api_final_yatube

**Cоздать и активировать виртуальное окружение:**

python3 -m venv env для mac/linux
pyyhon -m venv venv windows

source venv/Scripts/activate

**Установить зависимости из файла requirements.txt:**

pip install -r requirements.txt

**Выполнить миграции:**

cd yatube_api

python3 manage.py migrate для mac/linux
python manage.py migrate для windows

**Запустить проект:**

python3 manage.py runserver для mac/linux
python manage.py runserver для windows
