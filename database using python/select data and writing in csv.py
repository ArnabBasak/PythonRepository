import pymysql
import csv
#database connection for world database
connworld =  pymysql.connect(host = "localhost",user = "root",password = "baban123",db = "world")

#selecting data from table city
curcity_world = connworld.cursor()
curcity_world.execute("select * from city")
resultcity_world = curcity_world.fetchall()
myfilecity_world = csv.writer(open('E:/python programs/database using python/world_city.csv','w',encoding = 'utf-8'))
col_names = [i[0] for i in curcity_world.description]
myfilecity_world.writerow(col_names)
myfilecity_world.writerows(resultcity_world)
print("world_city.csv file has been written")

#selecting data from table country
curcountry_world = connworld.cursor()
curcountry_world.execute("select * from country")
resultcountry_world = curcountry_world.fetchall()
myfilecountry_world = csv.writer(open('E:/python programs/database using python/world_country.csv','w',encoding = 'utf-8'))
col_names = [i[0] for i in curcountry_world.description]
myfilecountry_world.writerow(col_names)
myfilecountry_world.writerows(resultcountry_world)
print("world_country.csv file has been written")

#selecting data from table countrylanguage
curCL_world = connworld.cursor()
curCL_world.execute("select * from countrylanguage")
resultCL_world = curCL_world.fetchall()
myfileCL_world = csv.writer(open('E:/python programs/database using python/world_countrylanguage.csv','w',encoding = 'utf-8'))
col_names = [i[0] for i in curCL_world.description]
myfileCL_world.writerow(col_names)
myfileCL_world.writerows(resultCL_world)
print("world_countrylanguage.csv file has been written")
connworld.close()


#dattabase connection for world2 databasse
connworld2 = pymysql.connect(host = "localhost",user = "root",password = "baban123",db = "world2")

#selecting data from table city
curcity_world2 = connworld2.cursor()
curcity_world2.execute("select * from city")
resultcity_world2 = curcity_world2.fetchall()
myfilecity_world2 = csv.writer(open('E:/python programs/database using python/world2_city.csv','w',encoding = 'utf-8'))
col_names = [i[0] for i in curCL_world.description]
myfilecity_world2.writerow(col_names)
myfilecity_world2.writerows(resultcity_world2)
print("world2_city.csv file has been written")


#selecting data from table country
curcountry_world2 = connworld2.cursor()
curcountry_world2.execute("select * from country")
resultcountry_world2 = curcountry_world2.fetchall()
myfilecountry_world2 = csv.writer(open('E:/python programs/database using python/world2_country.csv','w',encoding = 'utf-8'))
col_names = [i[0] for i in curcountry_world2.description]
myfilecountry_world2.writerow(col_names)
myfilecountry_world2.writerows(resultcountry_world2)
print("world2_country.csv file has been written")


#selecting data from table countrylanguage
curCL_world2 = connworld2.cursor()
curCL_world2.execute("select * from countrylanguage")
resultCL_world2 = curCL_world.fetchall()
myfileCL_world2 = csv.writer(open('E:/python programs/database using python/world2_countrylanguage.csv','w',encoding = 'utf-8'))
col_names = [i[0] for i in curCL_world2.description]
myfileCL_world2.writerow(col_names)
myfileCL_world2.writerows(resultCL_world2)
print("world2_countrylanguage.csv file has been written")
connworld2.close()


