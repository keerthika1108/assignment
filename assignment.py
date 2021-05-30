#Student_marks_list.csv
import csv
import operator


  def student(file):
     student_totals = {}
     subject1_list = []  
     subject2_list = [] 
     subject3_list = [] 
     subject4_list = []  
     subject5_list = []    
     subject6_list = []   
     with open(file, 'r') as file:      
       reader = csv.reader(file)     
       for row in reader:         
         if row[0]=="Name":       
           continue          
         else:            
           student_name = row[0]    
           student_total = int(row[1])+int(row[2])+int(row[3])+int(row[4])+int(row[5])+int(row[6]) 
           student_totals[student_name] = student_total 
           subject1 = [row[0],int(row[1])]   
           subject2 = [row[0],int(row[2])]                
           subject3 = [row[0],int(row[3])]                
           subject4 = [row[0],int(row[4])]               
           subject5 = [row[0],int(row[5])] 
           subject6 = [row[0],int(row[6])]  
           
           subject1_list.append(subject1)
           subject2_list.append(subject2)                
           subject3_list.append(subject3)               
           subject4_list.append(subject4)                
           subject5_list.append(subject5)                
           subject6_list.append(subject6)                        

 sort_orders = sorted(student_totals.items(), key=lambda x: x[1], reverse=True)    
 toppers_3 = sort_orders[0:3]  
 print("3 toppers",toppers_3)         

  maths = sorted(subject1_list, key=lambda x: x[1], reverse=True)    
  biology = sorted(subject2_list, key=lambda x: x[1], reverse=True)    
  english = sorted(subject3_list, key=lambda x: x[1], reverse=True)    
  physics =sorted(subject4_list, key=lambda x: x[1], reverse=True)    
  chemistry =sorted(subject5_list, key=lambda x: x[1], reverse=True)    
  hindi =sorted(subject6_list, key=lambda x: x[1], reverse=True)        

  print("maths_topper",maths[0])    
  print("biology_topper",biology[0])    
  print("english_topper",english[0])    
  print("physics_topper",physics[0])    
  print("chemistry_topper",chemistry[0])   
  print("hindi_topper",hindi[0])    


student("Student_marks_list.csv")