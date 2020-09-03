import re
import requests
from bs4 import BeautifulSoup

class Tracker:
   def __init__( self ):
       self.url = 'https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1%3F'
    
   def maincounter( self ):
       r = requests.get(self.url)
       if r.status_code == 200:
          r = r.text
          soup = BeautifulSoup(r, 'html.parser' )
          return soup
       else:
          return False

   def total_cases( self ):
       soup = self.maincounter()
       if soup:
          div = soup.find_all('div', attrs = {'class', 'maincounter-number'})
          regex_pattern = "<span.*>(.+?)</span>"
          
          items = list()
          for i in div:
              item = re.findall(regex_pattern, str(i))
              items.append(item)
        
          num = str(items[0][0]).replace(',','')
          num = int(num.strip())
          return num
       else:
          return None
          
   def total_deaths( self ):
       soup = self.maincounter()
       if soup:
          div = soup.find_all('div', attrs = {'class', 'maincounter-number'})
          regex_pattern = "<span.*>(.+?)</span>"
          
          items = list()
          for i in div:
              item = re.findall(regex_pattern, str(i))
              items.append(item)
        
          num = str(items[1][0]).replace(',','')
          num = int(num.strip())
          return num
       else:
          return None
   
   def total_recoveries( self ):
       soup = self.maincounter()
       if soup:
          div = soup.find_all('div', attrs = {'class', 'maincounter-number'})
          regex_pattern = "<span.*>(.+?)</span>"
          
          items = list()
          for i in div:
              item = re.findall(regex_pattern, str(i))
              items.append(item)
        
          num = str(items[2][0]).replace(',','')
          num = int(num.strip())
          return num
       else:
          return None
          
   def data_grab( self ):
       try:
          r = requests.get(self.url)
          r = r.text
           
          soup = BeautifulSoup(r, 'html.parser')
          data = soup.find_all('div', attrs = { 'class': 'panel_front'})
          
          regex_pattern = r">(.+?)<"
          
          main_numbers = list()
          
          for i in data:
              soup = BeautifulSoup(str(i), 'html.parser')
              item = soup.find_all('div', attrs = {'class': 'number-table-main'})
              if item:
                 for j in item:
                     val = re.findall(regex_pattern, str(j))
                     if val:
                        for k in val:
                            main_numbers.append(k)
                            
          regex_pattern = r">\s*(.+?)<"
          
          secondary_numbers = list()
          
          for i in data:
              soup = BeautifulSoup(str(i), 'html.parser')
              item = soup.find_all('span', attrs = {'class': 'number-table'})
              if item:
                 for j in item:
                     val = re.findall(regex_pattern, str(j))
                     if val:
                        for k in val:
                            secondary_numbers.append(k)
                            
          combined_List = list()
          for i in range(4):
              try:
                 combined_List.append(main_numbers[i])
              except:
                 pass
              try:
                 combined_List.append(secondary_numbers[i])
              except:
                 pass
           
          data = list()
          for i in combined_List:
              data.append(int(i.replace(',','').strip()))
          if data:
             return data
          else:
             return False
           
       except:
          return False
          
   def active_cases( self ):
       data = self.data_grab()
       
       if data:
          actives = {
             'currently infected patients' : data[0],
             'patients in mild conditions' : data[1],
             'serious/critical conditions' : data[3]
          }
          
          return actives
       else:
          return False
          
   def closed_cases( self ):
       data = self.data_grab()
       
       if data:
          closed = {
             'outcomes' : data[2],
             'recovered/discharged' : data[4],
             'deaths' : data[5]
          }
          
          return closed
       else:
          return False
          
   def country_info( self ):
       try:
          r = requests.get(self.url)
          r = r.text
          
          soup = BeautifulSoup(r, 'html.parser')
          
          data = soup.find_all('table', attrs = {'id' : 'main_table_countries_today'})
          data = str(data)

          soup = BeautifulSoup(data, 'html.parser')

          data = soup.find_all('tr')
          for i in range(8):
              data.pop(0)

          regex_pattern = r">(.*?)<"

          rows = list()

          for i in data:
              soup = BeautifulSoup(str(i), 'html.parser')
              Data = soup.find_all('td')
              Data = str(Data)

              item = re.findall(regex_pattern, Data)
              for i in range(item.count(', ')):
                  item.pop(item.index(', '))
            
              try:
                  rows.append(item)
              except:
                  pass
                  
          if rows:
             return rows
          else:
             return False
       except:
          return False
          
   def country_names( self ):
       data = self.country_info()
       if data:
          data = data[1:-8]
          
          names = list()
          for i in data:
              names.append(i[2])
          
          if names:
             return names
          else: 
             return False
       else:
          return False
          
   def country_info_by_name( self, name ):
       if name is not None:
          
          data = self.country_info()
          
          if data:
             data = data[1:-8]
             name = name.upper()
             
             bool = False
             for i in data:
                 if i[2].upper() == name:
                    bool = True
                    break
            
             if bool:
                n_list = list()
                
                for j in range(len(i)):
                    item = i[j].replace(',','')
                    item = item.replace('+','')
                    item.strip()
                    
                    try:
                       item = int(item)
                    except:
                       item = 'N/A'
                       
                    n_list.append(item)
                j = i
                i = n_list
                    
                info = {
                    'id': int(j[0].strip()),
                    'name': j[2],
                    'total cases': i[4],
                    'new cases': i[5],
                    'total deaths': i[6],
                    'new deaths': i[7],
                    'total recoveries': i[8],
                    'new recoveries': i[9],
                    'active cases': i[10],
                    'critical cases': i[11],
                    'total cases/1M pop': i[12],
                    'deaths/1M pop': i[13],
                    'total tests/1M pop': i[14],
                    'tests/1M pop': i[15],
                    'population': i[17],
                    'continent': j[19],
                    '1 case every X ppl': i[20],
                    '1 death every X ppl': i[21],
                    '1 test every X ppl': i[22],
                }
                
                return info
             else:
                return bool
          else:
             return False
          
       else:
          return False
          
          
   def country_info_by_id( self, id ):
       if id is not None:
          
          data = self.country_info()
          
          if data:
             data = data[1:-8]
             
             bool = False
             for i in data:
                 if int(i[0].strip()) == id:
                    bool = True
                    break
            
             if bool:
                n_list = list()
                
                for j in range(len(i)):
                    item = i[j].replace(',','')
                    item = item.replace('+','')
                    item.strip()
                    
                    try:
                       item = int(item)
                    except:
                       item = 'N/A'
                       
                    n_list.append(item)
                j = i
                i = n_list
                    
                info = {
                    'id': int(j[0].strip()),
                    'name': j[2],
                    'total cases': i[4],
                    'new cases': i[5],
                    'total deaths': i[6],
                    'new deaths': i[7],
                    'total recoveries': i[8],
                    'new recoveries': i[9],
                    'active cases': i[10],
                    'critical cases': i[11],
                    'total cases/1M pop': i[12],
                    'deaths/1M pop': i[13],
                    'total tests/1M pop': i[14],
                    'tests/1M pop': i[15],
                    'population': i[17],
                    'continent': j[19],
                    '1 case every X ppl': i[20],
                    '1 death every X ppl': i[21],
                    '1 test every X ppl': i[22],
                }
                
                return info
             else:
                return bool
          else:
             return False
          
       else:
          return False
          
   def cont_info( self ):
       try:
          r = requests.get(self.url)
          r = r.text
          
          soup = BeautifulSoup(r, 'html.parser')
          
          data = soup.find_all('table', attrs = {'id' : 'main_table_countries_today'})
          data = str(data)

          soup = BeautifulSoup(data, 'html.parser')

          data = soup.find_all('tr')
          data = data[1:8]
    
          regex_pattern = r">(.*?)<"

          rows = list()

          for i in data:
              soup = BeautifulSoup(str(i), 'html.parser')
              Data = soup.find_all('td')
              Data = str(Data)

              item = re.findall(regex_pattern, Data)
              for i in range(item.count(', ')):
                  item.pop(item.index(', '))
            
              try:
                  rows.append(item)
              except:
                  pass
                  
          if rows:
             return rows
          else:
             return False
       except:
          return False
          
   def continent_info( self, name ):
       if name is not None:
          
          data = self.cont_info()
          
          if data:
             name = name.upper()
             
             bool = False
             for i in data:
                 if i[1].upper().replace('AUSTRALIA/OCEANIA','OCEANIA') == name:
                    bool = True
                    break
            
             if bool:
                n_list = list()
                
                for j in range(len(i)):
                    item = i[j].replace(',','')
                    item = item.replace('+','')
                    item.strip()
                    
                    try:
                       item = int(item)
                    except:
                       item = 'N/A'
                       
                    n_list.append(item)
                    
                
                j = i
                i = n_list
                    
                info = {
                    'name': j[1],
                    'total cases': i[2],
                    'new cases': i[3],
                    'total deaths': i[4],
                    'new deaths': i[5],
                    'total recoveries': i[6],
                    'new recoveries': i[7],
                    'active cases': i[8],
                    'critical cases': i[9],
                }
                
                return info
             else:
                return bool
          else:
             return False
          
       else:
          return False
          
          
   def countries_info_by_continent( self, name ):
       if name is not None:
          
          data = self.country_info()
          
          if data:
             data = data[1:-8]
             name = name.upper()
             
             countries = list()
             
             bool = False
             for i in data:
                 if i[19].upper().replace('AUSTRALIA/OCEANIA','OCEANIA') == name:
                    bool = True
                    countries.append(i)
            
             if bool:
                n_list = list()
                
                info = list()
                
                for i in countries:
                    for j in range(len(i)):
                        item = i[j].replace(',','')
                        item = item.replace('+','')
                        item.strip()
                    
                        try:
                           item = int(item)
                        except:
                           item = 'N/A'
                       
                        n_list.append(item)
                   
                    j = i
                    i = n_list
                    
                    info.append({
                        'id': int(j[0].strip()),
                        'name': j[2],
                        'total cases': i[4],
                        'new cases': i[5],
                        'total deaths': i[6],
                        'new deaths': i[7],
                        'total recoveries': i[8],
                        'new recoveries': i[9],
                        'active cases': i[10],
                        'critical cases': i[11],
                        'total cases/1M pop': i[12],
                        'deaths/1M pop': i[13],
                        'total tests/1M pop': i[14],
                        'tests/1M pop': i[15],
                        'population': i[17],
                        'continent': j[19],
                        '1 case every X ppl': i[20],
                        '1 death every X ppl': i[21],
                        '1 test every X ppl': i[22],
                    })
                
                return info
             else:
                return bool
          else:
             return False
          
       else:
          return False        



