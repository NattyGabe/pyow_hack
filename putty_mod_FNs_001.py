#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numba
import numpy as np




@numba.jit
def rec_balls(recpicks, xpicks, rand1, rand2):
    for ind0 in range(0, len(xpicks)):
        xpic = xpicks[ind0]
        r1pic = rand1[ind0]
        r2pic = rand2[ind0]
        rc = recpicks[ind0]
        if xpic == 0 and rc == 0:
            recpicks[ind0] = 0 + r2pic
        elif xpic == 0 and rc == 1:
            if r1pic == 0:
                recpicks[ind0] = 0 + r2pic
            elif r1pic == 1:
                recpicks[ind0] = 2 + r2pic
        elif xpic == 0 and rc == 2:
            if r1pic == 0:
                recpicks[ind0] = 2 + r2pic
            elif r1pic == 1:
                recpicks[ind0] = 0 + r2pic
        elif xpic == 0 and rc == 3:
            recpicks[ind0] = 2 + r2pic
    return recpicks





@numba.jit
def sig_cor(sig4r, sigfail4p, xpic2, rand11):
    for ind1 in range(0, len(xpic2)):
        if xpic2[ind1] == 0:
            if rand11[ind1] == 0:
                id2change = ind1*2+1
                sig4r[id2change] = 0
                sigfail4p[id2change] = 0
            elif rand11[ind1] == 1:
                id2change = ind1*2
                sig4r[id2change] = 0
                sigfail4p[id2change] = 0
    return sig4r, sigfail4p









@numba.jit
def putty_draws(cdraws, xdraws):
    drawslen = len(cdraws)
    rtd = np.zeros(drawslen, dtype = np.int8)
    for ind2 in range(0, drawslen):
        if xdraws[ind2] == 0:
            if cdraws[ind2]== 0:
                rtd[ind2] = 1
            elif cdraws[ind2] == 1:
                rtd[ind2] = 1
            elif cdraws[ind2] == 2:
                rtd[ind2] = 4
            elif cdraws[ind2] == 3:
                rtd[ind2] = 4
        elif xdraws[ind2] == 1:
            if cdraws[ind2]== 0:
                rtd[ind2] = 0
            elif cdraws[ind2] == 1:
                rtd[ind2] = 2
            elif cdraws[ind2] == 2:
                rtd[ind2] = 3
            elif cdraws[ind2] == 3:
                rtd[ind2] = 5
                
    return rtd


@numba.jit
def avg_succ(xsn, asn, bsn, crec, xrec):
    val2return = 0

    for bit00 in range(0, 6):
        
        
        rcurn2 = 99
        rcurn3 = 99
        rcurn4 = 99
        
        if asn[bit00] == 0 and bsn[bit00] == 0:
            if xsn[bit00] == 1:
                rcurn = 0
            elif xsn[bit00] == 0:
                rcurn = 0
                rcurn2 = 1
        
        elif asn[bit00] == 0 and bsn[bit00] == 1:
            if xsn[bit00] == 1:
                rcurn = 1
            elif xsn[bit00] == 0:
                rcurn = 0
                rcurn2 = 1
                rcurn3 = 2
                rcurn4 = 3
            
        elif asn[bit00] == 1 and bsn[bit00] == 0:
            if xsn[bit00] == 1:
                rcurn = 2
            elif xsn[bit00] == 0:
                rcurn = 2
                rcurn2 = 3
                rcurn3 = 0
                rcurn4 = 1
            
            
        elif asn[bit00] == 1 and bsn[bit00] == 1:
            if xsn[bit00] == 1:
                rcurn = 3
            elif xsn[bit00] == 0:
                rcurn = 2
                rcurn2 = 3
            
            
        
        recurnlist = [rcurn, rcurn2, rcurn3, rcurn4]
        
        if rcurn2 == 99:
            recsplit = 1
        elif rcurn3 == 99:
            recsplit = 2
        else:
            recsplit = 4
        
        part_avg = 0
        for bit02 in recurnlist[:recsplit]:
            
        
            if xrec[xsn[bit00]] == 0 and crec[bit02] == 0:
                avg_action = 1
            elif xrec[xsn[bit00]] == 0 and crec[bit02] == 1:
                avg_action = 1
            elif xrec[xsn[bit00]] == 0 and crec[bit02] == 2:
                avg_action = 4
            elif xrec[xsn[bit00]] == 0 and crec[bit02] == 3:
                avg_action = 4
            elif xrec[xsn[bit00]] == 1 and crec[bit02] == 0:
                avg_action = 0
            elif xrec[xsn[bit00]] == 1 and crec[bit02] == 1:
                avg_action = 2
            elif xrec[xsn[bit00]] == 1 and crec[bit02] == 2:
                avg_action = 3
            elif xrec[xsn[bit00]] == 1 and crec[bit02] == 3:
                avg_action = 5


            if avg_action == bit00:
                part_avg = part_avg+1
                
        avg_pay = part_avg/recsplit
            
            
            
        val2return = val2return+avg_pay
            
    return val2return





@numba.jit
def runs_nash_counter(x_send_tot, a_send_tot, b_send_tot, c_rec_tot, x_rec_tot, numruns, sigpermsexe, sigpermsA, sigpermsB, recperms, exerecperms):

    
    nashcount = 0
    notnashcount = 0
    countcheck = 0
    
    

    for bit04 in range(0, numruns):
        
        x_send = x_send_tot[bit04]
        a_send = a_send_tot[bit04]
        b_send = b_send_tot[bit04]
        c_rec = c_rec_tot[bit04]
        x_rec = x_rec_tot[bit04]
        
        state_suc = avg_succ(x_send, a_send, b_send, c_rec, x_rec)
        countcheck = countcheck+1
        checker0 = 0
        checker1 = 0
        checker2 = 0
        checker3 = 0
        checker4 = 0
        nasher0 = 0
        nasher1 = 0
        nasher2 = 0
        nasher3 = 0
        nasher4 = 0
        stopper = 0

        exeln = len(sigpermsexe)
        asln = len(sigpermsA)
        bsln = len(sigpermsB)
        crln = len(recperms)
        xrln = len(exerecperms)

        #need to change this while loop to stopper
        # so i can update the list of nash equilibrium
        while stopper == 0:





            while checker0+nasher0 == 0:
                for c0i in range(exeln):
                    c0 = sigpermsexe[c0i]
                    c0ck = avg_succ(c0, a_send, b_send, c_rec, x_rec)
                    if c0ck > state_suc:
                        checker0 = 1
                    elif c0i == (exeln - 1):
                        nasher0 = 1

            nasher = nasher0+nasher1+nasher2+nasher3+nasher4
            if checker0+checker1+checker2+checker3+checker4 > 0:
                # this means not nash
#                                 not_nash_list = np.concatenate(x_send, a_send, b_send, c_rec, x_rec)
                stopper = 1
            elif nasher == 5:
#                                 nash_list  = np.concatenate(x_send, a_send, b_send, c_rec, x_rec)
                stopper = 1


            while checker1+nasher1 == 0:
                for c1i in range(asln):
                    c1 = sigpermsA[c1i]
                    c1ck = avg_succ(x_send, c1, b_send, c_rec, x_rec)
                    if c1ck > state_suc:
                        checker1 = 1
                    elif c1i == (asln - 1):
                        nasher1 = 1



            nasher = nasher0+nasher1+nasher2+nasher3+nasher4
            if checker0+checker1+checker2+checker3+checker4 > 0:
                # this means not nash
#                                 not_nash_list = np.concatenate(x_send, a_send, b_send, c_rec, x_rec)
                stopper = 1
            elif nasher == 5:
#                                 nash_list  = np.concatenate(x_send, a_send, b_send, c_rec, x_rec)
                stopper = 1





            while checker2+nasher2 == 0:
                for c2i in range(bsln):
                    c2 = sigpermsB[c2i]
                    c2ck = avg_succ(x_send, a_send, c2, c_rec, x_rec)
                    if c2ck > state_suc:
                        checker2 = 1
                    elif c2i == (bsln - 1):
                        nasher2 = 1

            nasher = nasher0+nasher1+nasher2+nasher3+nasher4
            if checker0+checker1+checker2+checker3+checker4 > 0:
                # this means not nash
#                                 not_nash_list = np.concatenate(x_send, a_send, b_send, c_rec, x_rec)
                stopper = 1
            elif nasher == 5:
#                                 nash_list  = np.concatenate(x_send, a_send, b_send, c_rec, x_rec)
                stopper = 1





            while checker3+nasher3 == 0:
                for c3i in range(crln):
                    c3 = recperms[c3i]
                    c3ck = avg_succ(x_send, a_send, b_send, c3, x_rec)
                    if c3ck > state_suc:
                        checker3 = 1
                    elif c3i == (crln - 1):
                        nasher3 = 1


            nasher = nasher0+nasher1+nasher2+nasher3+nasher4
            if checker0+checker1+checker2+checker3+checker4 > 0:
                # this means not nash
#                                 not_nash_list = np.concatenate(x_send, a_send, b_send, c_rec, x_rec)
                stopper = 1
            elif nasher == 5:
#                                 nash_list  = np.concatenate(x_send, a_send, b_send, c_rec, x_rec)
                stopper = 1







            while checker4+nasher4 == 0:
                for c4i in range(xrln):
                    c4 = recperms[c4i]
                    c4ck = avg_succ(x_send, a_send, b_send, c_rec, c4)
                    if c4ck > state_suc:
                        checker4 = 1
                    elif c4i == (xrln - 1):
                        nasher4 = 1


            nasher = nasher0+nasher1+nasher2+nasher3+nasher4
            if checker0+checker1+checker2+checker3+checker4 > 0:
                # this means not nash
#                                 not_nash_list = np.concatenate(x_send, a_send, b_send, c_rec, x_rec)
                stopper = 1
            elif nasher == 5:
#                                 nash_list  = np.concatenate(x_send, a_send, b_send, c_rec, x_rec)
                stopper = 1



        if checker0+checker1+checker2+checker3+checker4 > 0:
            # this means not nash
            notnashcount = notnashcount+1
        elif nasher == 5:
            nashcount = nashcount+1
        else:
            countcheck = countcheck+100



                                
                                
    return nashcount, notnashcount, countcheck



# In[ ]:




