# Описание
###Для запуска сервиса:
```sh
pip install -r requirements.txt
python main.py
```
###Настройки
все ключевые настройки включая желаемое количество потоков.
Находятся в файле ".env"
###Дополнительно
В проекте есть дополнительный endpoint "/processing/body".
Который поддерживает метод POST и принимает bytes в поле body.
Ничем не отличается от endpoint "/processing/video".


В задании я использовал библиотеке imageAI ("https://imageai.readthedocs.io/en/latest/index.html") которая требует наличие yolo.h5 файла который весит больше чем 100мб.
По требованию github я не могу его запушить, зато могу скачать при старте:)
В качестве сервиса используется flask-restx.
В качестве сохранения состояния video я использовал sqlite
Тесты к сожелению не успеваю написать:(