{
    "configurations": [
        {
            "configuration": {
                "hostname": "R1",
                "interfaces": [
                    {
                        "interface": "FastEthernet0/1",
                        "address": "192.178.2.21",
                        "subnet_mask": "255.255.128.0",
                        "status": "no shutdown",
                    }
                ],
                "routing": {
                    "static": [
                        {
                            "destination": "10.10.10.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "1.1.1.1",
                        },
                        {
                            "destination": "128.10.1.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "2.2.2.2",
                        },
                        {
                            "destination": "130.20.2.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "3.3.3.3",
                        },
                    ],
                    "ospf": {
                        "networks": [
                            {
                                "network": "40.40.40.0",
                                "subnet_mask": "255.255.255.0",
                                "area": 2,
                            },
                            {
                                "network": "30.30.0.0",
                                "subnet_mask": "255.255.0.0",
                                "area": 3,
                            },
                            {
                                "network": "50.50.30.0",
                                "subnet_mask": "255.255.255.0",
                                "area": 4,
                            },
                        ],
                        "router_id": "4.4.4.4",
                    },
                },
            }
        },
        {
            "configuration": {
                "hostname": "R2",
                "interfaces": [
                    {
                        "interface": "FastEthernet0/1",
                        "address": "192.178.2.25",
                        "subnet_mask": "255.255.128.0",
                        "status": "no shutdown",
                    }
                ],
                "routing": {
                    "static": [
                        {
                            "destination": "10.10.10.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "1.1.1.1",
                        },
                        {
                            "destination": "128.10.1.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "2.2.2.2",
                        },
                        {
                            "destination": "130.20.2.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "3.3.3.3",
                        },
                    ],
                    "ospf": {
                        "networks": [
                            {
                                "network": "40.40.40.0",
                                "subnet_mask": "255.255.255.0",
                                "area": 12,
                            },
                            {
                                "network": "30.30.0.0",
                                "subnet_mask": "255.255.0.0",
                                "area": 13,
                            },
                            {
                                "network": "50.50.30.0",
                                "subnet_mask": "255.255.255.0",
                                "area": 14,
                            },
                        ],
                        "router_id": "11.10.10.2",
                    },
                },
            }
        },
        {
            "configuration": {
                "hostname": "R3",
                "interfaces": [
                    {
                        "interface": "FastEthernet0/1",
                        "address": "192.178.2.41",
                        "subnet_mask": "255.255.128.0",
                        "status": "no shutdown",
                    }
                ],
                "routing": {
                    "static": [
                        {
                            "destination": "10.10.10.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "1.1.1.1",
                        },
                        {
                            "destination": "128.10.1.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "2.2.2.2",
                        },
                        {
                            "destination": "130.20.2.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "3.3.3.3",
                        },
                    ],
                    "ospf": {
                        "networks": [
                            {
                                "network": "40.40.40.0",
                                "subnet_mask": "255.255.255.0",
                                "area": 20,
                            },
                            {
                                "network": "30.30.0.0",
                                "subnet_mask": "255.255.0.0",
                                "area": 30,
                            },
                            {
                                "network": "50.50.30.0",
                                "subnet_mask": "255.255.255.0",
                                "area": 40,
                            },
                        ],
                        "router_id": "4.4.4.4",
                    },
                },
            }
        },
        {
            "configuration": {
                "hostname": "R4",
                "interfaces": [
                    {
                        "interface": "FastEthernet0/1",
                        "address": "192.178.2.48",
                        "subnet_mask": "255.255.128.0",
                        "status": "no shutdown",
                    }
                ],
                "routing": {
                    "static": [
                        {
                            "destination": "10.10.10.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "1.1.1.1",
                        },
                        {
                            "destination": "128.10.1.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "2.2.2.2",
                        },
                        {
                            "destination": "130.20.2.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "3.3.3.3",
                        },
                    ],
                    "ospf": {
                        "networks": [
                            {
                                "network": "40.40.40.0",
                                "subnet_mask": "255.255.255.0",
                                "area": 22,
                            },
                            {
                                "network": "30.30.0.0",
                                "subnet_mask": "255.255.0.0",
                                "area": 32,
                            },
                            {
                                "network": "50.50.30.0",
                                "subnet_mask": "255.255.255.0",
                                "area": 42,
                            },
                        ],
                        "router_id": "6.6.6.6",
                    },
                },
            }
        },
        {
            "configuration": {
                "hostname": "SW1",
                "routing": {
                    "static": [
                        {
                            "destination": "10.10.10.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "1.1.1.1",
                        },
                        {
                            "destination": "128.10.1.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "2.2.2.2",
                        },
                        {
                            "destination": "130.20.2.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "3.3.3.3",
                        },
                    ],
                    "ospf": null,
                },
            }
        },
        {
            "configuration": {
                "hostname": "SW2",
                "routing": {
                    "static": [
                        {
                            "destination": "10.10.10.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "1.1.1.1",
                        },
                        {
                            "destination": "128.10.1.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "2.2.2.2",
                        },
                        {
                            "destination": "130.20.2.0",
                            "subnet_mask": "255.255.255.0",
                            "next_hop": "3.3.3.3",
                        },
                    ],
                    "ospf": null,
                },
            }
        },
    ]
}
