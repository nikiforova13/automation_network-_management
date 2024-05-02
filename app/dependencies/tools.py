import ipaddress


def subnet_masks():
    subnet_masks = []
    for prefix_length in range(33):
        network = ipaddress.IPv4Network(("0.0.0.0", prefix_length), strict=False)
        subnet_masks.append(f"{str(network.netmask)}")
    return subnet_masks
