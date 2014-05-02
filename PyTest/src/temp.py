import csv

CUTOFF = 6

path = 'C:\Users\myeong\Desktop\GeoGame_data\cleaned_data.csv'
cnt_list = [[0 for x in xrange(9)] for x in xrange(100)]

with open(path, 'r') as csvfile:
    line = csv.reader(csvfile, delimiter=',')
    ids = []
    i = 0
    
    print "[id, all count, landmark cnt, address cnt, correct landmark, correct address, all familiarity]"
    for row in line:   
        if row[0] in ids:
            for k in cnt_list:
                if k[0]==row[0]:
                    if row[4]=="L":
                        k[2]+=1
                        if row[5]=='1':
                            k[4]+=1
                        if int(row[2])>=CUTOFF:
                            k[7]+=1 
                    else:
                        k[3]+=1
                        if row[5]=='1':
                            k[5]+=1
                        if int(row[2])>=CUTOFF:
                            k[8]+=1
                    k[1] += 1
                    k[6] += int(row[2])
                    break
        else:
            ids.append(row[0])
            cnt_list[i][0] = row[0]
            cnt_list[i][1] += 1  
            cnt_list[i][6] = int(row[2])#familiarity          
            if row[4]=="L": 
                cnt_list[i][2]+=1       #landmark answers
                if int(row[2])>=CUTOFF:
                    cnt_list[i][7]+=1                
                if row[5]=='1':
                    cnt_list[i][4]+=1   #correctness
            else:
                cnt_list[i][3]+=1
                if int(row[2])>=CUTOFF:
                    cnt_list[i][8]+=1
                if row[5]=='1':
                    cnt_list[i][5]+=1
            i+=1
    
    for c in cnt_list:
        if c[0]==0:
            break
        print c  
        
#writing data
with open('C:\Users\myeong\Desktop\GeoGame_data\count_data.csv', 'wb') as csvfile: 
    i=0
    writer = csv.writer(csvfile, delimiter=',')    
    for k in cnt_list:            
        if str(k[0]) == '0':
            break
        i+=1
        writer.writerow(k)
    print "Complete " + str(i)+ " rows!"