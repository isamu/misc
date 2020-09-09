import platform
import signal, os, subprocess
import concurrent.futures
import time

def run_a():
    while True:
        print("a " + str(os.getpid()))
        time.sleep(1)
    return 6

def run_b():
    while True:
        print("b " + str(os.getpid()))
        time.sleep(1)
    return 


executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)

a = executor.submit(run_b)
b = executor.submit(run_a)

def get_children(parent_pid):
    ps_command = None
    if platform.system() =="Linux":
        ps_command = subprocess.Popen("ps -o pid --ppid %d --noheaders" % parent_pid, shell=True, stdout=subprocess.PIPE)
        
    if platform.system() =="Darwin":
        ps_command = subprocess.Popen("pgrep  -P %d" % parent_pid, shell=True, stdout=subprocess.PIPE)

    ps_output = ps_command.stdout.read().decode("utf-8").split("\n")
    ps_output.remove("")
    # retcode = ps_command.wait()
    return ps_output

def kill_procs(processes):
    for pid_str in processes:
        if pid_str != "":
            print("child2 " + str(pid_str))
            sig=signal.SIGTERM
            os.kill(int(pid_str), sig)
    
while True:
    children = get_children(os.getpid())
    time.sleep(2)
    kill_procs(children)
    executor.shutdown(a)
    print(a)

