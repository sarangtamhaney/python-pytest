import subprocess

# set report type to allure or pytest
report_type = "pytest"

if report_type == "pytest":
    # for pytest report
    subprocess.run(["python", "-m", "pytest", "--html=reports/report.html", "--self-contained-html"])
else:
    # for allure report
    subprocess.run(["python", "-m", "pytest", "--alluredir=reports/allure"])
    subprocess.run(["allure", "serve", "reports/allure"])

