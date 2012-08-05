from socket import *
VERBOSE=True
def print_debug(msg,verbose=VERBOSE):
    if not verbose:
        return
    print msg


def tcp_check(serverHost, serverPort):
    result = 1
    verbose = False
    s = socket(AF_INET, SOCK_STREAM)    #create a TCP socket
    try:
        s.connect((serverHost, serverPort))    #connect to server on the port
        s.shutdown(2)                #disconnect
        print_debug("Success. Connected to " + serverHost + " on port: " + str(serverPort), verbose)
        result -= 1
    except:
        print_debug("Failure. Cannot connect to " + serverHost + " on port: " + str(serverPort))
    return result

def tcp_check_bulk(serverHost, serverPort, connectTimes):
    result = connectTimes
    count = 0
    successcount = 0
    failurecount = 0
    verbose = False
    while (count < connectTimes) :
        curr_result = tcp_check(serverHost,serverPort)
        if curr_result:
            failurecount += 1
        else:
            successcount += 1
        count += 1
    result -= successcount 
    if result:
        verbose = True
    print_debug("Done with " + serverHost + " on port: " + str(serverPort), verbose)
    print_debug("Done. Failures : " + repr(failurecount) + " Successes : " + repr(successcount), verbose)
    return result
