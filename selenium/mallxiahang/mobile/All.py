from all_product import all_product 
from group_order import group_order
from score_mall import score_mall 
from crowd_list import crowd_list 
from pickup import pickup 

from package_manage import *

if __name__ == '__main__':
	driver = webdriver.Chrome()
	Start().config_driver(driver) 
	
	all_product(driver) # 全部商品
	group_order(driver) # 团购列表
	# score_mall(driver) # 积分商城
	crowd_list(driver) # 众筹列表
	pickup(driver) # 提货券
