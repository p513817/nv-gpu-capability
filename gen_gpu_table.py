from bs4 import BeautifulSoup
import requests, json, argparse

def get_gpu_info(write_file=False):
    # ------------------------------------------------------------------------------------------
    source = "https://developer.nvidia.com/cuda-gpus"
    content = requests.get(source)            #以get的方式取得網頁
    soup = BeautifulSoup(content.text, "html.parser")
    # ------------------------------------------------------------------------------------------
    title_map = {
        "collapseOne": "CUDA-Enabled Datacenter Products",
        "collapse2": "CUDA-Enabled NVIDIA Quadro and NVIDIA RTX",
        "collapse3": "CUDA-Enabled NVS Products",
        "collapse4": "CUDA-Enabled GeForce and TITAN Products",
        "collapse5": "CUDA-Enabled Jetson Products",
    }
    # ------------------------------------------------------------------------------------------
    template, total = {}, {}
    # ------------------------------------------------------------------------------------------
    for tag, title in title_map.items():
        # 找到 大標的位置
        title_tag = soup.find(id=tag)
        # 找到小標的位置 ( Jetson 是 col-md-12 )
        div_tag = title_tag.find_all("div", { "class", "col-md-6" })
        if div_tag==[]:
            div_tag = title_tag.find_all("div", { "class", "col-md-12" })
        # 解析所有小標內容

        for div in div_tag:
            # 找到小標
            sub_title = div.find('h3').text.strip()
            # 直接找 gpu 內容
            tr_tag = div.find_all("tr")
            for tr in tr_tag:
                td_tag = tr.find_all("td")
                if td_tag==[]: 
                    continue

                gpu_name = td_tag[0].text.strip()
                gpu_capability = td_tag[1].text.strip()
                gpu_title = title
                gpu_subtitle = sub_title
                # 每一個 tr 都是一個 gpu 的資訊
                total.update(
                    {
                        gpu_name: {
                            'title': gpu_title,
                            'sub_title': gpu_subtitle,
                            'capability': gpu_capability,
                        }
                    }
                )
    # ------------------------------------------------------------------------------------------
    if write_file:
        with open('gpu_info.json', 'w') as f:
            f.writelines(json.dumps({'information':total}))
    # ------------------------------------------------------------------------------------------
    return total

if __name__ == "__main__":
    info = get_gpu_info(write_file=True)
    import pprint
    pprint.pprint(info)