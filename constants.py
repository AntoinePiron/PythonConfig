data = {
    '5000': {
        'GigabitEthernet1/0' : {
            'ip' : '192.168.0.1',
            'subnetwork' : '192.168.0.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet2/0' : {
            'ip' : '192.168.1.1',
            'subnetwork' : '192.168.1.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet3/0' : {
            'ip' : '192.168.12.1',
            'subnetwork' : '192.168.12.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : True,
        },
        'as_number' : 1,
        'CE': False,
        'edge': True,
        'neigbors' : {
            '5008' : {
                'ip' : '192.168.12.2',
                'as_number' : 2,
            }
        },
        'vrf': {
            'client1': {
                'interface' : 'GigabitEthernet3/0',
                'rt' : '100:100',
                'rd' : '100:100',
            }
        },
    }, 
    '5001': {
        'GigabitEthernet1/0' : {
            'ip' : '192.168.3.1',
            'subnetwork' : '192.168.3.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet2/0' : {
            'ip' : '192.168.2.1',
            'subnetwork' : '192.168.2.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'as_number' : 1,
        'CE': False,
        'edge': True,
    }, 
    '5002': {
        'GigabitEthernet1/0' : {
            'ip' : '192.168.0.2',
            'subnetwork' : '192.168.0.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet2/0' : {
            'ip' : '192.168.2.2',
            'subnetwork' : '192.168.2.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet3/0' : {
            'ip' : '192.168.6.1',
            'subnetwork' : '192.168.6.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet4/0' : {
            'ip' : '192.168.7.1',
            'subnetwork' : '192.168.7.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'as_number' : 1,
        'CE': False,
        'edge': False,
    }, 
    '5003': {
        'GigabitEthernet1/0' : {
            'ip' : '192.168.3.2',
            'subnetwork' : '192.168.3.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet2/0' : {
            'ip' : '192.168.1.2',
            'subnetwork' : '192.168.1.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet3/0' : {
            'ip' : '192.168.6.2',
            'subnetwork' : '192.168.6.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet4/0' : {
            'ip' : '192.168.5.1',
            'subnetwork' : '192.168.5.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'as_number' : 1,
        'CE': False,
        'edge': False,
    },
    '5004': {
         'GigabitEthernet1/0' : {
            'ip' : '192.168.11.2',
            'subnetwork' : '192.168.11.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet2/0' : {
            'ip' : '192.168.9.2',
            'subnetwork' : '192.168.9.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet3/0' : {
            'ip' : '192.168.4.2',
            'subnetwork' : '192.168.4.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet4/0' : {
            'ip' : '192.168.5.2',
            'subnetwork' : '192.168.5.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'as_number' : 1,
        'CE': False,
        'edge': False,
    },
    '5005': {
        'GigabitEthernet1/0' : {
            'ip' : '192.168.8.2',
            'subnetwork' : '192.168.8.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet2/0' : {
            'ip' : '192.168.10.2',
            'subnetwork' : '192.168.10.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet3/0' : {
            'ip' : '192.168.4.1',
            'subnetwork' : '192.168.4.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet4/0' : {
            'ip' : '192.168.7.2',
            'subnetwork' : '192.168.7.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'as_number' : 1,
        'CE': False,
        'edge': False,
    },
    '5006': {
        'GigabitEthernet1/0' : {
            'ip' : '192.168.8.1',
            'subnetwork' : '192.168.8.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet2/0' : {
            'ip' : '192.168.9.1',
            'subnetwork' : '192.168.9.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet3/0' : {
            'ip' : '192.168.13.1',
            'subnetwork' : '192.168.13.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : True,
        },
        'as_number' : 1,
        'CE': False,
        'edge': True,
        'neigbors' : {
            '5009' : {
                'ip' : '192.168.13.2',
                'as_number' : 3,
            }
        },
        'vrf': {
            'client1': {
                'interface' : 'GigabitEthernet3/0',
                'rt' : '100:100',
                'rd' : '100:100',
            }
        },
    }, 
    '5007': {
        'GigabitEthernet1/0' : {
            'ip' : '192.168.11.1',
            'subnetwork' : '192.168.11.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'GigabitEthernet2/0' : {
            'ip' : '192.168.10.1',
            'subnetwork' : '192.168.10.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'as_number' : 1,
        'CE': False,
        'edge': True,
    }, 
    '5008' :{
        'GigabitEthernet1/0' : {
            'ip' : '192.168.12.2',
            'subnetwork' : '192.168.12.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : True,
        },
        'GigabitEthernet2/0' : {
            'ip' : '192.168.14.2',
            'subnetwork' : '192.168.14.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'as_number': 2,
        'CE': True,
        'edge': True,
        'neigbors' : {
            '5000' : {
                'ip' : '192.168.12.1',
                'as_number' : 1,
            }
        }
    },
    '5009' :{
        'GigabitEthernet1/0' : {
            'ip' : '192.168.13.2',
            'subnetwork' : '192.168.13.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : True,
        },
        'GigabitEthernet2/0' : {
            'ip' : '192.168.15.2',
            'subnetwork' : '192.168.15.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'as_number': 3,
        'CE': True,
        'edge': True,
        'neigbors' : {
            '5006' : {
                'ip' : '192.168.13.1',
                'as_number' : 1,
            }
        }
    }
}