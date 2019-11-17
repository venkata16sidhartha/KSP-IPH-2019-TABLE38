def enter_user(beat_number,person_id,name):
    file=open("passwords.txt",'a')
    usertemp="_"+str(beat_number)+"_"+str(person_id)
    user=name+usertemp
    pswdtemp="_"+(str(beat_number).encode('base64'))+"_"+(str(person_id).encode('base64'))
    pswd=name+pswdtemp
    file.write(user+"::"+pswd)
    file.close()


def confirm_user(username,password):
    with open('passwords.txt') as f:
        s=[password[5],password[6]]
        d=[password[8],password[9]]
        if(username+"::"+password[0]+password[1]+password[2]+password[3]+password[4]+("".join(s)).encode('base64')+"_"+("".join(d)).encode('base64') in f.read()):
            print("nice")
        else:
            print("get lost")


if( __name__ == '__main__'):
    beat_number=int(input("enter user id : "))
    person_id=int(input("enter personal id : "))
    name=str(input("enter the class : "))
    enter_user(beat_number,person_id,name)
    usr=str(input("entr the username : "))
    psd=str(input("enter the pswd : "))
    confirm_user(usr,psd)
