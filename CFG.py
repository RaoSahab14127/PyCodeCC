digits = ["1","2","3","4","5","6","7","8","9","0"]
keyword=["intg", "flt", "chrc", "strg","yes", "no", "check", "ncheckall",
                 "ncheck", "floop", "wloop", "both", "only", "nop", "room", "mine",
                 "__initi__", "fun", "display" ]
i=0
##########DEC CFG##################

def dec(token):
    global i
    if token[i][1]=="DT":
        i+=1
        if token[i][1]=="ID":
            i+=1
            if dec_op(token[i][2]):
                return True
            else:
                return False
        else:
                return False
    else:
                return False 

def dec_op(token):
    if (token[i][2]==("=",";")) and (dec_op2(token[i][2])):
        return True
    elif (token[i][2]==("=",";")):
        return True
    else:
        return False
def dec_op2(token):
    if is_int_float(token[i][2]) or is_char_constant(token[i][2]) or is_int_constant(token[i][2]):
        return True
    else:
                return False



##########While CFG##################

def Wloop(token):
    global i
    if token[i][2]=="wloop":
        i+=1
        if token[i][2]=="(":
            i+=1
            if token[i][1]=="ID":
                i+=1
                if ROP(token[i][2]):
                    i+=1
                    if ID_count(token[i][2]):
                        i+=1
                        if token[i][2]==")":
                            i+=1
                            if token[i][2]=="{":
                                i+=1
                                if body(token[i][2]):
                                    i+=1
                                    if token[i][2]=="}":
                                        return True
                                    else:
                                        return False
                                else:
                                        return False
                            else:
                                        return False
                        else:
                                        return False
                    else:
                                        return False
                else:
                                        return False
            else:
                                        return False
        else:
                                        return False
    else:
                                        return False
                                
   
    

###########Start##############################

def Start(token):
    global i
    i=0
    if(token[i][1]=='main'):
        i+= 1
        if(token[i][1] == '('):
            i += 1
            if(token[i][1] == ')'):
                i += 1
                if(token[i][1] == '{'):
                            i += 1
                            if(body(token)):
                                if(token[i][1] == '}'):
                                        return True
        # return True
    else:
        return False


def SyntaxAnalyzer(token):
    global i
    if(Start(token)):
        print("Valid Syntax")
    else:
        print("Syntax Error at Line Number ", token[i][0])    


####################################################################

def if_ElseOpt(TKs):
    global i
    option= ['while','if','else', 'elif']
    if(token[i][1] in option):
        if(token[i][1] == 'else'):
            i += 1
            if(body(token)):
                return True
        elif(token[i][1] == 'elif'):
            i += 1
            if(token[i][1] == '('):
                i += 1
                if(expression(token)):
                    if(token[i][1] == ')'):
                        i += 1
                        if(body(token)):
                            if(if_ElseOpt(TKs)):
                                return True

        return True
    else:
        return False


def If_Else(TKs):
    global i
    if(token[i][1]== 'if'):
        i += 1
        if(token[i][1] == '('):
            i += 1
            if(expression(token)):
                if(token[i][1] == ')'):
                    i += 1
                    if(body(token)):
                        if(if_ElseOpt(token)):
                            return True
    else:
        return False



