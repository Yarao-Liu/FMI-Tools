from fmi.attribute import *
from fmi.emulate import *


def simulation(filename):
    info = FMI_version_and_type(fmu)
    print(info)
    platform = FMI_platform(fmu)
    print(platform)

    FMI_attribute(fmu)

    desc = FMI_model_description(fmu)
    print(desc)
    # 初始值
    value = FMI_start_values(fmu)
    print(value)

    result = FMI_simple_simulation(fmu)
    print(result)

    FMI_polt_result(result)

    # 设置初始值
    start_time = 0.0
    stop_time = 1.0
    step_size = 1e-2
    # output_interval = 2e-2
    kwargs = {
        'filename': fmu,
        'start_time': start_time,
        'stop_time': stop_time,
        'fmi_type': info,
        'step_size': step_size,
        # 'output_interval': output_interval,
    }
    # 仿真步骤
    result = FMI_complex_simulation(**kwargs)
    FMI_csv_result("../target/RecResult.csv", result)
    FMI_polt_result(result)
    exit(0)


if __name__ == '__main__':
    fmu = "D:/workspace/FMIDemo/fmiResources/Rectifier.fmu"
    simulation(fmu)