# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:18:55 2021

@author: Tamilvannan Ganesan

"""

import pandas as pd

#******************* For Reading the Dataframe **************************


#******************* For Reading the Dataframe **************************

def read_dataframe(sheet_url): 
    
    #sheet_url = str(input())
    try:
        csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
        df = pd.read_csv(csv_export_url,encoding='utf-8', engine='c')
    except:
        csv_export_url = sheet_url.replace('/edit?urlBuilderDomain=smartsetter.io#gid=', '/export?format=csv&gid=')
        df = pd.read_csv(csv_export_url,encoding='utf-8', engine='c')
        
    
    return df


#state finder
def state_finder(columns):
    state = ''
    for col in columns:
        if 'state' in col.lower():
            print('Taking '+col+ " as state ")
            state = col
            
    return state

#full name finder
def full_name_finder(columns):
    full_name = ''
    for col in columns:
        if 'full' in col.lower() and col != 'Full_Name':
            print("Taking "+col+" as full name ")
            full_name = col
            
    return full_name

#concatenate first name and last name
def Full_name_creator(columns):
    first_name = ''
    last_name = ''
    for col in columns:
        
        if 'first' in col.lower():
            print("Taking "+col+" as First name")
            first_name = col
        if 'last' in col.lower():
            print("Taking "+col+ " as Last name")
            last_name = col

    
    return first_name, last_name


def emaiL_finder(columns):
    email = ''
    for col in columns:
        if 'email' in col.lower():
            print("Taking "+col+ " as Email")
            email = col
    
    return email


def license_finder(columns):
    license = ''
    for col in columns:
        if 'license' in col.lower():
            print("Taking ",col,"as license")
            license = col
    return license

def zip_finder(columns):
    Zip = ''
    for col in columns:
        if 'zip' in col.lower():
            print("Taking ",col,"as zip")
            Zip = col
    return Zip

#finding mobile numbers using name
def finding_mobile_name(name,state, ph , Zip):
    

    if ph == None and str(Zip).lower()!='nan' and Zip != None and str(state).lower() != 'nan':
        
        Zip = str(Zip).replace(".0","")
        Zip_file =  globals()[f"{state}"][globals()[f"{state}"]["zip"]== str(Zip)]    
        Zip_file.reset_index(drop = True , inplace = True)
        
        if str(name).lower() != 'nan' and str(state).lower() != 'nan':
            for name_index , manual_name in enumerate(Zip_file["name"]):
                if str(name).lower() == str(manual_name).lower():
                    return Zip_file.loc[name_index,'phone']
            
    else:
        return ph
    
# #finding mobile numbers using name
# def finding_mobile_name(name,state, ph):
    
    
#     if ph == None:
        
#         if str(name).lower() != 'nan' and str(state).lower() != 'nan':
#             for name_index , manual_name in enumerate(globals()[f"{state}"]["name"]):
#                 if str(name).lower() == str(manual_name).lower():
#                     return globals()[f"{state}"].loc[name_index,'phone']
            
#     else:
#         return ph


#finding mobile numbers using name

def finding_mobile_email(email, state, ph , Zip):
    
    if ph == None and str(Zip).lower() != 'nan' and Zip != None and str(state).lower() != 'nan':
        
        Zip = str(Zip).replace(".0","")
        Zip_file =  globals()[f"{state}"][globals()[f"{state}"]["zip"]== str(Zip)]    
        Zip_file.reset_index(drop = True , inplace = True)
        
        if str(email).lower() != 'nan'and str(state).lower() != 'nan':
            for email_index , manual_email in enumerate(Zip_file["email"]):
                if str(email).lower() == str(manual_email).lower():
                    return Zip_file.loc[email_index,'phone']
            
    else:
        return ph
    
    
# #finding mobile numbers using name
# def finding_mobile_email(email, state, ph):
    
#     if ph == None:
#         if str(email).lower() != 'nan'and str(state).lower() != 'nan':
#             for email_index , manual_email in enumerate(globals()[f"{state}"]["email"]):
#                 if str(email).lower() == str(manual_email).lower():
#                     return globals()[f"{state}"].loc[email_index,'phone']
            
#     else:
#         return ph
    

#Autmate file allocation for full day

def assign(file,count,name):

    #pint("blanks from this file is ",len(file))
    
    try:
        assign_index = file[file["Assign"].isna()].index
    except:
        assign_index = file.index
    
    for ind in assign_index:
        if count != 500:
            file.loc[ind,'Assign'] = name
            count = count + 1
        

    if file["Assign"].notna().sum() == len(file.index):
        status = "done"
        #print(count, "Assigned for ",name)
    
    else:
        status = "not done"
        


    return file,count,status

#Autmate file allocation for Half day
def assign_half(file,count,name):

    #pint("blanks from this file is ",len(file))
    
    try:
        assign_index = file[file["Assign"].isna()].index
    except:
        assign_index = file.index
    
    for ind in assign_index:
        if count != 250:
            file.loc[ind,'Assign'] = name
            count = count + 1
        

    if file["Assign"].notna().sum() == len(file.index):
        status = "done"
    
    else:
        status = "not done"
        
    return file,count,status




#args ----> pass Dataframe and column name to count
def license_count(Data,column_name): #for count license and mobile numbers
    

    Data[column_name+"_count"] = 0
    
    
    for index_no, agent in enumerate(Data[column_name]):
        
        count = len(Data[Data[column_name]==agent])
        
        if count == None:
            count = 0
            
        Data.loc[index_no,column_name+"_count"]= count
    

    
    return Data

#for finding duplicates and to display the comments

def comment(Data):
    
    length = len(Data)
    for index in range(length):
        
        lic_count = Data.loc[index,'license_id_count']
        found_mob_count = Data.loc[index,'Found_Mobile_count']
        
        if lic_count == found_mob_count:
            Data.loc[index,'Comments'] = None
            
        if found_mob_count != 0 and lic_count > 1 and found_mob_count < lic_count:
            Data.loc[index,'Comments'] = "Check this record"
        
        if lic_count != 0 and found_mob_count > lic_count:
            
            Data.loc[index,'Comments'] = "Check this record"
            
            # Data.loc[index,"Found_Mobile"] = None
            # Data.loc[index,"Assign"] = None
            
    
    return Data


def duplicate_check(Data):
    try:
        duplicate_index = Data[(Data['license_id_count']<= 1 ) & (Data['Found_Mobile_count']>1) &(Data['Found_Mobile']!='None') & (Data['Found_Mobile']!='Not Found') & (Data['Found_Mobile'].notna())].index
        Data.loc[duplicate_index,'Assign'] = None
        Data.loc[duplicate_index,'Found_Mobile'] = None
    except:
        Data = Data
    
    return Data


def city_finder(columns):
    sel_city = ''
    for col in columns:
        if 'city' in col.lower():
            sel_city = col
    return sel_city


def agent_name_finder(columns):
    agent_name = ''
    for col in columns:
        if col.lower() == 'agent':
            agent_name = col
    return agent_name


def Name_checker(Data,Agent_Name):

    try:
        
        for index , name_split in enumerate(Data[Agent_Name]):
            if name_split != None and str(name_split).lower() !='nan':
                if ',' in name_split:
                    split_name = name_split.split(',')
                    if len(split_name) > 1:
                        Data.loc[index,'First_Name'] = split_name[-1].strip()
                        Data.loc[index,'Last_Name'] = split_name[0].strip()
                elif ' ' in name_split:
                    split_name = name_split.split(' ')
                    if len(split_name) > 1:
                        Data.loc[index,'First_Name'] = split_name[-1].strip()
                        Data.loc[index,'Last_Name'] = split_name[0].strip() 
                else:
                    pass
                
    except:
        pass
    
    return Data

def Automate_File_Allocation(file): #edit #manual count
    
    #print("This file has "+str(file.shape[0])+" Records")
    #blank_index = file[file["Assign"].isna()].index
    #print("Blank from the file is ",len(blank_index))
    analyst_name_fullday = []
    
    try:
        no_analyst_fullday = int(input("Enter the number of persons : "))
    except:
        print("Enter the valid number")
        try:
            no_analyst_fullday = int(input("Enter the number of persons : "))
        except:
            print("Enter the valid number")
            no_analyst_fullday = int(input("Enter the number of persons : "))
            
    if no_analyst_fullday > 0:
        print("Enter the name of the person who are going to work")
        for person_no in range(no_analyst_fullday):
            name = str(input(str(person_no+1)+" Enter the Name :"))
            analyst_name_fullday.append(name)
    
    
    #print(len(file[file["Found_Mobile"].notna()]), "got from vlookup")
    #assign_index = file[file["Found_Mobile"].isna()].index
    #print(len(assign_index), "blanks left")
    try:
        assign_index = file[file["Assign"].isna()].index
    except:
        assign_index = file.index
    
    start_slice = 0
    end_slice = 0
    
    if no_analyst_fullday > 0:
        

        #print("Blank left ",len(assign_index))


        for no, assign in enumerate(analyst_name_fullday):

            try:
                try:   
                    count = int(input("\nEnter the Assign count for "+str(assign)+" : "))
                except:
                    print("Enter the valid count")
                    count = int(input("\nEnter the Assign count for "+str(assign)+" : "))
                    
                end_slice = end_slice + count
                file.loc[assign_index[start_slice:end_slice],'Assign'] =  assign
                start_slice = end_slice
                print(count, "Assigned to ",assign)
            except:
                print("file might be exhausted...! count must be less than or equal to blank counts")
                print("Couldn't assign for these people in this file", analyst_name_fullday[no:])

                break
    print("\n*********************************************************************************\n")
    
    return file