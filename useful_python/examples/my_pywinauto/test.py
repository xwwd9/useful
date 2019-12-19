import logging.config

import pywinauto
import requests

from useful_python.examples.my_pywinauto.tools import init_weixin

logger = logging.getLogger("main")


if __name__ == "__main__":

    logging.config.fileConfig('logging.cfg')

    # logger.debug("debug")
    # logger.info("info")
    # logger.error("error")



    ret = pywinauto.findwindows.find_windows(class_name="WeChatMainWndForPC")


    a = "okk"
    a.translate()


    # dlg = init_weixin()

