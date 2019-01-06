# coding: utf-8

import os
import sys
import logging
from random import uniform
from time import sleep

device_x, device_y = 1920, 1080

logging.basicConfig(format='%(asctime)s %(message)s',
					datefmt='%m/%d/%Y %I:%M:%S %p',
					level=logging.DEBUG)

def tap_screen(pos):
	base_x, base_y = 1920, 1080
	x = int(float(pos[0]) / base_x * device_x + uniform(0, 10) - 5)
	y = int(float(pos[1]) / base_y * device_y + uniform(0, 10) - 5)
	os.system("adb shell input tap {} {}".format(x, y))


autoPos = [1780, 40]
skipPos = [1720, 80]
againPos = [1600, 980]
startPos = [1600, 970]
continuePos = [960, 540]

def work(times):
	# logging.debug('第1次刷副本...')
	logging.debug('-' * 20 + 'ROUND 1 START' + '-' * 20)
	logging.debug('#1' + ':闯关')
	tap_screen(startPos)
	sleep(25)

	logging.debug('#1' + ':跳过')
	tap_screen(skipPos)
	sleep(2)

	# logging.debug('点击自动按钮...')
	# tap_screen(autoPos)
	sleep(75)

	logging.debug('#1' + ':跳过')
	tap_screen(skipPos)
	sleep(10)

	logging.debug('#1' + ':跳过')
	tap_screen(skipPos)
	sleep(7)

	logging.debug('#1' + ':任意处继续')
	tap_screen(continuePos)
	sleep(5)

	logging.debug('-' * 20 + 'ROUND 1 END' + '-' * 20)

	for i in xrange(1, times):
		# logging.debug('第{}次刷副本...'.format(i+1))

		logging.debug(str(i + 1) + ':再次挑战')
		tap_screen(againPos)
		sleep(8)

		logging.debug('-' * 20 + 'ROUND ' + str(i + 1) + ' START' + '-' * 20)

		logging.debug('#' + str(i + 1) + ':闯关')
		tap_screen(startPos)
		sleep(25)

		logging.debug('#' + str(i + 1) + ':跳过')
		tap_screen(skipPos)
		sleep(2)

		# logging.debug('点击自动按钮...')
		# tap_screen(autoPos)
		sleep(75)

		logging.debug('#' + str(i + 1) + ':跳过')
		tap_screen(skipPos)
		sleep(10)

		logging.debug('#' + str(i + 1) + ':跳过')
		tap_screen(skipPos)
		sleep(7)

		logging.debug('#' + str(i + 1) + ':任意处继续')
		tap_screen(continuePos)
		sleep(5)

		logging.debug('-' * 20 + 'ROUND ' + str(i + 1) + ' END' + '-' * 20)

if __name__ == '__main__':
	# 
	work(30)
		
