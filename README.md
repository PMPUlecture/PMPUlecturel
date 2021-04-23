# База зананий ПМ-ПУ

[![Django CI](https://github.com/PMPUlecture/PMPUlecture/actions/workflows/django.yml/badge.svg?branch=for_deploy&event=push)](https://github.com/PMPUlecture/PMPUlecture/actions/workflows/django.yml)

Web-сервис для хранения учебных материалов и использование их другими студентами. 

![IMG](https://i.imgur.com/H0Xwh0E.png)

Основные фичи: 
- Навигация по семестрам
- Ссылки на страницы преподавателей на сайте факультета
- Группировка материалов по группам
- Возможность добавлять материалы всем студентам
- Возможность скрывать некоторые материалы от незарегестрированных пользователей 
- SPA (Single Page Application)
- Поиск преподавателей по имени

Сервис был создан в учебных целях как проек для дисциплины Языки программирования.

## Запуск

### Установка ПО

Для запуска сервера необходим Python3, а для разработки фронтэнда - node.js и Vue.js
 
### Установка зависимостей

#### *Python*

В папке проекта запустить команды.

```bash
$ pip install -r requirements.txt
```
**Внимание** Для запуска проекта на локальном сервере используется база данных SQLite. Однако при развёртывании на сервере используется PostgreSQL. Если на вашем компьютере не настроена база данных PostgreSQL, может не установиться зависимости `psycopg2, pytz, sqlparse`. Удалите эти строчки из файла `requirements.txt` и повторите попытку.

Для настройки базы данных:

```bash
$ python manage.py makemigrations; python manage.py migrate; python manage.py createsuperuser 
```

Будут запрошены почта и пароль для создания суперпользователя.

#### *Vue.js*

Для установки зависимостей используется **npm**.

Перейдите в директорию `frontend/PMPU/` и выполните команды: 

```bash
$ npm install -i
```
Для запуска сервера для разработки 
```
$ npm run dev
```

Для сборки проекта 

```
$ ./build.sh
```
 
## Документация для API

Всю необходимую документацию для работы с API сайта вы найдете на [WIKI странице](https://github.com/PMPUlecture/PMPUlecture/wiki/API)
