# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 04:29:16 2020

@author: ellix
"""
# https://classes.uwaterloo.ca/under.html

def contains (result, course): 
    link = result[0] 
    if '<td align="center">' + str (course) + '</td>' in str(link):
        return True 
    else: return False 

def main(coursecode): 
    output = 'stasdsfsdfrt \n'
    try:
            
        import sys
        
        from bs4 import BeautifulSoup 
        output = 'bs4 successful \n'
        
        import requests
        output ='requests successful \n'
        
    
    
    except Exception as e: 
        exc_type, exc_obj, exc_tb = sys.exc_info()
        output = str(e) + str (exc_tb.tb_lineno)
        print (e)
        input()
        return output
    	 
    
    output = ''
    
    
    #while (True): 
    try:
        print ('enter course code like soc 262')
        #coursecode = 'SOC 262'.split()
        coursecode = input()
        coursecode = coursecode.upper().split()
        subject = coursecode[0]
        course = coursecode[1]
        #print (subject, course)
        output += ''
        
        #fall classes 
        output += ('FALL \n')
        for year in range (1149, 1210, 10): 
            url = 'https://info.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?sess=' + str(year) + '&level=under&subject=' + subject + '&cournum='
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            result = soup.findAll()
            output += str(int(year/10 + 1899.1)) + ' ' + str(contains (result, course )) + '\n'
        
        output += '\n'
        
        output += ('WINTER \n')
        for year in range (1151, 1212, 10): 
            url = 'https://info.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?sess=' + str(year) + '&level=under&subject=' + subject + '&cournum='
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            result = soup.findAll()
            output += str (int(year/10 + 1899.9)) + ' ' + str(contains (result, course )) + '\n'
        
        output += '\n'
        
        output+= ('SUMMER \n')
        for year in range (1155, 1206, 10): 
            url = 'https://info.uwaterloo.ca/cgi-bin/cgiwrap/infocour/salook.pl?sess=' + str(year) + '&level=under&subject=' + subject + '&cournum='
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            result = soup.findAll()
            output+= str (int(year/10 + 1899.5)) + ' ' + str(contains (result, course )) + '\n'

        #output += '\n'
        return output
    except Exception as e: 
        output += str( e)
        return output

if __name__ == "__main__":
    print ('START')
    while (True):
        output = main('mte 120')
        print (output)
    
print  ('END')
