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
                'vrf' : 'client1'
            }
        },
        'neigbors_bgp' : ['5006', '5007', '5001'],
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
        'GigabitEthernet3/0' : {
            'ip' : '192.168.20.1',
            'subnetwork' : '192.168.20.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : True,
        },
        'as_number' : 1,
        'CE': False,
        'edge': True,
        'neigbors' : {
            '5014' : {
                'ip' : '192.168.20.2',
                'as_number' : 6,
                'vrf' : 'client2'
            }
        },
        'neigbors_bgp' : ['5006', '5007', '5000'],
        'vrf': {
            'client2': {
                'interface' : 'GigabitEthernet3/0',
                'rt' : '200:200',
                'rd' : '200:200',
            }
        },
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
        'GigabitEthernet4/0' : {
            'ip' : '192.168.16.1',
            'subnetwork' : '192.168.16.0',
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
                'vrf' : 'client1'
            },
            '5015': {
                'ip' : '192.168.16.2',
                'as_number' : 4,
                'vrf' : 'client2'
            }
        },
        'neigbors_bgp' : ['5000', '5007', '5001'],
        'vrf': {
            'client1': {
                'interface' : 'GigabitEthernet3/0',
                'rt' : '100:100',
                'rd' : '100:100',
            },
            'client2': {
                'interface' : 'GigabitEthernet4/0',
                'rt' : '200:200',
                'rd' : '200:200',
            },
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
        'GigabitEthernet3/0' : {
            'ip' : '192.168.18.1',
            'subnetwork' : '192.168.18.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : True,
        },
        'as_number' : 1,
        'CE': False,
        'edge': True,
        'neigbors' : {
            '5016': {
                'ip' : '192.168.18.2',
                'as_number' : 5,
                'vrf' : 'client2'
            }
        },
        'neigbors_bgp' : ['5000', '5006', '5001'],
        'vrf': {
            'client2': {
                'interface' : 'GigabitEthernet3/0',
                'rt' : '200:200',
                'rd' : '200:200',
            },
        },
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
                'vrf' : 'client1'
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
                'vrf' : 'client1'
            }
        }
    },
    '5015' :{
        'GigabitEthernet1/0' : {
            'ip' : '192.168.16.2',
            'subnetwork' : '192.168.16.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : True,
        },
        'GigabitEthernet2/0' : {
            'ip' : '192.168.17.2',
            'subnetwork' : '192.168.17.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'as_number': 4,
        'CE': True,
        'edge': True,
        'neigbors' : {
            '5006' : {
                'ip' : '192.168.16.1',
                'as_number' : 1,
                'vrf' : 'client2'
            }
        }
    },
    '5016' :{
        'GigabitEthernet1/0' : {
            'ip' : '192.168.18.2',
            'subnetwork' : '192.168.18.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : True,
        },
        'GigabitEthernet2/0' : {
            'ip' : '192.168.19.2',
            'subnetwork' : '192.168.19.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'as_number': 5,
        'CE': True,
        'edge': True,
        'neigbors' : {
            '5007' : {
                'ip' : '192.168.18.1',
                'as_number' : 1,
                'vrf' : 'client2'
            }
        }
    },
    '5014' :{
        'GigabitEthernet1/0' : {
            'ip' : '192.168.20.2',
            'subnetwork' : '192.168.20.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : True,
        },
        'GigabitEthernet2/0' : {
            'ip' : '192.168.21.2',
            'subnetwork' : '192.168.21.0',
            'mask' : '255.255.255.248',
            'edgeInterface' : False,
        },
        'as_number': 6,
        'CE': True,
        'edge': True,
        'neigbors' : {
            '5001' : {
                'ip' : '192.168.20.1',
                'as_number' : 1,
                'vrf' : 'client2'
            }
        }
    }
}

PC = {
    'PC1' : 'ip 192.168.15.1 255.255.255.248 gateway 192.168.15.2',
    'PC2' : 'ip 192.168.14.1 255.255.255.248 gateway 192.168.14.2',
    'PC5' : 'ip 192.168.17.1 255.255.255.248 gateway 192.168.17.2',
    'PC4' : 'ip 192.168.19.1 255.255.255.248 gateway 192.168.19.2',
    'PC3' : 'ip 192.168.21.1 255.255.255.248 gateway 192.168.21.2',
}