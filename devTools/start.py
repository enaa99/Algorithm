# 1.
# a = 2

# for i in range(2):
#     for i in range(1,10):
#         if i == 4: continue
        
#         print(f"{a} * {i} = {a*i}",end = '  ' if a*i < 10 else ' ' )
#         print(f"{a+1} * {i} = {(a+1)*i}",end = '  ' if (a+1)*i < 10 else ' ' )
#         print(f"{a+2} * {i} = {(a+2)*i}",end = '  ' if (a+2)*i < 10 else ' ' )
#         print(f"{a+3} * {i} = {(a+3)*i}")
#     print()
#     a += 4


# 2.

# SELECT DEPTNO AS 부서번호, COUNT(DEPTNO) AS 근무자수, SUM(SAL) AS 급여합
# FROM EMP
# GROUP BY DEPTNO
# ORDER BY DEPTNO DESC;


# 3.
# SELECT a.DEPTNO AS 부서번호, 부서명, COUNT(a.DEPTNO) AS 근무자수, SUM(a.SAL) AS 급여합
# FROM EMP as a
# LEFT JOIN DEPT as b
# ON a.DEPTNO = b.DEPTNO
# GROUP BY DEPTNO
# ORDER BY DEPTNO DESC;



# 4.
#     1 .select * from table A inner join table b on a.key = b.key
#     2. select * from table a left join table b on a.key=b.key
#     3. select * from table a left join table b on a.key = b.key where b.key is null
#     4. select * from table a full outer join table b on a.key = b.key 
#     where a.key is null or b.key is null
#     5. select * from table a full outer join table b on a.key = b.key
    

# 5.
#     void swap(int*p, int*q)
#     {
#         int tmp = *p;
#         *p = *q;
#         *q = tmp;
        
#     }
