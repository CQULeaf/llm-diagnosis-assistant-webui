import requests
import re

def ask_image_model(user_input: str) -> dict:
    url = "http://localhost:11434/api/generate"
    system_prompt = (
        "你是一名影像科医生，你现在需要为患者观察影像图片并生成影像报告。"
        "你需要生成两部分内容，分别是'影像所见'和'影像诊断'。"
        "影像所见是对X光片上观察到的具体影像学表现的描述。"
        "影像诊断是通过影像所见的结果来对疾病做出诊断。"
        "在格式方面，你要严格遵守格式："
        "影像所见部分，'影像所见：'开头，句号结尾。"
        "影像诊断部分，'影像诊断：'开头，句号结尾。"
    )

    payload = {
        "model": "qwen3:4b",
        "system": system_prompt,
        "prompt": user_input,
        "stream": False
    }

    response = requests.post(url, json=payload)
    text = response.json()["response"]

    result = {
        "description": "",
        "imaging_diagnosis": "",
        "original": text
    }

    pattern = r'影像所见：([\s\S]*?)影像诊断：([\s\S]*?)$'

    match = re.search(pattern, text)
    if match:
        result["impression"] = match.group(1).strip()
        result["imaging_diagnosis"] = match.group(2).strip()
    return result