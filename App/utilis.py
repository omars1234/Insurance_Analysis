def gender_string_to_number(gender):
          match gender:
            case "M": return 0
            case "F": return 1
    

def numclaims_string_to_number(numclaims):
          match numclaims:
            case "0": return 0
            case "1": return 1
            case "2": return 2
            case "3": return 3

def veh_body_string_to_number(veh_body):
          match veh_body:
            case 'SEDAN':return 9
            case 'HBACK' :return 3
            case 'STNWG':return 10
            case 'TRUCK':return 11 
            case 'HDTOP':return 4
            case 'UTE':return 12
            case 'COUPE':return 2
            case 'BUS':return 0 
            case 'PANVN':return 7
            case 'MIBUS':return 6
            case 'RDSTR':return 8
            case 'CONVT':return 1
            case 'MCARA':return 5

def veh_age_string_to_number(veh_age):
          match veh_age:
            case '1':return 0
            case '2':return 1
            case '3':return 2
            case '4':return 3 
            case '5':return 4

def area_string_to_number(area):
          match area:
            case 'A':return 0
            case 'B':return 1
            case 'C':return 2
            case 'D':return 3 
            case 'E':return 4
            case 'F':return 5

def agecat_string_to_number(agecat):
          match agecat:
            case '1':return 0
            case '2':return 1
            case '3':return 2
            case '4':return 3 
            case '5':return 4
            case '6':return 5
            case '7':return 6
                