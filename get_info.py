from gen_gpu_table import get_gpu_info
import requests, json, argparse
# ------------------------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="gpu name", type=str)
parser.add_argument("--capability", action='store_true', help="return capability")
parser.add_argument("--fullname", action='store_true', help="return full name")
args = parser.parse_args()

gpu_info = get_gpu_info(write_file=False)
full_info = False if True in [args.capability, args.fullname] else True
for key, val in gpu_info.items():
    if args.name.lower() in key.lower():
        if full_info:
            print('NAME: ', key)
            for key, val in val.items():
                print('{}: {}'.format(key.upper(), val))
        else:
            if args.capability:
                print(val['capability'])
            if args.fullname:
                print(key)
