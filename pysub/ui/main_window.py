# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pysub/ui/main_window.ui'
#
# Created: Sat Sep 13 13:45:15 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 510)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStatusTip("")
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1, 1))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_wdiget = QtGui.QWidget(self.centralwidget)
        self.main_wdiget.setObjectName("main_wdiget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.main_wdiget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.status_label = QtGui.QLabel(self.main_wdiget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.status_label.setFont(font)
        self.status_label.setObjectName("status_label")
        self.verticalLayout_4.addWidget(self.status_label)
        self.file_list = QtGui.QTreeView(self.main_wdiget)
        self.file_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.file_list.setProperty("showDropIndicator", False)
        self.file_list.setAlternatingRowColors(True)
        self.file_list.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.file_list.setItemsExpandable(False)
        self.file_list.setSortingEnabled(True)
        self.file_list.setAnimated(True)
        self.file_list.setAllColumnsShowFocus(True)
        self.file_list.setExpandsOnDoubleClick(False)
        self.file_list.setObjectName("file_list")
        self.verticalLayout_4.addWidget(self.file_list)
        self.verticalLayout_2.addWidget(self.main_wdiget)
        self.settings_widget = QtGui.QWidget(self.centralwidget)
        self.settings_widget.setEnabled(True)
        self.settings_widget.setObjectName("settings_widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.settings_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bx_settings = QtGui.QToolBox(self.settings_widget)
        self.bx_settings.setObjectName("bx_settings")
        self.pge_set_norm = QtGui.QWidget()
        self.pge_set_norm.setGeometry(QtCore.QRect(0, 0, 669, 204))
        self.pge_set_norm.setObjectName("pge_set_norm")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.pge_set_norm)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.layout_chkboxes = QtGui.QFormLayout()
        self.layout_chkboxes.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.layout_chkboxes.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.layout_chkboxes.setObjectName("layout_chkboxes")
        self.chk_auto_dl = QtGui.QCheckBox(self.pge_set_norm)
        self.chk_auto_dl.setObjectName("chk_auto_dl")
        self.layout_chkboxes.setWidget(1, QtGui.QFormLayout.LabelRole, self.chk_auto_dl)
        self.lbl_auto_dl = QtGui.QLabel(self.pge_set_norm)
        font = QtGui.QFont()
        font.setFamily("Droid Sans")
        font.setItalic(False)
        font.setUnderline(False)
        self.lbl_auto_dl.setFont(font)
        self.lbl_auto_dl.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_auto_dl.setScaledContents(False)
        self.lbl_auto_dl.setWordWrap(True)
        self.lbl_auto_dl.setObjectName("lbl_auto_dl")
        self.layout_chkboxes.setWidget(1, QtGui.QFormLayout.FieldRole, self.lbl_auto_dl)
        self.chk_overwrite = QtGui.QCheckBox(self.pge_set_norm)
        self.chk_overwrite.setObjectName("chk_overwrite")
        self.layout_chkboxes.setWidget(3, QtGui.QFormLayout.LabelRole, self.chk_overwrite)
        self.lbl_overwrite = QtGui.QLabel(self.pge_set_norm)
        self.lbl_overwrite.setWordWrap(True)
        self.lbl_overwrite.setObjectName("lbl_overwrite")
        self.layout_chkboxes.setWidget(3, QtGui.QFormLayout.FieldRole, self.lbl_overwrite)
        self.dl_folder_layout = QtGui.QHBoxLayout()
        self.dl_folder_layout.setObjectName("dl_folder_layout")
        self.lbl_save_folder = QtGui.QLabel(self.pge_set_norm)
        self.lbl_save_folder.setObjectName("lbl_save_folder")
        self.dl_folder_layout.addWidget(self.lbl_save_folder)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.dl_folder_layout.addItem(spacerItem)
        self.lne_save_folder = QtGui.QLineEdit(self.pge_set_norm)
        self.lne_save_folder.setObjectName("lne_save_folder")
        self.dl_folder_layout.addWidget(self.lne_save_folder)
        self.layout_chkboxes.setLayout(5, QtGui.QFormLayout.SpanningRole, self.dl_folder_layout)
        self.language_layout = QtGui.QHBoxLayout()
        self.language_layout.setObjectName("language_layout")
        self.lbl_language = QtGui.QLabel(self.pge_set_norm)
        self.lbl_language.setWordWrap(True)
        self.lbl_language.setObjectName("lbl_language")
        self.language_layout.addWidget(self.lbl_language)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.language_layout.addItem(spacerItem1)
        self.cbo_language = QtGui.QComboBox(self.pge_set_norm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbo_language.sizePolicy().hasHeightForWidth())
        self.cbo_language.setSizePolicy(sizePolicy)
        self.cbo_language.setMinimumSize(QtCore.QSize(150, 0))
        self.cbo_language.setObjectName("cbo_language")
        self.language_layout.addWidget(self.cbo_language)
        self.layout_chkboxes.setLayout(6, QtGui.QFormLayout.SpanningRole, self.language_layout)
        self.lbl_prompt = QtGui.QLabel(self.pge_set_norm)
        self.lbl_prompt.setWordWrap(True)
        self.lbl_prompt.setObjectName("lbl_prompt")
        self.layout_chkboxes.setWidget(4, QtGui.QFormLayout.FieldRole, self.lbl_prompt)
        self.chk_prompt = QtGui.QCheckBox(self.pge_set_norm)
        self.chk_prompt.setObjectName("chk_prompt")
        self.layout_chkboxes.setWidget(4, QtGui.QFormLayout.LabelRole, self.chk_prompt)
        self.horizontalLayout_2.addLayout(self.layout_chkboxes)
        self.bx_settings.addItem(self.pge_set_norm, "")
        self.pge_set_adv = QtGui.QWidget()
        self.pge_set_adv.setGeometry(QtCore.QRect(0, 0, 669, 427))
        self.pge_set_adv.setObjectName("pge_set_adv")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.pge_set_adv)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.advanced_group_box = QtGui.QGroupBox(self.pge_set_adv)
        self.advanced_group_box.setEnabled(False)
        self.advanced_group_box.setTitle("")
        self.advanced_group_box.setFlat(True)
        self.advanced_group_box.setCheckable(False)
        self.advanced_group_box.setChecked(False)
        self.advanced_group_box.setObjectName("advanced_group_box")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.advanced_group_box)
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.advanced_layout = QtGui.QVBoxLayout()
        self.advanced_layout.setObjectName("advanced_layout")
        self.lbl_file_ext = QtGui.QLabel(self.advanced_group_box)
        self.lbl_file_ext.setObjectName("lbl_file_ext")
        self.advanced_layout.addWidget(self.lbl_file_ext)
        self.txt_file_ext = QtGui.QPlainTextEdit(self.advanced_group_box)
        self.txt_file_ext.setMinimumSize(QtCore.QSize(0, 0))
        self.txt_file_ext.setObjectName("txt_file_ext")
        self.advanced_layout.addWidget(self.txt_file_ext)
        self.lbl_sub_ext = QtGui.QLabel(self.advanced_group_box)
        self.lbl_sub_ext.setObjectName("lbl_sub_ext")
        self.advanced_layout.addWidget(self.lbl_sub_ext)
        self.txt_sub_ext = QtGui.QPlainTextEdit(self.advanced_group_box)
        self.txt_sub_ext.setObjectName("txt_sub_ext")
        self.advanced_layout.addWidget(self.txt_sub_ext)
        self.lbl_lang_json = QtGui.QLabel(self.advanced_group_box)
        self.lbl_lang_json.setObjectName("lbl_lang_json")
        self.advanced_layout.addWidget(self.lbl_lang_json)
        self.txt_lang_json = QtGui.QPlainTextEdit(self.advanced_group_box)
        self.txt_lang_json.setObjectName("txt_lang_json")
        self.advanced_layout.addWidget(self.txt_lang_json)
        self.cutoff_layout = QtGui.QHBoxLayout()
        self.cutoff_layout.setObjectName("cutoff_layout")
        self.lbl_cutoff = QtGui.QLabel(self.advanced_group_box)
        self.lbl_cutoff.setObjectName("lbl_cutoff")
        self.cutoff_layout.addWidget(self.lbl_cutoff)
        self.sl_cutoff = QtGui.QSlider(self.advanced_group_box)
        self.sl_cutoff.setMaximum(100)
        self.sl_cutoff.setSingleStep(1)
        self.sl_cutoff.setPageStep(1)
        self.sl_cutoff.setProperty("value", 75)
        self.sl_cutoff.setOrientation(QtCore.Qt.Horizontal)
        self.sl_cutoff.setInvertedAppearance(False)
        self.sl_cutoff.setInvertedControls(False)
        self.sl_cutoff.setObjectName("sl_cutoff")
        self.cutoff_layout.addWidget(self.sl_cutoff)
        self.sl_label = QtGui.QLabel(self.advanced_group_box)
        self.sl_label.setObjectName("sl_label")
        self.cutoff_layout.addWidget(self.sl_label)
        self.advanced_layout.addLayout(self.cutoff_layout)
        self.ua_server_layout = QtGui.QHBoxLayout()
        self.ua_server_layout.setObjectName("ua_server_layout")
        self.lbl_ua = QtGui.QLabel(self.advanced_group_box)
        self.lbl_ua.setObjectName("lbl_ua")
        self.ua_server_layout.addWidget(self.lbl_ua)
        self.lne_ua = QtGui.QLineEdit(self.advanced_group_box)
        self.lne_ua.setObjectName("lne_ua")
        self.ua_server_layout.addWidget(self.lne_ua)
        self.lbl_server = QtGui.QLabel(self.advanced_group_box)
        self.lbl_server.setObjectName("lbl_server")
        self.ua_server_layout.addWidget(self.lbl_server)
        self.lne_server = QtGui.QLineEdit(self.advanced_group_box)
        self.lne_server.setObjectName("lne_server")
        self.ua_server_layout.addWidget(self.lne_server)
        self.advanced_layout.addLayout(self.ua_server_layout)
        self.horizontalLayout_7.addLayout(self.advanced_layout)
        self.verticalLayout_3.addWidget(self.advanced_group_box)
        self.chk_enable_advanced_sett = QtGui.QCheckBox(self.pge_set_adv)
        self.chk_enable_advanced_sett.setObjectName("chk_enable_advanced_sett")
        self.verticalLayout_3.addWidget(self.chk_enable_advanced_sett)
        self.bx_settings.addItem(self.pge_set_adv, "")
        self.verticalLayout.addWidget(self.bx_settings)
        self.layout_settings_buttons = QtGui.QHBoxLayout()
        self.layout_settings_buttons.setObjectName("layout_settings_buttons")
        self.btn_reset_conf = QtGui.QPushButton(self.settings_widget)
        self.btn_reset_conf.setCheckable(False)
        self.btn_reset_conf.setFlat(False)
        self.btn_reset_conf.setObjectName("btn_reset_conf")
        self.layout_settings_buttons.addWidget(self.btn_reset_conf)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.layout_settings_buttons.addItem(spacerItem2)
        self.btn_apply = QtGui.QPushButton(self.settings_widget)
        self.btn_apply.setToolTip("")
        self.btn_apply.setFlat(False)
        self.btn_apply.setObjectName("btn_apply")
        self.layout_settings_buttons.addWidget(self.btn_apply)
        self.btn_save_conf = QtGui.QPushButton(self.settings_widget)
        self.btn_save_conf.setObjectName("btn_save_conf")
        self.layout_settings_buttons.addWidget(self.btn_save_conf)
        self.verticalLayout.addLayout(self.layout_settings_buttons)
        self.verticalLayout_2.addWidget(self.settings_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setWeight(50)
        font.setBold(False)
        self.toolBar.setFont(font)
        self.toolBar.setStatusTip("")
        self.toolBar.setMovable(True)
        self.toolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionAddFiles = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/toolbar/add_files"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddFiles.setIcon(icon1)
        self.actionAddFiles.setObjectName("actionAddFiles")
        self.actionAddFolder = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/toolbar/add_folder"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddFolder.setIcon(icon2)
        self.actionAddFolder.setObjectName("actionAddFolder")
        self.actionSettings = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/toolbar/settings"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.actionSettings.setFont(font)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setEnabled(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/toolbar/about"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon4)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSearch = QtGui.QAction(MainWindow)
        self.actionSearch.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/toolbar/search"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearch.setIcon(icon5)
        self.actionSearch.setObjectName("actionSearch")
        self.actionStop = QtGui.QAction(MainWindow)
        self.actionStop.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/toolbar/stop"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon6)
        self.actionStop.setVisible(False)
        self.actionStop.setObjectName("actionStop")
        self.actionExitSettings = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/toolbar/back"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExitSettings.setIcon(icon7)
        self.actionExitSettings.setVisible(False)
        self.actionExitSettings.setObjectName("actionExitSettings")
        self.actionDownload = QtGui.QAction(MainWindow)
        self.actionDownload.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/toolbar/download"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDownload.setIcon(icon8)
        self.actionDownload.setObjectName("actionDownload")
        self.actionSkip = QtGui.QAction(MainWindow)
        self.actionSkip.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/toolbar/skip"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSkip.setIcon(icon9)
        self.actionSkip.setObjectName("actionSkip")
        self.actionClearList = QtGui.QAction(MainWindow)
        self.actionClearList.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/toolbar/remove"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClearList.setIcon(icon10)
        self.actionClearList.setObjectName("actionClearList")
        self.toolBar.addAction(self.actionAddFiles)
        self.toolBar.addAction(self.actionAddFolder)
        self.toolBar.addAction(self.actionClearList)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSearch)
        self.toolBar.addAction(self.actionStop)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDownload)
        self.toolBar.addAction(self.actionSkip)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addAction(self.actionExitSettings)
        self.toolBar.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        self.bx_settings.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionSettings, QtCore.SIGNAL("triggered()"), self.main_wdiget.hide)
        QtCore.QObject.connect(self.actionExitSettings, QtCore.SIGNAL("triggered()"), self.main_wdiget.show)
        QtCore.QObject.connect(self.actionSettings, QtCore.SIGNAL("triggered()"), self.settings_widget.show)
        QtCore.QObject.connect(self.actionExitSettings, QtCore.SIGNAL("triggered()"), self.settings_widget.hide)
        QtCore.QObject.connect(self.chk_enable_advanced_sett, QtCore.SIGNAL("toggled(bool)"), self.advanced_group_box.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.status_label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>List of video files:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_auto_dl.setText(QtGui.QApplication.translate("MainWindow", "Auto Download Subtitles", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_auto_dl.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" color:#747474;\">Skips asking you which subtitle to download for every file and will automatically picks best one it can find. </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_overwrite.setText(QtGui.QApplication.translate("MainWindow", "Overwrite Existing Subs", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_overwrite.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" color:#747474;\">Overwrite subtitle if one already exists without prompting user</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_save_folder.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" color:#676767;\">Relative to video subtitle folder to save to:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_language.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" color:#737373;\">Search subtitles for this language:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_prompt.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" color:#747474;\">If auto download is used and it doesn\'t find any suitable subtitles you\'ll have to manually select one (or skip file)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_prompt.setText(QtGui.QApplication.translate("MainWindow", "Prompt if auto-dl fails", None, QtGui.QApplication.UnicodeUTF8))
        self.bx_settings.setItemText(self.bx_settings.indexOf(self.pge_set_norm), QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_file_ext.setText(QtGui.QApplication.translate("MainWindow", "File extensions", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_sub_ext.setText(QtGui.QApplication.translate("MainWindow", "Sub ext", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_lang_json.setText(QtGui.QApplication.translate("MainWindow", "Languages JSON:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_cutoff.setText(QtGui.QApplication.translate("MainWindow", "Match cutoff:", None, QtGui.QApplication.UnicodeUTF8))
        self.sl_label.setText(QtGui.QApplication.translate("MainWindow", "00", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_ua.setText(QtGui.QApplication.translate("MainWindow", "User Agent:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_server.setText(QtGui.QApplication.translate("MainWindow", "XMLRPC Server URL:", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_enable_advanced_sett.setText(QtGui.QApplication.translate("MainWindow", "Enable Advanced Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.bx_settings.setItemText(self.bx_settings.indexOf(self.pge_set_adv), QtGui.QApplication.translate("MainWindow", "Advanced Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_reset_conf.setStatusTip(QtGui.QApplication.translate("MainWindow", "Reset fields to their default values", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_reset_conf.setText(QtGui.QApplication.translate("MainWindow", "Reset to default", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_apply.setStatusTip(QtGui.QApplication.translate("MainWindow", "Applies settings to this session only", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_apply.setText(QtGui.QApplication.translate("MainWindow", "Apply Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_save_conf.setStatusTip(QtGui.QApplication.translate("MainWindow", "Apply and save settings to be used as default", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_save_conf.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddFiles.setText(QtGui.QApplication.translate("MainWindow", "Add Files", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddFiles.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add one or multiple video files to the list", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddFolder.setText(QtGui.QApplication.translate("MainWindow", "Add folder", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddFolder.setStatusTip(QtGui.QApplication.translate("MainWindow", "Add all valid files in the folder to the file list", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setStatusTip(QtGui.QApplication.translate("MainWindow", "Show configuration panel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setStatusTip(QtGui.QApplication.translate("MainWindow", "Show information about application", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setText(QtGui.QApplication.translate("MainWindow", "Start Searching", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSearch.setStatusTip(QtGui.QApplication.translate("MainWindow", "Start searching subtitles for the files in the list", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setText(QtGui.QApplication.translate("MainWindow", "Stop Searching", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStop.setStatusTip(QtGui.QApplication.translate("MainWindow", "Stop searching for subtitles and return to file list", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExitSettings.setText(QtGui.QApplication.translate("MainWindow", "Exit Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExitSettings.setStatusTip(QtGui.QApplication.translate("MainWindow", "Close settings panel and return to file list view", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownload.setText(QtGui.QApplication.translate("MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownload.setToolTip(QtGui.QApplication.translate("MainWindow", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownload.setStatusTip(QtGui.QApplication.translate("MainWindow", "Download the selected subtitle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSkip.setText(QtGui.QApplication.translate("MainWindow", "Skip", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSkip.setToolTip(QtGui.QApplication.translate("MainWindow", "Skip", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSkip.setStatusTip(QtGui.QApplication.translate("MainWindow", "Skip downloading subtitles for this file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClearList.setText(QtGui.QApplication.translate("MainWindow", "Clear List", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClearList.setStatusTip(QtGui.QApplication.translate("MainWindow", "Remove all files from the file list", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc