import pytest

def test_status_code_200(api_get, default_params):
    """API должно отвечать статусом 200"""
    response = api_get(default_params)

    assert response.status_code == 200


def test_response_is_json(api_get, default_params):
    """Ответ должен быть в формате JSON"""
    response = api_get(default_params)

    assert response.headers["Content-Type"].startswith("application/json")


def test_search_python_returns_results(api_get, default_params):
    """Поиск 'Python' должен вернуть хотя бы один результат"""
    params = {
        **default_params,
        "list": "search",
        "srsearch": "Python"
    }

    response = api_get(params)
    data = response.json()

    assert len(data["query"]["search"]) > 0


def test_search_result_contains_title(api_get, default_params):
    """Каждый результат поиска должен содержать поле title"""
    params = {
        **default_params,
        "list": "search",
        "srsearch": "Python"
    }

    response = api_get(params)
    first_result = response.json()["query"]["search"][0]

    assert "title" in first_result
    assert first_result["title"] != ""


def test_search_nonsense_returns_empty_list(api_get, default_params):
    """Поиск бессмысленного слова должен вернуть пустой список"""
    params = {
        **default_params,
        "list": "search",
        "srsearch": "asdkfjhasdkjfhakjsdhf"
    }

    response = api_get(params)
    data = response.json()

    assert data["query"]["search"] == []
