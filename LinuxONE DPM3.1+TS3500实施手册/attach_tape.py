#!/usr/bin/env python

import os, httplib, sys, getopt, json, ssl

session_id = None   # The WS API session ID from a successful Logon operation
part_uri = None
sg_uri = None

me = os.path.basename(__file__)
syntax_line = "Syntax:\n\t%s -h <hmc_address> -u <userid> -p <password>" % me


# Set some defaults
port=6794   # The HMC's WS APIs port (SSL/TLS)

##############################
# Start of Declaration Section 
##############################
hmc_address = "9.xyz.abc.10"              # Specify The IP of the HMC

hmc_userid = "SUPERMAN"                   # Specify Target User with Superadele privileges

hmc_password = "password"                 # Specify Password associated with the user

cpc_name = 'P000M6010'                    # Specify CPC name

#partition_object_id_customer = "49fb08ac-b5ab-11e9-af90-00106f0d81cb" # Specify Object ID of the target partition where storage group needs to be attached, e.g. "0b70e384-b599-11e9-b521-00106f0d81cb"

storage_group_uuid_customer = "6d8cface-b75d-11e9-ac66-00106f0d81cb"         # Specify UUID of the Target Storage Group, e.g. "0c086628-b599-11e9-ae7e-00106f0d81cb"

## Specify UUIDs of adapters to be added as a candidate adapter in the Storage Group depends on the target storage group Connectivity value
adapter_port_list = ['B0D3C2F0-4FC4-11E9-B8FD-00106F0D81C9',
                     'AEFE68FE-4FC4-11E9-B8FD-00106F0D81C9']

##############################
# End of Declaration Section 
##############################


if hmc_address is None or hmc_userid is None or hmc_password is None or cpc_name is None :	
    print "Missing target system required detail(s)"
    sys.exit(3)


#if partition_object_id_customer is not None :
#    part_uri = '/api/partitions/'+partition_object_id_customer
#else :
#    print "Missing target partition Object ID"
#    sys.exit(3)


if storage_group_uuid_customer is not None :
    sg_uri = '/api/storage-groups/'+storage_group_uuid_customer
else :
    print "Missing target storage group UUID"
    sys.exit(3)

method_get = "GET"
method_post = "POST"
method_delete = "DELETE"


#############################################################################################
# Simple function to read a response body and verify the HTTP status code.  If the status
# code does not match the expected value, an Exception is raised; otherwise, the response
# body is returned in JSON format.
#############################################################################################
def check_response(response, expected_status_code):
    http_status_code = response.status  # Get the HTTP status code
    response_body = response.read()     # Get the response body
    if response_body != None and len(response_body) > 0:    # There is a response body
        response_body = json.loads(response_body)           # Get the response body as JSON

    if http_status_code != expected_status_code: # Failed
        if response_body != None:   # There's a response body; look for reason code and error message
            reason_code = response_body["reason"] if "reason" in response_body else None
            message = response_body["message"] if "message" in response_body else None
        raise Exception("Request failed (uri: %s, status: %d, reason: %s, message: %s)" % (uri, http_status_code, reason_code, message))

    return response_body


#############################################################################################
# Simple function to print a JSON response body.  Make it pretty and sort it by the key names.
#############################################################################################
def print_response_body(response_body):
    print "\nResponse body:\n%s" % json.dumps(response_body, True, indent=1, separators=(',',':'))


try:
    # Parse the command line
    opts, args = getopt.getopt(sys.argv[1:],"?h:u:p:")

except getopt.GetoptError as error:
    print(str(error))
    print syntax_line
    sys.exit(2)

# Process the command line options and arguments
for opt, arg in opts:
    if opt == "-?":
        print syntax_line
        sys.exit(1)
    elif opt in ("-h"):
        hmc_address = arg
    elif opt in ("-u"):
        hmc_userid = arg
    elif opt in ("-p"):
        hmc_password = arg

if hmc_address is None or hmc_userid is None or hmc_password is None:
    print "Missing required argument(s)"
    print syntax_line
    sys.exit(3)

try:
    # Connect to the HMC's WS API port.
    # Beginning with Python 2.7, SSL connections are more secure and require a valid
    # X509 certificate signed by a trusted CA.  Since test HMCs use a self-signed certificate,
    # we revert to previous Python behavior by explicitly requesting an unverified context.
    # This is generally not advisable, for obvious security reasons, but it is acceptable in the
    # development and test environments in which these API test utilities are intended to be used.
    
    if sys.hexversion < 0x02070000: # Prior to 2.7; use default behavior
        conn = httplib.HTTPSConnection(hmc_address, int(port))
    else:   # 2.7 or later; specifically request prior behavior
        conn = httplib.HTTPSConnection(hmc_address, int(port), context=ssl._create_unverified_context())


    ################### Build and issue a "Logon" request ###############################

    # logon to the WS APIs and create an authenticated session
    uri = "/api/sessions"   # The request URI for the Logon operation
    request_body = {"userid":hmc_userid, "password":hmc_password}
    request_headers = {"Content-type":"application/json", "Accept":"*/*"}

    conn.request("POST", uri, json.dumps(request_body), request_headers)    # Send the Logon request
    response = conn.getresponse()                   # Get the response
    response_body = check_response(response, 200)   # Check the response and get the response body

#   print_response_body(response_body)access

    # Logon succeeded; get the session ID
    session_id = response_body["api-session"]

    # All subsequent requests for this session must include the WS API session ID in a header
    standard_request_headers = {"Content-type":"application/json", "Accept":"*/*", "X-API-Session":session_id}

    ################### Build and issue a "Query API Version" request ###############################
    # This is a GET request with no request body

    # Build the request
    
    uri = "/api/version"

    print "\nAbout to issue request: %s %s" % (method_get, uri)
    conn.request(method_get, uri, None, standard_request_headers)    # Send the request
    response = conn.getresponse()                       # Get the response
    response_body = check_response(response, 200)       # Check the response and get the response body

    print_response_body(response_body)

    ################### Build and issue a "???" request ###############################
    # This is a POST request with a request body
    
    list_cpc_uri = "/api/cpcs?name="+cpc_name
    
    print "\nAbout to issue request: %s %s" % (method_get, list_cpc_uri)
    conn.request(method_get, list_cpc_uri, None, standard_request_headers)    # Send the request
    response = conn.getresponse()                       # Get the response
    response_body = check_response(response, 200)       # Check the response and get the response body
    print_response_body(response_body)
    
    cpc_uri = response_body['cpcs'][0]['object-uri']
    
    print "The uri of the target CPC is: "+ cpc_uri   

    
    #print "The uri of the given parition is : "+ part_uri   

    
    sg_uri = '/api/storage-groups/'+storage_group_uuid_customer
    print "\nAbout to issue request: %s %s%s" % (method_get, sg_uri, "/storage-volumes?usage=boot")
    conn.request(method_get, sg_uri+'/storage-volumes?usage=boot', None, standard_request_headers)    # Send the request
    response = conn.getresponse()                       # Get the response
    response_body = check_response(response, 200)  
    volume_uri = response_body['storage-volumes'][0]['element-uri']
    
    
    
    port_list = []
    for adapter_uuid in adapter_port_list:
        adapter_port_uri = '/api/adapters/'+adapter_uuid+'/storage-ports/0'
        port_list.append(adapter_port_uri)
        
    
    print "\nAbout to issue request: %s %s" % (method_post, sg_uri+'/operations/add-candidate-adapter-ports')
    print "Request body is: %s", json.dumps({'adapter-port-uris' : port_list})
    
    conn.request(method_post, sg_uri+'/operations/add-candidate-adapter-ports', json.dumps({'adapter-port-uris' : port_list}), standard_request_headers)    # Send the request
    response = conn.getresponse()                       # Get the response
    response_body = check_response(response, 204) 
    print_response_body(response_body)
    #'''
        
    print "\nAbout to issue request: %s %s" % (method_post, sg_uri+'/operations/fulfill-fcp-storage-volume')
    print "Request body is: %s ", json.dumps({'adapter-port-uri' : port_list[0],'world-wide-port-name':'1234567890abcdef','logical-unit-number':'1234567890abcdef'})
    
    print "\n Doing the Manual Fulfillment on the FCP Storage Volume with the following Attributes:"
    print '\n Volume URI: '+volume_uri
    print '\n adapter-port-uri : '+port_list[0]
    conn.request(method_post, volume_uri+'/operations/fulfill-fcp-storage-volume', json.dumps({'adapter-port-uri' : port_list[0],'world-wide-port-name':'1234567890abcdef','logical-unit-number':'1234567890abcdef'}), standard_request_headers)    # Send the request
    response = conn.getresponse()                       # Get the response
    response_body = check_response(response, 204) 
    print_response_body(response_body)
    
    
    #print "\nAbout to issue request: %s %s" % (method_post, part_uri+'/operations/attach-storage-group')
    #conn.request(method_post, part_uri+'/operations/attach-storage-group', json.dumps({'storage-group-uri' : sg_uri}), standard_request_headers)    # Send the request
    #response = conn.getresponse()                       # Get the response
    #response_body = check_response(response, 204)  
    #print_response_body(response_body)
    
    #vhba_props = sg_uri+'/virtual-storage-resources?adapter-port-uri='+port_list[0]
    #print "\nAbout to issue request: %s %s" % (method_get, vhba_props)
    #conn.request(method_get, vhba_props, None, standard_request_headers)    # Send the request
    #response = conn.getresponse()                       # Get the response
    #response_body = check_response(response, 200) 
    #print_response_body(response_body)
    #volume_uri = response_body['virtual-storage-resources'][0]['element-uri']
    
except Exception as exc:
    print "Caught Exception: %s" % exc

finally:
    # If an Exception is caught after a successful Logon, issue a Logoff, so we don't leave an API session hanging around
    
    
         
    if session_id is not None:  # We've logged on
        ######################################################################################
        ################### Build and issue a "Logoff" request ###############################
        ######################################################################################
        uri = "/api/sessions/this-session"
        request_headers = {"Content-type":"application/json", "Accept":"*/*", "X-API-Session":session_id}
        print "\nIssuing a Logoff request..."
        conn.request(method_delete, uri, None, request_headers)  # Send the Logoff request
