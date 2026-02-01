<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Wikipedia API Autotests</title>
</head>
<body>

<h1>Wikipedia API Autotests (pytest + requests)</h1>

<p>
    Pet-проект с API-автотестами для Wikipedia.
    Тесты написаны на <strong>Python</strong> с использованием
    <strong>pytest</strong> и <strong>requests</strong>.
    Проект собран аккуратно и максимально приближен к реальному рабочему.
</p>

<p>
    Используются pytest-fixtures, учтены реальные ограничения API
    (обязательный <code>User-Agent</code>), добавлены позитивные и негативные сценарии.
    Репозиторий можно склонировать и запустить локально без дополнительной настройки.
</p>

<h2>Что проверяют тесты</h2>

<ul>
    <li>API доступен и отвечает <code>200 OK</code></li>
    <li>Ответ приходит в формате JSON</li>
    <li>Поиск по валидному запросу возвращает результаты</li>
    <li>Результаты содержат обязательное поле <code>title</code></li>
    <li>Поиск по несуществующему запросу возвращает пустой список</li>
</ul>

<p>
    <em>
        Проект воспроизводится через <code>git clone</code> и запуск
        <code>pytest</code>.
    </em>
</p>

</body>
</html>
