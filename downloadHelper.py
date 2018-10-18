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
            "D bad quality video\nE video thumbnail and video\n"
            "F type your command\nG list formats\n"
            "H video 720 if available\nI video 480 if available\n"
            "j video 360 if available\nK thumbnail only\n"
            "0 For No Command\n"
            "\nplease choose what you want: "
            )
Vtype=Vtype.lower()
#check input and run
if (Vtype=="a"):
    dwnOut(li," -f bestaudio -c")
    #dwn(li," -f bestaudio -c")
elif (Vtype=="b"):
    dwnOut(li," -f worstaudio ")
    #dwn(li," -f worstaudio -c")
elif (Vtype=="c"):
    dwnOut(li," -f best -c")
    #dwn(li," -f best -c")
elif (Vtype=="d"):
    dwnOut(li," -f worst -c")
    #dwn(li," -f worst -c")
elif (Vtype=="e"):
    dwnOut(li," --write-thumbnail -c")
    #dwn(li," --write-thumbnail -c")
elif (Vtype=="f"):
    cmd=input("Enter your commad")
    if(cmd[0]!=" "):
        cmd=" "+cmd
    dwnOut(li,cmd)
    #dwn(li,cmd)
elif (Vtype=="g"):
    dwnOut(li," --list-formats -c")
    input("perss any key to continue")
    #dwn(li," --list-formats ")
elif (Vtype=="h"):
    dwnOut(li," -f best[height=720] -c")
    #dwn(li," -f best[height=720] ")
elif (Vtype=="i"):
    dwnOut(li," -f best[height=480] -c")
    #dwn(li," -f best[height=480] ")
elif (Vtype=="j"):
    dwnOut(li," -f best[height=360] -c")
    #dwn(li," -f best[height=360] ")
elif (Vtype=="0"):
    dwnOut(li,"")
elif (Vtype=="k"):
    dwnOut(li," --write-thumbnai --skip-download ")
else:
    print("command not find")
input("send any key to close!")
