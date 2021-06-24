"""
    this python file needs to be run in the
    interactive python in terminal
"""

imports = \
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2 as cv
import pytz

import core
from core.datetime__ import *
from core.json__ import *
from core.numbers__ import *
from core.path__ import *
from core.random__ import *
from core.selenium__ import *
from core.winapi__ import *
from core.zip__ import *

from core.collections__ import *
from core.gui import *
from core.sounds import *

from core.audio import *
from core.aesthetics import *
from core.algorithms import *
from core.animations import *
from core.backtracking import *
from core.development import *
from core.download import *
from core.drive import *
from core.exceptions import *
from core.image import *
from core.pdf import *
from core.romania import *
from core.statistics import *
from core.weather import *
"""
exec(imports)

print(imports. \
    replace("core", yellow_bold("core")). \
    replace("import", red_bold("import")). \
    replace("from", red_bold("from")))
print()
print(f"Python: {get_python_version()}")
print(f"{green('Welcome')} to {yellow('Python Iteractive')}\na better version where you have everything")
print(f"all packages that you need are imported :)\n")
