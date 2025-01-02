# these functionality used frequently in ur code that's why write it in this file 

import os
from box.exceptions import BoxValueError 
import yaml
from GarbageCassification import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64