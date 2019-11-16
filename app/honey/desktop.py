import os
import time
from contextlib import closing
import requests
from PySide2.QtCore import Slot

from app.honey.base import BaseHoney, Actions
from app.lib.global_var import G
from app.lib.worker import Worker
from app.lib.diy_ui import AppDiv, InstalledDiv


def format_size(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%.3fG" % (G)
        else:
            return "%.3fM" % (M)
    else:
        return "%.3fK" % (kb)


class HDesktop(BaseHoney):
    def __init__(self, widget, ui_name, action):
        self.widget = widget
        self.__ui_name = ui_name
        ##
        self.name = "desktop"
        # self.download_url = "https://github.com/ctpbee/ctpbee_desktop/archive/master.zip"
        self.download_url = "https://github.com/ctpbee/bee_box/archive/master.zip"
        self.versions = ["1.0"]
        self.app_url = "https://github.com/ctpbee/ctpbee_desktop"
        self.install_path = os.path.join(G.config.install_path, f'{self.name}.zip')
        self.desc = 'ctpbee桌面端'
        self.icon = "app/resource/icon/bee_temp_grey.png"
        ##
        self.action = action
        self.div = self.div_init()

    def div_init(self):
        if self.action == Actions.INSTALL:
            return AppDiv(self.widget)
        elif self.action == Actions.RUN:
            return InstalledDiv(self.widget)

    @property
    def ui_name(self):
        return self.__class__.__name__ + "_" + self.__ui_name

    def download_handler(self):
        with closing(requests.get(self.download_url, stream=True)) as response:
            chunk_size = 1024  # 单次请求最大值
            is_chunked = response.headers.get('transfer-encoding', '') == 'chunked'
            content_length_s = response.headers.get('content-length')
            if not is_chunked and content_length_s.isdigit():
                content_size = int(content_length_s)
                self.div.progressbar.setRange(0, content_size)
            else:
                content_size = None
            with open(self.install_path, "wb") as file:
                s = response.iter_content(chunk_size=chunk_size)
                for data in s:
                    if not self.flag or G.pool_done:
                        self.action = Actions.INSTALL
                        self.div.progressbar.setVisible(False)
                        self.div.progress_msg.setVisible(False)
                        self.div.action.setText(self.action)
                        return False
                    file.write(data)  ##
                    self.count += 1
                    ##show
                    if content_size:
                        self.div.progressbar.setValue((chunk_size * self.count))
                        self.div.progress_msg.setText("download...")
                    else:
                        speed = format_size((chunk_size * self.count) / (time.time() - self.start_time))
                        self.div.progress_msg.setText(speed + "/s")
        return True

    def on_download_success(self):
        signal = dict(cls=self.__class__, action=Actions.RUN, version=self.versions[0])
        self.widget.mainwindow.job.install_signal.emit(signal)
        self.action = Actions.INSTALL
        self.div.action.setText(self.action)
        self.div.progressbar.setVisible(False)
        self.div.progress_msg.setVisible(False)

    def install_handler(self):
        pass

    def run_handler(self):
        pass

    def action_handler(self):
        if self.action == Actions.INSTALL:
            print(self.action)
            self.start_time = time.time()
            self.count = 0
            self.flag = True
            self.div.progressbar.setVisible(True)
            self.div.progress_msg.setVisible(True)
            self.div.progress_msg.setText("connect...")
            self.action = Actions.CANCEL
            self.div.action.setText(self.action)
            G.thread_pool.start(Worker(self.download_handler, callback=self.on_download_success))
            # 显示
        elif self.action == Actions.CANCEL:
            print(self.action)
            self.flag = False
