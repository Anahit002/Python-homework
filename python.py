def get_netlist_models(netlist, output_file=None):
    devices = {"transistor": [], "resistor": []}

    with open(netlist) as channel:
        for line in channel:
            if line.startswith('Xm') and 'w=' in line and 'l=' in line:
                parts = line.split()
                name = parts[0]
                parameters = " ".join(parts[6:])
                devices["transistor"].append({"device_name": name, "device_parameter": parameters})
            elif line.startswith('R'):
                parts = line.split()
                name = parts[0]
                parameters = " ".join(parts[3:])
                devices["resistor"].append({"device_name": name, "device_parameter": parameters})

    if output_file is not None:
        with open(output_file, 'w') as channel:
            channel.write(f'Finished parsing netlist {netlist}, devices are:\n')
            for device, data in devices.items():
                channel.write(f'    {device}: {data}\n')

            for transistor in devices["transistor"]:
                line = f"{transistor['device_name']} {transistor['device_parameter']}\n"
                channel.write(line)

            for resistor in devices["resistor"]:
                line = f"{resistor['device_name']} {resistor['device_parameter']}\n"
                channel.write(line)

    return devices