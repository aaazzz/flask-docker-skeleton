# 
# @file error_definition.py
# 
# @brief 
# 
# @version 0.9.0
# @date 14-Aug. 2019
# @copyright Copyright (c) 2019
# 
from enum import Enum

# Result Difinition
class Result(Enum):
    NO_MODEL=1
    NO_DOCS=2
    NO_CORPUS=3
    WRONG_INPUT=4
    SOMETHING_WRONG=5
    SUCCESS=6
    NO_DICTIONARY=7
    NO_TOPICS=8
    SAME_DOC=9
    NO_NUM_TOPICS=10

