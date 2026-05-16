import unittest

import allure

from api.http_client import ApiClient


@allure.epic("feed_system")
@allure.feature("System")
@allure.story("Health check")
class TestHealth:
    @allure.title("health 接口返回服务健康状态")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_health_returns_ok(self, api_client: ApiClient) -> None:
        with allure.step("发送 GET /health 请求"):
            response = api_client.get("/health")

        with allure.step("校验 HTTP 状态码"):
            assert response.status_code == 200

        with allure.step("校验响应体"):
            body = response.json()
            assert body["code"] == 0
            assert body["message"] == "ok"
            assert body["data"]["status"] == "ok"


if __name__ == "__main__":
    unittest.main()
