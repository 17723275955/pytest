import requests
import demjson
import random

class Write():
    def __init__(self):
        self.session=requests.session()

    def write1(self):
        url="http://192.168.1.125:8877/nurse/user/add"
        headers={'Content-Type': 'application/json;charset=UTF-8',
                 'auth-token': 'a80e78b9-2b47-48f6-a39d-8848f2ae4085'}
        for i in range(8011,8015):
            data={"jialandUserDTO":{"id":'null',"userName":f"李四{i}","jobNo":f"{i}","sex":f"{random.randint(0,1)}","orgId":f"{random.choice([187,189])}","roleId":[f'{random.choice([143,145,147,149])}'],
                                    "mobile":f"1371328{random.randint(1000,9000)}","email":f"{i}@qq.com","avatar":"","roleList":[{"roleId":f'{random.choice([143,145,147,149])}',"userId":'null'}]},
                  "nurseUserDTO":{"telephone":"1","birthDate":f"{random.choice(['1987-03-01','1997-03-02','1977-03-02','1967-03-02]'])}","nation":1,"age":5,"politicalOutlook":f"{random.randint(1,13)}",
                                  "marital":"1","cornet":"023","hjszd":'null',"province":'null',"registeredResidence":"11,1101","nativePlace":"12,1201","homeAddress":"云南","idNumber":"500234199710096398",
                                  "emergencyContact":f"麻子{i}","urgentPhone":"13713287934","urgentRelationship":"1","startingWorkDate":f"{random.choice(['2021-03-09','2011-03-09','2001-03-09','1991-03-09','1951-03-09'])}"
                      ,"startingHospitalDate":f"{random.choice(['2021-03-09','2011-03-09','2001-03-09','1991-03-09','1951-03-09'])}","contractEndDate":"2023-03-06","rehireDate":"2023-03-08","nurseNature":f"{random.randint(1,5)}",
                                  "bank":"1","bankCardNo":"6222031202013763155","clothingNumber":"2","capNumber":"2","shoesNumber":"3","height":"175","rostering":"1","checkWork":"1","nightAccess":"1","specialAccess":"1","teachingQualification":"1",
                                  "postTrainingGrade":f"{random.choice([1967,2011,1997,1987,2005,2015])}","professionalCategory":f"{random.randint(1,5)}","nursingAgeDate":"2019-03-13","huling":4,"nurseTitle":f"{random.randint(1,5)}",
                                  "post":f"{random.randint(1,4)}","nursingLevel":f"{random.randint(1,4)}","specialistNurse":"1","notIncludedNursing":"2","picUrl":'null'}}
            res=self.session.post(url=url,headers=headers,data=demjson.encode(data))
            res=res.content.decode()
            print(res)
if __name__ == '__main__':
    Write().write1()
# s=random.choice(['2018-03-01','2018-03-02'])
# print(s)