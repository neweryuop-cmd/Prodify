import sys
import os
import random
import time
import json
import requests
import math
from PyQt6.QtGui import QIcon
from datetime import datetime
from PyQt6.QtCore import Qt, QTimer, QRectF, QPropertyAnimation, QEasingCurve, pyqtProperty, QSize
from PyQt6.QtGui import QPainter, QColor, QLinearGradient, QBrush, QFont, QPen, QPixmap, QPainterPath
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QLineEdit, QListWidget,
                             QListWidgetItem, QAbstractItemView, QSlider, QFrame, QSizePolicy)

# 天气图标初始化
WEATHER_ICONS = {}


def init_weather_icons():
    """初始化天气图标QPixmap"""
    global WEATHER_ICONS
    WEATHER_ICONS = {
        "clear": QPixmap(64, 64),
        "few_clouds": QPixmap(64, 64),
        "scattered_clouds": QPixmap(64, 64),
        "clouds": QPixmap(64, 64),
        "rain": QPixmap(64, 64),
        "thunderstorm": QPixmap(64, 64),
        "snow": QPixmap(64, 64),
        "mist": QPixmap(64, 64),
        "drizzle": QPixmap(64, 64),
        "unknown": QPixmap(64, 64)
    }

    # 晴天
    pixmap = WEATHER_ICONS["clear"]
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setBrush(QBrush(QColor(255, 215, 0)))
    painter.setPen(QPen(QColor(255, 165, 0), 2))
    painter.drawEllipse(12, 12, 40, 40)
    painter.setBrush(QBrush(QColor(255, 255, 0)))
    painter.drawEllipse(17, 17, 30, 30)
    painter.end()

    # 少云
    pixmap = WEATHER_ICONS["few_clouds"]
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setBrush(QBrush(QColor(255, 215, 0)))
    painter.setPen(QPen(QColor(255, 165, 0), 2))
    painter.drawEllipse(12, 12, 40, 40)
    painter.setBrush(QBrush(QColor(255, 255, 0)))
    painter.drawEllipse(17, 17, 30, 30)

    # 添加云朵
    painter.setBrush(QBrush(QColor(255, 255, 255, 200)))
    painter.setPen(Qt.PenStyle.NoPen)
    path = QPainterPath()
    path.moveTo(20, 40)
    path.quadTo(30, 30, 40, 40)
    path.quadTo(50, 50, 30, 50)
    path.quadTo(20, 50, 20, 40)
    painter.drawPath(path)
    painter.end()

    # 散云
    pixmap = WEATHER_ICONS["scattered_clouds"]
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setBrush(QBrush(QColor(255, 255, 255, 200)))
    painter.setPen(Qt.PenStyle.NoPen)

    # 第一朵云
    path1 = QPainterPath()
    path1.moveTo(15, 40)
    path1.quadTo(25, 30, 45, 30)
    path1.quadTo(55, 35, 50, 45)
    path1.quadTo(45, 55, 30, 55)
    path1.quadTo(15, 55, 15, 40)
    painter.drawPath(path1)

    # 第二朵云
    path2 = QPainterPath()
    path2.moveTo(30, 35)
    path2.quadTo(40, 25, 50, 35)
    path2.quadTo(60, 45, 45, 50)
    path2.quadTo(35, 55, 25, 45)
    path2.quadTo(20, 35, 30, 35)
    painter.drawPath(path2)
    painter.end()

    # 多云
    pixmap = WEATHER_ICONS["clouds"]
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setBrush(QBrush(QColor(255, 255, 255, 200)))
    painter.setPen(Qt.PenStyle.NoPen)

    # 第一朵云
    path1 = QPainterPath()
    path1.moveTo(10, 40)
    path1.quadTo(20, 30, 40, 30)
    path1.quadTo(50, 35, 45, 45)
    path1.quadTo(40, 55, 25, 55)
    path1.quadTo(10, 55, 10, 40)
    painter.drawPath(path1)

    # 第二朵云
    path2 = QPainterPath()
    path2.moveTo(25, 35)
    path2.quadTo(35, 25, 45, 35)
    path2.quadTo(55, 45, 40, 50)
    path2.quadTo(30, 55, 20, 45)
    path2.quadTo(15, 35, 25, 35)
    painter.drawPath(path2)

    # 第三朵云
    path3 = QPainterPath()
    path3.moveTo(35, 30)
    path3.quadTo(45, 20, 55, 30)
    path3.quadTo(65, 40, 50, 45)
    path3.quadTo(40, 50, 30, 40)
    path3.quadTo(25, 30, 35, 30)
    painter.drawPath(path3)
    painter.end()

    # 雨
    pixmap = WEATHER_ICONS["rain"]
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    # 云
    painter.setBrush(QBrush(QColor(255, 255, 255, 200)))
    painter.setPen(Qt.PenStyle.NoPen)
    path = QPainterPath()
    path.moveTo(15, 40)
    path.quadTo(25, 30, 45, 30)
    path.quadTo(55, 35, 50, 45)
    path.quadTo(45, 55, 30, 55)
    path.quadTo(15, 55, 15, 40)
    painter.drawPath(path)

    # 雨滴
    painter.setPen(QPen(QColor(100, 150, 255), 2))
    painter.drawLine(25, 50, 25, 60)
    painter.drawLine(35, 50, 35, 60)
    painter.drawLine(45, 50, 45, 60)
    painter.end()

    # 雷暴
    pixmap = WEATHER_ICONS["thunderstorm"]
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    # 云
    painter.setBrush(QBrush(QColor(50, 50, 50, 200)))
    painter.setPen(Qt.PenStyle.NoPen)
    path = QPainterPath()
    path.moveTo(15, 40)
    path.quadTo(25, 30, 45, 30)
    path.quadTo(55, 35, 50, 45)
    path.quadTo(45, 55, 30, 55)
    path.quadTo(15, 55, 15, 40)
    painter.drawPath(path)

    # 闪电
    painter.setBrush(QBrush(QColor(255, 215, 0)))
    painter.setPen(Qt.PenStyle.NoPen)
    lightning = QPainterPath()
    lightning.moveTo(30, 40)
    lightning.lineTo(35, 50)
    lightning.lineTo(25, 50)
    lightning.lineTo(35, 60)
    lightning.closeSubpath()
    painter.drawPath(lightning)
    painter.end()

    # 雪
    pixmap = WEATHER_ICONS["snow"]
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    # 云
    painter.setBrush(QBrush(QColor(255, 255, 255, 200)))
    painter.setPen(Qt.PenStyle.NoPen)
    path = QPainterPath()
    path.moveTo(15, 40)
    path.quadTo(25, 30, 45, 30)
    path.quadTo(55, 35, 50, 45)
    path.quadTo(45, 55, 30, 55)
    path.quadTo(15, 55, 15, 40)
    painter.drawPath(path)

    # 雪花
    painter.setPen(QPen(QColor(135, 206, 235), 1.5))

    # 第一片雪花
    painter.drawLine(30, 50, 34, 54)
    painter.drawLine(32, 48, 32, 52)
    painter.drawLine(34, 50, 30, 54)

    # 第二片雪花
    painter.drawLine(40, 50, 44, 54)
    painter.drawLine(42, 48, 42, 52)
    painter.drawLine(44, 50, 40, 54)

    # 第三片雪花
    painter.drawLine(50, 50, 54, 54)
    painter.drawLine(52, 48, 52, 52)
    painter.drawLine(54, 50, 50, 54)
    painter.end()

    # 雾
    pixmap = WEATHER_ICONS["mist"]
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    # 云
    painter.setBrush(QBrush(QColor(240, 248, 255, 150)))
    painter.setPen(Qt.PenStyle.NoPen)
    path = QPainterPath()
    path.moveTo(15, 35)
    path.quadTo(25, 25, 45, 25)
    path.quadTo(55, 30, 50, 40)
    path.quadTo(45, 50, 30, 50)
    path.quadTo(15, 50, 15, 35)
    painter.drawPath(path)

    # 雾线
    painter.setPen(QPen(QColor(169, 169, 169), 3))
    painter.setOpacity(0.7)
    painter.drawLine(10, 40, 54, 40)
    painter.drawLine(15, 45, 50, 45)
    painter.drawLine(20, 50, 45, 50)
    painter.end()

    # 毛毛雨
    pixmap = WEATHER_ICONS["drizzle"]
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    # 云
    painter.setBrush(QBrush(QColor(255, 255, 255, 200)))
    painter.setPen(Qt.PenStyle.NoPen)
    path = QPainterPath()
    path.moveTo(15, 40)
    path.quadTo(25, 30, 45, 30)
    path.quadTo(55, 35, 50, 45)
    path.quadTo(45, 55, 30, 55)
    path.quadTo(15, 55, 15, 40)
    painter.drawPath(path)

    # 雨滴
    painter.setPen(QPen(QColor(135, 206, 235), 2))
    painter.drawLine(30, 45, 30, 50)
    painter.drawLine(40, 45, 40, 50)
    painter.drawLine(50, 45, 50, 50)
    painter.end()

    # 未知天气
    pixmap = WEATHER_ICONS["unknown"]
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setBrush(QBrush(QColor(255, 215, 0)))
    painter.setPen(QPen(QColor(255, 165, 0), 2))
    painter.drawEllipse(12, 12, 40, 40)
    painter.setBrush(QBrush(QColor(255, 255, 0)))
    painter.drawEllipse(17, 17, 30, 30)
    painter.setFont(QFont("Arial", 20))
    painter.setPen(QPen(QColor(0, 0, 0)))
    painter.drawText(QRectF(0, 0, 64, 64), Qt.AlignmentFlag.AlignCenter, "?")
    painter.end()


class CircularProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = 0  # 使用内部变量
        self.max_value = 100
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = QColor(94, 129, 172)
        self.text_color = QColor(255, 255, 255)
        self.enable_bg = True
        self.bg_color = QColor(68, 71, 90)
        self.enable_text = True
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.text_offset = 0
        self.animation = QPropertyAnimation(self, b"value")
        self.animation.setDuration(1000)
        self.animation.setEasingCurve(QEasingCurve.Type.OutQuad)

        # 新增倒计时文本
        self.timer_text = ""

    # 定义value属性
    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value
        self.update()

    value = pyqtProperty(int, get_value, set_value)

    def paintEvent(self, event):
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = int(self.progress_width / 2)  # 转换为整数
        value = self._value * 360 / self.max_value

        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.RenderHint.Antialiasing)

        rect = QRectF(0, 0, self.width, self.height)
        paint.setPen(Qt.PenStyle.NoPen)
        paint.drawRect(rect)

        # Background circle
        if self.enable_bg:
            pen = QPen()
            pen.setColor(self.bg_color)
            pen.setWidth(self.progress_width)
            paint.setPen(pen)
            # 使用QRectF确保参数正确
            paint.drawArc(QRectF(margin, margin, width, height), 0, 360 * 16)

        # Progress circle
        pen = QPen()
        pen.setColor(self.progress_color)
        pen.setWidth(self.progress_width)
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        paint.setPen(pen)
        paint.drawArc(QRectF(margin, margin, width, height), -90 * 16, -int(value) * 16)

        # Text
        if self.enable_text:
            font = QFont(self.font_family, self.font_size)
            paint.setFont(font)
            paint.setPen(QPen(self.text_color))

            # 显示进度百分比和倒计时
            display_text = f"{self._value}{self.suffix}"
            if self.timer_text:
                display_text += f"\n{self.timer_text}"

            paint.drawText(rect, Qt.AlignmentFlag.AlignCenter, display_text)

        paint.end()


class TodoItem(QWidget):
    def __init__(self, text, item, parent=None):
        super().__init__(parent)
        self.item = item  # 保存关联的QListWidgetItem
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 5, 10, 5)

        self.checkbox = QPushButton()
        self.checkbox.setFixedSize(20, 20)
        self.checkbox.setCheckable(True)
        self.checkbox.setStyleSheet("""
            QPushButton {
                border: 2px solid #5E81AC;
                border-radius: 10px;
                background-color: transparent;
            }
            QPushButton:checked {
                background-color: #5E81AC;
            }
        """)

        self.label = QLabel(text)
        self.label.setStyleSheet("font-size: 14px; color: #ECEFF4;")
        self.label.setWordWrap(True)

        self.layout.addWidget(self.checkbox)
        self.layout.addWidget(self.label, 1)

        # 连接信号
        self.checkbox.toggled.connect(self.on_checked)

    def on_checked(self, checked):
        if checked:
            # 创建淡出动画
            self.animation = QPropertyAnimation(self, b"windowOpacity")
            self.animation.setDuration(500)
            self.animation.setStartValue(1.0)
            self.animation.setEndValue(0.0)
            self.animation.finished.connect(self.remove_item)
            self.animation.start()
        else:
            # 如果取消勾选，移除删除线效果
            self.label.setStyleSheet("font-size: 14px; color: #ECEFF4;")

    def remove_item(self):
        # 从列表中移除该项
        if self.parent() and self.parent().parent():
            todo_widget = self.parent().parent()
            if hasattr(todo_widget, "todo_list"):
                # 安全地获取行号
                try:
                    row = todo_widget.todo_list.row(self.item)
                    if row >= 0:
                        todo_widget.todo_list.takeItem(row)
                except Exception as e:
                    print(f"移除待办事项时出错: {e}")
                finally:
                    # 确保动画完成后删除widget
                    self.deleteLater()


class TodoWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(15, 15, 15, 15)
        self.layout.setSpacing(10)

        # 标题
        self.title = QLabel("待办事项")
        self.title.setStyleSheet("font-size: 18px; font-weight: bold; color: #88C0D0;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 输入框和添加按钮
        self.input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("添加新任务...")
        self.input_field.setStyleSheet("""
            QLineEdit {
                background-color: #434C5E;
                border: 1px solid #4C566A;
                border-radius: 10px;
                padding: 8px;
                color: #ECEFF4;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #5E81AC;
            }
        """)

        self.add_btn = QPushButton("添加")
        self.add_btn.setStyleSheet("""
            QPushButton {
                background-color: #5E81AC;
                color: #ECEFF4;
                border: none;
                border-radius: 10px;
                padding: 8px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
        """)
        self.add_btn.setFixedWidth(80)

        self.input_layout.addWidget(self.input_field)
        self.input_layout.addWidget(self.add_btn)

        # 任务列表
        self.todo_list = QListWidget()
        self.todo_list.setStyleSheet("""
            QListWidget {
                background-color: #3B4252;
                border: 1px solid #4C566A;
                border-radius: 10px;
                color: #ECEFF4;
                font-size: 14px;
                padding: 5px;
            }
            QListWidget::item {
                border-bottom: 1px solid #4C566A;
                padding: 5px;
            }
            QListWidget::item:selected {
                background-color: #434C5E;
            }
        """)
        self.todo_list.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.todo_list.setSpacing(5)

        # 连接信号
        self.add_btn.clicked.connect(self.add_task_from_input)
        self.input_field.returnPressed.connect(self.add_task_from_input)

        # 添加到布局
        self.layout.addWidget(self.title)
        self.layout.addLayout(self.input_layout)
        self.layout.addWidget(self.todo_list, 1)

    def add_task_from_input(self):
        text = self.input_field.text().strip()
        if text:
            self.add_task(text)
            self.input_field.clear()

    def add_task(self, text):
        item = QListWidgetItem(self.todo_list)
        item.setSizeHint(QSize(0, 60))  # 设置初始高度为60像素
        widget = TodoItem(text, item, self)
        self.todo_list.addItem(item)
        self.todo_list.setItemWidget(item, widget)

        # 添加动画效果
        animation = QPropertyAnimation(widget, b"geometry")
        animation.setDuration(300)
        animation.setEasingCurve(QEasingCurve.Type.OutBack)

        start_rect = widget.geometry()
        start_rect.setHeight(0)
        end_rect = widget.geometry()

        widget.setGeometry(start_rect)
        animation.setStartValue(start_rect)
        animation.setEndValue(end_rect)
        animation.start()


class WeatherWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(15, 15, 15, 15)
        self.layout.setSpacing(10)

        # 标题
        self.title = QLabel("天气信息")
        self.title.setStyleSheet("font-size: 18px; font-weight: bold; color: #88C0D0;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 位置和天气图标
        self.top_layout = QHBoxLayout()

        self.location_label = QLabel("加载中...")
        self.location_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #ECEFF4;")

        self.icon_label = QLabel()
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon_label.setFixedSize(64, 64)  # 固定图标大小

        self.top_layout.addWidget(self.location_label, 1)
        self.top_layout.addWidget(self.icon_label)

        # 温度、湿度和提示信息
        self.temp_label = QLabel("--°C")
        self.temp_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #ECEFF4;")
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.humidity_label = QLabel("湿度: --%")
        self.humidity_label.setStyleSheet("font-size: 14px; color: #D8DEE9;")
        self.humidity_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tip_label = QLabel("正在获取提示...")
        self.tip_label.setStyleSheet("font-size: 14px; font-style: italic; color: #A3BE8C;")
        self.tip_label.setWordWrap(True)
        self.tip_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 添加到布局
        self.layout.addWidget(self.title)
        self.layout.addLayout(self.top_layout)
        self.layout.addWidget(self.temp_label)
        self.layout.addWidget(self.humidity_label)
        self.layout.addWidget(self.tip_label, 1)

        # 初始化天气数据
        self.temperature = "--"
        self.humidity = "--"
        self.location = "未知位置"
        self.tip = "正在获取天气信息..."

    def update_weather(self, temp, humidity, icon_key, location, tip):
        self.temperature = f"{temp}°C"
        self.humidity = f"{humidity}%"
        self.location = location
        self.tip = tip

        # 设置天气图标
        if icon_key in WEATHER_ICONS:
            pixmap = WEATHER_ICONS[icon_key]
            self.icon_label.setPixmap(pixmap)
        else:
            pixmap = WEATHER_ICONS.get("unknown", QPixmap(64, 64))
            self.icon_label.setPixmap(pixmap)

        self.temp_label.setText(self.temperature)
        self.humidity_label.setText(f"湿度: {self.humidity}")
        self.location_label.setText(self.location)
        self.tip_label.setText(self.tip)


class TomatoTimer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(15, 15, 15, 15)
        self.layout.setSpacing(15)

        # 标题
        self.title = QLabel("番茄时钟")
        self.title.setStyleSheet("font-size: 18px; font-weight: bold; color: #88C0D0;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 进度条
        self.progress = CircularProgressBar()
        self.progress.setFixedSize(200, 200)

        # 时间滑块
        self.slider_layout = QHBoxLayout()
        self.slider_label = QLabel("25 分钟")
        self.slider_label.setStyleSheet("font-size: 14px; color: #ECEFF4;")
        self.slider_label.setFixedWidth(80)

        self.time_slider = QSlider(Qt.Orientation.Horizontal)
        self.time_slider.setRange(5, 120)  # 5到120分钟
        self.time_slider.setValue(25)
        self.time_slider.setTickInterval(5)
        self.time_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.time_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                background: #4C566A;
                height: 8px;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #5E81AC;
                width: 16px;
                height: 16px;
                margin: -4px 0;
                border-radius: 8px;
            }
            QSlider::sub-page:horizontal {
                background: #81A1C1;
                border-radius: 4px;
            }
        """)
        self.time_slider.valueChanged.connect(self.update_slider_label)

        self.slider_layout.addWidget(self.slider_label)
        self.slider_layout.addWidget(self.time_slider)

        # 控制按钮
        self.btn_layout = QHBoxLayout()

        self.start_btn = QPushButton("开始")
        self.start_btn.setStyleSheet("""
            QPushButton {
                background-color: #A3BE8C;
                color: #2E3440;
                border: none;
                border-radius: 10px;
                padding: 8px 15px;
                font-weight: bold;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #B5D89C;
            }
        """)

        self.reset_btn = QPushButton("重置")
        self.reset_btn.setStyleSheet("""
            QPushButton {
                background-color: #D08770;
                color: #2E3440;
                border: none;
                border-radius: 10px;
                padding: 8px 15px;
                font-weight: bold;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #EBCAB7;
            }
        """)
        self.reset_btn.setEnabled(False)

        self.btn_layout.addWidget(self.start_btn)
        self.btn_layout.addWidget(self.reset_btn)

        # 添加到布局
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.progress, 0, Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(self.slider_layout)
        self.layout.addLayout(self.btn_layout)

        # 计时器相关
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.remaining_time = 25 * 60  # 25分钟转换为秒
        self.is_running = False

        # 连接信号
        self.start_btn.clicked.connect(self.toggle_timer)
        self.reset_btn.clicked.connect(self.reset_timer)

        # 初始化进度条文本
        self.update_progress_text()

    def update_slider_label(self, value):
        self.slider_label.setText(f"{value} 分钟")
        if not self.is_running:
            self.remaining_time = value * 60
            self.update_progress_text()

    def toggle_timer(self):
        if not self.is_running:
            # 开始计时
            self.is_running = True
            self.start_btn.setText("暂停")
            self.time_slider.setEnabled(False)
            self.reset_btn.setEnabled(True)
            self.remaining_time = self.time_slider.value() * 60
            self.timer.start(1000)  # 每秒更新一次
        else:
            # 暂停计时
            self.is_running = False
            self.start_btn.setText("继续")
            self.timer.stop()

    def reset_timer(self):
        self.is_running = False
        self.timer.stop()
        self.start_btn.setText("开始")
        self.time_slider.setEnabled(True)
        self.reset_btn.setEnabled(False)
        self.remaining_time = self.time_slider.value() * 60
        self.update_progress()
        self.update_progress_text()

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_progress()
        else:
            self.timer_completed()

    def update_progress_text(self):
        """更新进度条上的倒计时文本"""
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.progress.timer_text = f"{minutes:02d}:{seconds:02d}"
        self.progress.update()

    def update_progress(self):
        total_seconds = self.time_slider.value() * 60
        progress = 100 - (self.remaining_time / total_seconds * 100)
        self.progress.value = progress
        self.update_progress_text()

    def timer_completed(self):
        self.timer.stop()
        self.is_running = False
        self.start_btn.setText("开始")
        self.time_slider.setEnabled(True)
        self.reset_btn.setEnabled(False)
        self.progress.value = 100
        self.progress.timer_text = "完成!"
        self.progress.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = self.load_config()

        # 设置窗口图标
        base_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_dir, "app_icon.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # 设置窗口属性
        self.setWindowTitle("Prodify - 生产力工具")
        self.setGeometry(100, 100, 1000, 700)
        self.setMinimumSize(800, 600)

        # 设置窗口背景为半透明
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet("background-color: rgba(46, 52, 64, 220); border-radius: 15px;")

        # 创建主控件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(30, 30, 30, 30)
        self.main_layout.setSpacing(20)

        # 顶部信息区
        self.top_info = QWidget()
        self.top_info.setStyleSheet("""
            background-color: rgba(59, 66, 82, 200);
            border-radius: 15px;
            border: 1px solid rgba(136, 192, 208, 0.3);
        """)
        self.top_layout = QHBoxLayout(self.top_info)
        self.top_layout.setContentsMargins(20, 15, 20, 15)

        # 天气部件
        self.weather_widget = WeatherWidget()

        # 应用标题和状态
        self.app_title = QLabel("Prodify")
        self.app_title.setStyleSheet("font-size: 28px; font-weight: bold; color: #88C0D0;")

        self.app_status = QLabel("状态: 运行中")
        self.app_status.setStyleSheet("font-size: 14px; color: #D8DEE9;")

        title_layout = QVBoxLayout()
        title_layout.addWidget(self.app_title)
        title_layout.addWidget(self.app_status)
        title_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 时间日期显示 - 美化版
        self.time_date_widget = QWidget()
        self.time_date_layout = QVBoxLayout(self.time_date_widget)
        self.time_date_layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

        # 时间标签 - 更大的字体
        self.time_label = QLabel()
        self.time_label.setStyleSheet("""
            font-size: 28px; 
            font-weight: bold; 
            color: #88C0D0;
            background-color: rgba(76, 86, 106, 0.4);
            border-radius: 10px;
            padding: 5px 10px;
        """)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 日期标签 - 更紧凑的设计
        self.date_label = QLabel()
        self.date_label.setStyleSheet("""
            font-size: 16px; 
            color: #D8DEE9;
            background-color: rgba(76, 86, 106, 0.4);
            border-radius: 10px;
            padding: 5px 10px;
            margin-top: 5px;
        """)
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 星期标签 - 新增
        self.week_label = QLabel()
        self.week_label.setStyleSheet("""
            font-size: 16px; 
            color: #A3BE8C;
            font-weight: bold;
            background-color: rgba(76, 86, 106, 0.4);
            border-radius: 10px;
            padding: 5px 10px;
            margin-top: 5px;
        """)
        self.week_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.time_date_layout.addWidget(self.time_label)
        self.time_date_layout.addWidget(self.date_label)
        self.time_date_layout.addWidget(self.week_label)

        # 更新时间
        self.update_time_date()
        self.time_timer = QTimer(self)
        self.time_timer.timeout.connect(self.update_time_date)
        self.time_timer.start(1000)  # 每秒更新一次

        self.top_layout.addWidget(self.weather_widget, 1)
        self.top_layout.addLayout(title_layout, 1)
        self.top_layout.addWidget(self.time_date_widget, 1)

        # 中央任务区
        self.center_widget = QWidget()
        self.center_widget.setStyleSheet("""
            background-color: rgba(59, 66, 82, 200);
            border-radius: 15px;
            border: 1px solid rgba(136, 192, 208, 0.3);
        """)
        self.center_layout = QHBoxLayout(self.center_widget)
        self.center_layout.setContentsMargins(20, 20, 20, 20)

        # 待办事项部件
        self.todo_widget = TodoWidget()
        self.center_layout.addWidget(self.todo_widget, 1)

        # 分隔线
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.Shape.VLine)
        self.separator.setFrameShadow(QFrame.Shadow.Sunken)
        self.separator.setStyleSheet("background-color: #4C566A;")
        self.center_layout.addWidget(self.separator)

        # 番茄钟部件
        self.tomato_timer = TomatoTimer()
        self.center_layout.addWidget(self.tomato_timer, 1)

        # 底部工具区 - 改为静态装饰
        self.bottom_widget = QWidget()
        self.bottom_widget.setStyleSheet("""
            background-color: rgba(59, 66, 82, 200);
            border-radius: 15px;
            border: 1px solid rgba(136, 192, 208, 0.3);
        """)
        self.bottom_layout = QHBoxLayout(self.bottom_widget)
        self.bottom_layout.setContentsMargins(20, 15, 20, 15)

        # 静态装饰文本
        quotes = [
            "专注当下，成就未来",
            "每一分钟的努力都是积累",
            "今日事，今日毕",
            "小步快跑，持续进步",
            "专注是最高效的生产力"
        ]

        self.decor_label = QLabel(random.choice(quotes))
        self.decor_label.setStyleSheet("""
            font-size: 16px;
            font-style: italic;
            color: #88C0D0;
            padding: 8px;
            border-radius: 10px;
        """)
        self.decor_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bottom_layout.addWidget(self.decor_label)

        # 添加装饰标签更新定时器
        self.quote_timer = QTimer(self)
        self.quote_timer.timeout.connect(self.update_decor_label)
        self.quote_timer.start(10000)  # 每10秒更换一次文本

        # 添加到主布局
        self.main_layout.addWidget(self.top_info)
        self.main_layout.addWidget(self.center_widget, 1)
        self.main_layout.addWidget(self.bottom_widget)

        # 天气更新定时器
        self.weather_timer = QTimer(self)
        self.weather_timer.timeout.connect(self.update_weather)
        # 初始立即更新一次，然后每30分钟更新一次
        self.update_weather()  # 初始更新
        self.weather_timer.start(30 * 60 * 1000)  # 30分钟

        # 背景动画定时器
        self.hue = 0
        self.bg_timer = QTimer(self)
        self.bg_timer.timeout.connect(self.update_background)
        self.bg_timer.start(50)

    def update_decor_label(self):
        quotes = [
            "专注当下，成就未来",
            "每一分钟的努力都是积累",
            "今日事，今日毕",
            "小步快跑，持续进步",
            "专注是最高效的生产力",
            "完成比完美更重要",
            "坚持就是胜利",
            "积少成多，聚沙成塔",
            "行动是成功的阶梯",
            "时间是最好的投资"
        ]
        self.decor_label.setText(random.choice(quotes))

    def update_time_date(self):
        """更新时间日期显示"""
        now = datetime.now()
        # 中文日期格式
        date_str = now.strftime("%Y年%m月%d日")
        # 中文时间格式（24小时制）
        time_str = now.strftime("%H:%M:%S")
        # 中文星期
        weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        week_str = weekdays[now.weekday()]

        self.time_label.setText(time_str)
        self.date_label.setText(date_str)
        self.week_label.setText(week_str)

    def load_config(self):
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
        default_config = {
            "city": "北京",
            "glass_opacity": 0.25,
            "border_radius": 20,
            "animation_duration": 300,
            "hue_speed": 0.5
        }

        try:
            if os.path.exists(config_path):
                with open(config_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                # 创建默认配置文件
                with open(config_path, 'w', encoding='utf-8') as f:
                    json.dump(default_config, f, indent=4, ensure_ascii=False)
                return default_config
        except Exception as e:
            print(f"加载配置文件失败: {e}")
            return default_config

    def update_weather(self):
        try:
            # 这里应该使用OpenWeather API，但为了演示使用模拟数据
            city = self.config.get("city", "北京")

            # 模拟天气数据
            weather_types = ["晴", "多云", "阴", "小雨", "中雨", "大雨", "小雪", "中雪", "大雪", "雾"]
            weather = random.choice(weather_types)
            temp = random.randint(-5, 35)
            humidity = random.randint(30, 90)

            # 生成智能提示
            hour = datetime.now().hour
            tip = self.generate_tip(weather, hour)

            # 映射天气到图标键
            icon_map = {
                "晴": "clear",
                "多云": "few_clouds",
                "阴": "clouds",
                "小雨": "drizzle",
                "中雨": "rain",
                "大雨": "rain",
                "小雪": "snow",
                "中雪": "snow",
                "大雪": "snow",
                "雾": "mist"
            }
            icon_key = icon_map.get(weather, "unknown")

            # 更新天气部件
            self.weather_widget.update_weather(temp, humidity, icon_key, f"{city} | {weather}", tip)
        except Exception as e:
            print(f"更新天气失败: {e}")

    def generate_tip(self, weather, hour):
        if "雨" in weather or "雪" in weather:
            return "下雨/雪天是专注工作的好时机！"
        elif "晴" in weather and 6 <= hour < 10:
            return "早晨的阳光充满活力，开始新的一天吧！"
        elif "晴" in weather and 10 <= hour < 14:
            return "阳光正好，适合处理需要创造力的任务！"
        elif "晴" in weather and 14 <= hour < 18:
            return "下午阳光温暖，保持专注！"
        elif hour < 6 or hour >= 22:
            return "夜深了，注意休息！"
        elif "多云" in weather or "阴" in weather:
            return "多云天气适合处理日常工作！"
        elif "雾" in weather:
            return "雾天请注意休息，避免过度用眼！"
        else:
            return "保持专注，提高效率！"

    def update_background(self):
        # 更新背景色调 - 更柔和的渐变
        self.hue += self.config.get("hue_speed", 0.3)
        if self.hue > 360:
            self.hue = 0

        # 创建更柔和的渐变背景
        base_hue = self.hue / 360
        color1 = QColor.fromHsvF(base_hue, 0.15, 0.15, 0.8)
        color2 = QColor.fromHsvF((base_hue + 0.1) % 1.0, 0.12, 0.18, 0.8)
        color3 = QColor.fromHsvF((base_hue + 0.2) % 1.0, 0.10, 0.20, 0.8)

        # 应用样式
        style = f"""
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 {color1.name(QColor.NameFormat.HexArgb)},
                stop:0.5 {color2.name(QColor.NameFormat.HexArgb)},
                stop:1 {color3.name(QColor.NameFormat.HexArgb)}
            );
            border-radius: {self.config.get('border_radius', 20)}px;
        """
        self.central_widget.setStyleSheet(style)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 设置应用程序图标
    base_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(base_dir, "app_icon.ico")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))

    # 在QApplication创建后初始化天气图标
    init_weather_icons()

    window = MainWindow()
    window.show()
    sys.exit(app.exec())