# BOT AGENT (iOS)
# ----------------------------------------------------------------------------

import os

CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
PROJECT_DIR = "agent/"

# ----------------------------------------------------------------------------
# Screenshot

DATA_DIR = "data/"
IMAGE = "screen.png"
IMAGE_DIR = PROJECT_DIR + DATA_DIR + IMAGE


# ----------------------------------------------------------------------------
# Params

# iphone X: 0.00125
# iphone 6/7: 0.0021
TIME_COEFF = 0.0021
