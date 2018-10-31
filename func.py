import MySQLdb as db
import urllib
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

#download file
def dlf(us,ur,wp,fp,fn,ti):
    conn = db.connect("localhost", "root", "newpass", "wechat", charset='utf8' )
    cursor = conn.cursor()
    sql11 = "INSERT INTO download(user,time,url,webpath,filepath,fname) \
        VALUES ('%s', str_to_date(DATE_FORMAT(NOW(),'%%Y-%%m-%%d %%H:%%i:%%s'),'%%Y-%%m-%%d %%H:%%i:%%s'), '%s', '%s', '%s', '%s')" % \
        (us,ur,wp,fp,fn)
    sql12 = "update usertimes set times=times-'%d',dat=curdate() where '%s'=user" % (ti,us)
    cursor.execute(sql11)
    cursor.execute(sql12)
    conn.commit()
    conn.close();
    return 'done';

#get download file list
def gdlf(us):
    conn = db.connect("localhost", "root", "newpass", "wechat", charset='utf8' )
    cursor = conn.cursor()
    sql2 = "select user,DATE_FORMAT(time,'%%Y-%%m-%%d %%H:%%i:%%s'),url,webpath,filepath,fname from download where '%s'=user order by time desc" % (us)
    cursor.execute(sql2)
    results = cursor.fetchall()
    conn.close();
    return results;

#add message
# def mes(us,me):
#     conn = db.connect("localhost", "root", "newpass", "wechat", charset='utf8' )
#     conn.set_character_set('utf8')
#     cursor = conn.cursor()
#     cursor.execute('SET NAMES utf8;')
#     cursor.execute('SET CHARACTER SET utf8;')
#     cursor.execute('SET character_set_connection=utf8;')
#     me=me.encode("utf-8")
#     print me
#     me=urllib.quote(me)
#     print me
#     sql = "INSERT INTO messages(user,time,message) \
#        VALUES ('%s', NOW(), '%s')" % \
#        (us,me)
#     cursor.execute(sql)
#     me=urllib.unquote(me);
#     print me
#     me=me.decode("utf-8");
#     print me;
#     conn.commit();
#     sql2 = "select message from messages"
#     cursor.execute(sql2)
#     results = cursor.fetchall();
#     for row in results:
#         me=row[0];
#         print me+' '+me.decode("utf-8");
#         me=urllib.unquote(me);
#         print me;
#         me=urllib.unquote(me).decode("utf-8");
#         print me;
#     conn.close();
#     return 'done';


#get download times
def gdlt(us):
    conn = db.connect("localhost", "root", "newpass", "wechat", charset='utf8' )
    cursor = conn.cursor()
    try:
        sql1 = "select times from usertimes where '%s'=user" % (us)
        cursor.execute(sql1)
        results = cursor.fetchall();
        if len(results)==0:
            sql2 = "INSERT INTO usertimes(user,times,dat) \
            VALUES ('%s', 10, curdate())" % \
            (us)
            cursor.execute(sql2)
            conn.commit();
            conn.close();
            return 10;
        else:
            sql2="update usertimes set dat=curdate(),times=5 where '%s'=user and times<5 and dat<curdate()" % \
            (us)
            cursor.execute(sql2)
            conn.commit();
            conn.close();
            return results[0][0];
    except:
        conn.rollback();
        conn.close();
        return -233;

#use coupon
def uc(us,co):
    conn = db.connect("localhost", "root", "newpass", "wechat", charset='utf8' )
    cursor = conn.cursor()
    sql1 = "select times from coupon where '%s'=code and user is NULL" % (co)
    cursor.execute(sql1)
    results = cursor.fetchall();
    if len(results)==0:
        conn.close();
        return 'flase';
    else:
        ti=results[0][0];
        sql21 = "update coupon set user='%s' where '%s'=code" % (us,co)
        sql22 = "update usertimes set times=times+'%d' where '%s'=user" % (ti,us)
        cursor.execute(sql21);
        cursor.execute(sql22);
        conn.commit();
        conn.close();
        return 'true';

#delete download
def deldl(us,ti):
    print ti 
    print us
    conn = db.connect("localhost", "root", "newpass", "wechat", charset='utf8' )
    cursor = conn.cursor()
    sql1 = "select * from download where user='%s' and DATE_FORMAT(time,'%%Y-%%m-%%d %%H:%%i:%%s')='%s'" % (us,ti)
    cursor.execute(sql1)
    results = cursor.fetchall();
    if len(results)>0:
        sql2 = "delete from download where user='%s' and DATE_FORMAT(time,'%%Y-%%m-%%d %%H:%%i:%%s')='%s'" % (us,ti)
        cursor.execute(sql2)
        conn.commit();
        conn.close();
        return 'done';
    else:
        conn.close();
        return 'tan90';

#clean all
def cla(us):
    conn = db.connect("localhost", "root", "newpass", "wechat", charset='utf8' )
    cursor = conn.cursor()
    sql = "delete from download where '%s'=user" % (us)
    cursor.execute(sql)
    conn.commit();
    conn.close();
    return 'done';

#add coupon
def adc(co,ti):
    conn = db.connect("localhost", "root", "newpass", "wechat", charset='utf8' )
    cursor = conn.cursor()
    sql = "INSERT INTO coupon(code,user,times) values('%s',NULL,'%d')" % \
        (co,ti)
    cursor.execute(sql)
    conn.commit()
    conn.close();
    return 'done';


# def pmes():
#     conn = db.connect("localhost", "root", "newpass", "wechat", charset='utf8' )
#     cursor = conn.cursor()
#     sql = "select message from messages"
#     cursor.execute(sql)
#     results = cursor.fetchall();
#     for row in results:
#         print row[0];
#         print urllib.unquote(row[0]);
#         print urllib.unquote(row[0]).decode("gbk");
#     conn.close();
#     return 'done';