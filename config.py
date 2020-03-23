# coding=utf-8

import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))


#DEBUG参数配置
DEBUG_CACHE_DIR = PROJECT_PATH + "/cache/"
DEBUG_REPORT_CACHE = True


#防御型策略配置
DEFENSIVE_PE_LIMIT = 15 #防御型策略 - 市盈率指标
DEFENSIVE_FOUNDING_TIME_LIMIT = 10 #防御型策略 - 创办时长指标
DEFENSIVE_PROFIT_YEAR_LIMIT = 5 #防御型策略 - 持续盈利时长指标


#积极型策略配置
POSITIVE_PE_LIMIT = 9 #积极型策略 - 市盈率指标
POSITIVE_FOUNDING_TIME_LIMIT = 5 #积极型策略 - 创办时长指标
POSITIVE_PROFIT_YEAR_LIMIT = 5 #积极型策略 - 持续盈利时长指标




