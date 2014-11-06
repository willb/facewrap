#!/usr/bin/env python

import plistlib
import uuid as uuidlib
import sys
import os

def unique_id():
    return uuidlib.uuid4().urn[9:].upper()

def font2payload(family, fontfile):
    with open(fontfile, 'r') as f: 
        data = f.read()
    uuid = unique_id()
    return {
        'Font': plistlib.Data(data),
        'PayloadIdentifier': 'com.freevariable.facewrap.' + uuid, 
        'PayloadOrganization': 'freeariable.com', 
        'PayloadType': 'com.apple.font',
        'PayloadUUID': uuid, 'PayloadVersion': 1
    }

def config(family, fontfiles):
    uuid = unique_id()
    
    result = {
        'PayloadContent': [ font2payload(family, ff) for ff in fontfiles ],
        'PayloadDescription': "installs %s fonts" % family,
        'PayloadDisplayName': family,
        'PayloadIdentifier': 'com.freevariable.facewrap.' + uuid,
        'PayloadOrganization': 'freevariable.com', 
        'PayloadRemovalDisallowed': False, 
        'PayloadType': 'Configuration',
        'PayloadUUID': uuid,
        'PayloadVersion': 1
    }
    
    return plistlib.writePlistToString(result)

if __name__ == '__main__':
    sys.stdout.write(config(sys.argv[1],sys.argv[2:]))