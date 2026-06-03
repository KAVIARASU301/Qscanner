"""Institutional dark trading-terminal theme for the scanner GUI."""

_BG0 = "#050709"
_BG1 = "#0a0d12"
_BG2 = "#0f1318"
_BG3 = "#141920"
_BG4 = "#1a2030"
_BGTB = "#070a0f"
_BULL = "#00d4a8"
_BEAR = "#ff4d6a"
_AMBER = "#f59e0b"
_CYAN = "#00d4ff"
_BLUE = "#3b82f6"
_T0 = "#e8f0ff"
_T1 = "#a8bcd4"
_T2 = "#5a7090"
_T3 = "#2a3a50"
_SEL = "#1a2840"
_UI_FONT = "'Inter', 'Aptos', 'Segoe UI', 'Roboto', 'Noto Sans', sans-serif"
_MONO = "'JetBrains Mono', 'Consolas', monospace"
_ROW_H = 24

DARK_STYLESHEET = f"""
    * {{
        font-family: {_UI_FONT};
        font-size: 11px;
        color: {_T0};
        selection-background-color: {_SEL};
        selection-color: {_T0};
    }}

    QMainWindow, QDialog, QWidget {{
        background: {_BG1};
        color: {_T0};
    }}

    QToolBar {{
        background: {_BGTB};
        border: none;
        border-bottom: 1px solid {_BG4};
        padding: 3px 6px;
        spacing: 4px;
    }}
    QToolBar::separator {{
        background: {_BG4};
        width: 1px;
        margin: 4px 6px;
    }}

    QMenuBar {{
        background: {_BGTB};
        color: {_T1};
        border-bottom: 1px solid {_BG4};
        padding: 1px 4px;
    }}
    QMenuBar::item {{
        background: transparent;
        padding: 4px 8px;
    }}
    QMenuBar::item:selected {{
        background: {_BG3};
        color: {_T0};
    }}
    QMenu {{
        background: {_BG2};
        color: {_T0};
        border: 1px solid {_BG4};
        padding: 4px 0;
    }}
    QMenu::item {{ padding: 4px 22px 4px 12px; }}
    QMenu::item:selected {{
        background: {_SEL};
        color: {_T0};
    }}
    QMenu::item:disabled {{ color: {_T3}; }}
    QMenu::separator {{
        background: {_BG4};
        height: 1px;
        margin: 4px 8px;
    }}

    QLabel {{ color: {_T1}; background: transparent; }}
    QLabel:disabled {{ color: {_T3}; }}

    QGroupBox {{
        background: {_BG2};
        color: {_T1};
        border: 1px solid {_BG4};
        border-radius: 2px;
        margin-top: 10px;
        padding: 10px 8px 8px 8px;
        font-weight: 700;
    }}
    QGroupBox::title {{
        subcontrol-origin: margin;
        left: 8px;
        padding: 0 4px;
        color: {_T2};
        background: {_BG1};
        font-size: 10px;
        font-weight: 800;
    }}

    QCheckBox, QRadioButton {{
        color: {_T1};
        spacing: 5px;
        background: transparent;
    }}
    QCheckBox:hover, QRadioButton:hover {{ color: {_T0}; }}
    QCheckBox:disabled, QRadioButton:disabled {{ color: {_T3}; }}
    QCheckBox::indicator, QRadioButton::indicator {{
        width: 13px;
        height: 13px;
        border: 1px solid {_BG4};
        background: {_BG0};
    }}
    QCheckBox::indicator {{ border-radius: 2px; }}
    QRadioButton::indicator {{ border-radius: 7px; }}
    QCheckBox::indicator:checked, QRadioButton::indicator:checked {{
        background: {_AMBER};
        border: 1px solid {_AMBER};
    }}
    QCheckBox::indicator:disabled, QRadioButton::indicator:disabled {{
        background: {_BG1};
        border: 1px solid {_T3};
    }}

    QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox,
    QDateEdit, QTimeEdit, QDateTimeEdit, QComboBox {{
        background: {_BG0};
        color: {_T0};
        border: 1px solid {_BG4};
        border-radius: 2px;
        padding: 3px 6px;
        min-height: 18px;
    }}
    QTextEdit, QPlainTextEdit {{
        background: {_BG0};
        font-family: {_MONO};
    }}
    QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus,
    QSpinBox:focus, QDoubleSpinBox:focus, QDateEdit:focus,
    QTimeEdit:focus, QDateTimeEdit:focus, QComboBox:focus {{
        border: 1px solid {_CYAN};
    }}
    QLineEdit:disabled, QTextEdit:disabled, QPlainTextEdit:disabled,
    QSpinBox:disabled, QDoubleSpinBox:disabled, QDateEdit:disabled,
    QTimeEdit:disabled, QDateTimeEdit:disabled, QComboBox:disabled {{
        background: {_BG1};
        color: {_T3};
        border: 1px solid {_BG4};
    }}
    QComboBox::drop-down {{
        border: none;
        border-left: 1px solid {_BG4};
        width: 18px;
        background: {_BG2};
    }}
    QComboBox QAbstractItemView {{
        background: {_BG2};
        color: {_T0};
        border: 1px solid {_BG4};
        selection-background-color: {_SEL};
        outline: 0;
    }}

    QPushButton {{
        background: {_BG2};
        color: {_T0};
        border: 1px solid {_BG4};
        border-radius: 2px;
        padding: 4px 10px;
        font-weight: 700;
        min-height: 18px;
    }}
    QPushButton:hover {{
        background: {_BG3};
        border-color: {_T2};
    }}
    QPushButton:pressed, QPushButton:checked {{
        background: {_SEL};
        border-color: {_AMBER};
        color: {_T0};
    }}
    QPushButton:disabled {{
        background: {_BG1};
        color: {_T3};
        border-color: {_BG4};
    }}

    QTableView, QTableWidget {{
        background: {_BG1};
        alternate-background-color: {_BG2};
        color: {_T0};
        gridline-color: transparent;
        border: 1px solid {_BG4};
        border-radius: 2px;
        outline: none;
        selection-background-color: {_SEL};
        selection-color: {_T0};
        font-size: 11px;
    }}
    QTableView::item, QTableWidget::item {{
        border: none;
        padding: 2px 6px;
    }}
    QTableView::item:hover, QTableWidget::item:hover {{
        background: {_BG3};
    }}
    QTableView::item:selected, QTableWidget::item:selected {{
        background: {_SEL};
        color: {_T0};
    }}
    QHeaderView {{ background: {_BG2}; }}
    QHeaderView::section {{
        background: {_BG2};
        color: {_T2};
        border: none;
        border-right: 1px solid {_BG4};
        border-bottom: 1px solid {_BG4};
        padding: 3px 6px;
        font-size: 10px;
        font-weight: 800;
    }}

    QSplitter::handle {{
        background: {_BG4};
    }}
    QSplitter::handle:hover {{ background: {_T2}; }}

    QTabWidget::pane {{
        border: 1px solid {_BG4};
        background: {_BG1};
    }}
    QTabBar::tab {{
        background: {_BGTB};
        color: {_T2};
        border: none;
        border-bottom: 2px solid transparent;
        padding: 5px 10px;
        font-weight: 700;
    }}
    QTabBar::tab:selected {{
        color: {_T0};
        border-bottom: 2px solid {_AMBER};
        background: {_BG2};
    }}
    QTabBar::tab:hover {{ color: {_T1}; background: {_BG3}; }}

    QStatusBar {{
        background: {_BGTB};
        color: {_T2};
        border-top: 1px solid {_BG4};
        min-height: 24px;
    }}
    QStatusBar QLabel {{ color: {_T2}; }}

    QScrollArea {{ border: none; background: transparent; }}
    QScrollBar:vertical {{
        background: {_BG1};
        width: 9px;
        margin: 0;
    }}
    QScrollBar::handle:vertical {{
        background: {_BG4};
        min-height: 20px;
        border-radius: 2px;
    }}
    QScrollBar::handle:vertical:hover {{ background: {_T2}; }}
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; }}
    QScrollBar:horizontal {{
        background: {_BG1};
        height: 9px;
        margin: 0;
    }}
    QScrollBar::handle:horizontal {{
        background: {_BG4};
        min-width: 20px;
        border-radius: 2px;
    }}
    QScrollBar::handle:horizontal:hover {{ background: {_T2}; }}
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{ width: 0; }}
"""
