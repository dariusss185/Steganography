import cv2
import pathlib
import os

def errorcatch():
    while True:
        try:
            m=str(input("Please input the name of the image you want to use for encryption: "))
            if m.lower().endswith(('.png'))==False:
                while m.lower().endswith(('.png'))==False:
                    m=str(input("We only accept PNG fileformat \nPlease input your correct value: "))
            break
        except ValueError:
            print("INVALID ENTRY. TRY AGAIN")
    return(m.lower())
    #checking to see if there is a valid input of png

class Test:
        def __init__(self, name):
            self.path=str(pathlib.Path(__file__).parent.resolve())+"/"+name
            self.image=cv2.imread(self.path,1)
            self.horizontal = self.image.shape[0]
            self.vertical = self.image.shape[1]
            self.maximum=self.horizontal*self.vertical*3

def decodeAscii(bin_string):
    binary_int = int(bin_string, 2);
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = "Bin string cannot be decoded"
    for enc in ['utf-8', 'ascii', 'ansi']:
        try:
            ascii_text = binary_array.decode(encoding=enc)
            break
        except:
            pass
    return(ascii_text)
    print(ascii_text)
    #decoding ascii to text


def decrypt(image,width,height):
    count=0
    lista=[]
    for i in range (0,width):
            for l in range(0,height):
                for p in range(0,3):
                    #print (int_to_binary(image[i,l,p]),image[i,l,p], "row",i,"column",l,"lsb:",(int_to_binary(image[i,l,p])[7]))
                    lista.append((int_to_binary(image.image[i,l,p])[7]))
                    if (int_to_binary(image.image[i,l,p])[7])=="0":
                        count=count+1
                    if len(lista)%8==0 and count!=8:
                        #print ("reset")
                        #print(count)
                        count=0
                        #print(lista)
                    elif (int_to_binary(image.image[i,l,p])[7])!="0":
                        count=0
                    
                    finalst=""
                    if count==8:
                        word=""
                        #print("finish")
                        #print(lista)
                        lista = lista[:len(lista)-8]
                        #print(lista)
                        #print(len(lista))
                        length=(len(lista))//8
                        for o in range(0,length):
                            word=""
                            #print(length)
                            for x in range(0,8):
                                word=word+lista[x]
                                #print(word)
                                if len(word)==8:
                                    lista= lista[8:]
                                    #print(word)
                                    #print("decoding")
                                    strings=decodeAscii(word)
                                    finalst=finalst+strings
                                    word=""
                        
                        print("Extracted text:"+finalst)
                        return

def int_to_binary(integer):
    binary_string = ''
    while(integer > 0):
        digit = integer % 2
        binary_string += str(digit)
        integer = integer // 2
    binary_string = binary_string[::-1]
    length=len(binary_string)
    for i in range (length,8):
        binary_string="0"+binary_string
    return (binary_string)

def Encryption(res,length,width):
    c=0
    finaloutput=[]
    finalvals=[]
    for i in range (0,width):
        for l in range(0,length):
            pixel1=(picture.image[i][l])
            for p in range(0,3):
                #print("------------")
                #print("this is row",i,"column",l)
                #print("this is",pixel1,"ON",i,l,p)
                if c==len(res):
                    reset=0
                    for z in range (i,width):
                        for s in range(l,length):
                            for f in range(p,3):
                                #print ("this is pixel,\n", picture.image[z][s], "on",z,s,f)
                                compare=(int_to_binary(picture.image[z][s][f]))
                                #print ("current binary and lsb", compare, compare[7])
                                #if compare =="0":
                                    #print("no change needed")
                                #print("currently", picture.image[z,s,f])
                                if compare!="0":
                                    picture.image[z,s,f]=picture.image.item(z,s,f)-1
                                    #print("we subtracted 1", picture.image[z,s,f])
                                if f==2:
                                    p=0
                                
                                finaloutput.append(int_to_binary(picture.image[z][s][f])[7])
                                reset=reset+1
                                #print("check the binary and last digit: ", (int_to_binary(picture.image[z][s][f])[7]),int_to_binary(picture.image[z][s][f]))
                                if reset==8:
                                    #print(finaloutput)
                                    cv2.imwrite(str(line_new),picture.image)
                                    #print("finish")
                                    return
                                

                pixelbin=int_to_binary(pixel1[p])
                if pixelbin[7]!=res[c]:
                    #print("BEFORE CHANGE", pixelbin) 
                    list1=list(pixelbin)
                    if res[c]=="1":  
                        list1[7] = "1"
                        pixelbin = ''.join(list1)
                        #print(pixel1)
                        picture.image[i,l,p]=picture.image.item(i,l,p)+1
                        #print("we add", picture.image[i,l,p])
                        pixelbin=int_to_binary(picture.image[i,l,p])

                    else:
                        list1[7] = "0"
                        #print(pixel1)
                        picture.image[i,l,p]=picture.image.item(i,l,p)-1
                        pixelbin = ''.join(list1)
                        #print("we subtract", picture.image[i,l,p])
                        pixelbin=int_to_binary(picture.image[i,l,p])
                finaloutput.append(pixelbin[7])

                c=c+1
                    #print(picture.image.item(0,0,0))
                #print("check last digit", pixelbin,"this is the counter",c)
    
name=errorcatch()
suffix='.png'
line_new = str(pathlib.Path(__file__).parent.resolve())+"/"+(name.removesuffix(suffix))+"_encrypted.png"
test_str=str(input("What is the text you want encoded: "))



#path0=pathlib.Path(__file__).parent.resolve()
#path=str(path0)+"/"+name
picture=Test(name)


#print(picture.vertical)

#picture.image=cv2.imread(picture.path,1)

#cv2.imshow("rgb_picture.image", picture.image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#height = picture.image.shape[0]
#width = picture.image.shape[1]



#printing original string
#print("The original string is : " + str(test_str))
 
# using join() + bytearray() + format()
# Converting String to binary
res = ''.join(format(i, '08b') for i in bytearray(test_str, encoding ='utf-8'))

if len(res)>=picture.maximum:
    print("Sorry but there is not enough space in the image \nPlease select a bigger picture.image OR make your message smaller")
else:
    Encryption(res,picture.horizontal,picture.vertical)

choice=str(input("Would you like to decrypt the image you just encrypted ? (Y OR N)"))

if choice.lower()=="y":
    img=Test((name.removesuffix(suffix))+"_encrypted.png")
    #or img=str(input("enter full path of the encrypted image"))
    decrypt(img,picture.horizontal,picture.vertical)

#FURTHER ERROR HANDLING CAN BE IMPLEMENTED AND A MORE INTERACTIVE TERMINAL. 

