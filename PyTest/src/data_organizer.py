import csv

NUM_COL = 2346
# NUM_COL = 30
final_list = [[0 for x in xrange(6)] for x in xrange(NUM_COL)]
target_list = [288,289,291,293,294,296,297,299,300,301,307,308,310,311,312,313,314,317,322,323,324,329,332,337,340,341,
               343,345,347,356,358,361,362,363,365,371,374,375,377,379,380,381,388,389,391,394,395,400,402,403,404,405]
path = 'C:\Users\myeong\Desktop\GeoGame_data\game_answers140419.csv'
# path = 'C:\Users\myeong\Desktop\GeoGame_data\game_test.csv'

with open(path, 'r') as csvfile:
    line = csv.reader(csvfile, delimiter=',')
    order_flag = False
    temp_row = []
    aggregate_cnt = 0            
    i = 0

    for row in line:    
        if row[0] == 0:
            break
        
        if not temp_row:
            temp_row = row
            continue
            
        elif temp_row[0] == row[0] and temp_row[1]==row[1]:            
            final_list[i][0] = row[0]   #User ID
            final_list[i][1] = row[1]   #Point ID

            #Familiarity
            if row[2]!="0" or temp_row[2]!="0":
                if row[2]=="0":
                    final_list[i][2] = temp_row[2]   #Familiarity
                else: 
                    final_list[i][2] = row[2]   #Familiarity
            else:                
                temp_row = []
                continue
                            
            #Address answer
            if row[3]=="NULL" and temp_row[3]=="NULL":   #if both lines's address answers are NULL
                final_list[i][3] = ' '   #The answer for adress is null
            else:
                if row[3]=="NULL": final_list[i][3] = str(temp_row[3])
                else: final_list[i][3] = str(row[3])
                final_list[i][4] = "A"
                            
            #Landmark answer
            if row[4]!="NULL" or temp_row[4]!="NULL":   #if both lines's landmark answers are NULL  
                if row[4]=="NULL": final_list[i][4] = str(temp_row[4])
                else: final_list[i][3] = str(row[4])
                final_list[i][4] = "L"
            temp_row = []            
            
        else: 
            temp_row = row
            continue
          
#         print final_list[i]
        i += 1
    
    i=0
        
    #correctness 
    for k in final_list:
        if str(k[0]) == '0':
            break
        if str(k[3]).isdigit():   
            if str(k[3]) == str(int(k[1])+1) and int(k[1])>2:
                k[5] = "1" #correct
            elif str(k[3]) == str(k[1]) and int(k[1])<=1:
                k[5] = "1" #correct
            else:
                k[5] = "0"
        else:   
            if ord(k[3]) == int(k[1]) + 97:
                k[5] = "1" #correct            
            else:
                k[5] = "0"
                        
    #final result
#     for k in final_list:
#         if str(k[0]) == '0':
#             break 
#         print str(i) + str(k)        
#         i+=1

with open('C:\Users\myeong\Desktop\GeoGame_data\cleaned_data.csv', 'wb') as csvfile: 
    i=0
    writer = csv.writer(csvfile, delimiter=',')    
    for k in final_list:            
        if str(k[0]) == '0':
            break
        if int(k[0]) not in target_list:
            continue        
        i+=1
        writer.writerow(k)
    print "Complete " + str(i)+ " rows!"