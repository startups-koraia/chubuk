
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:23:09 2019


"""

import subprocess

# ./sp_firedetect 프로그램을 실행하고, 그 프로그램의 출력을 파이프로 연결한다.
process1 = subprocess.Popen("./sp_firedetect", stdout=subprocess.PIPE, shell=True)

# tail -f ../log/sp_firedetect_20230912.log 명령을 실행하고, 그 프로그램의 출력을 파이프로 연결한다.
process2 = subprocess.Popen("tail -f ../log/sp_firedetect_20230913.log", stdout=subprocess.PIPE, shell=True)

# process1과 process2 중 하나라도 종료되면 루프를 빠져나온다.
while True:
    output = process2.stdout.readline()
    if b'start capture.read(frame)' in output:
        print("program exit.")
        # 영어로 첫번째 프로세스가 종료되었다는 메시지를 출력한다.
        break
    if output:
        print(output.strip())