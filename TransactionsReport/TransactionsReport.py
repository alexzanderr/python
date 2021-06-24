
import json
from core.system import *
from core.aesthetics import *

project_path = r"TransactionsReport"
TransactionsJSON = json.loads(open(project_path + "\\transactions.json").read())
username = "Alexandru Andrew"

# sorting the transactions
for month in TransactionsJSON:
    month["transactions"].sort(key=lambda tran: int(tran["date"].split(".")[0]))

print()
print(ConsoleColored("TRANSACTIONS REPORT:\n", "yellow", bold=True, underlined=True).center(80))

for month in TransactionsJSON:
    month_name = ConsoleColored(month["month_name"], "yellow", bold=True, underlined=True)
    print(month_name)
    for tran in month["transactions"]:
        sign = "+"
        color = "green"
        if tran["type"] == "outcome":
            sign = "-"
            color = "red"

        sign = ConsoleColored(sign, color)
        amount = ConsoleColored(str(tran["amount"]), color, bold=True)
        transaction_type = ConsoleColored(tran["type"], color, bold=True)
        items = tran["date"].split(".")
        day = int(items[0])
        year = items[2]
        date = "{} {} {}".format(day, month["month_name"], year)


        line_1 = "\t" + "Date".ljust(25) + username.ljust(20)
        line_1 += "{} {}".format(sign, amount).rjust(15)

        line_2 = "\t" + date.ljust(25) + transaction_type.ljust(20) + "RON".rjust(18)
        format_dim = len(delete_ansi_codes(line_2)) - 1
        print("\t" + "=" * format_dim)
        print(line_1)
        print(line_2)
    print("\t" + "=" * format_dim)
