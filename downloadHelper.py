from subprocess import call
#execute command number 1 
def dwn(link,Type):
    command = "youtube-dl "+link+Type
    call(command.split(), shell=False)
#execute command number 2 with output
def dwnOut(link,Type):
    import subprocess, sys
    cmd="youtube-dl "+link+Type
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=False)
    (output, err) = p.communicate()
    p_status = p.wait()
    print ("Command output : ", output)
    print ("Command exit status/return code : ", p_status)
#get input
li=input("send link to video: ")
Vtype=input("A audio\nB bad audio\nC best quality video\n"
            "D bad quality video\nE video thumbnail\n"
            "F type your command\nG video thumbnail\n"
            "H list formats\nI video 720 if available"
            "\nplease choose what you want: "
            )
Vtype=Vtype.lower()
#check input and run
if (Vtype=="a"):
    dwnOut(li," -f bestaudio ")
    #dwn(li," -f bestaudio ")
elif (Vtype=="b"):
    dwnOut(li," -f worstaudio ")
    #dwn(li," -f worstaudio ")
elif (Vtype=="c"):
    dwnOut(li," -f best ")
    #dwn(li," -f best ")
elif (Vtype=="d"):
    dwnOut(li," -f worst ")
    #dwn(li," -f worst ")
elif (Vtype=="e"):
    dwnOut(li," --write-thumbnail ")
    #dwn(li," --write-thumbnail ")
elif (Vtype=="f"):
    cmd=input("Enter your commad")
    if(cmd[0]!=" "):
        cmd=" "+cmd
    dwnOut(li,cmd)
    #dwn(li,cmd)
elif (Vtype=="g"):
    dwnOut(li," --list-formats ")
    #dwn(li," --list-formats ")
elif (Vtype=="g"):
    dwnOut(li," -f best[height=720] ")
    #dwn(li," -f best[height=720] ")
elif (Vtype=="j"):
    dwnOut(li," -f best[height=480] ")
    #dwn(li," -f best[height=480] ")
elif (Vtype=="k"):
    dwnOut(li," -f best[height=360] ")
    #dwn(li," -f best[height=360] ")
elif (Vtype=="0"):
    dwnOut(li,"")
else:
    print("command not find")
