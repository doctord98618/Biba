<h1 align="center">Biba</h1>

## Что это?
Подвязка GPT-4 бота Сидни с Бинга к Таверне

## Что можно?
Смут.</br>
По слованом анона 16-20к токенов.</br>
Кодинг с рабочим стримом (плюс в сравнении со скалой).</br>
Подтягивать данные из интернета.</br></br>
![image](https://github.com/Barbariskaa/Biba/assets/129290831/b5176621-4a1f-4b57-9c7f-865861825c30)</br></br>
Подтягивать подсказки из бинга (через /suggestion после указанного в URL режима).</br></br>
![image](https://user-images.githubusercontent.com/129290831/236729981-42f4cbf8-abbd-4deb-9a70-1a1cb5917119.png)

## Что по куму?
Ответы с сервера фильтруются посреди стрима, прямо как в чае. В среднем обрубает на 100 токенах и до нескольких сотен. Зависит от выбранного режима.<br>
Возможно это ограничение можно обойти, если повозиться с промптами.</br>
Также банят. Могут забанить за один день, в отличии от Слаки. Решается перерегом.</br>
С 29.05.2023г. на территории РФ работает только через VPN.

## Как поставить?
Нужны куки чата с Бингом.<br>
* Регистрируем учетку в Майкрософт.
* Заходим в сам чат с Бингом с Эджа. 

Если установлен не Windows с Эджем, то придется повозиться с юзерагентом. Можно поставить следующий ЮА:</br> `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51`</br></br>
Также, санкционным анонам придется повозиться с доступом к Бингу. Рекомендую использовать впн и чистить куки, затем искать в самом бинге Bing AI. Если нет кнопки перехода в чат, значит нужно либо чистить куки еще раз, либо пробовать другой айпи впна.</br></br>
![image](https://user-images.githubusercontent.com/129290831/236732426-91d87aa3-32e2-4f87-9758-ac5c4b222a71.png) </br>
Ссылка на чат по которой доступен Бинг в случае успешной настройки: https://www.bing.com/search?q=Bing+AI&showconv=1&wlsso=0 </br>

После успешного захода и открытия чата, нужно экспортировать сами куки. Для этого нужен следующий плагин:
* Хром/Эдж: https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm
* Лиса: https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/

Открываем расширение. 
* Жмем export, выбираем как `Export as JSON`. Куки сохранятся в буфер.
* Сливаем в cookies.json рядом с самим скриптом. 
* Затем запускаем сам скрипт через батник. 
 
После этого должно заработать.

# Отдельные упоминания и благодарности
https://github.com/acheong08/EdgeGPT</br>
https://github.com/InterestingDarkness/EdgeGPT</br>
