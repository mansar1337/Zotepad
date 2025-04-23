import sys
import os
from PyQt6.QtGui import QAction, QPalette, QColor, QActionGroup, QFont, QIcon, QPixmap, QPainter, QTextFormat, QBrush, QImage
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QFileDialog,
    QMessageBox, QFontDialog, QInputDialog, QSlider,
    QVBoxLayout, QWidget, QLabel, QDialog, QStatusBar,
    QPushButton, QHBoxLayout, QFrame, QLineEdit, QComboBox, QCheckBox, QDialogButtonBox,
    QColorDialog, QGroupBox, QRadioButton, QListWidget, QListWidgetItem
)
from PyQt6.QtCore import Qt, QSettings, QTimer, QUrl, QRect, pyqtSignal, QSize, QDateTime
from PyQt6.QtWidgets import QGraphicsBlurEffect
from PIL import Image, ImageDraw, ImageFont
from PyQt6.QtGui import QDesktopServices

# Доступные языки приложения
LANGUAGES = {
    "Русский": "ru",
    "English": "en"
}

# Словари переводов
TRANSLATIONS = {
    "ru": {
        # Меню
        "file_menu": "Файл",
        "new": "Новый",
        "open": "Открыть...",
        "save": "Сохранить",
        "save_as": "Сохранить как...",
        "exit": "Выход",
        
        "edit_menu": "Правка",
        "undo": "Отменить",
        "redo": "Повторить",
        "cut": "Вырезать",
        "copy": "Копировать",
        "paste": "Вставить",
        "delete": "Удалить",
        "find": "Найти...",
        "select_all": "Выделить всё",
        
        "format_menu": "Формат",
        "font": "Шрифт...",
        "word_wrap": "Перенос по словам",
        
        "encoding_menu": "Кодировка",
        
        "view_menu": "Вид",
        "theme_menu": "Тема оформления",
        "light_theme": "Светлая",
        "dark_theme": "Тёмная",
        "blue_theme": "Синяя",
        "green_theme": "Зелёная",
        "opacity": "Прозрачность...",
        
        "help_menu": "Справка",
        "settings": "Настройки",
        "about": "О программе",
        
        "blur_effect": "Размытие фона",
        "blur_radius": "Радиус размытия",
        "blur_enabled": "Включить размытие",
        
        # Диалоги
        "settings_title": "Настройки",
        "settings_app": "Настройки приложения",
        "lang_interface": "Язык интерфейса:",
        "save_btn": "Сохранить",
        "cancel_btn": "Отмена",
        "settings_saved": "Настройки сохранены",
        "restart_needed": "Некоторые изменения вступят в силу после перезапуска приложения.",
        
        "about_title": "О программе",
        "version": "Версия:",
        "theme": "Тема:",
        "opacity_label": "Прозрачность:",
        "encoding_label": "Кодировка:",
        "developers": "Разработчики:",
        
        "find_title": "Поиск и замена",
        "find_label": "Найти:",
        "replace_label": "Заменить на:",
        "find_next": "Найти далее",
        "replace": "Заменить",
        "replace_all": "Заменить все",
        
        "opacity_title": "Настройка прозрачности",
        "opacity_setting": "Настройка прозрачности окна",
        "opacity_value": "Прозрачность: {}%",
        
        # Статусбар и сообщения
        "ready": "Готов к работе",
        "encoding_status": "Кодировка: {}",
        "theme_changed": "Тема изменена на: {}",
        "light": "Светлую",
        "dark": "Тёмную",
        "blue": "Синяя",
        "green": "Зелёная",
        "opacity_set": "Прозрачность окна установлена: {}%",
        "file_opened": "Файл открыт: {}",
        "file_saved": "Файл сохранен: {}",
        "file_saved_as": "Файл сохранен как: {}",
        "new_document": "Создан новый документ",
        "save_changes": "Сохранить изменения?",
        "save_changes_question": "Сохранить изменения в текущем файле?",
        "text_replaced": "Текст заменен",
        "select_text": "Выделите текст для замены",
        "nothing_selected": "Ничего не выделено",
        "replacements": "Заменено {} совпадений",
        "text_not_found": "Текст '{}' не найден",
        "text_found": "Найдено: '{}'",
        "enter_search_text": "Введите текст для поиска",
        "font_changed": "Шрифт изменен",
        "word_wrap_on": "Перенос по словам: включен",
        "word_wrap_off": "Перенос по словам: выключен",
        "encoding_changed": "Кодировка изменена на {}",
        "encoding_error": "Невозможно открыть файл '{}' в кодировке {}. Попробуйте другую кодировку.",
        "opening_canceled": "Открытие файла отменено из-за ошибки кодировки",
        "choose_encoding": "Выбор кодировки",
        "encoding_error_message": "Не удалось открыть файл '{}' в кодировке {}.\nВыберите кодировку файла:",
        "file_not_found": "Файл не найден: {}",
        "readonly_mode": "Файл открыт в режиме только для чтения: {}",
        "background_image": "Фоновое изображение...",
        "background_image_title": "Выбор фонового изображения",
        "background_image_error": "Ошибка при загрузке изображения",
        "background_image_removed": "Фоновое изображение удалено",
        "background_image_set": "Фоновое изображение установлено",
        "background_opacity": "Прозрачность фона...",
        "background_opacity_title": "Настройка прозрачности фона",
        "background_opacity_value": "Прозрачность фона: {}%",
        "preview": "Предпросмотр",
        "enable_background": "Включить фоновое изображение",
        "social_networks": "Социальные сети",
        "telegram": "Telegram",
        "telegram_link": "https://t.me/kARTEL_EZZtemp",
        "github": "GitHub",
        "github_ezz": "https://github.com/EzzTEMP",
        "github_mansar": "https://github.com/mansar1337",
        "social_networks_title": "Наши социальные сети",
        "social_networks_message": "Присоединяйтесь к нам в социальных сетях!",
        "customize_colors": "Настройка цветов...",
        "background_color": "Цвет фона",
        "cursor_color": "Цвет курсора",
        "select_color": "Выбрать цвет",
        "colors_customized": "Цвета настроены",
        "customize_cursor": "Настройка курсора...",
        "cursor_width": "Ширина курсора",
        "cursor_style": "Стиль курсора",
        "cursor_blink": "Мигание курсора",
        "cursor_solid": "Сплошной",
        "cursor_dashed": "Пунктирный",
        "cursor_dotted": "Точечный",
        "cursor_customized": "Курсор настроен",
        "show_datetime": "Показывать дату и время",
        "datetime_format": "Формат даты и времени",
        "datetime_24h": "24-часовой формат",
        "datetime_12h": "12-часовой формат",
        "datetime_custom": "Пользовательский формат",
        "datetime_format_example": "Пример: dd.MM.yyyy HH:mm:ss",
        "datetime_updated": "Настройки времени обновлены",
        "highlight_settings": "Настройки подсветки...",
        "highlight_color": "Цвет подсветки",
        "highlight_opacity": "Прозрачность подсветки",
        "highlight_effects": "Эффекты подсветки",
        "highlight_gradient": "Градиентная подсветка",
        "highlight_animation": "Анимация подсветки",
        "highlight_speed": "Скорость анимации",
        "highlight_settings_updated": "Настройки подсветки обновлены",
        "select_city": "Выбрать город...",
        "city_search": "Поиск города",
        "city_list": "Список городов",
        "timezone": "Часовой пояс",
        "current_time": "Текущее время",
        "city_selected": "Город выбран",
        "city_not_found": "Город не найден",
    },
    "en": {
        # Меню
        "file_menu": "File",
        "new": "New",
        "open": "Open...",
        "save": "Save",
        "save_as": "Save As...",
        "exit": "Exit",
        
        "edit_menu": "Edit",
        "undo": "Undo",
        "redo": "Redo",
        "cut": "Cut",
        "copy": "Copy",
        "paste": "Paste",
        "delete": "Delete",
        "find": "Find...",
        "select_all": "Select All",
        
        "format_menu": "Format",
        "font": "Font...",
        "word_wrap": "Word Wrap",
        
        "encoding_menu": "Encoding",
        
        "view_menu": "View",
        "theme_menu": "Theme",
        "light_theme": "Light",
        "dark_theme": "Dark",
        "blue_theme": "Blue",
        "green_theme": "Green",
        "opacity": "Opacity...",
        
        "help_menu": "Help",
        "settings": "Settings",
        "about": "About",
        
        "blur_effect": "Background Blur",
        "blur_radius": "Blur Radius",
        "blur_enabled": "Enable Blur",
        
        # Диалоги
        "settings_title": "Settings",
        "settings_app": "Application Settings",
        "lang_interface": "Interface Language:",
        "save_btn": "Save",
        "cancel_btn": "Cancel",
        "settings_saved": "Settings Saved",
        "restart_needed": "Some changes will take effect after restarting the application.",
        
        "about_title": "About",
        "version": "Version:",
        "theme": "Theme:",
        "opacity_label": "Opacity:",
        "encoding_label": "Encoding:",
        "developers": "Developers:",
        
        "find_title": "Find and Replace",
        "find_label": "Find:",
        "replace_label": "Replace with:",
        "find_next": "Find Next",
        "replace": "Replace",
        "replace_all": "Replace All",
        
        "opacity_title": "Opacity Settings",
        "opacity_setting": "Window Opacity Settings",
        "opacity_value": "Opacity: {}%",
        
        # Статусбар и сообщения
        "ready": "Ready",
        "encoding_status": "Encoding: {}",
        "theme_changed": "Theme changed to: {}",
        "light": "Light",
        "dark": "Dark",
        "blue": "Blue",
        "green": "Green",
        "opacity_set": "Window opacity set to: {}%",
        "file_opened": "File opened: {}",
        "file_saved": "File saved: {}",
        "file_saved_as": "File saved as: {}",
        "new_document": "New document created",
        "save_changes": "Save changes?",
        "save_changes_question": "Save changes to current file?",
        "text_replaced": "Text replaced",
        "select_text": "Select text to replace",
        "nothing_selected": "Nothing selected",
        "replacements": "Replaced {} matches",
        "text_not_found": "Text '{}' not found",
        "text_found": "Found: '{}'",
        "enter_search_text": "Enter text to search",
        "font_changed": "Font changed",
        "word_wrap_on": "Word wrap: enabled",
        "word_wrap_off": "Word wrap: disabled",
        "encoding_changed": "Encoding changed to {}",
        "encoding_error": "Unable to open file '{}' with encoding {}. Try another encoding.",
        "opening_canceled": "File opening canceled due to encoding error",
        "choose_encoding": "Choose Encoding",
        "encoding_error_message": "Failed to open file '{}' with encoding {}.\nSelect file encoding:",
        "file_not_found": "File not found: {}",
        "readonly_mode": "File opened in read-only mode: {}",
        "background_image": "Background Image...",
        "background_image_title": "Choose Background Image",
        "background_image_error": "Error loading image",
        "background_image_removed": "Background image removed",
        "background_image_set": "Background image set",
        "background_opacity": "Background Opacity...",
        "background_opacity_title": "Background Opacity Settings",
        "background_opacity_value": "Background opacity: {}%",
        "preview": "Preview",
        "enable_background": "Enable background image",
        "social_networks": "Social Networks",
        "telegram": "Telegram",
        "telegram_link": "https://t.me/kARTEL_EZZtemp",
        "github": "GitHub",
        "github_ezz": "https://github.com/EzzTEMP",
        "github_mansar": "https://github.com/mansar1337",
        "social_networks_title": "Our Social Networks",
        "social_networks_message": "Join us on social networks!",
        "customize_colors": "Customize Colors...",
        "background_color": "Background Color",
        "cursor_color": "Cursor Color",
        "select_color": "Select Color",
        "colors_customized": "Colors customized",
        "customize_cursor": "Customize Cursor...",
        "cursor_width": "Cursor Width",
        "cursor_style": "Cursor Style",
        "cursor_blink": "Cursor Blink",
        "cursor_solid": "Solid",
        "cursor_dashed": "Dashed",
        "cursor_dotted": "Dotted",
        "cursor_customized": "Cursor customized",
        "show_datetime": "Show date and time",
        "datetime_format": "Date and time format",
        "datetime_24h": "24-hour format",
        "datetime_12h": "12-hour format",
        "datetime_custom": "Custom format",
        "datetime_format_example": "Example: dd.MM.yyyy HH:mm:ss",
        "datetime_updated": "Time settings updated",
        "highlight_settings": "Highlight Settings...",
        "highlight_color": "Highlight Color",
        "highlight_opacity": "Highlight Opacity",
        "highlight_effects": "Highlight Effects",
        "highlight_gradient": "Gradient Highlight",
        "highlight_animation": "Highlight Animation",
        "highlight_speed": "Animation Speed",
        "highlight_settings_updated": "Highlight settings updated",
        "select_city": "Select City...",
        "city_search": "Search city",
        "city_list": "City List",
        "timezone": "Time Zone",
        "current_time": "Current Time",
        "city_selected": "City selected",
        "city_not_found": "City not found",
    }
}

# Добавляем стиль кнопок в зависимости от темы
LIGHT_STYLE = """
    QMainWindow {
        background-color: #ffffff;
    }
    QTextEdit {
        background-color: white;
        color: #2c3e50;
        border: 2px solid #e1e1e1;
        border-radius: 12px;
        padding: 12px;
        selection-background-color: #3498db;
        selection-color: white;
        font-family: 'Segoe UI', sans-serif;
        line-height: 1.6;
    }
    QTextEdit:focus {
        border-color: #3498db;
        box-shadow: 0 0 5px rgba(52, 152, 219, 0.3);
    }
    QMenuBar {
        background-color: #ffffff;
        border-bottom: 1px solid #e1e1e1;
        color: #2c3e50;
        padding: 4px;
    }
    QMenuBar::item {
        padding: 8px 16px;
        background-color: transparent;
        border-radius: 6px;
        margin: 2px;
    }
    QMenuBar::item:selected {
        background-color: #f0f0f0;
        color: #3498db;
    }
    QMenuBar::item:pressed {
        background-color: #e1e1e1;
    }
    QMenu {
        background-color: #ffffff;
        border: 1px solid #e1e1e1;
        border-radius: 12px;
        padding: 8px;
        margin: 4px;
    }
    QMenu::item {
        padding: 8px 32px 8px 16px;
        border-radius: 6px;
        margin: 2px;
    }
    QMenu::item:selected {
        background-color: #f0f0f0;
        color: #3498db;
    }
    QMenu::separator {
        height: 1px;
        background-color: #e1e1e1;
        margin: 6px 0px;
    }
    QPushButton {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        min-width: 80px;
    }
    QPushButton:hover {
        background-color: #2980b9;
        transform: translateY(-1px);
    }
    QPushButton:pressed {
        background-color: #2472a4;
        transform: translateY(1px);
    }
    QPushButton:disabled {
        background-color: #bdc3c7;
    }
    QSlider::groove:horizontal {
        border: none;
        height: 8px;
        background: #e1e1e1;
        border-radius: 4px;
        margin: 4px 0;
    }
    QSlider::handle:horizontal {
        background: #3498db;
        width: 20px;
        height: 20px;
        margin: -6px 0;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    QSlider::handle:horizontal:hover {
        background: #2980b9;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
    }
    QStatusBar {
        background-color: #f8f9fa;
        color: #2c3e50;
        border-top: 1px solid #e1e1e1;
        padding: 4px;
    }
    QLabel {
        color: #2c3e50;
        font-size: 13px;
    }
    QDialog {
        background-color: #ffffff;
        border-radius: 12px;
    }
    QLineEdit {
        padding: 10px;
        border: 2px solid #e1e1e1;
        border-radius: 8px;
        background-color: white;
        color: #2c3e50;
        selection-background-color: #3498db;
        selection-color: white;
    }
    QLineEdit:focus {
        border-color: #3498db;
        box-shadow: 0 0 5px rgba(52, 152, 219, 0.3);
    }
    QComboBox {
        padding: 8px 12px;
        border: 2px solid #e1e1e1;
        border-radius: 8px;
        background-color: white;
        color: #2c3e50;
        min-width: 120px;
    }
    QComboBox:hover {
        border-color: #3498db;
    }
    QComboBox:focus {
        border-color: #3498db;
        box-shadow: 0 0 5px rgba(52, 152, 219, 0.3);
    }
    QComboBox::drop-down {
        border: none;
        width: 20px;
    }
    QComboBox::down-arrow {
        image: url(down_arrow.png);
        width: 12px;
        height: 12px;
    }
"""

DARK_STYLE = """
    QMainWindow {
        background-color: #1a1b1e;
    }
    QTextEdit {
        background-color: #2d2d30;
        color: #e1e1e1;
        border: 2px solid #3d3d3d;
        border-radius: 12px;
        padding: 12px;
        selection-background-color: #264f78;
        selection-color: white;
        font-family: 'Segoe UI', sans-serif;
        line-height: 1.6;
    }
    QTextEdit:focus {
        border-color: #264f78;
        box-shadow: 0 0 5px rgba(38, 79, 120, 0.3);
    }
    QMenuBar {
        background-color: #1a1b1e;
        border-bottom: 1px solid #3d3d3d;
        color: #e1e1e1;
        padding: 4px;
    }
    QMenuBar::item {
        padding: 8px 16px;
        background-color: transparent;
        border-radius: 6px;
        margin: 2px;
    }
    QMenuBar::item:selected {
        background-color: #2d2d30;
        color: #3a8ee6;
    }
    QMenuBar::item:pressed {
        background-color: #3d3d3d;
    }
    QMenu {
        background-color: #2d2d30;
        border: 1px solid #3d3d3d;
        border-radius: 12px;
        padding: 8px;
        margin: 4px;
    }
    QMenu::item {
        padding: 8px 32px 8px 16px;
        border-radius: 6px;
        margin: 2px;
        color: #e1e1e1;
    }
    QMenu::item:selected {
        background-color: #3d3d3d;
        color: #3a8ee6;
    }
    QMenu::separator {
        height: 1px;
        background-color: #3d3d3d;
        margin: 6px 0px;
    }
    QPushButton {
        background-color: #264f78;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        min-width: 80px;
    }
    QPushButton:hover {
        background-color: #1c3b5a;
        transform: translateY(-1px);
    }
    QPushButton:pressed {
        background-color: #15304d;
        transform: translateY(1px);
    }
    QPushButton:disabled {
        background-color: #3d3d3d;
    }
    QSlider::groove:horizontal {
        border: none;
        height: 8px;
        background: #3d3d3d;
        border-radius: 4px;
        margin: 4px 0;
    }
    QSlider::handle:horizontal {
        background: #264f78;
        width: 20px;
        height: 20px;
        margin: -6px 0;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    QSlider::handle:horizontal:hover {
        background: #1c3b5a;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    }
    QStatusBar {
        background-color: #1a1b1e;
        color: #e1e1e1;
        border-top: 1px solid #3d3d3d;
        padding: 4px;
    }
    QLabel {
        color: #e1e1e1;
        font-size: 13px;
    }
    QDialog {
        background-color: #1a1b1e;
        border-radius: 12px;
    }
    QLineEdit {
        padding: 10px;
        border: 2px solid #3d3d3d;
        border-radius: 8px;
        background-color: #2d2d30;
        color: #e1e1e1;
        selection-background-color: #264f78;
        selection-color: white;
    }
    QLineEdit:focus {
        border-color: #264f78;
        box-shadow: 0 0 5px rgba(38, 79, 120, 0.3);
    }
    QComboBox {
        padding: 8px 12px;
        border: 2px solid #3d3d3d;
        border-radius: 8px;
        background-color: #2d2d30;
        color: #e1e1e1;
        min-width: 120px;
    }
    QComboBox:hover {
        border-color: #264f78;
    }
    QComboBox:focus {
        border-color: #264f78;
        box-shadow: 0 0 5px rgba(38, 79, 120, 0.3);
    }
    QComboBox::drop-down {
        border: none;
        width: 20px;
    }
    QComboBox::down-arrow {
        image: url(down_arrow_white.png);
        width: 12px;
        height: 12px;
    }
"""

BLUE_STYLE = """
    QMainWindow {
        background-color: #1e3a5f;
    }
    QTextEdit {
        background-color: #2c4d7c;
        color: #e1e1e1;
        border: 2px solid #3d5d8c;
        border-radius: 12px;
        padding: 12px;
        selection-background-color: #4a7ab0;
        selection-color: white;
        font-family: 'Segoe UI', sans-serif;
        line-height: 1.6;
    }
    QTextEdit:focus {
        border-color: #4a7ab0;
        box-shadow: 0 0 5px rgba(74, 122, 176, 0.3);
    }
    QMenuBar {
        background-color: #1e3a5f;
        border-bottom: 1px solid #3d5d8c;
        color: #e1e1e1;
        padding: 4px;
    }
    QMenuBar::item {
        padding: 8px 16px;
        background-color: transparent;
        border-radius: 6px;
        margin: 2px;
    }
    QMenuBar::item:selected {
        background-color: #2c4d7c;
        color: #4a7ab0;
    }
    QMenuBar::item:pressed {
        background-color: #3d5d8c;
    }
    QMenu {
        background-color: #2c4d7c;
        border: 1px solid #3d5d8c;
        border-radius: 12px;
        padding: 8px;
        margin: 4px;
    }
    QMenu::item {
        padding: 8px 32px 8px 16px;
        border-radius: 6px;
        margin: 2px;
        color: #e1e1e1;
    }
    QMenu::item:selected {
        background-color: #3d5d8c;
        color: #4a7ab0;
    }
    QMenu::separator {
        height: 1px;
        background-color: #3d5d8c;
        margin: 6px 0px;
    }
    QPushButton {
        background-color: #4a7ab0;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        min-width: 80px;
    }
    QPushButton:hover {
        background-color: #3d5d8c;
        transform: translateY(-1px);
    }
    QPushButton:pressed {
        background-color: #2c4d7c;
        transform: translateY(1px);
    }
    QPushButton:disabled {
        background-color: #3d5d8c;
    }
    QSlider::groove:horizontal {
        border: none;
        height: 8px;
        background: #3d5d8c;
        border-radius: 4px;
        margin: 4px 0;
    }
    QSlider::handle:horizontal {
        background: #4a7ab0;
        width: 20px;
        height: 20px;
        margin: -6px 0;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    QSlider::handle:horizontal:hover {
        background: #3d5d8c;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    }
    QStatusBar {
        background-color: #1e3a5f;
        color: #e1e1e1;
        border-top: 1px solid #3d5d8c;
        padding: 4px;
    }
    QLabel {
        color: #e1e1e1;
        font-size: 13px;
    }
    QDialog {
        background-color: #1e3a5f;
        border-radius: 12px;
    }
    QLineEdit {
        padding: 10px;
        border: 2px solid #3d5d8c;
        border-radius: 8px;
        background-color: #2c4d7c;
        color: #e1e1e1;
        selection-background-color: #4a7ab0;
        selection-color: white;
    }
    QLineEdit:focus {
        border-color: #4a7ab0;
        box-shadow: 0 0 5px rgba(74, 122, 176, 0.3);
    }
    QComboBox {
        padding: 8px 12px;
        border: 2px solid #3d5d8c;
        border-radius: 8px;
        background-color: #2c4d7c;
        color: #e1e1e1;
        min-width: 120px;
    }
    QComboBox:hover {
        border-color: #4a7ab0;
    }
    QComboBox:focus {
        border-color: #4a7ab0;
        box-shadow: 0 0 5px rgba(74, 122, 176, 0.3);
    }
    QComboBox::drop-down {
        border: none;
        width: 20px;
    }
    QComboBox::down-arrow {
        image: url(down_arrow_white.png);
        width: 12px;
        height: 12px;
    }
"""

GREEN_STYLE = """
    QMainWindow {
        background-color: #1e3f2d;
    }
    QTextEdit {
        background-color: #2c4d3c;
        color: #e1e1e1;
        border: 2px solid #3d5d4c;
        border-radius: 12px;
        padding: 12px;
        selection-background-color: #4a7a60;
        selection-color: white;
        font-family: 'Segoe UI', sans-serif;
        line-height: 1.6;
    }
    QTextEdit:focus {
        border-color: #4a7a60;
        box-shadow: 0 0 5px rgba(74, 122, 96, 0.3);
    }
    QMenuBar {
        background-color: #1e3f2d;
        border-bottom: 1px solid #3d5d4c;
        color: #e1e1e1;
        padding: 4px;
    }
    QMenuBar::item {
        padding: 8px 16px;
        background-color: transparent;
        border-radius: 6px;
        margin: 2px;
    }
    QMenuBar::item:selected {
        background-color: #2c4d3c;
        color: #4a7a60;
    }
    QMenuBar::item:pressed {
        background-color: #3d5d4c;
    }
    QMenu {
        background-color: #2c4d3c;
        border: 1px solid #3d5d4c;
        border-radius: 12px;
        padding: 8px;
        margin: 4px;
    }
    QMenu::item {
        padding: 8px 32px 8px 16px;
        border-radius: 6px;
        margin: 2px;
        color: #e1e1e1;
    }
    QMenu::item:selected {
        background-color: #3d5d4c;
        color: #4a7a60;
    }
    QMenu::separator {
        height: 1px;
        background-color: #3d5d4c;
        margin: 6px 0px;
    }
    QPushButton {
        background-color: #4a7a60;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        min-width: 80px;
    }
    QPushButton:hover {
        background-color: #3d5d4c;
        transform: translateY(-1px);
    }
    QPushButton:pressed {
        background-color: #2c4d3c;
        transform: translateY(1px);
    }
    QPushButton:disabled {
        background-color: #3d5d4c;
    }
    QSlider::groove:horizontal {
        border: none;
        height: 8px;
        background: #3d5d4c;
        border-radius: 4px;
        margin: 4px 0;
    }
    QSlider::handle:horizontal {
        background: #4a7a60;
        width: 20px;
        height: 20px;
        margin: -6px 0;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    QSlider::handle:horizontal:hover {
        background: #3d5d4c;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    }
    QStatusBar {
        background-color: #1e3f2d;
        color: #e1e1e1;
        border-top: 1px solid #3d5d4c;
        padding: 4px;
    }
    QLabel {
        color: #e1e1e1;
        font-size: 13px;
    }
    QDialog {
        background-color: #1e3f2d;
        border-radius: 12px;
    }
    QLineEdit {
        padding: 10px;
        border: 2px solid #3d5d4c;
        border-radius: 8px;
        background-color: #2c4d3c;
        color: #e1e1e1;
        selection-background-color: #4a7a60;
        selection-color: white;
    }
    QLineEdit:focus {
        border-color: #4a7a60;
        box-shadow: 0 0 5px rgba(74, 122, 96, 0.3);
    }
    QComboBox {
        padding: 8px 12px;
        border: 2px solid #3d5d4c;
        border-radius: 8px;
        background-color: #2c4d3c;
        color: #e1e1e1;
        min-width: 120px;
    }
    QComboBox:hover {
        border-color: #4a7a60;
    }
    QComboBox:focus {
        border-color: #4a7a60;
        box-shadow: 0 0 5px rgba(74, 122, 96, 0.3);
    }
    QComboBox::drop-down {
        border: none;
        width: 20px;
    }
    QComboBox::down-arrow {
        image: url(down_arrow_white.png);
        width: 12px;
        height: 12px;
    }
"""

class OpacityDialog(QDialog):
    def __init__(self, parent=None, current_opacity=1.0, translations=None):
        super().__init__(parent)
        
        # Если переводы не переданы, используем русский по умолчанию
        if translations is None:
            translations = TRANSLATIONS["ru"]
        
        self.setWindowTitle(translations["opacity_title"])
        self.setFixedSize(400, 250)
        
        # Устанавливаем отступы
        self.setContentsMargins(20, 20, 20, 20)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # Добавляем заголовок
        title = QLabel(translations["opacity_setting"])
        title.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Добавляем разделитель с градиентом
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        if parent and parent.current_theme == "light":
            line.setStyleSheet("""
                QFrame {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                              stop:0 #007bff, stop:1 #00ff95);
                    height: 2px;
                    border: none;
                }
            """)
        else:
            line.setStyleSheet("""
                QFrame {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                              stop:0 #3a8ee6, stop:1 #00ffcc);
                    height: 2px;
                    border: none;
                }
            """)
        layout.addWidget(line)
        
        # Улучшенная этикетка
        self.label = QLabel(translations["opacity_value"].format(int(current_opacity * 100)))
        self.label.setFont(QFont("Segoe UI", 12))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        # Улучшенный слайдер
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(30, 100)
        self.slider.setValue(int(current_opacity * 100))
        self.slider.valueChanged.connect(self.update_opacity)
        layout.addWidget(self.slider)
        
        # Добавляем кнопки
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        cancel_button = QPushButton(translations["cancel_btn"])
        cancel_button.clicked.connect(self.reject)
        cancel_button.setMinimumWidth(100)
        
        apply_button = QPushButton(translations["save_btn"])
        apply_button.clicked.connect(self.accept)
        apply_button.setMinimumWidth(100)
        
        button_layout.addStretch()
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(apply_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
        
        # Сохраняем переводы для обновления текста
        self.translations = translations
    
    def update_opacity(self, value):
        self.label.setText(self.translations["opacity_value"].format(value))
        # Устанавливаем прозрачность только для главного окна
        opacity = value / 100
        parent = self.parent()
        if parent:
            parent.setWindowOpacity(opacity)
            # Сохраняем значение
            parent.opacity = opacity

class FindDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        
        # Получаем текущие переводы
        lang_code = LANGUAGES.get(self.parent.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        self.setWindowTitle(translations["find_title"])
        self.setFixedSize(500, 250)
        
        # Устанавливаем отступы
        self.setContentsMargins(20, 20, 20, 20)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # Добавляем заголовок
        title = QLabel(translations["find_title"])
        title.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Добавляем разделитель с градиентом
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        if parent.current_theme == "light":
            line.setStyleSheet("""
                QFrame {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                              stop:0 #007bff, stop:1 #00ff95);
                    height: 2px;
                    border: none;
                }
            """)
        else:
            line.setStyleSheet("""
                QFrame {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                              stop:0 #3a8ee6, stop:1 #00ffcc);
                    height: 2px;
                    border: none;
                }
            """)
        layout.addWidget(line)
        
        # Создаем группу для поиска
        search_layout = QHBoxLayout()
        search_layout.setSpacing(10)
        
        search_label = QLabel(translations["find_label"])
        search_label.setFont(QFont("Segoe UI", 11))
        self.search_input = QLineEdit()
        self.search_input.setFont(QFont("Segoe UI", 11))
        self.search_input.setPlaceholderText(translations["enter_search_text"])
        
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        layout.addLayout(search_layout)
        
        # Создаем группу для замены
        replace_layout = QHBoxLayout()
        replace_layout.setSpacing(10)
        
        replace_label = QLabel(translations["replace_label"])
        replace_label.setFont(QFont("Segoe UI", 11))
        self.replace_input = QLineEdit()
        self.replace_input.setFont(QFont("Segoe UI", 11))
        self.replace_input.setPlaceholderText(translations["enter_search_text"])
        
        replace_layout.addWidget(replace_label)
        replace_layout.addWidget(self.replace_input)
        layout.addLayout(replace_layout)
        
        # Используем таймер для предотвращения слишком частых обновлений
        self.search_timer = None
        self.search_input.textChanged.connect(self.on_text_changed)
        
        # Создаем кнопки
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        self.find_next_button = QPushButton(translations["find_next"])
        self.find_next_button.clicked.connect(lambda: self.find_next(move_next=True))
        self.find_next_button.setMinimumWidth(100)
        
        self.replace_button = QPushButton(translations["replace"])
        self.replace_button.clicked.connect(self.replace_current)
        self.replace_button.setMinimumWidth(100)
        
        self.replace_all_button = QPushButton(translations["replace_all"])
        self.replace_all_button.clicked.connect(self.replace_all)
        self.replace_all_button.setMinimumWidth(100)
        
        self.cancel_button = QPushButton(translations["cancel_btn"])
        self.cancel_button.clicked.connect(self.reject)
        self.cancel_button.setMinimumWidth(100)
        
        button_layout.addStretch()
        button_layout.addWidget(self.find_next_button)
        button_layout.addWidget(self.replace_button)
        button_layout.addWidget(self.replace_all_button)
        button_layout.addWidget(self.cancel_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
        
        # Инициализация переменных для поиска
        self.last_search = ""
        self.last_position = 0
        self.is_searching = False
        
        # Сохраняем переводы
        self.translations = translations
    
    def replace_current(self):
        """Заменяет текущее выделенное совпадение"""
        try:
            cursor = self.parent.text_edit.textCursor()
            if cursor.hasSelection():
                selected_text = cursor.selectedText()
                search_text = self.search_input.text()
                
                # Проверяем, что выделенный текст соответствует искомому
                if selected_text == search_text:
                    # Заменяем текст
                    cursor.insertText(self.replace_input.text())
                    self.parent.status_bar.showMessage(self.translations["text_replaced"], 3000)
                    # Ищем следующее совпадение
                    self.find_next(move_next=True)
                else:
                    self.parent.status_bar.showMessage(self.translations["select_text"], 3000)
            else:
                self.parent.status_bar.showMessage(self.translations["nothing_selected"], 3000)
        except Exception as e:
            self.parent.status_bar.showMessage(f"Ошибка при замене: {str(e)}", 3000)
    
    def replace_all(self):
        """Заменяет все совпадения в тексте"""
        try:
            search_text = self.search_input.text()
            replace_text = self.replace_input.text()
            
            if not search_text:
                self.parent.status_bar.showMessage(self.translations["enter_search_text"], 3000)
                return
            
            # Получаем весь текст
            text = self.parent.text_edit.toPlainText()
            
            # Подсчитываем количество замен
            count = text.count(search_text)
            
            if count > 0:
                # Заменяем все вхождения
                new_text = text.replace(search_text, replace_text)
                
                # Обновляем текст в редакторе
                self.parent.text_edit.setPlainText(new_text)
                
                # Показываем сообщение о количестве замен
                self.parent.status_bar.showMessage(
                    self.translations["replacements"].format(count), 3000)
            else:
                self.parent.status_bar.showMessage(
                    self.translations["text_not_found"].format(search_text), 3000)
        
        except Exception as e:
            self.parent.status_bar.showMessage(f"Ошибка при замене: {str(e)}", 3000)
    
    def on_text_changed(self, text):
        """Обработчик изменения текста с задержкой"""
        try:
            # Если таймер уже запущен, останавливаем его
            if self.search_timer is not None:
                self.search_timer.stop()
            
            # Создаем новый таймер с задержкой 300 мс
            self.search_timer = QTimer()
            self.search_timer.setSingleShot(True)
            self.search_timer.timeout.connect(lambda: self.find_next(move_next=False))
            self.search_timer.start(300)
        except Exception as e:
            self.parent.status_bar.showMessage(f"Ошибка при поиске: {str(e)}", 3000)
    
    def find_next(self, move_next=False):
        """Функция поиска текста"""
        try:
            # Защита от рекурсивного вызова
            if self.is_searching:
                return
            self.is_searching = True
            
            search_text = self.search_input.text()
            
            # Если текст поиска пустой, очищаем выделение
            if not search_text:
                cursor = self.parent.text_edit.textCursor()
                cursor.clearSelection()
                self.parent.text_edit.setTextCursor(cursor)
                self.parent.status_bar.clearMessage()
                self.is_searching = False
                return
            
            # Получаем текст из редактора
            text = self.parent.text_edit.toPlainText()
            cursor = self.parent.text_edit.textCursor()
            
            # Определяем начальную позицию поиска
            if search_text != self.last_search:
                # Новый поиск - начинаем с текущей позиции курсора
                self.last_position = cursor.position() if not move_next else 0
                self.last_search = search_text
            elif move_next:
                # Поиск следующего - начинаем с конца текущего выделения
                self.last_position = cursor.selectionEnd()
            
            # Проверяем границы
            if self.last_position < 0:
                self.last_position = 0
            
            # Ищем следующее вхождение
            start_position = self.last_position
            found = False
            
            # Первая попытка поиска с текущей позиции
            position = text.find(search_text, start_position)
            
            # Если не найдено и это явный поиск (кнопка "Найти далее"),
            # пробуем искать сначала файла
            if position == -1 and move_next and start_position > 0:
                position = text.find(search_text, 0)
                if position != -1 and position < start_position:
                    found = True
            else:
                found = position != -1
            
            if found:
                # Выделяем найденный текст
                cursor.setPosition(position)
                cursor.setPosition(position + len(search_text), 
                                 cursor.MoveMode.KeepAnchor)
                self.parent.text_edit.setTextCursor(cursor)
                self.last_position = position + 1
                self.parent.status_bar.showMessage(
                    self.translations["text_found"].format(search_text), 3000)
            else:
                self.parent.status_bar.showMessage(
                    self.translations["text_not_found"].format(search_text), 3000)
        
        except Exception as e:
            self.parent.status_bar.showMessage(f"Ошибка при поиске: {str(e)}", 3000)
        finally:
            self.is_searching = False

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        lang_code = LANGUAGES.get(self.parent.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        self.setWindowTitle(translations["settings_title"])
        self.setFixedSize(500, 300)
        
        # Устанавливаем отступы
        self.setContentsMargins(20, 20, 20, 20)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # Добавляем заголовок
        title = QLabel(translations["settings_app"])
        title.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Добавляем разделитель с градиентом
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        if parent.current_theme == "light":
            line.setStyleSheet("""
                QFrame {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                              stop:0 #007bff, stop:1 #00ff95);
                    height: 2px;
                    border: none;
                }
            """)
        else:
            line.setStyleSheet("""
                QFrame {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                              stop:0 #3a8ee6, stop:1 #00ffcc);
                    height: 2px;
                    border: none;
                }
            """)
        layout.addWidget(line)
        
        # Выбор языка
        language_layout = QHBoxLayout()
        language_layout.setSpacing(10)
        
        language_label = QLabel(translations["lang_interface"])
        language_label.setFont(QFont("Segoe UI", 11))
        self.language_combo = QComboBox()
        self.language_combo.setFont(QFont("Segoe UI", 11))
        
        # Добавляем доступные языки
        for lang_name in LANGUAGES.keys():
            self.language_combo.addItem(lang_name)
        
        # Устанавливаем текущий язык
        current_lang = self.parent.settings.value("language", "Русский")
        index = self.language_combo.findText(current_lang)
        if index >= 0:
            self.language_combo.setCurrentIndex(index)
        
        language_layout.addWidget(language_label)
        language_layout.addWidget(self.language_combo)
        language_layout.addStretch()
        
        layout.addLayout(language_layout)
        layout.addStretch()
        
        # Кнопки
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        cancel_button = QPushButton(translations["cancel_btn"])
        cancel_button.clicked.connect(self.reject)
        cancel_button.setMinimumWidth(100)
        
        save_button = QPushButton(translations["save_btn"])
        save_button.clicked.connect(self.save_settings)
        save_button.setMinimumWidth(100)
        
        button_layout.addStretch()
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(save_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def save_settings(self):
        # Сохраняем выбранный язык
        selected_language = self.language_combo.currentText()
        old_language = self.parent.settings.value("language", "Русский")
        
        # Обновляем настройки только если язык изменился
        if selected_language != old_language:
            self.parent.settings.setValue("language", selected_language)
            self.parent.current_language = selected_language
            
            # Получаем переводы для сообщения
            lang_code = LANGUAGES.get(selected_language, "ru")
            translations = TRANSLATIONS[lang_code]
            
            # Показываем сообщение о необходимости перезапуска
            QMessageBox.information(
                self,
                translations["settings_saved"],
                translations["restart_needed"]
            )
            
            # Обновляем интерфейс
            self.parent.apply_language()
        
        self.accept()

class LineNumberArea(QWidget):
    def __init__(self, editor, parent):
        super().__init__(editor)
        self.editor = editor
        self.parent = parent
        self.setFixedWidth(30)  # Фиксированная ширина для номеров строк

    def sizeHint(self):
        return QSize(self.parent.line_number_area_width(), 0)

    def paintEvent(self, event):
        self.parent.lineNumberAreaPaintEvent(event)

class BlurDialog(QDialog):
    def __init__(self, parent=None, current_blur=0, translations=None):
        super().__init__(parent)
        
        if translations is None:
            translations = TRANSLATIONS["ru"]
        
        self.setWindowTitle(translations["blur_effect"])
        self.setFixedSize(400, 250)
        
        self.setContentsMargins(20, 20, 20, 20)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        title = QLabel(translations["blur_effect"])
        title.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        if parent and parent.current_theme == "light":
            line.setStyleSheet("""
                QFrame {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                              stop:0 #007bff, stop:1 #00ff95);
                    height: 2px;
                    border: none;
                }
            """)
        else:
            line.setStyleSheet("""
                QFrame {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                              stop:0 #3a8ee6, stop:1 #00ffcc);
                    height: 2px;
                    border: none;
                }
            """)
        layout.addWidget(line)
        
        self.label = QLabel(translations["blur_radius"] + f": {current_blur}")
        self.label.setFont(QFont("Segoe UI", 12))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 20)
        self.slider.setValue(current_blur)
        self.slider.valueChanged.connect(self.update_blur)
        layout.addWidget(self.slider)
        
        self.enable_checkbox = QCheckBox(translations["blur_enabled"])
        self.enable_checkbox.setChecked(current_blur > 0)
        layout.addWidget(self.enable_checkbox)
        
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        cancel_button = QPushButton(translations["cancel_btn"])
        cancel_button.clicked.connect(self.reject)
        cancel_button.setMinimumWidth(100)
        
        apply_button = QPushButton(translations["save_btn"])
        apply_button.clicked.connect(self.accept)
        apply_button.setMinimumWidth(100)
        
        button_layout.addStretch()
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(apply_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
        
        self.translations = translations
    
    def update_blur(self, value):
        self.label.setText(self.translations["blur_radius"] + f": {value}")

class BackgroundOpacityDialog(QDialog):
    def __init__(self, parent, current_opacity, translations):
        super().__init__(parent)
        self.translations = translations
        self.current_opacity = current_opacity
        self.setWindowTitle(translations["background_opacity"])
        self.setMinimumWidth(400)
        self.setMinimumHeight(300)
        
        layout = QVBoxLayout()
        
        # Область предпросмотра
        preview_label = QLabel(translations["preview"])
        self.preview_text = QTextEdit()
        self.preview_text.setReadOnly(True)
        self.preview_text.setMinimumHeight(100)
        self.preview_text.setStyleSheet("""
            QTextEdit {
                background-color: #2b2b2b;
                color: #ffffff;
                border: 1px solid #3f3f3f;
                border-radius: 4px;
                padding: 5px;
            }
        """)
        self.preview_text.setText("Пример текста\nдля предпросмотра\nпрозрачности фона")
        
        # Слайдер прозрачности
        slider_layout = QHBoxLayout()
        self.opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.opacity_slider.setMinimum(0)
        self.opacity_slider.setMaximum(100)
        self.opacity_slider.setValue(current_opacity)
        self.opacity_label = QLabel(f"{current_opacity}%")
        
        slider_layout.addWidget(self.opacity_slider)
        slider_layout.addWidget(self.opacity_label)
        
        # Чекбокс включения/выключения фона
        self.enable_checkbox = QCheckBox(translations["enable_background"])
        self.enable_checkbox.setChecked(current_opacity > 0)
        self.enable_checkbox.stateChanged.connect(self.toggle_background)
        
        # Кнопки
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Cancel | 
            QDialogButtonBox.StandardButton.Ok
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        
        # Добавляем все элементы в layout
        layout.addWidget(preview_label)
        layout.addWidget(self.preview_text)
        layout.addLayout(slider_layout)
        layout.addWidget(self.enable_checkbox)
        layout.addWidget(button_box)
        
        self.setLayout(layout)
        
        # Подключаем сигналы
        self.opacity_slider.valueChanged.connect(self.update_preview)
        self.update_preview(current_opacity)
    
    def toggle_background(self, state):
        """Обработчик изменения состояния чекбокса"""
        if state == Qt.CheckState.Checked.value:
            self.opacity_slider.setValue(100)
        else:
            self.opacity_slider.setValue(0)
        self.update_preview(self.opacity_slider.value())
    
    def update_preview(self, value):
        """Обновление предпросмотра при изменении прозрачности"""
        self.opacity_label.setText(f"{value}%")
        if value == 0:
            self.preview_text.setStyleSheet("""
                QTextEdit {
                    background-color: #2b2b2b;
                    color: #ffffff;
                    border: 1px solid #3f3f3f;
                    border-radius: 4px;
                    padding: 5px;
                }
            """)
        else:
            self.preview_text.setStyleSheet(f"""
                QTextEdit {{
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                        stop:0 rgba(43, 43, 43, {value/100}),
                        stop:1 rgba(43, 43, 43, {value/100}));
                    color: #ffffff;
                    border: 1px solid #3f3f3f;
                    border-radius: 4px;
                    padding: 5px;
                }}
            """)

class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = QSettings("Zotepad", "Settings")
        self.setWindowTitle("Zotepad")
        self.setGeometry(100, 100, 800, 600)
        self.current_file = None
        
        # Включаем поддержку перетаскивания файлов
        self.setAcceptDrops(True)
        
        # Загружаем логотип для окна "О программе"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.logo_path = os.path.join(script_dir, "logo.png")
        self.logo_task_path = os.path.join(script_dir, "logo_task.png")
        self.down_arrow_path = os.path.join(script_dir, "down_arrow.png")
        self.down_arrow_white_path = os.path.join(script_dir, "down_arrow_white.png")
        
        # Устанавливаем иконку окна
        if os.path.exists(self.logo_task_path):
            self.setWindowIcon(QIcon(self.logo_task_path))
        
        # Проверяем наличие файлов иконок
        if not os.path.exists(self.logo_path):
            self.create_default_logo()
        if not os.path.exists(self.down_arrow_path):
            self.create_down_arrow_icons()
        
        # Список доступных кодировок
        self.encodings = [
            'UTF-8',
            'Windows-1251',
            'KOI8-R',
            'ISO-8859-5',
            'ASCII',
            'CP866'
        ]
        
        # Загружаем сохранённые настройки
        self.current_theme = self.settings.value("theme", "light")
        self.opacity = float(self.settings.value("opacity", 1.0))
        self.current_encoding = self.settings.value("encoding", "UTF-8")
        self.current_language = self.settings.value("language", "Русский")
        
        # Добавляем настройки размытия
        self.blur_radius = int(self.settings.value("blur_radius", 0))
        self.blur_enabled = self.settings.value("blur_enabled", "false").lower() == "true"
        
        # Добавляем настройки фонового изображения
        self.background_image = None
        self.background_opacity = float(self.settings.value("background_opacity", 1.0))
        
        # Применяем размытие если оно включено
        if self.blur_enabled and self.blur_radius > 0:
            self.apply_blur()
        
        # Создаем текстовый редактор с улучшенным шрифтом
        self.text_edit = QTextEdit(self)
        self.text_edit.setFont(QFont("Segoe UI", 10))
        
        # Создаем область для номеров строк
        self.line_number_area = LineNumberArea(self.text_edit, self)
        
        # Подключаем сигналы для обновления номеров строк
        self.text_edit.textChanged.connect(self.update_line_number_area_width)
        self.text_edit.verticalScrollBar().valueChanged.connect(self.update_line_number_area)
        self.text_edit.textChanged.connect(self.update_line_number_area)
        
        # Устанавливаем отступы для текста
        self.text_edit.setViewportMargins(self.line_number_area_width(), 0, 0, 0)
        
        self.setCentralWidget(self.text_edit)
        
        # Создаем меню
        self.create_menu()
        
        # Создаем статусбар с информацией о кодировке
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.encoding_label = QLabel(f"Кодировка: {self.current_encoding}")
        self.status_bar.addPermanentWidget(self.encoding_label)
        
        # Добавляем надпись "Made by EzzTEMP"
        self.made_by_label = QLabel("Made by EzzTEMP")
        self.made_by_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-style: italic;
                padding-right: 10px;
            }
        """)
        self.status_bar.addPermanentWidget(self.made_by_label)
        
        self.status_bar.showMessage("Готов к работе")
        
        # Применяем сохранённые настройки
        self.apply_theme()
        self.setWindowOpacity(self.opacity)
        
        # Применяем сохраненное фоновое изображение если оно есть
        saved_background = self.settings.value("background_image")
        if saved_background and os.path.exists(saved_background):
            self.background_image = saved_background
            self.apply_background_image()

        # Добавляем настройки цветов
        self.background_color = self.settings.value("background_color", "#ffffff")
        self.cursor_color = self.settings.value("cursor_color", "#000000")

        # Добавляем настройки курсора
        self.cursor_width = int(self.settings.value("cursor_width", 2))
        self.cursor_style = self.settings.value("cursor_style", "solid")
        self.cursor_blink = self.settings.value("cursor_blink", "true").lower() == "true"

    def line_number_area_width(self):
        """Вычисляет ширину области номеров строк"""
        digits = 1
        max_num = max(1, self.text_edit.document().blockCount())
        while max_num >= 10:
            max_num //= 10
            digits += 1
        space = 10 + self.text_edit.fontMetrics().horizontalAdvance('9') * digits
        return space

    def update_line_number_area_width(self):
        """Обновляет ширину области номеров строк"""
        width = self.line_number_area_width()
        self.text_edit.setViewportMargins(width, 0, 0, 0)
        self.line_number_area.setFixedWidth(width)

    def update_line_number_area(self, value=None):
        """Обновляет область номеров строк при прокрутке или изменении текста"""
        self.line_number_area.update()

    def lineNumberAreaPaintEvent(self, event):
        """Отрисовывает номера строк"""
        painter = QPainter(self.line_number_area)
        
        # Заполняем фон области номеров
        if self.current_theme == "light":
            painter.fillRect(event.rect(), QColor("#f0f0f0"))
        else:
            painter.fillRect(event.rect(), QColor("#2d2d30"))

        # Получаем первый видимый блок текста
        block = self.text_edit.firstVisibleBlock()
        block_number = block.blockNumber()
        
        # Получаем координаты первого блока
        top = self.text_edit.blockBoundingGeometry(block).translated(
            self.text_edit.contentOffset()).top()
        bottom = top + self.text_edit.blockBoundingRect(block).height()

        # Устанавливаем шрифт и цвет для номеров
        font = self.text_edit.font()
        font.setPointSize(9)  # Немного меньший размер шрифта для номеров
        painter.setFont(font)
        
        if self.current_theme == "light":
            painter.setPen(QColor("#666666"))
        else:
            painter.setPen(QColor("#a0a0a0"))

        # Отрисовываем номера строк
        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.drawText(0, int(top), self.line_number_area.width() - 5,
                               self.text_edit.fontMetrics().height(),
                               Qt.AlignmentFlag.AlignRight, number)
            
            block = block.next()
            top = bottom
            bottom = top + self.text_edit.blockBoundingRect(block).height()
            block_number += 1

    def create_default_logo(self):
        """Создает стандартный логотип, если файл logo.png отсутствует"""
        try:
            # Создаем изображение 64x64 пикселя
            img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            
            # Рисуем круг
            draw.ellipse([2, 2, 62, 62], fill='#007bff')
            
            # Добавляем букву "Z"
            font_size = 40
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except:
                font = ImageFont.load_default()
            
            # Размещаем букву "Z" в центре
            text = "Z"
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            
            x = (64 - text_width) // 2
            y = (64 - text_height) // 2
            
            # Рисуем текст
            draw.text((x, y), text, fill='white', font=font)
            
            # Сохраняем изображение
            img.save(self.logo_path, 'PNG')
            
        except Exception as e:
            print(f"Ошибка при создании логотипа: {e}")

    def create_down_arrow_icons(self):
        """Создает иконки для выпадающих списков"""
        try:
            # Создаем темную иконку
            dark_img = Image.new('RGBA', (12, 12), (0, 0, 0, 0))
            dark_draw = ImageDraw.Draw(dark_img)
            dark_draw.polygon([(2, 4), (10, 4), (6, 10)], fill='#2c3e50')
            dark_img.save(self.down_arrow_path, 'PNG')
            
            # Создаем светлую иконку
            light_img = Image.new('RGBA', (12, 12), (0, 0, 0, 0))
            light_draw = ImageDraw.Draw(light_img)
            light_draw.polygon([(2, 4), (10, 4), (6, 10)], fill='#e1e1e1')
            light_img.save(self.down_arrow_white_path, 'PNG')
            
        except Exception as e:
            print(f"Ошибка при создании иконок выпадающих списков: {e}")

    def create_menu(self):
        # Получаем код языка из названия
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        # Меню "Файл"
        file_menu = self.menuBar().addMenu(translations["file_menu"])

        new_action = QAction(translations["new"], self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        open_action = QAction(translations["open"], self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction(translations["save"], self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        save_as_action = QAction(translations["save_as"], self)
        save_as_action.triggered.connect(self.save_file_as)
        file_menu.addAction(save_as_action)

        file_menu.addSeparator()
        exit_action = QAction(translations["exit"], self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Меню "Правка"
        edit_menu = self.menuBar().addMenu(translations["edit_menu"])

        undo_action = QAction(translations["undo"], self)
        undo_action.setShortcut("Ctrl+Z")
        undo_action.triggered.connect(self.text_edit.undo)
        edit_menu.addAction(undo_action)

        redo_action = QAction(translations["redo"], self)
        redo_action.setShortcut("Ctrl+Y")
        redo_action.triggered.connect(self.text_edit.redo)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()
        cut_action = QAction(translations["cut"], self)
        cut_action.setShortcut("Ctrl+X")
        cut_action.triggered.connect(self.text_edit.cut)
        edit_menu.addAction(cut_action)

        copy_action = QAction(translations["copy"], self)
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(self.text_edit.copy)
        edit_menu.addAction(copy_action)

        paste_action = QAction(translations["paste"], self)
        paste_action.setShortcut("Ctrl+V")
        paste_action.triggered.connect(self.text_edit.paste)
        edit_menu.addAction(paste_action)

        delete_action = QAction(translations["delete"], self)
        delete_action.setShortcut("Del")
        delete_action.triggered.connect(self.delete_text)
        edit_menu.addAction(delete_action)

        edit_menu.addSeparator()
        
        # Добавляем действие поиска
        find_action = QAction(translations["find"], self)
        find_action.setShortcut("Ctrl+F")
        find_action.triggered.connect(self.show_find_dialog)
        edit_menu.addAction(find_action)
        
        edit_menu.addSeparator()
        select_all_action = QAction(translations["select_all"], self)
        select_all_action.setShortcut("Ctrl+A")
        select_all_action.triggered.connect(self.text_edit.selectAll)
        edit_menu.addAction(select_all_action)

        # Меню "Формат"
        format_menu = self.menuBar().addMenu(translations["format_menu"])

        font_action = QAction(translations["font"], self)
        font_action.triggered.connect(self.change_font)
        format_menu.addAction(font_action)

        wrap_action = QAction(translations["word_wrap"], self, checkable=True)
        wrap_action.setChecked(True)  # По умолчанию включено
        wrap_action.triggered.connect(self.toggle_word_wrap)
        format_menu.addAction(wrap_action)

        # Меню "Кодировка"
        encoding_menu = self.menuBar().addMenu(translations["encoding_menu"])
        
        # Создаем группу действий для кодировок
        encoding_group = QActionGroup(self)
        
        # Добавляем действия для каждой кодировки
        for encoding in self.encodings:
            action = QAction(encoding, self, checkable=True)
            action.setChecked(encoding == self.current_encoding)
            action.triggered.connect(lambda checked, enc=encoding: self.set_encoding(enc))
            encoding_menu.addAction(action)
            encoding_group.addAction(action)
        
        # Делаем группу эксклюзивной (можно выбрать только одну кодировку)
        encoding_group.setExclusive(True)

        # Меню "Вид"
        view_menu = self.menuBar().addMenu(translations["view_menu"])

        # Подменю "Тема"
        theme_menu = view_menu.addMenu(translations["theme_menu"])

        light_theme = QAction(translations["light_theme"], self, checkable=True)
        light_theme.setChecked(self.current_theme == "light")
        light_theme.triggered.connect(lambda: self.set_theme("light"))
        theme_menu.addAction(light_theme)

        dark_theme = QAction(translations["dark_theme"], self, checkable=True)
        dark_theme.setChecked(self.current_theme == "dark")
        dark_theme.triggered.connect(lambda: self.set_theme("dark"))
        theme_menu.addAction(dark_theme)

        blue_theme = QAction(translations["blue_theme"], self, checkable=True)
        blue_theme.setChecked(self.current_theme == "blue")
        blue_theme.triggered.connect(lambda: self.set_theme("blue"))
        theme_menu.addAction(blue_theme)

        green_theme = QAction(translations["green_theme"], self, checkable=True)
        green_theme.setChecked(self.current_theme == "green")
        green_theme.triggered.connect(lambda: self.set_theme("green"))
        theme_menu.addAction(green_theme)

        # Группа действий для тем (только одна активна)
        theme_group = QActionGroup(self)
        theme_group.addAction(light_theme)
        theme_group.addAction(dark_theme)
        theme_group.addAction(blue_theme)
        theme_group.addAction(green_theme)
        theme_group.setExclusive(True)

        # Прозрачность
        opacity_action = QAction(translations["opacity"], self)
        opacity_action.triggered.connect(self.set_opacity)
        view_menu.addAction(opacity_action)

        # Меню "Справка"
        help_menu = self.menuBar().addMenu(translations["help_menu"])
        
        # Добавляем пункт "Настройки"
        settings_action = QAction(translations["settings"], self)
        settings_action.triggered.connect(self.show_settings)
        help_menu.addAction(settings_action)
        
        # Добавляем пункт "Социальные сети"
        social_networks_action = QAction(translations["social_networks"], self)
        social_networks_action.triggered.connect(self.show_social_networks)
        help_menu.addAction(social_networks_action)
        
        about_action = QAction(translations["about"], self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

        # Добавляем пункт меню для размытия
        blur_action = QAction(translations["blur_effect"], self)
        blur_action.triggered.connect(self.set_blur)
        view_menu.addAction(blur_action)
        
        # Добавляем пункты меню для фонового изображения в меню "Вид"
        view_menu.addSeparator()
        
        # Добавляем пункт для выбора фонового изображения
        background_image_action = QAction(translations["background_image"], self)
        background_image_action.triggered.connect(self.set_background_image)
        view_menu.addAction(background_image_action)
        
        # Добавляем пункт для настройки прозрачности фона
        background_opacity_action = QAction(translations["background_opacity"], self)
        background_opacity_action.triggered.connect(self.set_background_opacity)
        view_menu.addAction(background_opacity_action)

        # Добавляем пункт меню для настройки цветов
        customize_colors_action = QAction(translations["customize_colors"], self)
        customize_colors_action.triggered.connect(self.customize_colors)
        view_menu.addAction(customize_colors_action)

        # Добавляем пункт меню для настройки курсора
        customize_cursor_action = QAction(translations["customize_cursor"], self)
        customize_cursor_action.triggered.connect(self.customize_cursor)
        view_menu.addAction(customize_cursor_action)

    def set_theme(self, theme_name):
        self.current_theme = theme_name
        self.apply_theme()
        # Сохраняем выбранную тему
        self.settings.setValue("theme", theme_name)
        
        # Получаем текущие переводы
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        # Обновляем статусбар с переводом
        theme_text = translations[f"{theme_name}_theme"]
        self.status_bar.showMessage(translations["theme_changed"].format(theme_text), 3000)

    def apply_theme(self):
        if self.current_theme == "dark":
            style = DARK_STYLE
        elif self.current_theme == "blue":
            style = BLUE_STYLE
        elif self.current_theme == "green":
            style = GREEN_STYLE
        else:
            style = LIGHT_STYLE
        
        QApplication.instance().setStyleSheet(style)

    def set_opacity(self):
        # Получаем текущие переводы
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        dialog = OpacityDialog(self, self.opacity, translations)
        if dialog.exec():
            # Сохраняем новое значение прозрачности
            self.settings.setValue("opacity", self.opacity)
            self.status_bar.showMessage(translations["opacity_set"].format(int(self.opacity * 100)), 3000)

    def set_encoding(self, encoding):
        """Устанавливает новую кодировку и перезагружает файл если он открыт"""
        try:
            # Получаем текущие переводы
            lang_code = LANGUAGES.get(self.current_language, "ru")
            translations = TRANSLATIONS[lang_code]
            
            self.current_encoding = encoding
            self.encoding_label.setText(translations["encoding_status"].format(encoding))
            self.settings.setValue("encoding", encoding)
            
            # Если файл открыт, перезагружаем его с новой кодировкой
            if self.current_file and os.path.exists(self.current_file):
                self.reload_file_with_encoding(self.current_file, encoding)
            
            self.status_bar.showMessage(translations["encoding_changed"].format(encoding), 3000)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при смене кодировки: {str(e)}")

    def reload_file_with_encoding(self, file_path, encoding):
        """Перезагружает файл с указанной кодировкой"""
        try:
            # Получаем текущие переводы
            lang_code = LANGUAGES.get(self.current_language, "ru")
            translations = TRANSLATIONS[lang_code]
            
            is_read_only = self.text_edit.isReadOnly() # Сохраняем состояние read-only
            with open(file_path, 'r', encoding=encoding) as file:
                self.text_edit.setPlainText(file.read())
            self.current_file = file_path # Убедимся, что current_file установлен
            self.setWindowTitle(f"Zotepad - {os.path.basename(file_path)}")
            self.encoding_label.setText(translations["encoding_status"].format(encoding)) # Обновляем label
            self.text_edit.setReadOnly(is_read_only) # Восстанавливаем read-only
        except UnicodeDecodeError:
            QMessageBox.warning(
                self,
                "Ошибка кодировки",
                translations["encoding_error"].format(os.path.basename(file_path), encoding)
            )
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при открытии файла: {str(e)}")

    def new_file(self):
        # Получаем текущие переводы
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        if self.text_edit.document().isModified():
            reply = QMessageBox.question(
                self, "Zotepad", translations["save_changes"],
                QMessageBox.StandardButton.Save |
                QMessageBox.StandardButton.Discard |
                QMessageBox.StandardButton.Cancel
            )
            if reply == QMessageBox.StandardButton.Save:
                 if not self.save_file(): # Проверяем результат сохранения
                    return # Не создаем новый файл, если сохранение отменено
            elif reply == QMessageBox.StandardButton.Cancel:
                return

        self.text_edit.clear()
        self.current_file = None
        self.setWindowTitle("Zotepad")
        self.text_edit.setReadOnly(False) # Убедимся, что можно редактировать
        self.status_bar.showMessage(translations["new_document"], 3000)

    def open_file(self):
        # Получаем текущие переводы
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        # Проверяем на сохранение изменений перед открытием нового файла
        if self.text_edit.document().isModified():
            reply = QMessageBox.question(
                self,
                "Zotepad",
                translations["save_changes_question"],
                QMessageBox.StandardButton.Save |
                QMessageBox.StandardButton.Discard |
                QMessageBox.StandardButton.Cancel
            )
            if reply == QMessageBox.StandardButton.Save:
                if not self.save_file(): # Если сохранение не удалось или отменено
                    return # Не открываем новый файл
            elif reply == QMessageBox.StandardButton.Cancel:
                return # Не открываем новый файл

        file_path, _ = QFileDialog.getOpenFileName(
            self, translations["open"], "", "Текстовые файлы (*.txt);;Все файлы (*)"
        )
        if file_path:
            self._load_file(file_path, self.current_encoding)

    def _load_file(self, file_path, encoding):
        """Вспомогательный метод для загрузки файла с обработкой кодировки."""
        try:
            # Получаем текущие переводы
            lang_code = LANGUAGES.get(self.current_language, "ru")
            translations = TRANSLATIONS[lang_code]
            
            with open(file_path, "r", encoding=encoding) as file:
                self.text_edit.setPlainText(file.read())
            self.current_file = file_path
            self.setWindowTitle(f"Zotepad - {os.path.basename(file_path)}")
            self.current_encoding = encoding # Устанавливаем текущую кодировку
            self.encoding_label.setText(translations["encoding_status"].format(encoding))
            self.text_edit.setReadOnly(False) # По умолчанию редактируемый
            self.text_edit.document().setModified(False) # Сбрасываем флаг изменения
            self.status_bar.showMessage(translations["file_opened"].format(file_path), 3000)
            return True
        except UnicodeDecodeError:
            # Если произошла ошибка кодировки, предлагаем выбрать другую
            encoding, ok = QInputDialog.getItem(
                self,
                translations["choose_encoding"],
                translations["encoding_error_message"].format(os.path.basename(file_path), encoding),
                self.encodings,
                self.encodings.index(self.current_encoding) if self.current_encoding in self.encodings else 0,
                False
            )
            if ok and encoding:
                # Рекурсивно вызываем _load_file с новой кодировкой
                return self._load_file(file_path, encoding)
            else:
                # Если пользователь отменил выбор кодировки
                self.status_bar.showMessage(translations["opening_canceled"], 3000)
                return False
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть файл: {e}")
            return False

    def save_file(self):
        """Сохраняет текущий файл. Возвращает True при успехе, False при ошибке/отмене."""
        # Получаем текущие переводы
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        if self.current_file:
            try:
                with open(self.current_file, "w", encoding=self.current_encoding) as file:
                    file.write(self.text_edit.toPlainText())
                self.text_edit.document().setModified(False)
                self.status_bar.showMessage(translations["file_saved"].format(self.current_file), 3000)
                return True # Успех
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {e}")
                return False # Ошибка
        else:
            return self.save_file_as() # Результат зависит от save_file_as

    def save_file_as(self):
        """Сохраняет файл с новым именем. Возвращает True при успехе, False при ошибке/отмене."""
        # Получаем текущие переводы
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        # Используем текущий каталог файла или домашний каталог по умолчанию
        default_dir = os.path.dirname(self.current_file) if self.current_file else os.path.expanduser("~")
        file_path, _ = QFileDialog.getSaveFileName(
            self, translations["save_as"], default_dir, "Текстовые файлы (*.txt);;Все файлы (*)"
        )
        if file_path:
            try:
                with open(file_path, "w", encoding=self.current_encoding) as file:
                    file.write(self.text_edit.toPlainText())
                self.current_file = file_path
                self.setWindowTitle(f"Zotepad - {os.path.basename(file_path)}") # Используем basename
                self.text_edit.document().setModified(False)
                self.status_bar.showMessage(translations["file_saved_as"].format(file_path), 3000)
                return True # Успех
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {e}")
                return False # Ошибка
        else:
             return False # Отмена

    def delete_text(self):
        cursor = self.text_edit.textCursor()
        cursor.removeSelectedText()

    def change_font(self):
        # Получаем текущие переводы
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        font, ok = QFontDialog.getFont(self.text_edit.font(), self)
        if ok:
            self.text_edit.setFont(font)
            self.status_bar.showMessage(translations["font_changed"], 3000)

    def toggle_word_wrap(self, checked):
        # Получаем текущие переводы
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        self.text_edit.setLineWrapMode(
            QTextEdit.LineWrapMode.WidgetWidth if checked
            else QTextEdit.LineWrapMode.NoWrap
        )
        self.status_bar.showMessage(
            translations["word_wrap_on"] if checked else translations["word_wrap_off"],
            3000
        )

    def show_about(self):
        try:
            # Получаем текущие переводы
            lang_code = LANGUAGES.get(self.current_language, "ru")
            translations = TRANSLATIONS[lang_code]
            
            # Создаем диалог
            about_dialog = QDialog(self)
            about_dialog.setWindowTitle(translations["about_title"])
            about_dialog.setFixedSize(400, 350)  # Увеличиваем высоту
            
            # Создаем layout
            layout = QVBoxLayout()
            
            # Создаем виджет для логотипа и заголовка
            header_widget = QWidget()
            header_layout = QHBoxLayout()
            
            # Добавляем логотип
            logo_label = QLabel()
            logo_pixmap = QPixmap(self.logo_path)
            # Масштабируем логотип до 64x64
            logo_pixmap = logo_pixmap.scaled(64, 64, Qt.AspectRatioMode.KeepAspectRatio, 
                                           Qt.TransformationMode.SmoothTransformation)
            logo_label.setPixmap(logo_pixmap)
            header_layout.addWidget(logo_label)
            
            # Добавляем заголовок с градиентом
            title_label = QLabel("Zotepad")
            if self.current_theme == "light":
                gradient_style = """
                    font-size: 24px;
                    font-weight: bold;
                    background: -webkit-linear-gradient(left, #007bff, #00ff95);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    padding: 10px;
                """
            else:
                gradient_style = """
                    font-size: 24px;
                    font-weight: bold;
                    background: -webkit-linear-gradient(left, #3a8ee6, #00ffcc);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    padding: 10px;
                """
            title_label.setStyleSheet(gradient_style)
            header_layout.addWidget(title_label)
            
            # Центрируем содержимое header_layout
            header_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            header_widget.setLayout(header_layout)
            layout.addWidget(header_widget)
            
            # Добавляем разделитель с градиентом
            line = QFrame()
            line.setFrameShape(QFrame.Shape.HLine)
            line.setFrameShadow(QFrame.Shadow.Sunken)
            if self.current_theme == "light":
                line.setStyleSheet("""
                    QFrame {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                                  stop:0 #007bff, stop:1 #00ff95);
                        height: 2px;
                        border: none;
                    }
                """)
            else:
                line.setStyleSheet("""
                    QFrame {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:0, 
                                                  stop:0 #3a8ee6, stop:1 #00ffcc);
                        height: 2px;
                        border: none;
                    }
                """)
            layout.addWidget(line)
            
            # Добавляем информацию
            info_label = QLabel()
            info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            info_label.setTextFormat(Qt.TextFormat.RichText)
            info_label.setOpenExternalLinks(True)  # Разрешаем открытие внешних ссылок
            
            # Получаем название темы для отображения
            theme_text = translations["light_theme"] if self.current_theme == "light" else translations["dark_theme"]
            
            info_text = f"""
                <p>Продолжение уже начетого...</p>
                <p><b>{translations["version"]}</b> 2.1</p>
                <p><b>{translations["theme"]}</b> {theme_text}</p>
                <p><b>{translations["opacity_label"]}</b> {int(self.opacity * 100)}%</p>
                <p><b>{translations["encoding_label"]}</b> {self.current_encoding}</p>
                <p><b>{translations["developers"]}</b> <a href="https://github.com/mansar1337">mansar1337</a></p>
                <hr>
                <p>© 2025 Разработано с помощью Python и PyQt6</p>
            """
            info_label.setText(info_text)
            layout.addWidget(info_label)
            
            # Добавляем кнопку OK
            ok_button = QPushButton("OK")
            ok_button.clicked.connect(about_dialog.accept)
            ok_button.setStyleSheet("""
                QPushButton {
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-weight: bold;
                }
            """)
            layout.addWidget(ok_button, alignment=Qt.AlignmentFlag.AlignCenter)
            
            about_dialog.setLayout(layout)
            about_dialog.exec()
        except Exception as e:
            print(f"Ошибка при отображении информации о программе: {e}")

    def show_find_dialog(self):
        dialog = FindDialog(self)
        dialog.exec()

    def show_settings(self):
        """Показывает диалог настроек приложения"""
        dialog = SettingsDialog(self)
        dialog.exec()

    def closeEvent(self, event):
        if self.text_edit.document().isModified():
            reply = QMessageBox.question(
                self, "Zotepad", "Сохранить изменения?",
                QMessageBox.StandardButton.Save |
                QMessageBox.StandardButton.Discard |
                QMessageBox.StandardButton.Cancel
            )
            if reply == QMessageBox.StandardButton.Save:
                if self.save_file():
                    event.accept() # Закрываем, если сохранено
                else:
                    event.ignore() # Не закрываем, если сохранение отменено/не удалось
            elif reply == QMessageBox.StandardButton.Discard:
                event.accept() # Закрываем без сохранения
            else:
                event.ignore() # Отмена закрытия
        else:
            event.accept() # Закрываем, если нет изменений

    def dragEnterEvent(self, event):
        """Обработка начала перетаскивания файла"""
        mime_data = event.mimeData()
        # Принимаем только URL'ы с локальными файлами
        if mime_data.hasUrls():
            urls = mime_data.urls()
            if urls and urls[0].isLocalFile():
                event.accept()
                event.setDropAction(Qt.DropAction.CopyAction)
                return # Выходим, если нашли подходящий URL
        # Если нет URL или URL не локальный, игнорируем
        event.ignore()

    def dragMoveEvent(self, event):
        """Обработка перемещения при перетаскивании"""
        # Аналогично dragEnterEvent, проверяем допустимость
        mime_data = event.mimeData()
        if mime_data.hasUrls():
            urls = mime_data.urls()
            if urls and urls[0].isLocalFile():
                event.accept()
                return
        event.ignore()

    def dropEvent(self, event):
        """Обработка броска файла в окно"""
        try:
            mime_data = event.mimeData()
            file_path = None

            if mime_data.hasUrls():
                urls = mime_data.urls()
                if urls:
                    file_url = urls[0]
                    # Убедимся, что это локальный файл
                    if file_url.isLocalFile():
                        file_path = file_url.toLocalFile()

            if not file_path:
                self.status_bar.showMessage("Ошибка: Перетаскиваемый объект не является локальным файлом", 3000)
                event.ignore()
                return

            # Нормализуем путь к файлу (на всякий случай)
            try:
                file_path = os.path.normpath(file_path)
            except Exception as norm_err:
                 QMessageBox.warning(self, "Ошибка", f"Не удалось нормализовать путь: {file_path}\n{norm_err}")
                 event.ignore()
                 return

            # Проверяем существование файла
            if not os.path.exists(file_path):
                QMessageBox.warning(self, "Ошибка", f"Файл не найден: {file_path}")
                event.ignore()
                return

            # Проверяем расширение файла
            is_bat = file_path.lower().endswith('.bat')
            read_only_mode = False

            if is_bat:
                # Показываем предупреждение для .bat файлов
                reply = QMessageBox.warning(
                    self,
                    "Внимание - Исполняемый файл",
                    f"Вы пытаетесь открыть исполняемый файл {os.path.basename(file_path)}.\n\n"
                    "Такие файлы могут содержать потенциально опасный код.\n"
                    "Вы хотите просмотреть его содержимое в режиме только для чтения?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No
                )

                if reply == QMessageBox.StandardButton.No:
                    event.ignore()
                    return
                read_only_mode = True
            else:
                 # Для обычных файлов проверяем на сохранение изменений
                if self.text_edit.document().isModified():
                    reply = QMessageBox.question(
                        self,
                        "Zotepad",
                        "Сохранить изменения в текущем файле?",
                        QMessageBox.StandardButton.Save |
                        QMessageBox.StandardButton.Discard |
                        QMessageBox.StandardButton.Cancel
                    )

                    if reply == QMessageBox.StandardButton.Save:
                        if not self.save_file(): # Если сохранение не удалось или отменено
                             event.ignore()
                             return
                    elif reply == QMessageBox.StandardButton.Cancel:
                        event.ignore()
                        return
                 # Режим редактирования для обычных файлов
                read_only_mode = False

            # Устанавливаем режим read-only *перед* попыткой загрузки
            self.text_edit.setReadOnly(read_only_mode)

            # Пытаемся открыть файл с помощью _load_file
            if self._load_file(file_path, self.current_encoding):
                 # Если файл успешно загружен, устанавливаем read-only еще раз (на случай смены кодировки)
                self.text_edit.setReadOnly(read_only_mode)
                if read_only_mode:
                    self.status_bar.showMessage(f"Файл открыт в режиме только для чтения: {file_path}", 3000)
                # Сообщение об успешном открытии уже есть в _load_file
                event.accept() # Принимаем событие drop
            else:
                 # Если _load_file вернул False (ошибка или отмена)
                self.text_edit.setReadOnly(False) # Сбрасываем read-only
                # Очищаем поле и сбрасываем состояние, если открытие не удалось
                self.new_file() # Вызываем new_file для чистого состояния (без запроса сохранения)
                self.status_bar.showMessage("Не удалось открыть перетаскиваемый файл.", 3000)
                event.ignore() # Игнорируем событие drop

        except Exception as e:
            QMessageBox.critical(self, "Критическая ошибка", f"Ошибка при обработке перетаскивания: {str(e)}")
            self.text_edit.setReadOnly(False) # На всякий случай сбрасываем read-only
            event.ignore()

    def apply_language(self):
        """Применяет текущий язык к интерфейсу программы"""
        # Получаем код языка из названия
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        # Обновляем меню
        menu_bar = self.menuBar()
        
        # Обновляем меню "Файл"
        file_menu = menu_bar.actions()[0]
        file_menu.setText(translations["file_menu"])
        file_actions = file_menu.menu().actions()
        file_actions[0].setText(translations["new"])
        file_actions[1].setText(translations["open"])
        file_actions[2].setText(translations["save"])
        file_actions[3].setText(translations["save_as"])
        file_actions[5].setText(translations["exit"])
        
        # Обновляем меню "Правка"
        edit_menu = menu_bar.actions()[1]
        edit_menu.setText(translations["edit_menu"])
        edit_actions = edit_menu.menu().actions()
        edit_actions[0].setText(translations["undo"])
        edit_actions[1].setText(translations["redo"])
        edit_actions[3].setText(translations["cut"])
        edit_actions[4].setText(translations["copy"])
        edit_actions[5].setText(translations["paste"])
        edit_actions[6].setText(translations["delete"])
        edit_actions[8].setText(translations["find"])
        edit_actions[10].setText(translations["select_all"])
        
        # Обновляем меню "Формат"
        format_menu = menu_bar.actions()[2]
        format_menu.setText(translations["format_menu"])
        format_actions = format_menu.menu().actions()
        format_actions[0].setText(translations["font"])
        format_actions[1].setText(translations["word_wrap"])
        
        # Обновляем меню "Кодировка"
        encoding_menu = menu_bar.actions()[3]
        encoding_menu.setText(translations["encoding_menu"])
        
        # Обновляем меню "Вид"
        view_menu = menu_bar.actions()[4]
        view_menu.setText(translations["view_menu"])
        view_actions = view_menu.menu().actions()
        theme_menu = view_actions[0].menu() 
        theme_menu.setTitle(translations["theme_menu"])
        theme_actions = theme_menu.actions()
        theme_actions[0].setText(translations["light_theme"])
        theme_actions[1].setText(translations["dark_theme"])
        theme_actions[2].setText(translations["blue_theme"])
        theme_actions[3].setText(translations["green_theme"])
        view_actions[1].setText(translations["opacity"])
        
        # Обновляем меню "Справка"
        help_menu = menu_bar.actions()[5]
        help_menu.setText(translations["help_menu"])
        help_actions = help_menu.menu().actions()
        help_actions[0].setText(translations["settings"])
        help_actions[1].setText(translations["about"])
        
        # Обновляем статусбар
        self.encoding_label.setText(translations["encoding_status"].format(self.current_encoding))
        self.status_bar.showMessage(translations["ready"])

    def apply_blur(self):
        """Применяет эффект размытия к текстовому редактору"""
        if self.blur_enabled and self.blur_radius > 0:
            blur_effect = QGraphicsBlurEffect()
            blur_effect.setBlurRadius(self.blur_radius)
            self.text_edit.setGraphicsEffect(blur_effect)
        else:
            self.text_edit.setGraphicsEffect(None)

    def set_blur(self):
        """Показывает диалог настройки размытия"""
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        dialog = BlurDialog(self, self.blur_radius, translations)
        if dialog.exec():
            self.blur_radius = dialog.slider.value()
            self.blur_enabled = dialog.enable_checkbox.isChecked()
            
            # Сохраняем настройки
            self.settings.setValue("blur_radius", self.blur_radius)
            self.settings.setValue("blur_enabled", self.blur_enabled)
            
            # Применяем размытие
            self.apply_blur()
            
            # Показываем сообщение
            self.status_bar.showMessage(
                translations["blur_effect"] + ": " + 
                ("Включено" if self.blur_enabled else "Выключено") + 
                f" (радиус: {self.blur_radius})", 
                3000
            )

    def set_background_image(self):
        """Устанавливает фоновое изображение для текстового редактора"""
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            translations["background_image_title"],
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        
        if file_path:
            try:
                # Загружаем изображение
                image = QImage(file_path)
                if image.isNull():
                    raise Exception("Invalid image")
                
                # Сохраняем путь к изображению
                self.background_image = file_path
                self.settings.setValue("background_image", file_path)
                
                # Применяем изображение
                self.apply_background_image()
                
                self.status_bar.showMessage(translations["background_image_set"], 3000)
                
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", translations["background_image_error"])
                self.status_bar.showMessage(translations["background_image_error"], 3000)
        else:
            # Если пользователь отменил выбор, удаляем текущее изображение
            self.text_edit.setStyleSheet("")
            self.background_image = None
            self.settings.remove("background_image")
            self.status_bar.showMessage(translations["background_image_removed"], 3000)

    def apply_background_image(self):
        """Применяет фоновое изображение с текущими настройками прозрачности"""
        if self.background_image:
            self.text_edit.setStyleSheet(f"""
                QTextEdit {{
                    background-image: url({self.background_image});
                    background-position: center;
                    background-repeat: no-repeat;
                    background-attachment: fixed;
                    background-color: rgba(255, 255, 255, {1 - self.background_opacity});
                }}
            """)

    def set_background_opacity(self):
        """Устанавливает прозрачность фонового изображения"""
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        # Преобразуем значение прозрачности в целое число (0-100)
        opacity_value = int(self.background_opacity * 100)
        
        dialog = BackgroundOpacityDialog(self, opacity_value, translations)
        if dialog.exec():
            self.background_opacity = dialog.opacity_slider.value() / 100
            self.settings.setValue("background_opacity", self.background_opacity)
            
            # Обновляем стиль с новой прозрачностью
            self.apply_background_image()
            
            self.status_bar.showMessage(
                translations["background_opacity_value"].format(int(self.background_opacity * 100)),
                3000
            )

    def resizeEvent(self, event):
        """Обработчик изменения размера окна"""
        super().resizeEvent(event)
        # Обновляем размер фонового изображения при изменении размера окна
        if self.background_image:
            self.apply_background_image()

    def show_social_networks(self):
        """Показывает диалог с социальными сетями"""
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        dialog = QDialog(self)
        dialog.setWindowTitle(translations["social_networks_title"])
        dialog.setFixedSize(400, 300)  # Увеличиваем высоту для новых кнопок
        
        layout = QVBoxLayout()
        
        # Добавляем сообщение
        message = QLabel(translations["social_networks_message"])
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(message)
        
        # Добавляем кнопку Telegram
        telegram_button = QPushButton(translations["telegram"])
        telegram_button.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(translations["telegram_link"])))
        telegram_button.setStyleSheet("""
            QPushButton {
                background-color: #0088cc;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
                min-width: 150px;
            }
            QPushButton:hover {
                background-color: #006699;
            }
        """)
        layout.addWidget(telegram_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Добавляем кнопку GitHub EzzTEMP
        github_ezz_button = QPushButton(f"{translations['github']} - EzzTEMP")
        github_ezz_button.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(translations["github_ezz"])))
        github_ezz_button.setStyleSheet("""
            QPushButton {
                background-color: #24292e;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
                min-width: 150px;
            }
            QPushButton:hover {
                background-color: #1b1f23;
            }
        """)
        layout.addWidget(github_ezz_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Добавляем кнопку GitHub mansar1337
        github_mansar_button = QPushButton(f"{translations['github']} - mansar1337")
        github_mansar_button.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(translations["github_mansar"])))
        github_mansar_button.setStyleSheet("""
            QPushButton {
                background-color: #24292e;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
                min-width: 150px;
            }
            QPushButton:hover {
                background-color: #1b1f23;
            }
        """)
        layout.addWidget(github_mansar_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Добавляем кнопку OK
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(dialog.accept)
        layout.addWidget(ok_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        dialog.setLayout(layout)
        dialog.exec()

    def customize_colors(self):
        """Показывает диалог настройки цветов"""
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        dialog = ColorCustomizationDialog(
            self,
            self.background_color,
            self.cursor_color
        )
        
        if dialog.exec():
            self.background_color = dialog.current_bg_color
            self.cursor_color = dialog.current_cursor_color
            
            # Сохраняем настройки
            self.settings.setValue("background_color", self.background_color)
            self.settings.setValue("cursor_color", self.cursor_color)
            
            # Применяем новые цвета
            self.apply_colors()
            
            # Показываем сообщение
            self.status_bar.showMessage(translations["colors_customized"], 3000)
    
    def apply_colors(self):
        """Применяет выбранные цвета к текстовому редактору"""
        self.text_edit.setStyleSheet(f"""
            QTextEdit {{
                background-color: {self.background_color};
                caret-color: {self.cursor_color};
            }}
        """)

    def customize_cursor(self):
        """Показывает диалог настройки курсора"""
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        dialog = QDialog(self)
        dialog.setWindowTitle(translations["customize_cursor"])
        dialog.setFixedSize(300, 150)
        
        layout = QVBoxLayout()
        
        # Создаем кнопку выбора цвета курсора
        color_layout = QHBoxLayout()
        color_label = QLabel(translations["cursor_color"])
        color_button = QPushButton()
        color_button.setFixedSize(50, 25)
        color_button.setStyleSheet(f"background-color: {self.cursor_color};")
        
        def select_color():
            color = QColorDialog.getColor()
            if color.isValid():
                color_button.setStyleSheet(f"background-color: {color.name()};")
        
        color_button.clicked.connect(select_color)
        
        color_layout.addWidget(color_label)
        color_layout.addWidget(color_button)
        color_layout.addStretch()
        
        # Создаем слайдер для ширины курсора
        width_layout = QHBoxLayout()
        width_label = QLabel(translations["cursor_width"])
        width_slider = QSlider(Qt.Orientation.Horizontal)
        width_slider.setRange(1, 5)
        width_slider.setValue(self.cursor_width)
        width_value = QLabel(str(self.cursor_width))
        
        width_slider.valueChanged.connect(lambda v: width_value.setText(str(v)))
        
        width_layout.addWidget(width_label)
        width_layout.addWidget(width_slider)
        width_layout.addWidget(width_value)
        
        # Добавляем все элементы в layout
        layout.addLayout(color_layout)
        layout.addLayout(width_layout)
        layout.addStretch()
        
        # Добавляем кнопки OK и Cancel
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | 
            QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        layout.addWidget(button_box)
        
        dialog.setLayout(layout)
        
        if dialog.exec():
            # Сохраняем новые настройки
            self.cursor_color = color_button.styleSheet().split(": ")[1].rstrip(";")
            self.cursor_width = width_slider.value()
            
            # Сохраняем в настройках
            self.settings.setValue("cursor_color", self.cursor_color)
            self.settings.setValue("cursor_width", self.cursor_width)
            
            # Применяем настройки только для курсора
            self.text_edit.setStyleSheet(f"""
                QTextEdit::cursor {{
                    background-color: {self.cursor_color};
                    width: {self.cursor_width}px;
                }}
            """)

    def show_city_selection(self):
        """Показывает диалог выбора города"""
        lang_code = LANGUAGES.get(self.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        dialog = CitySelectionDialog(self, self.selected_city, self.selected_timezone)
        
        if dialog.exec():
            city, timezone = dialog.get_selected_city()
            if city and timezone:
                self.selected_city = city
                self.selected_timezone = timezone
                
                # Сохраняем настройки
                self.settings.setValue("selected_city", self.selected_city)
                self.settings.setValue("selected_timezone", self.selected_timezone)
                
                # Обновляем время
                self.update_datetime()
                
                # Показываем сообщение
                self.status_bar.showMessage(translations["city_selected"], 3000)

class ColorCustomizationDialog(QDialog):
    def __init__(self, parent=None, current_bg_color="#ffffff", current_cursor_color="#000000"):
        super().__init__(parent)
        self.parent = parent
        self.current_bg_color = current_bg_color
        self.current_cursor_color = current_cursor_color
        
        # Получаем текущие переводы
        lang_code = LANGUAGES.get(self.parent.current_language, "ru")
        translations = TRANSLATIONS[lang_code]
        
        self.setWindowTitle(translations["customize_colors"])
        self.setFixedSize(400, 200)
        
        layout = QVBoxLayout()
        
        # Создаем кнопки для выбора цвета фона
        bg_layout = QHBoxLayout()
        bg_label = QLabel(translations["background_color"])
        self.bg_color_button = QPushButton()
        self.bg_color_button.setFixedSize(50, 30)
        self.bg_color_button.setStyleSheet(f"background-color: {current_bg_color};")
        self.bg_color_button.clicked.connect(lambda: self.select_color("background"))
        
        bg_layout.addWidget(bg_label)
        bg_layout.addWidget(self.bg_color_button)
        bg_layout.addStretch()
        
        # Создаем кнопки для выбора цвета курсора
        cursor_layout = QHBoxLayout()
        cursor_label = QLabel(translations["cursor_color"])
        self.cursor_color_button = QPushButton()
        self.cursor_color_button.setFixedSize(50, 30)
        self.cursor_color_button.setStyleSheet(f"background-color: {current_cursor_color};")
        self.cursor_color_button.clicked.connect(lambda: self.select_color("cursor"))
        
        cursor_layout.addWidget(cursor_label)
        cursor_layout.addWidget(self.cursor_color_button)
        cursor_layout.addStretch()
        
        # Добавляем кнопки в layout
        layout.addLayout(bg_layout)
        layout.addLayout(cursor_layout)
        layout.addStretch()
        
        # Добавляем кнопки OK и Cancel
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | 
            QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        self.setLayout(layout)
    
    def select_color(self, color_type):
        color = QColorDialog.getColor()
        if color.isValid():
            if color_type == "background":
                self.current_bg_color = color.name()
                self.bg_color_button.setStyleSheet(f"background-color: {self.current_bg_color};")
            else:
                self.current_cursor_color = color.name()
                self.cursor_color_button.setStyleSheet(f"background-color: {self.current_cursor_color};")

class CursorCustomizationDialog(QDialog):
    def __init__(self, parent=None, current_width=2, current_style="solid", current_blink=True):
        super().__init__(parent)
        self.parent = parent
        self.current_width = current_width
        self.current_style = current_style
        self.current_blink = current_blink
        
        # Получаем текущие переводы
        lang_code = LANGUAGES.get(self.parent.current_language, "ru")
        self.translations = TRANSLATIONS[lang_code]
        
        self.setWindowTitle(self.translations["customize_cursor"])
        self.setFixedSize(400, 250)
        
        layout = QVBoxLayout()
        
        # Создаем слайдер для ширины курсора
        width_layout = QHBoxLayout()
        width_label = QLabel(self.translations["cursor_width"])
        self.width_slider = QSlider(Qt.Orientation.Horizontal)
        self.width_slider.setRange(1, 10)
        self.width_slider.setValue(current_width)
        self.width_value_label = QLabel(str(current_width))
        self.width_slider.valueChanged.connect(
            lambda value: self.width_value_label.setText(str(value))
        )
        
        width_layout.addWidget(width_label)
        width_layout.addWidget(self.width_slider)
        width_layout.addWidget(self.width_value_label)
        
        # Создаем комбобокс для стиля курсора
        style_layout = QHBoxLayout()
        style_label = QLabel(self.translations["cursor_style"])
        self.style_combo = QComboBox()
        self.style_combo.addItems([
            self.translations["cursor_solid"],
            self.translations["cursor_dashed"],
            self.translations["cursor_dotted"]
        ])
        style_map = {
            self.translations["cursor_solid"]: "solid",
            self.translations["cursor_dashed"]: "dashed",
            self.translations["cursor_dotted"]: "dotted"
        }
        self.style_combo.setCurrentText(
            next(k for k, v in style_map.items() if v == current_style)
        )
        
        style_layout.addWidget(style_label)
        style_layout.addWidget(self.style_combo)
        
        # Создаем чекбокс для мигания курсора
        self.blink_checkbox = QCheckBox(self.translations["cursor_blink"])
        self.blink_checkbox.setChecked(current_blink)
        
        # Добавляем все элементы в layout
        layout.addLayout(width_layout)
        layout.addLayout(style_layout)
        layout.addWidget(self.blink_checkbox)
        layout.addStretch()
        
        # Добавляем кнопки OK и Cancel
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | 
            QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        self.setLayout(layout)
    
    def get_cursor_settings(self):
        """Возвращает настройки курсора"""
        style_map = {
            self.translations["cursor_solid"]: "solid",
            self.translations["cursor_dashed"]: "dashed",
            self.translations["cursor_dotted"]: "dotted"
        }
        return {
            "width": self.width_slider.value(),
            "style": style_map[self.style_combo.currentText()],
            "blink": self.blink_checkbox.isChecked()
        }

class HighlightSettingsDialog(QDialog):
    def __init__(self, parent=None, current_color="#4a7ab0", current_opacity=50,
                 current_gradient=False, current_animation=False, current_speed=1000):
        super().__init__(parent)
        self.parent = parent
        
        # Получаем текущие переводы
        lang_code = LANGUAGES.get(self.parent.current_language, "ru")
        self.translations = TRANSLATIONS[lang_code]
        
        self.setWindowTitle(self.translations["highlight_settings"])
        this.setFixedSize(400, 300)
        
        layout = QVBoxLayout()
        
        # Создаем кнопку выбора цвета
        color_layout = QHBoxLayout()
        color_label = QLabel(self.translations["highlight_color"])
        self.color_button = QPushButton()
        this.color_button.setFixedSize(50, 25)
        this.color_button.setStyleSheet(f"background-color: {current_color};")
        this.color_button.clicked.connect(lambda: self.select_color("color"))
        
        color_layout.addWidget(color_label)
        color_layout.addWidget(self.color_button)
        color_layout.addStretch()
        
        # Создаем слайдер для прозрачности
        opacity_layout = QHBoxLayout()
        opacity_label = QLabel(self.translations["highlight_opacity"])
        self.opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.opacity_slider.setRange(0, 100)
        self.opacity_slider.setValue(current_opacity)
        self.opacity_value_label = QLabel(f"{current_opacity}%")
        self.opacity_slider.valueChanged.connect(
            lambda value: self.opacity_value_label.setText(f"{value}%")
        )
        
        opacity_layout.addWidget(opacity_label)
        opacity_layout.addWidget(self.opacity_slider)
        opacity_layout.addWidget(self.opacity_value_label)
        
        # Создаем чекбоксы для эффектов
        self.gradient_checkbox = QCheckBox(self.translations["highlight_gradient"])
        self.gradient_checkbox.setChecked(current_gradient)
        
        self.animation_checkbox = QCheckBox(self.translations["highlight_animation"])
        this.animation_checkbox.setChecked(current_animation)
        
        # Создаем слайдер для скорости анимации
        speed_layout = QHBoxLayout()
        speed_label = QLabel(self.translations["highlight_speed"])
        this.speed_slider = QSlider(Qt.Orientation.Horizontal)
        this.speed_slider.setRange(100, 2000)
        this.speed_slider.setValue(current_speed)
        this.speed_value_label = QLabel(f"{current_speed}ms")
        this.speed_slider.valueChanged.connect(
            lambda value: self.speed_value_label.setText(f"{value}ms")
        )
        this.speed_slider.setEnabled(current_animation)
        
        speed_layout.addWidget(speed_label)
        speed_layout.addWidget(self.speed_slider)
        speed_layout.addWidget(self.speed_value_label)
        
        # Подключаем обновление состояния слайдера скорости
        this.animation_checkbox.toggled.connect(
            lambda checked: self.speed_slider.setEnabled(checked)
        )
        
        # Добавляем все элементы в layout
        layout.addLayout(color_layout)
        layout.addLayout(opacity_layout)
        layout.addWidget(self.gradient_checkbox)
        layout.addWidget(self.animation_checkbox)
        layout.addLayout(speed_layout)
        layout.addStretch()
        
        # Добавляем кнопки OK и Cancel
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | 
            QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        this.setLayout(layout)
    
    def select_color(self, color_type):
        """Выбор цвета"""
        color = QColorDialog.getColor()
        if color.isValid():
            if color_type == "color":
                self.color_button.setStyleSheet(f"background-color: {color.name()};")
                self.current_color = color.name()
    
    def get_settings(self):
        """Возвращает настройки подсветки"""
        return {
            "color": self.color_button.styleSheet().split(": ")[1].rstrip(";"),
            "opacity": self.opacity_slider.value(),
            "gradient": self.gradient_checkbox.isChecked(),
            "animation": self.animation_checkbox.isChecked(),
            "speed": self.speed_slider.value()
        }

class CitySelectionDialog(QDialog):
    def __init__(self, parent=None, current_city="", current_timezone="UTC"):
        super().__init__(parent)
        self.parent = parent
        
        # Получаем текущие переводы
        lang_code = LANGUAGES.get(self.parent.current_language, "ru")
        self.translations = TRANSLATIONS[lang_code]
        
        self.setWindowTitle(self.translations["select_city"])
        self.setFixedSize(500, 400)
        
        layout = QVBoxLayout()
        
        # Создаем поле поиска
        search_layout = QHBoxLayout()
        search_label = QLabel(self.translations["city_search"])
        self.search_edit = QLineEdit()
        self.search_edit.textChanged.connect(self.filter_cities)
        
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_edit)
        
        # Создаем список городов
        self.city_list = QListWidget()
        self.populate_city_list()
        
        # Создаем метку для отображения выбранного часового пояса
        self.timezone_label = QLabel()
        self.update_timezone_label()
        
        # Добавляем все элементы в layout
        layout.addLayout(search_layout)
        layout.addWidget(QLabel(self.translations["city_list"]))
        layout.addWidget(self.city_list)
        layout.addWidget(self.timezone_label)
        
        # Добавляем кнопки OK и Cancel
        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | 
            QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        self.setLayout(layout)
        
        # Выбираем текущий город, если он есть
        if current_city:
            items = self.city_list.findItems(current_city, Qt.MatchFlag.MatchExactly)
            if items:
                self.city_list.setCurrentItem(items[0])
    
    def populate_city_list(self):
        """Заполняет список городов"""
        # Получаем список всех часовых поясов
        timezones = pytz.all_timezones
        
        # Создаем словарь городов и их часовых поясов
        self.cities = {}
        for tz in timezones:
            city = tz.split('/')[-1].replace('_', ' ')
            self.cities[city] = tz
        
        # Добавляем города в список
        for city in sorted(self.cities.keys()):
            self.city_list.addItem(city)
    
    def filter_cities(self, text):
        """Фильтрует список городов по поисковому запросу"""
        for i in range(self.city_list.count()):
            item = self.city_list.item(i)
            item.setHidden(text.lower() not in item.text().lower())
    
    def update_timezone_label(self):
        """Обновляет метку с информацией о часовом поясе"""
        current_item = self.city_list.currentItem()
        if current_item:
            city = current_item.text()
            timezone = self.cities[city]
            current_time = QDateTime.currentDateTime().toPyDateTime()
            timezone_obj = pytz.timezone(timezone)
            local_time = timezone_obj.localize(current_time)
            
            self.timezone_label.setText(
                f"{self.translations['timezone']}: {timezone}\n"
                f"{self.translations['current_time']}: {local_time.strftime('%H:%M:%S')}"
            )
    
    def get_selected_city(self):
        """Возвращает выбранный город и его часовой пояс"""
        current_item = self.city_list.currentItem()
        if current_item:
            city = current_item.text()
            timezone = self.cities[city]
            return city, timezone
        return "", "UTC"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    notepad = Notepad()

    # Проверяем наличие аргументов командной строки
    if len(sys.argv) > 1:
        file_path_arg = sys.argv[1]
        # Проверяем, существует ли файл
        if os.path.isfile(file_path_arg):
            # Пытаемся загрузить файл с текущей кодировкой
            # _load_file сама обработает ошибки и режим read-only для .bat
            is_bat = file_path_arg.lower().endswith('.bat')
            read_only = False
            if is_bat:
                reply = QMessageBox.warning(
                    notepad, # Используем notepad как родителя
                    "Внимание - Исполняемый файл",
                    f"Вы пытаетесь открыть исполняемый файл {os.path.basename(file_path_arg)}.\n\n"
                    "Такие файлы могут содержать потенциально опасный код.\n"
                    "Вы хотите просмотреть его содержимое в режиме только для чтения?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No
                )
                if reply == QMessageBox.StandardButton.Yes:
                    read_only = True
                else:
                    # Если пользователь отказался, просто показываем пустое окно
                    file_path_arg = None # Сбрасываем путь, чтобы не загружать

            if file_path_arg: # Если путь не сброшен (не отказались от .bat)
                notepad.text_edit.setReadOnly(read_only) # Устанавливаем режим до загрузки
                if notepad._load_file(file_path_arg, notepad.current_encoding):
                    notepad.text_edit.setReadOnly(read_only) # Устанавливаем еще раз после загрузки
                    if read_only:
                         notepad.status_bar.showMessage(f"Файл открыт в режиме только для чтения: {file_path_arg}", 3000)
                else:
                     # Если _load_file вернул False (ошибка или отмена кодировки)
                     notepad.text_edit.setReadOnly(False) # Сбрасываем read-only
                     notepad.new_file() # Показываем чистый редактор
                     notepad.status_bar.showMessage(f"Не удалось открыть файл из аргумента: {file_path_arg}", 3000)

        else:
            # Показываем сообщение, если файл из аргумента не найден
            QMessageBox.warning(notepad, "Ошибка", f"Файл не найден: {file_path_arg}")


    notepad.show()
    sys.exit(app.exec())