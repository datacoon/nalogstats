# Работаем с налоговой статистикой в примерах

## Зачем это нужно?

Этот код предназначен для преобразования данных из налоговой статистики в простые ряды чисел. 
Скрипт nalogstats.py обрабатывает отчёты ФНС России в Excel по регистрации юридических лиц и ИП и выбирает оттуда данные:
* число зарегистрированных юрлиц
* число юрлиц прекративных деятельность
* число зарегистрированных ИП
* число ИП прекративших деятельность

Всё это рассматривается в разрезе годов с 2012 по 2018 и субъектов федерации
Скрипт сохраняет в файлы nalog_rosfed.csv статистику по РФ и в nalog_regions.csv статистику по всем субъектам федерации

## Что с этим делать?
Можно доработать и считать статистику по месяцам, например. Можно доработать и смотреть на разные причины регистрации и прекращения деятельности, 
можно дополнить данными и поискать корреляции. 

## Откуда данные?

Официальная статистика регистрации юридических лиц и индивидуальных предпринимателей публикуется на сайте ФНС России http://nalog.ru в соответствующем разделе.
