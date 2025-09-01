import requests
import re


def ask_image_model(user_input: str, image_input) -> dict:
    url = "http://localhost:11434/api/generate"
    system_prompt = (
        """
        你是一名专业的医学影像科医生，你现在需要为患者观察影像图片，结合临床诊断与图片并生成影像报告。
        你需要生成两部分内容，分别是'影像所见'和'影像诊断'。
        影像所见通常包括按解剖区域系统描述，包括胸廓骨架与软组织（肋骨、锁骨、肩胛、胸壁、皮下气肿或钙化等）、气道与气管走向、纵隔及纵隔轮廓与心影（形态、大小、心胸比）、肺门结构（肺动脉分支及淋巴结）、双肺野（纹理粗细、是否存在斑片状、网格状、实变、空洞、结节或气胸）、胸膜和肋膈角（积液、增厚、粘连）以及隔肌形态与肋膈角情况。
        影像诊断要简短，一句话概括所见异常，再用一句话概括可能的病情
        格式要求不要有任何换行或者分段，只在影像所见结束后换行，影像所见，影像报告都以一段话的形式呈现。
        可参考下面的例子：
        user:
        发热、咳嗽伴咳痰3天，加重伴气促1天。
        assistant:
        影像所见：双侧肋骨、锁骨及肩胛骨形态完整，未见骨折或骨质破坏；气管居中，纵隔轮廓正常；心影未见明显增大，心胸比正常；双肺纹理增粗，右下肺野见大片状、网格状混浊影，边界欠清，部分实变；左下肺野见少许斑片状浸润影；双侧肋膈角锐利，未见胸腔积液或游离气体；胃泡及纵隔结构未见异常。
        
        影像诊断：双肺炎性浸润，以右下肺为主。考虑急性肺炎。
        """
    )

    payload = {
        "model": "qwen2.5vl:7b",
        "system": system_prompt,
        "prompt": user_input,
        "image": image_input,
        "stream": False,
    }

    response = requests.post(url, json=payload)
    text = response.json()["response"]

    result = {"description": "", "imaging_diagnosis": "", "original": text}

    pattern = r"影像所见[:：]([\s\S]*?)影像诊断[:：]([\s\S]*)"

    match = re.search(pattern, text)
    if match:
        result["description"] = match.group(1).strip()
        result["imaging_diagnosis"] = match.group(2).strip()
    return result
