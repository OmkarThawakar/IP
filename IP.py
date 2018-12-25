import math
import pandas as pd
class IP:
    
    def __init__(self,ip):
        self.ip=ip
        self.is_dd = self.is_DD()
        self.is_binary = self.is_Binary()
        self.is_hex = self.is_Hex()
        self.binary = self.get_Binary()
        self.dd = self.get_DD()
        self.hex = self.get_Hex()
        self.class_= self.get_class()
        
    def get_details(self):
        print('IP : ',self.ip)
        print('Class : ',self.class_)
        print('Binary representation : ',self.binary)
        print('Dotted Decimal Representation : ',self.dd)
        print('hexadecimal representation : ',self.hex)
        
    def get_class(self):
        ip = self.dd.split('.')
        if 1<=int(ip[0])<=127 :
            return 'A'
        elif 128<=int(ip[0])<=192 :
            return 'B'
        elif 193<=int(ip[0])<=224:
            return 'C'
        else:
            return 'D'
    
    def get_class_details(self):
        ip = self.dd.split('.')
        if self.class_=='A':
            self.net_id=ip[0]
            self.net_add=ip[0]+'.0.0.0'
            self.host_id = ip[1]+'.'+ip[2]+'.'+ip[3]
            self.subnet_mask = '255.0.0.0'
        elif self.class_=='B':
            self.net_id=ip[0]+'.'+ip[1]
            self.net_add=self.net_id+'.0.0'
            self.host_id = ip[2]+'.'+ip[3]
            self.subnet_mask = '255.255.0.0'
        elif self.class_=='C':
            self.net_id=ip[0]+'.'+ip[1]+'.'+ip[2]
            self.net_add=iself.net_id+'.0'
            self.host_id = ip[3]
            self.subnet_mask = '255.255.255.0'
        else:
            self.net_id=None
            self.net_add=None
            self.host_id = None
            self.subnet_mask = None
        print('Net ID : ',self.net_id)
        print('Network Address : ',self.net_add)
        print('Host ID : ',self.host_id)
        print('Defaut Subnet mask : ',self.subnet_mask)
        
    def is_Hex(self):
        if len(self.ip.split(':'))==4:
            for byte in self.ip.split(':'):
                if len(byte)>2:
                    return False
            return True
        return False  
        
    def is_Binary(self):
        if len(self.ip)==32:
            for i in str(np.array([str(i) for i in range(2,10)])):
                if i in self.ip:
                    return False
            return True
        return False
        
    def is_DD(self):
        if len(self.ip.split('.'))==4:
            for byte in self.ip.split('.'):
                if 0<=int(byte)<=255:
                    if byte[0]=='0' :
                        if len(str(byte))>1:
                            print("SHOULD BE NO LEADING 0 IN DOTTED DECIMAL NOTATION")
                            return False
                        else:
                            print("EROR IN BYTE : ",byte)
                        return False
                return True
        return False
    
    def get_DD(self):
        if self.is_dd==True:
            return self.ip
        elif self.is_binary==True:
            return self.binary_dd(self.ip)
        else:
            return self.Hex_DD()
         
    def get_Binary(self):
        if self.is_binary == True:
            return self.ip
        elif self.is_hex == True :
            ip = self.Hex_DD()
        else:
            ip=self.ip
        self.binary = ''
        for byte in list(map(int,ip.split('.'))):
            tmp = ''
            while byte>0:
                tmp = str(byte%2) + tmp
                byte=byte//2
            if len(tmp)<8:
                for i in range(8-len(tmp)):
                    tmp = str(0)+tmp
            self.binary += tmp
        return self.binary
    
    def binary_decimal(self,num):
        decimal=0
        for i in range(len(num)):
            decimal += int(num[len(num)-i-1])*2**i
        return int(decimal)
    
    def get_Hex(self):
        self.hex = ''
        if self.is_hex == True :
            return self.ip
        if self.is_binary==True:
            ip = self.ip
        if self.is_dd==True:
            ip = self.get_Binary()
        dict_={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        for i in range(0,len(ip),8):
            num1,num2 = ip[i:i+4],ip[i+4:i+8]
            h1,h2 = self.binary_decimal(num1),self.binary_decimal(num2)
            self.hex = self.hex + dict_[h1]+dict_[h2]+':' 
        return self.hex[:len(self.hex)-2]

    def binary_dd(self,ip):
        self.dd=''
        for i in range(0,len(ip),8):
            self.dd = self.dd+'.'+str(self.binary_decimal(ip[i:i+8]))
        return self.dd[1:]
    
    def binary_decimal(self,num):
        decimal=0
        for i in range(len(num)):
            decimal += int(num[len(num)-i-1])*2**i
        return int(decimal)
    def binary_hex(self):
        res = ''
        dict_={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        for i in range(0,len(self.ip),8):
            num1,num2 = ip[i:i+4],ip[i+4:i+8]
            h1,h2 = binary_decimal(num1),binary_decimal(num2)
            res = res + dict_[h1]+dict_[h2]+':' 
        return res
    
    def Hex_DD(self):
        dd = ''
        dict_ = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        for byte in self.ip.split(':'):
            dd+= '.'+str(dict_[byte[0]]*16+dict_[byte[1]]*1)
        return dd[1:]
            
    def get_subnet_details(self,n):
        ip = self.binary
        #mask=self.subnet_mask
        mask = ''
        not_mask = ''
        for i in range(1,33):
            if i<= n :
                mask+='1'
                not_mask+='0'
            else:
                mask+='0'
                not_mask+='1'
        first=''
        last=''
        for (i,j) in zip(ip,mask):
            first+=str(int(i) and int(j))
        for (i,j) in zip(ip,not_mask):
            last+=str(int(i) or int(j))
        first_add = self.binary_dd(first)
        last_add = self.binary_dd(last)
        no_add_sub = 2**(32-n)
        not_mask = ''
        print('Initial Address : ',first_add)
        print('No of addreses in subnets are : ',no_add_sub)
        print('Last address : ',last_add)
        

class Subnet(IP):

    def __init__(self,ip):
        self.ip = ip
        self.ip=ip
        self.is_dd = self.is_DD()
        self.is_binary = self.is_Binary()
        self.is_hex = self.is_Hex()
        self.binary = self.get_Binary()
        self.dd = self.get_DD()
        self.hex = self.get_Hex()
        self.class_= self.get_class()
        
    def get_subnet_details(self,n=0):
        ip = self.binary
        if n==0:
            mask,n = self.get_default_mask()
            mask = ''
            not_mask = ''
            for i in range(1,33):
                if i<= n :
                    mask+='1'
                    not_mask+='0'
                else:
                    mask+='0'
                    not_mask+='1'
        else:   
            mask = ''
            not_mask = ''
            for i in range(1,33):
                if i<= n :
                    mask+='1'
                    not_mask+='0'
                else:
                    mask+='0'
                    not_mask+='1'
        first=''
        last=''
        for (i,j) in zip(ip,mask):
            first+=str(int(i) and int(j))
        for (i,j) in zip(ip,not_mask):
            last+=str(int(i) or int(j))
        self.first_add = self.binary_dd(first)
        self.last_add = self.binary_dd(last)
        no_add_sub = 2**(32-n)
        not_mask = ''
        print('Initial Address : ',self.first_add)
        print('No of addreses in one subnet are : ',no_add_sub)
        print('Last address : ',self.last_add)
        
    def get_default_mask(self):
        if self.class_=='A':
            return ('255.0.0.0',8)
        elif self.class_=='B':
            return ('255.255.0.0',16)
        elif self.class_=='C':
            return ('255.255.255.0',24)
        else:
            return ('240.0.0.0',4)
        
    def conv_dd(self,num):
        dd = ''
        if num%256 == 0 :
            while num!=0:
                if num > 256:
                    dd='.'+str(255)+dd
                    num = num//256
                else :
                    dd='.'+str(num-1)+dd
                    num = num//256
            if len(dd[1:].split('.'))!=4:
                if len(dd[1:].split('.'))==1:
                    dd = '0.0.0'+dd
                elif len(dd[1:].split('.'))==2:
                    dd = '0.0'+dd
                elif len(dd[1:].split('.'))==3:
                    dd = '0'+dd
                else:
                    pass
            return dd
        else:
            if num<256 :
                return '0.0.0.'+str(num)
            print('please enter number multiple of 256 .')
            
    def binary(self,num):
        binary = ''
        while num!=0 :
            binary = str(num%2) + binary
            num = num//2
        if len(binary)!=32 :
            for i in range(32-len(binary)):
                binary='0'+binary
        return binary
    
    def get_binary(self,num):
        binary = ''
        while num!=0 :
            binary = str(num%2) + binary
            num = num//2
        if len(binary)!=32 :
            for i in range(32-len(binary)):
                binary='0'+binary
        return binary
            
    def binary_dd(self,ip):
        dd=''
        for i in range(0,len(ip),8):
            dd = dd+'.'+str(self.binary_decimal(ip[i:i+8]))
        return dd[1:]
            
    def binary_decimal(self,num):
        decimal=0
        for i in range(len(num)):
            decimal += int(num[len(num)-i-1])*2**i
        return decimal
            
        
    def get_subnets(self,subnets,mask=0):
        from_ = []
        to_ = []
        if mask!=0 :
            mask_ = ''
            not_mask_ = ''
            for i in range(1,33):
                if i<= mask :
                    mask_+='1'
                    not_mask_+='0'
                else:
                    mask_+='0'
                    not_mask_+='1'
        else:
            mask_,mask = self.get_default_mask()
            not_mask_ = ''
            for i in range(1,33):
                if i<= mask :
                    not_mask_+='0'
                else:
                    not_mask_+='1'
            print('Default Mask : ',mask_)
        if subnets > self.binary_decimal(not_mask_)+1:
            print('{} Subnets are not possible with given IP .'.format(subnets))
            return None
        mask_n = round(math.log2(subnets))
        if 2**mask_n >= subnets :
            pass
        else:
            mask_n+=1
        total_add = 2**(32-(mask))
        add_per_subnets = (2**(32-(mask+mask_n)))
        print("Total address : ",total_add)
        print('add_per_subnets : ',add_per_subnets)
        add_inc = self.conv_dd(add_per_subnets)
        print(add_inc)
        from_.append(self.first_add)
        for i in range(subnets):
            addr = from_[-1].split('.')
            num=0
            for i in range(len(addr)):
                num += int(addr[len(addr)-(i+1)])*(256**i)
            to_.append(self.binary_dd(self.get_binary(num+add_per_subnets-1)))
            addr = to_[-1].split('.')
            num=0
            for i in range(len(addr)):
                num += int(addr[len(addr)-(i+1)])*(256**i)
            from_.append(self.binary_dd(self.get_binary(num+1)))
            
        return pd.DataFrame({'From':from_[:-1],'To':to_})
        
    