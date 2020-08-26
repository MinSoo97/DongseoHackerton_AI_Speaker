#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import print_function
import ex2_getVoice2Text as STT
import pymysql.cursors

# a is if parameter
a = 0
# i is while parameter
i = 1
while(i):
    conn = pymysql.connect(host='localhost', user='user', password='******', db='zolzac_DB', charset='utf8mb4')
    print("*********************************************************************")
    print("1. 오케이 구글")
    print("******************************날씨************************************")
    print("2. 날씨 어때? 3. 비 와? 4. 미세먼지 어때?")
    print("******************************날짜************************************")
    print("5. 오늘 몇일이야? 6. 지금 몇 시야?")
    print("******************************음악************************************")
    print("7. 음악 틀어줘 8. 다음 곡 재생 9. 이전 곡 재생 10. 노래 꺼 ")
    print("******************************볼륨************************************")
    print("11. 볼륨 높여줘 12. 볼륨 줄여줘")
    print("******************************종료************************************")
    print("프로그램 종료를 하실려면 ctrl + c 누르세요")
    a = int(input())
    data = ""
    if a==1:
        # CALL STT
        data = STT.getVoice2Text()
        with conn.cursor() as cursor:
            sql1 = 'select * from google where name = %s'
            cursor.execute(sql1,(data))
            rows = cursor.fetchall()
            if rows == ():
                #SQL insert into giga
                sql = 'insert into google(name) values (%s)'
                cursor.execute(sql,(data))
                # DATA SAVE
                conn.commit()
                conn.close()
                # Exception handling (data = null)
                if cursor.rowcount==0:
                    print("데이터를 입력하지 못했어요")
        continue
    if a==2:
        # CALL STT
        data = STT.getVoice2Text()
        with conn.cursor() as cursor:
            sql1 = 'select * from weather where name = %s'
            cursor.execute(sql1,(data))
            rows = cursor.fetchall()
            if rows == ():
                #SQL insert into giga
                sql = 'insert into weather(name) values (%s)'
                cursor.execute(sql,(data))
                # DATA SAVE
                conn.commit()
                conn.close()
                # Exception handling (data = null)
                if cursor.rowcount==0:
                    print("데이터를 입력하지 못했어요")
        continue
    if a==3:
        # CALL STT
        data = STT.getVoice2Text()
        with conn.cursor() as cursor:
            sql1 = 'select * from rain where name = %s'
            cursor.execute(sql1,(data))
            rows = cursor.fetchall()
            if rows == ():
                #SQL insert into giga
                sql = 'insert into rain(name) values (%s)'
                cursor.execute(sql,(data))
                # DATA SAVE
                conn.commit()
                conn.close()
                # Exception handling (data = null)
                if cursor.rowcount==0:
                    print("데이터를 입력하지 못했어요")
        continue
    if a==4:
        # CALL STT
        data = STT.getVoice2Text()
        with conn.cursor() as cursor:
            sql1 = 'select * from dust where name = %s'
            cursor.execute(sql1,(data))
            rows = cursor.fetchall()
            if rows == ():
                #SQL insert into giga
                sql = 'insert into dust(name) values (%s)'
                cursor.execute(sql,(data))
                # DATA SAVE
                conn.commit()
                conn.close()
                # Exception handling (data = null)
                if cursor.rowcount==0:
                    print("데이터를 입력하지 못했어요")
        continue
    if a==5:
        # CALL STT
        data = STT.getVoice2Text()
        with conn.cursor() as cursor:
            sql1 = 'select * from date where name = %s'
            cursor.execute(sql1,(data))
            rows = cursor.fetchall()
            if rows == ():
                #SQL insert into giga
                sql = 'insert into date(name) values (%s)'
                cursor.execute(sql,(data))
                # DATA SAVE
                conn.commit()
                conn.close()
                # Exception handling (data = null)
                if cursor.rowcount==0:
                    print("데이터를 입력하지 못했어요")
        continue
    if a==6:
        # CALL STT
        data = STT.getVoice2Text()
        with conn.cursor() as cursor:
            sql1 = 'select * from time where name = %s'
            cursor.execute(sql1,(data))
            rows = cursor.fetchall()
            if rows == ():
                #SQL insert into giga
                sql = 'insert into time(name) values (%s)'
                cursor.execute(sql,(data))
                # DATA SAVE
                conn.commit()
                conn.close()
                # Exception handling (data = null)
                if cursor.rowcount==0:
                    print("데이터를 입력하지 못했어요")
        continue 
    if a==7:
        # CALL STT
        data = STT.getVoice2Text()
        with conn.cursor() as cursor:
            sql1 = 'select * from music where name = %s'
            cursor.execute(sql1,(data))
            rows = cursor.fetchall()
            if rows == ():
                #SQL insert into giga
                sql = 'insert into music(name) values (%s)'
                cursor.execute(sql,(data))
                # DATA SAVE
                conn.commit()
                conn.close()
                # Exception handling (data = null)
                if cursor.rowcount==0:
                    print("데이터를 입력하지 못했어요")
        continue
    if a==8:
        # CALL STT
        data = STT.getVoice2Text()
        with conn.cursor() as cursor:
            sql1 = 'select * from next where name = %s'
            cursor.execute(sql1,(data))
            rows = cursor.fetchall()
            if rows == ():
                #SQL insert into giga
                sql = 'insert into next(name) values (%s)'
                cursor.execute(sql,(data))
                # DATA SAVE
                conn.commit()
                conn.close()
                # Exception handling (data = null)
                if cursor.rowcount==0:
                    print("데이터를 입력하지 못했어요")
        continue
    if a==9:
        # CALL STT
        data = STT.getVoice2Text()
        with conn.cursor() as cursor:
            sql1 = 'select * from pre where name = %s'
            cursor.execute(sql1,(data))
            rows = cursor.fetchall()
            if rows == ():
                #SQL insert into giga
                sql = 'insert into pre(name) values (%s)'
                cursor.execute(sql,(data))
                # DATA SAVE
                conn.commit()
                conn.close()
                # Exception handling (data = null)
                if cursor.rowcount==0:
                    print("데이터를 입력하지 못했어요")
        continue
    if a==10:
        # CALL STT
        data = STT.getVoice2Text()
        with conn.cursor() as cursor:
            sql1 = 'select * from stop where name = %s'
            cursor.execute(sql1,(data))
            rows = cursor.fetchall()
            if rows == ():
                #SQL insert into giga
                sql = 'insert into stop(name) values (%s)'
                cursor.execute(sql,(data))
                # DATA SAVE
                conn.commit()
                conn.close()
                # Exception handling (data = null)
                if cursor.rowcount==0:
                    print("데이터를 입력하지 못했어요")
        continue
    if a==11:
        # CALL STT
        data = STT.getVoice2Text()
        with conn.cursor() as cursor:
            sql1 = 'select * from up where name = %s'
            cursor.execute(sql1,(data))
            rows = cursor.fetchall()
            if rows == ():
                #SQL insert into giga
                sql = 'insert into up(name) values (%s)'
                cursor.execute(sql,(data))
                # DATA SAVE
                conn.commit()
                conn.close()
                # Exception handling (data = null)
                if cursor.rowcount==0:
                    print("데이터를 입력하지 못했어요")
        continue
    if a==12:
        # CALL STT
        data = STT.getVoice2Text()
        with conn.cursor() as cursor:
            sql1 = 'select * from down where name = %s'
            cursor.execute(sql1,(data))
            rows = cursor.fetchall()
            if rows == ():
                #SQL insert into giga
                sql = 'insert into down(name) values (%s)'
                cursor.execute(sql,(data))
                # DATA SAVE
                conn.commit()
                conn.close()
                # Exception handling (data = null)
                if cursor.rowcount==0:
                    print("데이터를 입력하지 못했어요")
        continue
