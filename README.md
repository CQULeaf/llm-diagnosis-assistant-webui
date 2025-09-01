# 智渝（ZhiYu）

## 一款多模态大模型智能辅诊系统

本仓库代码是基于 Gradio 构建的 WebUI 页面，包括用户登录注册、智能问诊（初诊文本 & 复诊图像）、报告生成（门诊病历 & 影像报告）、报告清单汇总以及外接知识库等功能。

### 项目结构

```text
.
├── README.md
├── SavedImageRecords
│   └── README.md
├── SavedMedicalRecords
│   └── README.md
├── Template
│   ├── ImageTemplate.docx
│   └── MedicalReportTemplate.docx
├── app.py
├── requirements.txt
└── src
    ├── CustomCss.py
    ├── ImageModel.py
    ├── ImageToPDF.py
    ├── Model.py
    ├── OperationFunc.py
    ├── TextToPDF.py
    ├── UploadedFiles
    │   └── README.md
    ├── UploadedImages
    │   └── README.md
    ├── VoiceToText.py
    ├── app.db
    └── database.py
```

### 如何使用

1. 先在根目录下运行指令进行环境安装：`pip install -r requirements.txt`

2. 模型下载与加载：运行项目前需先启动 ollama 服务`ollama serve`，在`src/model.py`中修改模型与模型参数，运行`app.py`会自动下载需要的语言识别模型。
    >这里可以选用任何开源模型，你可以根据实际需要进行调整。当然这里默认为我们基于 Qwen 微调的 8B 医疗模型 [CQULeaf/ZhiYu](https://huggingface.co/CQULeaf/ZhiYu)，可以下载后使用。

3. 直接使用`python app.py`即可运行，也可以使用`gradio app.py`进行热部署，但部分情况下会出现Bug，仅推荐开发时使用。

### 最后声明

该项目为学校实习任务，团队共五人用时半月左右完成，故可用性与专业度仍有很大提升空间，可作为学生初步接触学习大模型微调与应用参考使用。

### 相关链接

[模型训练、增强与评测部分](https://github.com/CQULeaf/llm-diagnosis-assistant)