# MUIV-Telegram-schedule-bot
Here is my MUIV telegram schedule bot

Отчет по проекту "Telegram Бот расписание для университета"

ВВЕДЕНИЕ

Цель данного проекта - создание Telegram бота, который будет предоставлять студентам университета информацию о расписании занятий.

ОСНОВНАЯ ЧАСТЬ

ТЕХНОЛОГИЧЕСКАЯ ЗАДАЧА

1.1 Список решаемых задач

Разработка и написание кода для бота на языке программирования Python
Подключение к API Telegram для работы с ботом
Разработка базы данных для хранения информации о расписании
Создание интерфейса для взаимодействия со студентами
Организация процесса обновления расписания
1.1.1 Подключаемые модули, платформы и т.д.

Для реализации проекта были использованы следующие модули и платформы:

Python 3.9
PyTelegramBotAPI
SQLite
1.2 РЕАЛИЗУЕМАЯ АРХИТЕКТУРА

1.2.1 Модули программы, функции, структуры данных

Модули программы:

bot.py - основной модуль, содержащий код для работы бота
database.py - модуль, содержащий функции для работы с базой данных
Функции:

send_message - отправка сообщения пользователю
get_schedule - получение расписания занятий из базы данных
update_schedule - обновление расписания занятий в базе данных
Структуры данных:

Таблица schedule - хранение расписания занятий в базе данных
Описания и диаграммы
ОПИСАНИЕ РАБОТЫ

1.3 Экран приложения

Бот имеет несколько экранов:

Главное меню - пользователь может выбрать день недели, чтобы получить расписание на этот день
Экран с расписанием - здесь отображается расписание занятий на выбранный день
Экран обновления расписания - администратор может загрузить новое расписание из файла или с помощью парсера
ВЫВОДЫ

В результате выполнения проекта был создан Telegram бот, который может помочь студентам университета получать актуальную информацию о расписании занятий. Бот имеет простой и интуитивно понятный интерфейс, который позволяет пользователям легко получать необходимую информацию.

БИБЛИОГРАФИЯ

Официальная документация PyTelegramBotAPI: https://github.com/eternnoir/pyTelegramBotAPI

