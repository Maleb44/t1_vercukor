# -*- coding: cp1250 -*-


## Anita glose_level -- vércukor szin táblázatok
##
## 1. jav. vércukor értekek xx.40-től felfelé igazitva (10.57 -> 11)
## 2. jav Basis kitöltése 2013.06.04
## 3. jav Value error     2014.06.09  Bolus uj tipusu rekordok
##                                    'időtartam 0:30 h'
##                                    'idĹ‘tartam 0:30 h'
## 4. jav Bolus  xx.44-től felfelé  2014.06.10
##
##
## 5. jav  2015.02.19
##
##     hetfő, csütörtök, péntek vasárnap ékezetzes betük, 
##     konverzios probléma ??
##     input elemzés 
##
import string
import xlwt

# -*- coding: cp1250 -*-

def load_map(mapFilename):
    
   
    print "Loading map from file..."
    inFile=open(mapFilename,'r',0)
   
    b1 = True
    b2 = True
    b3 = True
    b4 = False
    lis2=[]
    lis2_bolus=[]
    lis2_bazis=[]
    count = 0
    while b1 :
        line = inFile.readline()
        count +=1
        a = string.split(line)
        if line == '':
            b1 = False
        else:
           
            if len(a) == 0:
                line = inFile.readline()
                a = string.split(line)
            if len(a) == 1:
                s3 = a[0]
                if s3[0:14] == '[g]123Megjegyz' :
                    line = inFile.readline()
                    count +=1
                    line = inFile.readline()
                    count +=1		
                    a = string.split(line)
                    print 'Vercukor értékek beolvasása'
                    while b2:
                        
                        store1(lis2, a)
                        line = inFile.readline()
                        count +=1
                        a = string.split(line)                                                   
                        while len(a) == 0:
                            line = inFile.readline()
                            a = string.split(line)
                        if len(a) == 2:
                     
                      #      print 'Itt a vege ??'
                        
                            b2 = False

                            
                                                
                    print 'Vége a vercukor értékek beolvasásának'
           
            #########################################
           
          
          
            if len(a) > 0:
                s3 = a[0]
                if s3 == 'Bólus' or s3 == 'BĂłlus':
                    print 'Bólus!!!!!!!!!!!!!!!!!'
                    
                    line = inFile.readline()
                    a = string.split(line)
                    while len (a) == 0:
                        line = inFile.readline()
                        a = string.split(line)
                        
                    s3 =a[0]
          ##        print 'a1', a
                   
          ##        while s3 <> 'BĂłlus':  ### 2014.09.24                    
          ##        while s3 <> 'Bólus':   ### 2015.02.19 modosítás
                    
                    while s3 <> 'BĂłlus':  ### 2015.02.19 modosítás
          ##            print s3   ### 2015.02.19
                        line = inFile.readline()
                        a = string.split(line)
                        if len(a) > 0:
                            s3 = a[0]
                            
                    while s3 <> 'BĂłlus':  ### 2015.02.19 modosítás
          ##            print s3   ### 2015.02.19
                        line = inFile.readline()
                        a = string.split(line)
                        if len(a) > 0:
                            s3 = a[0]
                            
            ##      for i in range (4):
                    for i in range (13):    
                        line = inFile.readline()
            ##          print 'line. :', line   ### 2015.02.19
                    a = string.split(line)
            ##      print a
                    print 'Bolus értékek beolvasása'
                    while b3:                                   
                                               
                        if len(a) > 1:
                            if len(a) == 5:
                                ertek1 = a[1]
                                ido1   = '24:00'
                                x = str(a[0]) + ido1 + ertek1
                     
                            if len (a) == 3:     ##  3. jav
                                x =str(a[0])     ##  3. jav
                                a1=len(x)        ##  3. jav
                                x = x[0:a1-10]   ##  3. jav 
                            a[0]=x
                        ## print a  ### jav 2014.06.09
                        store1(lis2_bolus, a)  
                     
                        line = inFile.readline()
                        a = string.split(line)
                  ##    print 'a:  ', a
                        if len(a) == 0:
                            print 'Vége a bólus beolvasásának'
                        while len(a) == 0:
                            line = inFile.readline()
                            a = string.split(line)
                            print 'a........', a    
                 
                        """
                        if len(a) == 2:
                            
                  ##        print 'a:  ', a 
                            print 'Itt a vege bólusnak'
                            b4 = True  # ???
                            b3 = False
                            s3 = a[0]
                      ##    print 's3......', s3
                        """
                        s3=a[0]
                  
                            
                        
       ########Bazis
                        ################
                        ################
                    
               ##         print 's3:', s3    ### 2013.11.12 modositas
               ##       if s3 == 'B\xc3\xa1zis':   # Bázis
                        if s3 == 'B\xc3\xa1zis' or s3 == 'Bázis':     # 2014.09.23
                            print 'Bázis!!!!!!!!!!!!!!!!!'
                            b3 =False
                            b4 = True
                            
                       #    print b4
                       ##   for i in range (4):
                           
                       ##   for i in range (14):
                       ##       line = inFile.readline()
                       ##       a = string.split(line)
                       ##       print a
                       
                       #
                       # Üres sorok átolvasása
                       #
                            line = inFile.readline()
                            a = string.split(line)
                            count +=1
                            while len(a) == 0:
                                line = inFile.readline()
                                a = string.split(line)
                                count +=1
                         ##     print 'x1.. ', a
                                
                      ##          
                      ## DátumIdőAlapritmus [U/h]Megjegyzések sor átolvasása
                      ##          
                            line = inFile.readline()
                            a = string.split(line)
                            count +=1
                        ##  print 'x2.. ', a
                       # Üres sorok átolvasása        
                            while len(a) == 0:
                                line = inFile.readline()
                                a = string.split(line)
                                count +=1
                        ##      print 'x3.. ', a    
                            
                            while b4:
                                ###
                                if len(a) > 1:
                                    if a[1] <> 'Stop':
                                        store1(lis2_bazis, a)
                                        
                                if len(a) == 1:
                                    store1(lis2_bazis, a)
                                line = inFile.readline()
                                a = string.split(line)
                                if len(a) == 0:
                                    b4 = False
                        
                            if len(a) == 0:
                                b1 = False
                                b4 = False
                                line = inFile.readline()
                                a = string.split(line)
                            print 'Vege a Bázisnak !!!!!!!!!'
                              
  ##############################################################
  
                      
   
    return lis2,lis2_bolus, lis2_bazis
def store1(lista,a):
    ## print 'store ??'   ### 2015.02.19
    
    ## print a
   
    
    if a[0][0:3] == 'Vas':
        if vasarnap(a) <> None:
            lista.append(vasarnap(a))
    else:
        if a[0][0:7] == 'Szombat':
            if szombat(a) <> None:
                lista.append(szombat(a))
        else:
            if a[0][0:1] == 'P':
                if pentek(a) <> None:
                    lista.append(pentek(a))
            else:
                if a[0][0:2] == 'Cs':
                    if csutortok(a) <> None:
                        lista.append(csutortok(a))
                else:
                    if a[0][0:6] == 'Szerda':
                        if szerda(a) <> None:
                            lista.append(szerda(a))
                    else:
                        if a[0][0:4] == 'Kedd':
                            if kedd(a) <> None:
                                lista.append(kedd(a))
                        else:
                            if a[0][0:1] == 'H':
                                if hetfo(a) <> None:
                                    lista.append(hetfo(a))


                                                            
    
def vasarnap(a):
    s1 = a[0]
    
##    datum1 = s1[8:18]  ### 2015.02.19    
##    ido1    = s1[18:23]
##    ertek1=s1[23:]
    
    datum1 = s1 [9:19] ##
    ido1    = s1[19:24] 
    ertek1=s1[24:]
    
    nap = 'Vasarnap'
   
    if len(ido1) == 0 or len(ertek1) == 0:
        return None
    else:
        lis1=[nap,datum1,ido1,ertek1]
        return lis1
def szombat(a):
    s1 = a[0]
    datum1  = s1[7:17]
    ido1    = s1[17:22]
    ertek1  = s1[22:]
    nap = 'Szombat'
    
   
    if len(ido1) == 0 or len(ertek1) == 0:
        return None
    else:
        lis1=[nap,datum1,ido1,ertek1]
        return lis1
def pentek(a):
    s1 = a[0]
    
   ## datum1 = s1[6:16]
   ## ido1    = s1[16:21]
   ## ertek1=s1[21:]
    
    datum1 = s1[7:17]
    ido1    = s1[17:22]
    ertek1=s1[22:]
    
    nap = 'Pentek'
    
    
    if len(ido1) == 0 or len(ertek1) == 0:
        return None
    else:
        lis1=[nap,datum1,ido1,ertek1]
        return lis1
def csutortok(a):
    s1 = a[0]
    """   2013.02.19
    datum1 = s1[9:19]
    ido1    = s1[19:24]
    ertek1=s1[24:]
    """
    ########## 2013.02.19
    datum1 = s1[12:22]
    ido1    = s1[22:27]
    ertek1=s1[27:]
    #########
    
    nap = 'Csutortok'
    
    
    if len(ido1) == 0 or len(ertek1) == 0:
        return None
    else:
        lis1=[nap,datum1,ido1,ertek1]
        return lis1
    
def szerda(a):
    s1 = a[0]
    datum1 = s1[6:16]
    
    ido1    = s1[16:21]
    ertek1=s1[21:]
    nap = 'Szerda'
    if len(ido1) == 0 or len(ertek1) == 0:
        return None
    else:
        lis1=[nap,datum1,ido1,ertek1]
        return lis1
    
def kedd(a):
    s1 = a[0]
    datum1 = s1[4:14]
    
    ido1    = s1[14:19]
    ertek1=s1[19:]
    nap = 'Kedd'
    if len(ido1) == 0 or len(ertek1) == 0:
        return None
    else:
        lis1=[nap,datum1,ido1,ertek1]
        return lis1
   
    
    
def hetfo(a):
    
    s1 = a[0]
    """ 2015.02.19
    datum1 = s1[5:15]   
    ido1    = s1[15:20] 
    ertek1=s1[20:]
    """
    ####
    
    datum1 = s1[7:17]   
    ido1    = s1[17:22] 
    ertek1=s1[22:]
    ######
    
    nap = 'Hetfo'
    if len(ido1) == 0 or len(ertek1) == 0:
        return None
    else:
        lis1=[nap,datum1,ido1,ertek1]
        return lis1 
    


import xlwt
from datetime import datetime


      
#############################################

def ex_iras(begin_dat,listak):
##    import xlwt
    import datetime
    lista1      = listak[0]
    lista_bolus = listak[1]
    lista_bazis = listak[2]
   

 #  style0 = xlwt.easyxf('font: name Times New Roman, colour_index black, bold on;'
 #  style0 = xlwt.easyxf('font: name Times New Roman, colour_index black, bold on, height 280;'
    style0 = xlwt.easyxf('font: name Times New Roman, colour_index black, bold on, height 240;'                     
                                  "borders: top medium, bottom medium, left thin, right thin;")
    
  #  style1 = xlwt.easyxf(num_format_str='YYYY-MM-DD')
  
    style5 = xlwt.easyxf('font: name Times New Roman, colour_index black, bold off,height 240; align: horiz center;  '
                             "borders: top medium, bottom medium, left thin, right thin;")



    
    
  
    wb = xlwt.Workbook('Windows-1250')
    ws = wb.add_sheet('Pumpa')
    ws.portrait=False
  
    ws.col(1).width=256*8
    ws.write(0, 1, 'Óra', style0)
    
   
    for i in range (24):
        ws.col(2+i).width=5*256
        ws.write(0,2+i,i,style0) ## 0 - 23 fejléc 
        
        
    
 
    ws.col(26).width=6*256    ## ??????????????
    ws.write(0,26,'sum',style0)  ## napi summa fejlec /head
        

        
    Napok=['Hétfő','Kedd','Szerda','Csütörtök','Péntek','Szombat','Vasárnap']    
    for i in range (7):
    
    
        ws.col(1).width=8*256
        ws.write(1+3*i, 1,'Vércukor',style0)
        ws.write(2+3*i, 1,'Bólus',style0)
        ws.write(3+3*i, 1,'Bázis',style0)
        
    dd=begin_dat[0:2]    
    mm=begin_dat[3:5]
    jj=begin_dat[6:10]
    datum_ymt=[]
    
   
    ## now hetfo
    now =datetime.date(int(jj),int(mm),int(dd)) 
    delta=datetime.timedelta(days=1)
    # hetfo
    first_col=ws.col(0) # First column
    first_col.width=256*10
    
  
    datum_ymt.append(now)
    
    dat_kedd = now + delta
 #   str_kedd = dat_kedd.strftime('%d.%m.%Y')
    str_kedd = dat_kedd.strftime('%d.%m.%Y')
    datum_ymt.append(dat_kedd)
    
    
    dat_szerda = dat_kedd + delta
    str_szerda = dat_szerda.strftime('%d.%m.%Y')
    datum_ymt.append(dat_szerda)
    
    dat_csutortok = dat_szerda + delta
    str_csutortok = dat_csutortok.strftime('%d.%m.%Y')
    datum_ymt.append(dat_csutortok)
    
    
    dat_pentek = dat_csutortok + delta
    str_pentek = dat_pentek.strftime('%d.%m.%Y')
    datum_ymt.append(dat_pentek)
    
    dat_szombat = dat_pentek + delta
    str_szombat = dat_szombat.strftime('%d.%m.%Y')
    datum_ymt.append(dat_szombat)
    
    dat_vasarnap = dat_szombat + delta
    str_vasarnap = dat_vasarnap.strftime('%d.%m.%Y')
    datum_ymt.append(dat_vasarnap)

    
    
    for j in range(7):
        ws.col(0).width=10*256
        k_str=str(datum_ymt[j])
        
        ws.write(2+3*j, 0,k_str[2:],style5)
        ws.write(1+3*j, 0, Napok[j],style0)
        
    for m,e1 in enumerate (lista1):
        if e1[1] == begin_dat:
            ## Hetfo
           
            ido=e1[2]
            ido[0:2]
            cell_o= int(ido[0:2]) + 2
            ws.write (1,cell_o,e1[3],style5)
      
            
        
        if e1[1] == str_kedd:
            ## kedd
           
            ido=e1[2]
            ido[0:2]
            cell_o= int(ido[0:2]) + 2
            ws.write (4,cell_o,e1[3],style5)              
        if e1[1] == str_szerda:
            ## szerda
         
            ido=e1[2]
            ido[0:2]
            cell_o= int(ido[0:2]) + 2
            ws.write (7,cell_o,e1[3],style5)
            
        if e1[1] == str_csutortok:
            ## csutortok
           
            ido=e1[2]
            ido[0:2]
            cell_o= int(ido[0:2]) + 2
            ws.write (10,cell_o,e1[3],style5)              
        if e1[1] == str_pentek:
            ## pentek
           
            ido=e1[2]
            ido[0:2]
            cell_o= int(ido[0:2]) + 2
            ws.write (13,cell_o,e1[3],style5)  
        if e1[1] == str_szombat:
            ## szombat
           
            ido=e1[2]
            ido[0:2]
            cell_o= int(ido[0:2]) + 2
            ws.write (16,cell_o,e1[3],style5)              
        if e1[1] == str_vasarnap:
            ## vasarnap
           
            ido=e1[2]
            ido[0:2]
            cell_o= int(ido[0:2]) + 2
            ws.write (19,cell_o,e1[3],style5)
   
    ### bolus ###
    #############        
    for m,e1 in enumerate (lista_bolus):
     
        if e1[1] == begin_dat:
            ## Hetfo
           
            ido=e1[2]
            ido[0:2]
            cell_o= int(ido[0:2]) + 2
            ws.write (2,cell_o,e1[3],style5)
      
            
        
        if e1[1] == str_kedd:
            ## kedd
           
            ido=e1[2]
            ido[0:2]
            cell_o= int(ido[0:2]) + 2
            ws.write (5,cell_o,e1[3],style5)              
        if e1[1] == str_szerda:
            ## szerda
       
            ido=e1[2]
            ido[0:2]
            cell_o= int(ido[0:2]) + 2
            ws.write (8,cell_o,e1[3],style5)
            
        if e1[1] == str_csutortok:
            ## csutortok
        
            ido=e1[2]
            ido[0:2]
            cell_o= int(ido[0:2]) + 2
            ws.write (11,cell_o,e1[3],style5)              
        if e1[1] == str_pentek:
            ## pentek
        
            ido=e1[2]
            if len (ido) > 0:
                ido[0:2]
                cell_o= int(ido[0:2]) + 2
                try:
                    ws.write (14,cell_o,e1[3],style5)
                except Exception:
                    print 'Overrite hiba'
                    print 'Bolus'
                    print 14
                    print cell_o
                    print e1[3]
                    
        if e1[1] == str_szombat:
            ## szombat
        
            ido=e1[2]
            if len (ido) > 0:
                ido[0:2]
                cell_o= int(ido[0:2]) + 2
                ws.write (17,cell_o,e1[3],style5)              
        if e1[1] == str_vasarnap:
            ## vasarnap
           
            ido=e1[2]
            if len(ido)> 0:
                ido[0:2]
                cell_o= int(ido[0:2]) + 2  ### overrite
                try:
                    ws.write (20,cell_o,e1[3],style5)
                except Exception:
                    print 'Overrite hiba'
                    print 'Bolus'
                    print 20
                    print cell_o
                    print e1[3]

    ### Basis ###
    #############
    ### Bazis summa naponként
    sum_bazis=[0,0,0,0,0,0,0]                
   
    for m,e1 in enumerate (lista_bazis):
    
         
        ex = e1[3][0:4]
     
        if ex <> '0.00':
       #    print float(ex) 
            
           if e1[1] == begin_dat:
                ## Hetfo
                sum_bazis[0] = sum_bazis[0] + float(ex)
               
                ido=e1[2]
                ido[0:2]
                cell_o= int(ido[0:2]) + 2
                try:
                    ws.write (3,cell_o,ex,style5)
                except Exception:
                        print 'Overrite hiba'
                        print 'Bazis'
                        print 3
                        print cell_o
                        print e1[3]        
      
            
        
           if e1[1] == str_kedd:
               ## kedd
                sum_bazis[1] = sum_bazis[1] + float(ex)   
                ido=e1[2]
                ido[0:2]
                cell_o= int(ido[0:2]) + 2
                try:
                    ws.write (6,cell_o,ex,style5)
                except Exception:
                        print 'Overrite hiba'
                        print 'Bazis'
                        print 6
                        print cell_o
                        print e1[3]    
                
           if e1[1] == str_szerda:
            ## szerda
                sum_bazis[2] = sum_bazis[2] + float(ex)
                ido=e1[2]
                ido[0:2]
                cell_o= int(ido[0:2]) + 2
                try:
                    ws.write (9,cell_o,ex,style5)
                except Exception:
                        print 'Overrite hiba'
                        print 'Bazis'
                        print 9
                        print cell_o
                        print e1[3]       
            
           if e1[1] == str_csutortok:
                ## csutortok
                sum_bazis[3] = sum_bazis[3] + float(ex)
                ido=e1[2]
                ido[0:2]
                cell_o= int(ido[0:2]) + 2
                try:
                    ws.write (12,cell_o,ex,style5)
                except Exception:
                        print 'Overrite hiba'
                        print 'Bazis'
                        print 12
                        print cell_o
                        print e1[3]    
           if e1[1] == str_pentek:
                ## pentek
                sum_bazis[4] = sum_bazis[4] + float(ex)
                ido=e1[2]
                
                cell_o= int(ido[0:2]) + 2
                try:
                    ws.write (15,cell_o,ex,style5)
                except Exception:
                    print 'Overrite hiba'
                    print 'Bazis'
                    print 15
                    print cell_o
                    print e1[3]
                    
           if e1[1] == str_szombat:
                ## szombat
                sum_bazis[5] = sum_bazis[5] + float(ex)
                ido=e1[2]
                cell_o= int(ido[0:2]) + 2
                try:
                    ws.write (18,cell_o,ex,style5)
                except Exception:
                    print 'Overrite hiba'
                    print 'Bazis'
                    print 18
                    print cell_o
                    print e1[3]
                    
           if e1[1] == str_vasarnap:
                ## vasarnap
                sum_bazis[6] = sum_bazis[6] + float(ex)
                ido=e1[2]
                if len(ido)> 0:
                    ido[0:2]
                    cell_o= int(ido[0:2]) + 2  ### overrite
                    try:
                        ws.write (21,cell_o,ex,style5)
                    except Exception:
                        print 'Overrite hiba'
                        print 'Bazis'
                        print 21
                        print cell_o
                        print e1[3]

    for k  in range (7):
        print sum_bazis[k]
        sum_1= sum_bazis[k]
        ws.write(3+3*k,26,sum_1,style5)
        
    for k  in range(22):
        for j in range (27):
            try:
              #  print 'j  ',j
                ws.write(k,j,'   -   ',style5)
            except Exception:
                pass
    datum_yyyy_mm_tt=begin_dat[6:10] + '.' + begin_dat[3:5] + '.' + begin_dat[0:2]

   # file_name='Anita_'+begin_dat + '.xls'
    file_name='Anita_'+datum_yyyy_mm_tt + '.xls'
    wb.save(file_name)

    
def normal(list_old,mod):
    j = 0
    list_new=[]
    print 'input_hossz:', len (list_old)
 ## print list_new
    print 'List_old !!!!!!!'
 ## print list_old
    for i in range (len(list_old)):
      #  print 'list_old:', list_old[i]
      #  if mod == 0:
        if (mod ==0 or mod ==1):    ## 4. jav
            ### Vercukor
            time_1 =str(list_old[i][2])
       ##   print 'time_1: ', time_1
            ora= int(time_1[0:2])
            perc= int(time_1[3:5])
            
            if perc > 40:
                if ora <> 23:
                    ora +=1
               
                if ora > 9:
                    time_2=str(ora) + ":" + "00"
                else:
                    time_2="0" + str(ora) + ":" + "00"
            else:
                time_2 = list_old[i][2]
            list_old[i][2]=time_2
        
      
        if i == 0:
            list_new.append(list_old[i])
            
        else:
            
            key_new = list_new[j][1] + list_new[j][2][0:3]
            key_old = list_old[i][1] + list_old[i][2][0:3]
            if key_new == key_old:
                item_new=['','','','']
                item_new[0]=list_new[j][0]
                item_new[1]=list_new[j][1]
                item_new[2]=list_new[j][2]
                
                if mod == 0 :
                    ertek= (float(list_new[j][3]) + float(list_old[i][3]))/2
                if mod == 1 :
                    ## Bolus
               ##     print 'jjjjjj:', j
               ##     print 'iiiiii:', i
                    
               ##     print list_new[j][3]
                    
               ##     print list_old[i][3]
                    ertek= float(list_new[j][3]) + float(list_old[i][3])
                if mod == 2:
                    ## Bazis
                    ertek = float(list_new[j][3])
                
                item_new[3]=str(ertek)
                list_new[j] = item_new
         
            else:
             
                list_new.append(list_old[i])
                j +=1
                
   
        
    print 'output_hossz:', len(list_new)
            
    return list_new
def NormBazis(lista,datum):
    import datetime
    print 'NormBazis'
 #   print lista
    lista_n=[]
    Napok=['Hetfo','Kedd','Szerda','Csutortok','Pentek','Szombat','Vasarnap']
    
   
    dat1=datum
    wert = '0.00'
    
    dd=dat1[0:2]    
    mm=dat1[3:5]
    jj=dat1[6:10]
    now =datetime.date(int(jj),int(mm),int(dd)) 
    delta=datetime.timedelta(days=1)
    for i in range(7):
 #   for i in range(14):    
        nap =Napok[i]
        if i == 0:
            new_date = now
        else:
            new_date = new_date + delta
            
  ##    print '__________'
  ##    print new_date

        dat1 = new_date.strftime('%d.%m.%Y')
  ##    print new_date
        for k in range (24):
            if k < 10:
                ido=str(0) + str(k)+':'+'00'
            else:
                ido=str(k)+':'+'00'
            
            new_elem=[nap,dat1,ido,wert]
            lista_n.append(new_elem)
   # print lista_n        
    lista_mm=[]
    count_t  = 0
    count_nt = 0
    cr_wert='0.00'
    cr_lista=['XXX','','00:00','0.00']
    for l in range (len(lista_n)):
        
  
        dat1 =lista_n[l][1]
        ora_perc =lista_n[l][2]
        ora=ora_perc[0:2]
          
        talalt = - 1
        for m in range (len(lista)):
        #    print 'lista__1:',lista[m]
            if dat1 == lista[m][1]:
             #   print lista[m]
                if ora == lista[m][2][0:2]:
                    
                    talalt = m
                    break
            
        if talalt > 0:
            count_t +=1
            lista[m][3]=lista[m][3][0:4]
            lista_mm.append(lista[m])
            cr_wert=lista[m][3]
          
        else:
            count_nt +=1
            lista_n[l][3]=cr_wert
            lista_mm.append(lista_n[l])
      
    print count_t, count_nt        
    print 'XXXXXXXXXXXXXXXXXX'
    
#    print lista_mm
    return lista_mm


##########################################################
def main_bg():
    import datetime
    
    FileName=raw_input("Add meg az input file nevet- .txt : ")
    print 'File_name:',FileName
    datum=raw_input("Add meg a kezdodatumot, <nn.hh.eeee> : ")
    print 'Első hét'
    print 'Datum.', datum

    datum_yyyy_mm_tt=datum[6:10] + '.' + datum[3:5] + '.' + datum[0:2]
    
    print 'Datum_ev_ho_nap:', datum_yyyy_mm_tt
   
    
    print 'Anita blootGlocose'
    
   
    Tab=load_map(FileName)
    
  
  
    Tab_norm=['','','']
    print 'mod :  0'
    Tab_norm[0]=normal(Tab[0],0)
    print 'mod  : 1'                
    Tab_norm[1]=normal(Tab[1],1)
    
    print ' '
    print 'Első hét:', datum
    print ' '  
    
    Tab_norm[2]=NormBazis(normal(Tab[2],2),datum)
    
    begin_dat = datum
    ex_iras(begin_dat,Tab_norm)
    

    ## 2.hét
    dd=datum[0:2]    
    mm=datum[3:5]
    jj=datum[6:10]
 
    now =datetime.date(int(jj),int(mm),int(dd)) 
    delta=datetime.timedelta(days=7)
    dat_2 = now + delta
    begin_dat_2 = dat_2.strftime('%d.%m.%Y')
    
    print ' '
    print 'Második hét:', begin_dat_2
    print ' '
    
    Tab_norm[2]=NormBazis(normal(Tab[2],2),begin_dat_2)
    ex_iras(begin_dat_2,Tab_norm)

main_bg()    
    


    
