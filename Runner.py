import os
import argparse


def run(report_type):
    if report_type == "pytest":
        # for pytest report
        os.system("python -m pytest --html=reports/report.html --self-contained-html")
    if report_type == "allure":
        # for allure report
        os.system("python -m pytest --alluredir=reports/allure")


# Pass --report_type through cli command
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--report_type", help="set report type to allure or pytest", type=str)
    args = parser.parse_args()
    run(args.report_type)

# For viewing the allure report
# os.system("allure serve reports/allure")