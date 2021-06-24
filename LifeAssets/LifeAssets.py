
from core.aesthetics import *

assets = [
    "<Every day is a beautiful day filled with hope from God! :)>",
    "<Rugaciunea inimii>",
    "<Fereste-te de rau si fa bine, cauta pacea si o urmeaza pe ea>",
    "<Fericit barbatul care nadajduieste intru Domnul>"
]

print()
print_yellow_bold(fancy_title.format(title="LIFE ASSETS").center(50, thicc_line))
print("\n" + thicc_line * 5 + "\n")
for asset in assets:
    print(asset)
    print("\n" + thicc_line * 5 + "\n")

print()