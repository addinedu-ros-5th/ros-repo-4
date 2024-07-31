# final_project
***
### 빌드시 주의사항
#### 0. humble (로스환경불러오기)
#### 1. Local로 clone or pull했을 때, log, install, build 삭제 src파일만 남겨둠

#### 2. workspace에서 의존성 자동 설치
rosdep install --from-paths src --ignore-src -r -y

#### 3. colcon build
***

### AWS RDS 상 DB 정보 로컬에 저장
```
~/dev_ws/git_ws$ mysqldump -h database-1.cdigc6umyoh0.ap-northeast-2.rds.amazonaws.com -P 3306 -u root -p DFC_system_db > DFC_system_db.sql
Enter password: 슬랙에 있는 AWS RDS PW: xxxxxx
```
### 로컬 디렉토리에 해당하는 sql 파일 로컬 MYSQL에 import
```
~/dev_ws/git_ws$ mysql -u root -p
Enter password: 본인 로컬 MYSQL PW
```

```
mysql > create database DFC_system_db;
mysql > use DFC_system_db;
mysql > SOURCE DFC_system_db.sql 위치한 절대 경로;
mysql > show tables;
```
