import random
import time

import pymssql

class MSSQL:
    """
    对pymssql的简单封装
    pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启

    用法：

    """
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        """
        执行非查询语句
        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()


    def test(self):
        frequency_code={'QD':'1',"BID":"2","TID":'3','QOD':'4','BIW':'5','Q6H':'6','Q4H':'7','QW':'8','ST':'9','PRN':'10','Q8H':'11','Q12H':'12','QN':'13','QID':'17'}
        re=['QD',"BID","TID",'QOD','BIW','Q6H','Q4H','QW','ST','PRN','Q8H','Q12H','QN','QID']
        s=random.choice(re)
        # print(s,frequency_code[f'{s}'])
        return s,frequency_code[f'{s}']




def main():
    ## ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
    ## #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    ## ms.ExecNonQuery("insert into WeiBoUser values('2','3')")

    supply_code = (1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 14, 16, 17, 18, 28, 32, 33, 42, 49, 56, 61)
    frequency_code={'QD':'1',"BID":"2","TID":'3','QOD':'4','BIW':'5','Q6H':'6','Q4H':'7','QW':'8','ST':'9','PRN':'10','Q8H':'11','Q12H':'12','QN':'13','QID':'17'}
    re=['QD',"BID","TID",'QOD','BIW','Q6H','Q4H','QW','ST','PRN','Q8H','Q12H','QN','QID']
    s=random.choice(re)

    supply_name={'口服':'1',"静滴":'2','静推':'3','肌注':'4','外用':'5','雾化':'6','直肠给药':'8','微泵':'10','皮下注射':'11','滴眼':'12','皮内注射':'14','腹腔滴注':'16','吸入':'17','喷入':'18',
                 '局封':'28','治疗':'32','冲管用':'42','灌肠':'49','局部浸润':'56','覆膜透析':'61'
                 }

    rs=['口服',"静滴",'静推','肌注','外用','雾化','直肠给药','微泵','皮下注射','滴眼','皮内注射','腹腔滴注','吸入','喷入','局封','治疗','冲管用','灌肠','局部浸润','覆膜透析']
    s1=random.choice(rs)
    # print(s1,supply_name[f'{s1}'])

    order_class1={'a':"西药,中成药",'b':"暂无",'c':"检查",'d':"检验",'e':"治疗",'f':'手术','i':'膳食'}
    order_class = ['a', 'b', 'c', 'd', 'e', 'f', 'i']
    s2=random.choice(order_class)

    # order_class = ('a', 'b', 'c', 'd', 'e', 'f', 'i')
    gwyw = (1, 2)
    order_name=('房颤','心电监护','血氧饱和度监测','测血压','葡萄糖测定（床边）','吸痰护理','记尿量','记出入量','高危压疮防范护理','VTE风险评估','VTE风险评估 [低危]','VTE风险评估 [中危]','VTE风险评估 [高危]',
                '鼻导管吸氧','留置导尿','深静脉置管护理(长期血透导管)','深静脉置管护理(临时血透导管)','深静脉置管护理(CVC)','深静脉置管护理(PICC)')
    order_class_name=('西药、中成药','检验','检查','治疗','手术','膳食')
    high_risk=(0,1)
    ss=('临时医嘱','长期医嘱')
    '''
    数据库新增数据
    '''

    ms = MSSQL(host="192.168.1.220", user="sa", pwd="Zjsk@123456", db="testdb_qjy")
    case=random.choice(order_name)
    resList = ms.ExecNonQuery(f"INSERT INTO dbo.v_zhongjia_inpatient_order VALUES ('{random.randint(385641760,385650760)}','{random.randint(385640760,385649760)}',   N'{random.randint(199710,202010)}_01',N'{case}', N'{case}',  N'7437556',N'1', N'01278096', N'365  ', N'+7  ', N'365', N'90mg*10粒', '{s}', '{frequency_code[f'{s}']}', N'90', N'mg', N'{supply_name[f'{s1}']}',N'{s1}',  N'在用', '{s2}', N'{order_class1[f'{s2}']}', N'{random.choice(ss)}', '{random.choice(high_risk)}', NULL, N'0', N'0', N'0', N'{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}', N'{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}', N'{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}', N'黄宇', NULL, NULL, NULL, NULL, NULL, '{random.choice(gwyw)}', NULL, N'1', N'0')")
    print('数据添加中')
def main_remove():
    '''
       数据库删除数据
    '''
    ms = MSSQL(host="192.168.1.220", user="sa", pwd="Zjsk@123456", db="testdb_qjy")
    resList = ms.ExecNonQuery("delete from dbo.v_zhongjia_inpatient_order where doctor_name like N'%黄%'")
    print('数据删除成功')
if __name__ == '__main__':
    for i in range(2):
        main()
