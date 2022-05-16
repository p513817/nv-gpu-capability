from gen_gpu_table import get_gpu_info
import requests, json, argparse

def get_info(name, capability=False, fullname=False):
    gpu_info = get_gpu_info(write_file=False)
    full_info = False if True in [capability, fullname] else True
    ret = []
    temp = {}
    for key, val in gpu_info.items():
        if name.lower() in key.lower():
            if full_info:
                temp = { "NAME: ":key }
                temp.update( val )                
                ret.append(temp)
            else:
                if capability:
                    ret.append(val["capability"])
                if fullname:
                    ret.append(key)
    return ret

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="gpu name", type=str)
    parser.add_argument("--capability", action="store_true", help="return capability")
    parser.add_argument("--fullname", action="store_true", help="return full name")
    args = parser.parse_args()

    from pprint import pprint
    pprint(get_info(args.name, args.capability, args.fullname))