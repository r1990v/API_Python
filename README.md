# API_Python



import requests
import json
import time


def executeapitest(temp1, temp2, temp3, iterations):

    for i in range(1, iterations+1):
        print("Iteration: "+str(i))
        logonurl = "http://mo-9d4145d58.mo.sap.corp:6405/biprws/logon/long"
        logonpayload = {'userName': 'Administrator', 'password': 'Password1', 'auth': 'secEnterprise'}
        abouturl = "http://mo-9d4145d58.mo.sap.corp:6405/biprws/v1/about"
        logoffurl = "http://mo-9d4145d58.mo.sap.corp:6405/biprws/logoff"

        # Create a dictionary which will set accept and content-type to json
        jsonheader = {'Accept': 'application/json', 'Content-Type': 'application/json'}

        # Calling get method on Logon api url to get list of parameters required to logon
        # logonGetRequest = requests.get(logonurl, headers=jsonheader)
        # print(logonGetRequest | logonGetRequest.text | logonGetRequest.headers)

        # Start the timer before making the post request
        start = time.time()
        post_request = requests.post(logonurl, data=json.dumps(logonpayload), headers=jsonheader)
        # print(post_request.headers['X-SAP-LogonToken'])

        assert 'X-SAP-LogonToken' in post_request.headers, "Text check validation failed for logon api call"
        # Stop the timer after sap logon token is found.
        end = time.time()
        # print("Time taken to open logon section: {0:.2f}".format(end - start))
        temp1 = temp1 + (end - start)

        sap_logontoken = {'X-SAP-LogonToken': post_request.headers['X-SAP-LogonToken']}

        # Create a new Dictionary object and Copy value of Simple json header to it
        headerwithlogontoken = jsonheader.copy()
        # Add/append/update newly created dictionary with SAP Logon Token received in response of post request made to
        # logon api url
        headerwithlogontoken.update(sap_logontoken)
        # print(newHeader)

        start = time.time()
        getaboutinfo = requests.get(abouturl, headers=headerwithlogontoken)
        assert 'SAP SE or an SAP affiliate company' in getaboutinfo.text, "Text check validation failed for about" \
                                                                          " api call"
        end = time.time()
        # print("Time taken to display About information: {0:.2f}".format(end - start))
        # print(getaboutinfo.text)
        temp2 = temp1 + (end - start)
        start = time.time()
        requests.get(logoffurl, headers=headerwithlogontoken)
        end = time.time()
        # print("Time taken to Logoff from BOE machine: {0:.2f}".format(end - start))
        temp3 = temp1 + (end - start)

    print(('-'*18) + "Final Results" + ('-'*18))
    print("Logon API call average response time: {0:.3f} Sec\nAbout API call  average response time: {1:.3f} Sec\n"
          "Logoff API call average response time: {2:.3f} Sec".format((temp1/iterations), (temp2/iterations),
                                                                      (temp3/iterations)))
    print(('-'*18) + "Results End" + ('-'*20))


def main():
    numberofiterations = 10
    valueinit = 0.0
    executeapitest(valueinit, valueinit, valueinit, numberofiterations)

if __name__ == '__main__':
    main()

__author__ = "Rahul Vats"
