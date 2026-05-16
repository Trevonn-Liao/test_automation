from pathlib import Path
import shutil
import subprocess
import sys

import pytest


PROJECT_ROOT = Path(__file__).resolve().parent
ALLURE_RESULTS_DIR = PROJECT_ROOT / "reports" / "allure-results"
ALLURE_REPORT_DIR = PROJECT_ROOT / "reports" / "allure-report"


if __name__ == "__main__":
    # 1. 运行 pytest。pytest.ini 里已经配置了:
    #    - 用例目录 tests
    #    - Allure 原始结果目录 reports/allure-results
    #    这里额外传入 tests 的绝对路径，是为了避免 IDE 工作目录不一致导致找不到用例。
    pytest_exit_code = pytest.main([
        str(PROJECT_ROOT / "tests"),
        "--clean-alluredir",
    ])

    # 2. 如果测试失败，直接退出。这样 IDE/命令行能正确看到失败状态。
    if pytest_exit_code != 0:
        sys.exit(pytest_exit_code)

    # 3. allure-pytest 只能生成 Allure 原始结果文件。
    #    要生成/打开 HTML 报告，本机还需要安装 Allure CLI，也就是 allure 命令。
    if shutil.which("allure") is None:
        print(f"Allure result files generated at: {ALLURE_RESULTS_DIR}")
        print("Allure CLI is not installed, so HTML report was not generated.")
        print("After installing Allure CLI, run: allure serve reports/allure-results")
        sys.exit(0)

    # 4. 根据 allure-results 生成静态 HTML 报告到 reports/allure-report。
    subprocess.run([
        "allure",
        "generate",
        str(ALLURE_RESULTS_DIR),
        "-o",
        str(ALLURE_REPORT_DIR),
        "--clean",
    ], check=True)

    # 5. 自动打开生成好的 HTML 报告。
    subprocess.run([
        "allure",
        "open",
        str(ALLURE_REPORT_DIR),
    ], check=True)
