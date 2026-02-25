# Smart-FAE - 充电协议分析器

Smart-FAE 是一款功能强大的充电协议分析器 GUI 应用，基于 Python 和 PySide6 开发，专为工程师和技术人员设计，用于分析和监控各种充电协议。

## 项目概述

Smart-FAE (WindLink) 是一个综合性的充电协议分析工具，提供了多种协议分析功能，包括有线充电协议、Qi 无线充电协议、串口通信和 I2C 通信等。该应用采用现代化的深色主题界面，操作直观，功能丰富。

## 主要功能

### 1. 设备配置 (Device Config)
- 设备参数配置
- 连接设置管理

### 2. 串口功能 (Serial Port)
- 串口通信监控
- 数据传输分析

### 3. I2C 工具
- I2C 总线分析
- 设备通信监控

### 4. 有线协议分析器 (Wired Protocol Analyzer)
- 充电协议数据分析
- 实时监控和显示
- 详细的消息解析

### 5. Qi 协议分析器 (Qi Protocol Analyzer)
- 无线充电协议分析
- 协议消息解析
- 性能监控

### 6. 充电监控 (Charging Monitor)
- 充电状态实时监控
- 电压电流数据记录
- 充电过程分析

## 技术栈

- **开发语言**: Python 3
- **GUI 框架**: PySide6 (Qt for Python)
- **打包工具**: cx_Freeze
- **界面设计**: Qt Designer

## 项目结构

```
Smart-FAE/
├── main.py              # 主应用程序
├── main.ui              # 界面设计文件
├── main.spec            # PyInstaller 配置文件
├── setup.py             # cx_Freeze 配置文件
├── resources.qrc        # 资源文件
├── resources_rc.py      # 编译后的资源文件
├── icon.ico             # 应用图标
├── themes/              # 主题文件目录
├── .gitignore           # Git 忽略文件
└── LICENSE              # 许可证文件
```

## 安装说明

### 环境要求
- Python 3.7 或更高版本
- PySide6
- cx_Freeze (用于打包)

### 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/yourusername/Smart-FAE.git
   cd Smart-FAE
   ```

2. **安装依赖**
   ```bash
   pip install PySide6 cx_Freeze
   ```

3. **运行应用**
   ```bash
   python main.py
   ```

4. **打包应用**
   ```bash
   python setup.py build
   ```

## 使用方法

1. **启动应用**
   - 运行 `main.py` 或使用打包后的可执行文件

2. **导航菜单**
   - 使用左侧导航栏切换不同功能模块
   - 点击 "Hide" 按钮可折叠/展开左侧菜单

3. **功能模块**
   - **设备配置**: 设置设备参数和连接选项
   - **串口功能**: 监控和分析串口通信
   - **I2C 工具**: 分析 I2C 总线通信
   - **有线协议分析器**: 分析有线充电协议数据
   - **Qi 协议分析器**: 分析无线充电协议数据
   - **充电监控**: 实时监控充电状态

4. **数据显示**
   - 应用使用表格形式显示协议数据
   - 支持实时更新和数据分析

## 界面特点

- **现代化深色主题**: 基于 Dracula 配色方案，视觉效果舒适
- **响应式布局**: 适配不同屏幕尺寸
- **自定义标题栏**: 提供最小化、最大化和关闭按钮
- **可折叠侧边栏**: 优化空间利用
- **实时数据更新**: 动态显示分析结果

## 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。

## 联系方式

- 项目维护者: WindLink
- 项目名称: Smart-FAE (WindLink)
- 描述: Charging Protocol Analyzer

---

© 2024 WindLink. 保留所有权利。