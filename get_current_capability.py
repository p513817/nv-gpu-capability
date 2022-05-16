# Import caffe and GPUtil
import GPUtil, os, copy, argparse
import get_gpu_info
import pprint

def rm_keyword(in_str, keys:list):
    temp_str = copy.deepcopy(in_str)
    if len(keys)==0:
        return temp_str
    else:
        for key in keys:
            # got position
            if key.lower() in in_str.lower():
                pos_start = in_str.lower().index(key.lower())
                pos_end = pos_start + len(key)
                trg_key = in_str[pos_start:pos_end]
                print("Remove key: {}".format(trg_key), end="\t")
                temp_str = temp_str.replace(trg_key, "")

    print(", After remove key: {}".format(temp_str))
    return temp_str.strip()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--capability", action="store_true", help="return capability")
    parser.add_argument("--first", action="store_true", help="return first gpu")
    args = parser.parse_args()

    # Set CUDA_DEVICE_ORDER so the IDs assigned by CUDA match those from nvidia-smi
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    # Get the first available GPU
    GPUs = GPUtil.getGPUs()

    for GPU in GPUs[: len(GPUs) if not args.first else 1 ]:
        g_name = rm_keyword(GPU.name.strip(), ['NVIDIA', 'Ti', 'super']) 
        g_info = get_gpu_info.get_info(g_name, args.capability)[0]
        pprint.pprint( g_info )
