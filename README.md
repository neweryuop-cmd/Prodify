# Prodify - 现代化生产力桌面应用

**提醒：**

- 本人高中生，没有太多时间修理各种bug，反馈后可能一两周才会修理更新。

- 第一次开发python软件，粗制滥造的作品勿喷！如果让你感到不愉快，我在此向您说声对不起！

### 1. 顶部信息区

- 实时天气显示（温度+湿度）
    
- 智能情境提示（根据天气和时间给出建议）
    
- 应用标题和状态信息
    
- 实时显示时间24小时制

### 2. 中央任务区

- 优雅的待办事项管理
    
- 添加/完成任务时的流畅动画
    
- 任务自动排序和编号
### 3. 底部工具区

- 创意番茄钟计时器
    
- 时间滑块（0-120分钟可调）
    
- 开始/重置控制按钮
## 核心功能：
- 📝 智能待办事项管理
    
- ⏱ 番茄工作法计时器
    
-  🌤 情境感知天气提示
Prodify集成了实时天气数据，并根据当前天气和时间提供智能建议：
```
# 智能提示算法
if "雨" in weather or "雪" in weather:
    tip = "下雨/雪天是专注工作的好时机！"
elif "晴" in weather and 6 <= hour < 10:
    tip = "早晨的阳光充满活力，开始新的一天吧！"
# ...更多情境判断...
```
Prodify基于Python和PyQt6构建，技术栈选择兼顾了**功能强大**和**开发效率**：

- **PyQt6**：成熟的跨平台GUI框架
    
- **Requests**：获取天气数据
    
- **SVG**：矢量天气图标，完美适配不同分辨率
    
- **JSON配置**：用户设置灵活管理
    

整个应用仅需**4个核心文件**，结构清晰：
```
Prodify/
├── main.py            # 主程序
├── weather_icons.py   # 天气图标
├── requirements.txt   # 依赖库
└── config.json        # 配置设置
```
## 如何开始你的高效之旅

### 三步安装指南

1. 安装Python环境（建议3.8+版本）
    
2. 安装依赖库：`pip install -r requirements.txt`
    
<<<<<<< HEAD
3. [获取OpenWeather API密钥](https://openweathermap.org/)（免费注册）（需要填写到config.json中）
=======
3. [获取OpenWeather API密钥](https://openweathermap.org/)（免费注册）

- 一定要把密钥填写到config.json里！否则实时天气不会运行。
>>>>>>> edb83acf0788c8af7248f6cc17828bac52fc5995
    

### 个性化设置

编辑`config.json`文件，定制你的专属体验：

json
```
{
<<<<<<< HEAD

    "api_key": "your api_key here",

    "city": "北京",

    "glass_opacity": 0.25,

    "border_radius": 20,

    "animation_duration": 300,

    "hue_speed": 0.5,

    "alarm_sound": "alarm.wav"

=======
    "api_key": "your api_key here",
    "city": "北京",
    "glass_opacity": 0.25,
    "border_radius": 20,
    "animation_duration": 300,
    "hue_speed": 0.5,
    "alarm_sound": "alarm.wav"
>>>>>>> edb83acf0788c8af7248f6cc17828bac52fc5995
}
```
