
import numpy as np

class OBJ_JP():
  
    def __init__(self,F,V):
        self.F=F
        self.V=V
        
    def loadObj(file=None,*args,**kwargs):
    
        cellCsv=np.loadtxt(file,dtype='str',delimiter=' ')
        firstLetter=cellCsv[:,0]
        d1=np.compare_chararrays("v",firstLetter,"==","true")
        vv=cellCsv[d1,1:4]
        V=vv.astype(np.float)
    
        d2=np.compare_chararrays("f",firstLetter,"==","true")
        ff=cellCsv[d2,1:4]
        F=ff.astype(np.float);
    
        fv={'faces':F,'vertices':V}
        return fv
    
    def saveObj(fv,fileName):
        
        nv=np.size(fv['vertices'],0)# number of vertices
        nf=np.size(fv['faces'],0)# number of faces
        #strArr = np.empty(nv+nf, dtype='str')
        
        lines = list()
        
        for v in fv['vertices']:
            lines.append('v ' + str(v[0]) + ' ' + str(v[1]) + ' ' + str(v[2]) + '\n')
            
        for f in fv['faces']:
            line = 'f'
            for i in range(0, len(f)):
                line += ' ' + str(int(f[i]))
            line += '\n'
            lines.append(line)
            
        
        file = open(fileName, 'w')
        file.writelines(lines)
        file.close()
            
            
#        
#        strArr_v = np.empty(nv, dtype='str')
#        
#        for i in range(0,nv):
#            strArr_v[i] = 'v'
#        Obj_v=np.column_stack((strArr_v,fv['vertices']))
#        
#        strArr_f = np.empty(nf, dtype='str')
#        for i in range(0,nf):
#            strArr_f[i] = 'f'
#        Obj_f=np.column_stack((strArr_f,fv['faces']))
#        
##        a_width = a.shape[1]
##        b_width = b.shape[1]
##        if a_width < b_width:
##            a = np.append(a, np.zeros((len(a), b_width - a_width), 'S0'), axis=1) # 'U0' in Python 3
##        if b_width < a_width:
##            b = np.append(b, np.zeros((len(b), a_width - b_width), 'S0'), axis=1)
##        
#        Obj=np.vstack((Obj_v,Obj_f))
#        
#        #data=np.concatenate((fv['vertices'], fv['faces']), axis=0) 
#        #data=data.astype(np.str)
#        
#        #Obj=np.column_stack((strArr,data))
#        
#        np.savetxt(file, Obj, delimiter=' ',fmt="%s")
        
if __name__ == '__main__':
    pass
    