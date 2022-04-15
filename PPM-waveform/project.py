am = 219104

binary = 0
ctr = 0 #length of binary
temp = am  #copy am's number


#find binary value using while loop
while(temp > 0):
    binary = ((temp%2)*(10**ctr)) + binary
    temp = int(temp/2)
    ctr += 1
    
zero_filled_number = binary

#if the binary number is not multiply of 3
while ctr % 3 != 0:
    number_str = str(binary)
    zero_filled_number = number_str.zfill(ctr+1)
    ctr += 1
    
#output the result       
print("\nThe number {x} in binary system is: {y}".format(x=am, y=zero_filled_number))


#separate the binary number by 3 bits
n=[int(i) for i in str(zero_filled_number)]

z=[n[i : i + 3] for i in range(0, len(n), 3)]

print("\nBinary number separated by 3 bits: \n{z}".format(z=z))


#convert code Gray to ppm bits
ppm_list=[]

for i in range(0,len(z)):
    if z[i]==[0,0,0]: #binary: 000
        ppm_list.append("10000000")
    elif z[i]==[0,0,1]: #binary: 001
        ppm_list.append("01000000")
    elif z[i]==[0,1,1]: #binary: 010
        ppm_list.append("00100000")
    elif z[i]==[0,1,0]: #binary: 011
        ppm_list.append("00010000")
    elif z[i]==[1,1,0]: #binary: 100
        ppm_list.append("00001000")
    elif z[i]==[1,1,1]: #binary: 101
        ppm_list.append("00000100")
    elif z[i]==[1,0,1]: #binary: 110
        ppm_list.append("00000010")
    elif z[i]==[1,0,0]: #binary: 111
        ppm_list.append("00000001")
    
print("\nThe corresponding PPM numbers are: \n{t}".format(t=ppm_list))
   

#create the diagram PPM
import numpy as np
import matplotlib.pyplot as plt


#split list is a list which includes all of the bits one by one
split_list=[]
x = ''
for i in range(0,len(ppm_list)):
    x = x + ppm_list[i]
   
for i in range(1,len(x)+1):
    split_list.append(int(x[i-1:i]))

print("\nSeperated bits: \n{j}".format(j=split_list))

plt.close('all')

samples=10 #10 points for each bit
no_sym =len(split_list)

plt.stem(split_list)

#generate signal
TS=3*10**-6 #the period in msec
M=8 #we want 8-ppm
N=480 #because we have 80 samples of each pulse, and I have 6 pulses

signal=np.zeros(samples*no_sym)
split_array = np.array(split_list)

id_n=np.where(split_array==1)

for i in id_n[0]:
    temp=int(i*samples)
    signal[temp:temp+samples]=1  #make the axon y
    
time = np.arange(0, len(signal)*(TS*10**6/(M*10)), TS*10**6/(M*10)) #make the axon x

font = {'family' : 'Times New Roman', 
        'weight' : 'normal',
        'size'   : 20}   


plt.rc('font', **font)
plt.figure()
plt.plot(time,signal, marker='o', color='purple') #represantation of ppm pulse
plt.title('PPM Pulse')
plt.grid(axis = 'x')
plt.ylabel('x(t)')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.3)
plt.xlabel('Time [msec]')