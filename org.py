import re
sep=[';', ',', '\n', ':', '[', ']', '{', '}', '(', ')',' ','@']
oper=[ '*', '/', '%', '+', '-', '<','>', '=', '!','.','"', "'"]
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
keyword=["intg", "flt", "chrc", "strg","yes", "no", "check", "ncheckall",
                 "ncheck", "floop", "wloop", "both", "only", "nop", "room", "mine",
                 "__initi__", "fun", "display" ]
assignments = ['+=', '-=', '*=', '/=', '%=', '=']
MDM = ['*', '/', '%']
PM = ['+', '-']
ROP = ['<', '>', '>=', '<=', '!=', '==']
DT = ['int', 'float', 'char', 'double', 'string']
quotes = ['"', "'"]
f=open("file.txt")
words=f.read()



def wordbreaker(words):
    i=0
    wb=[]
    lex=""
    while (i<=(len(words))):
        if (words[i] not in sep) and (words[i] not in oper):
                lex+=words[i]
                if i== (len(words)-1):
                    wb.append(lex)
                    break
                i+=1
                if ((words[i] in sep) or (words[i] in oper)):
                    wb.append(lex)
                    wb.append(words[i])
                    if i== (len(words)-1):
                        break
                    i+=1
                    lex=""
        if (words[i] in sep) or (words[i] in oper):
            wb.append(words[i])
            if i== (len(words)-1):
                break
            i+=1
    return wb



def wordbreaker2(wb):
    i=0
    nwb=[]
    lex=""
    while(i<=(len(wb))):
        if (wb[i]=="<"and wb[i+1]=="!")or (wb[i]=='"')or(wb[i]=="'")or(wb[i] in oper and wb[i+1]=="=") or (wb[i]=="+" and wb[i+1]=="+") or (wb[i]=="-" and wb[i+1]=="-" ):
            
                if wb[i]=="<"and wb[i+1]=="!":
                        lex+=wb[i]
                        lex+=wb[i+1]
                        
                        
                        if i== (len(wb)-1):
                                break
                        i+=2
                        while wb[i]!="!"and wb[i+1]!=">":
                                lex+=wb[i]
                                
                                if i== (len(wb)-1):
                                        break
                                i+=1
                                if wb[i]=="!"and wb[i+1]==">":
                                        lex+=wb[i]
                                        lex+=wb[i+1]
                                        nwb.append(lex)
                                        
                                        
                                        i+=2
                                        lex=""
                                        break
                elif wb[i]=='"':

                        lex+=wb[i]
                        
                        
                        if i== (len(wb)-1):
                                break
                        i+=1
                        while wb[i]!='"':
                                lex+=wb[i]
                                
                                if i== (len(wb)-1):
                                    nwb.append(lex)
                                    break
                                i+=1
                                if wb[i]=='"':
                                        lex+=wb[i]
                                        nwb.append(lex)
                                        i+=1
                                        lex=""
                                        break
                elif wb[i]=="'":

                        lex+=wb[i]
                        
                        
                        if i== (len(wb)-1):
                                break
                        i+=1
                        while wb[i]!="'":
                                lex+=wb[i]
                                
                                if i== (len(wb)-1):
                                    nwb.append(lex)
                                    break
                                i+=1
                                if wb[i]=="'":
                                        lex+=wb[i]
                                        nwb.append(lex)
                                        i+=1
                                        lex=""
                                        break
                
                elif wb[i]=="+" and wb[i+1]=="+":
                                lex+= wb[i]
                                lex+= wb[i+1]
                                nwb.append(lex)
                                lex=""
                                
                                if i== (len(wb)-1):
                                        break
                                i+=2
                elif (wb[i] in oper and wb[i+1]=="="):
                                lex+= wb[i]
                                lex+= wb[i+1]
                                nwb.append(lex)
                                lex=""
                                

                                if i== (len(wb)-1):
                                        break
                                i+=2
                elif ((wb[i]=="-" and wb[i+1]=="-")):
                                lex+= wb[i]
                                lex+= wb[i+1]
                                nwb.append(lex)
                                lex=""
                                if i== (len(wb)-1):
                                        break
                                i+=2

                else:
                    
                    nwb.append(wb[i])
                    
                    if i== (len(wb)-1):
                        break
                    i+=1
                
                
                                
                                    
        else:
            
            nwb.append(wb[i])

            
            if i== (len(wb)-1):
                        break
            i+=1
    return nwb
def is_identifier(test_string):
        pattern= ("(^[^\d\W]\w*\Z)")
        result = re.match(pattern, test_string)
        if result:
            #print("1. Is identifier " ,(test_string))
            return True
        else :
            #print("4. Is constant ",(test_string))
            return False
        
def is_int_constant(test_string):
        pattern="^(\+|-)?\d+$"
        result = re.match(pattern, test_string)
        if result:
            #print("2. Is integer ",(test_string))
            return True
        else :
            #print("4. Is constant ",(test_string))
            return False
def is_int_float(test_string):
        pattern="([+|-][0-9]*[.][0-9]+)|([0-9]*[.][0-9]+)"
        result = re.match(pattern, test_string)
        if result:
            #print("3. Is float ",(test_string))
            return True
        else :
            #print("4. Is constant ",(test_string))
            return False

def is_char_constant(test_string):
        pattern="[\w\w]"
        result = re.match(pattern, test_string)
        if result:
            #print("4. Is constant ",(test_string))
            return True
        else :
            #print("4. Is constant ",(test_string))
            return False
def is_keyword(test_string):
     
     if test_string in keyword:
            #print("5. Is keyword ",(test_string))
         return True
     else :
            #print("4. Is constant ",(test_string))
            return False
def isAlpha(ch):
    if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
        if(ch in sep):
            return False
        return True


def isDigit(ch):
    if(ch in digits):
        return True
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
keyword=["intg", "flt", "chrc", "strg","yes", "no", "check", "ncheckall",
                 "ncheck", "floop", "wloop", "both", "only", "nop", "room", "mine",
                 "__initi__", "fun", "display" ]


def tok(nwb):
    ntoken=[]
    token=[]
    i=0
    lineno=0
    classpart=""
    valuepart=""
    while (i<=(len(nwb))):
     
        if nwb[i]=="\Inteln":
            lineno+=1
            
            if i== (len(words)-1):
                        break
            i+=1
        elif "<!" in nwb[i]:
            if "!>"in nwb[i]:
                classpart="Comment"
                valuepart=nwb[i]
                ntoken.append(lineno)
                ntoken.append(classpart)
                ntoken.append(valuepart)
                token.append(ntoken)
                ntoken=[]
                classpart=""
                
                if i== (len(nwb)-1):
                        break
                i+=1
            else:
                classpart="Error"
                valuepart=nwb[i]
                ntoken.append(lineno)
                ntoken.append(classpart)
                ntoken.append(valuepart)
                token.append(ntoken)
                ntoken=[]
                classpart=""
                
                if i== (len(nwb)-1):
                        break
                i+=1
        elif(nwb[i][0] == '_'):
            if(is_identifier(nwb[i])):
                classpart="ID"
                valuepart=nwb[i]
                ntoken.append(lineno)
                ntoken.append(classpart)
                ntoken.append(valuepart)
                token.append(ntoken)
                ntoken=[]
                classpart=""
                
                if i== (len(nwb)-1):
                        break
                i+=1
                
            else:
                classpart="Error"
                valuepart=nwb[i]
                ntoken.append(lineno)
                ntoken.append(classpart)
                ntoken.append(valuepart)
                token.append(ntoken)
                ntoken=[]
                classpart=""
                
                if i== (len(nwb)-1):
                        break
                i+=1
        elif(isAlpha(nwb[i])):
            if(is_identifier(nwb[i])):
                status =is_keyword(nwb[i])
                if(status == False):
                    classpart="ID"
                    valuepart=nwb[i]
                    ntoken.append(lineno)
                    ntoken.append(classpart)
                    ntoken.append(valuepart)
                    token.append(ntoken)
                    ntoken=[]
                    classpart=""
                    
                    if i== (len(nwb)-1):
                        break
                    i+=1
                    
                else:
                    if(wb[i] in DT):
                        classpart= 'DT'
                    else:
                        classpart= wb[i]
                    valuepart=wb[i]
                    ntoken.append(lineno)
                    ntoken.append(classpart)
                    ntoken.append(valuepart)
                    token.append(ntoken)
                    ntoken=[]
                    classpart=""
                    
                    if i== (len(nwb)-1):
                        break
                    i+=1
                    
                        
            else:
                classpart="Error"
                valuepart=nwb[i]
                ntoken.append(lineno)
                ntoken.append(classpart)
                ntoken.append(valuepart)
                token.append(ntoken)
                ntoken=[]
                classpart=""
                
                if i== (len(nwb)-1):
                        break
                i+=1
                
        elif(nwb[i] in sep or nwb[i] in oper ):
                if(nwb[i] in sep) and (nwb[i] != "\n"):
                    classpart="Sep"
                elif(nwb[i] == "\n"):
                    lineno+=1
                elif(nwb[i] in MDM):
                    classpart="MDM"
                elif(nwb[i] in PM):
                    classpart="PM"
                elif(nwb[i] in ROP):
                    classpart="Rop"
                else:
                    classpart=nwb[i]
                valuepart=nwb[i]
                ntoken.append(lineno)
                ntoken.append(classpart)
                ntoken.append(valuepart)
                token.append(ntoken)
                ntoken=[]
                classpart=""
                
                if i== (len(nwb)-1):
                        break
                i+=1
                
        elif(isDigit(nwb[i]) or ((nwb[i][0] == '+' or nwb[i][0] == '-') and (nwb not in oper))):
            if(is_int_constant(nwb[i])):
                classpart="Int"
                valuepart=nwb[i]
                ntoken.append(lineno)
                ntoken.append(classpart)
                ntoken.append(valuepart)
                token.append(ntoken)
                ntoken=[]
                classpart=""
                
                if i== (len(nwb)-1):
                        break
                i+=1
            elif(is_int_float(nwb[i])):
                classpart="Float"
                valuepart=nwb[i]
                ntoken.append(lineno)
                ntoken.append(classpart)
                ntoken.append(valuepart)
                token.append(ntoken)
                ntoken=[]
                classpart=""
                
                if i== (len(nwb)-1):
                        break
                i+=1
            else:
                classpart="Error"
                valuepart=nwb[i]
                ntoken.append(lineno)
                ntoken.append(classpart)
                ntoken.append(valuepart)
                token.append(ntoken)
                ntoken=[]
                classpart=""
                
                if i== (len(nwb)-1):
                        break
                i+=1
        elif(nwb[i][0] in quotes and nwb[i][-1] in quotes):
            classpart="Qoutes"
            valuepart=nwb[i]
            ntoken.append(lineno)
            ntoken.append(classpart)
            ntoken.append(valuepart)
            token.append(ntoken)
            ntoken=[]
            classpart=""
                
            if i== (len(nwb)-1):
                        break
            i+=1
                
        else:
            classpart="ErRRor"
            valuepart=nwb[i]
            ntoken.append(lineno)
            ntoken.append(classpart)
            ntoken.append(valuepart)
            token.append(ntoken)
            ntoken=[]
            classpart=""
                
            if i== (len(nwb)-1):
                break
            i+=1
            
    return token
wb=wordbreaker(words)
nwb=wordbreaker2(wb)
token=tok(nwb)
print(token)

                
