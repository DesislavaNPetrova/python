### AWS VPN Tunnel States: 'State': 'pending'|'available'|'deleting'|'deleted'
### AWS credentions are available on the machine

#!/usr/bin/env python3

import sys
import boto3
import json
import pprint


REGION = 'us-east-2'

def main():
    if len(sys.argv) < 2:
    	print("Please supply a VPN status as an argument")
    else:
        state = sys.argv[1]
        print("VPN connection state:", state)	

        # Display VPN instances in VPC
        client = boto3.client('ec2', region_name=REGION)
        responce = client.describe_vpn_connections()

        # Use lambda to filter VPN instances that are in our VPC
        vpn_connections = list( lambda x: x["State"] ==state, response["VPNConnections"] ) )
        if len(vpn_connections) > 0:
           print("\nVPN Tunnels info:")
           for vpn in vpn_connections:
           	  pprint.pprint(vpn["VgwTelemetry"])
        else:
            print("There is no Vpn Conenctions in  this VPC!")   	  

if __name__ == "__main__":
    main()            

    