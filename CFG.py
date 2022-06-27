digits = ["1","2","3","4","5","6","7","8","9","0"]
keyword=["intg", "flt", "chrc", "strg","yes", "no", "check", "ncheckall",
                 "ncheck", "floop", "wloop", "both", "only", "nop", "room", "mine",
                 "__initi__", "fun", "display" ]

##########DEC CFG##################

def dec(token):
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
                                
##########If Else CFG##################

def if_else(token):
    if token[i][2]=="check":
        i+=1
        if token[i][2]=="(":
            i+=1
            if token[i][1]=="ID":
                i+=1
                if ROP(token[i]):
                    i+=1
                    if idconst(token[i]):
                        i+=1
                        if token[i][2]==")":
                            i+=1
                            if body(token[i]) or elseOp():
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

def idconst(token):
    if token[i][2]=="ID" or token[i][2] in digits:
        return True
def elseOp(token):
    if token[i][1]=="ncheckall":
        i+=1
        if elseOp2(token[i]):
            i+=1
    if not in token[i]:
        return True

def elseOp2(token):
    if body(token[i]) or if_else(token[i]):
        return True
    else:
        return False
                            
    

############### CFG of expression##########
def oe(token):
    if AE(token[i]):
        i+=1
        if O_E(token[i]):
            return True
        else:
            return False
    else:
        return False
def O_E(token):
    if AE(token[i]):
        i+=1
        if O_E(token[i])or :
            return True
        else:
            return False
    else:
        return False
    

###########Class##############################
    
