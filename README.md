# IP
IP address python library for conversion and subnet calculation for Classful and Classless IP addresses.

### How to use

### 1. Import Clasess
```
from IP import *
```

### 2. Create object of IP address

```
ip = IP('167.199.170.82')
```

### 3. Get details of given IP address
```
print(ip.get_details())
```
Result
```
IP :  167.199.170.82
Class :  B
Binary representation :  10100111110001111010101001010010
Dotted Decimal Representation :  167.199.170.82
hexadecimal representation :  A7:C7:AA:5
```

### 4. Get Class Details (NetID and HostID)
```
print(ip.get_class_details()) 
```
Result
```
Net ID :  167.199
Network Address :  167.199.0.0
Host ID :  170.82
Defaut Subnet mask :  255.255.0.0
```

### 5. Get Subnet Related Details

```
print(ip.get_subnet_details(27)) 
```
Here ``` get_subnet_details(length_of_mask)``` contains argument as mask length if it is provided otherwise default mask length.
Result
```
Initial Address :  167.199.170.64
No of addreses in subnets are :  32
Last address :  167.199.170.95
```

### 6. Create object of subnet class

```
s = Subnet('143.50.0.0') 
```

### 7. Get Subnets

```
print(s.get_subnets(no_of_subnets))
```
Result
```
Default Mask :  255.255.0.0
Total address :  65536
add_per_subnets :  4096
0.0.15.255


            From              To
0     143.50.0.0   143.50.15.255
1    143.50.16.0   143.50.31.255
2    143.50.32.0   143.50.47.255
3    143.50.48.0   143.50.63.255
4    143.50.64.0   143.50.79.255
5    143.50.80.0   143.50.95.255
6    143.50.96.0  143.50.111.255
7   143.50.112.0  143.50.127.255
8   143.50.128.0  143.50.143.255
9   143.50.144.0  143.50.159.255
10  143.50.160.0  143.50.175.255
11  143.50.176.0  143.50.191.255
12  143.50.192.0  143.50.207.255
13  143.50.208.0  143.50.223.255
14  143.50.224.0  143.50.239.255
15  143.50.240.0  143.50.255.255

```
Function get_subnets(no_of_subnets) has parameter no of subnets that user has to produce from given IP address.
