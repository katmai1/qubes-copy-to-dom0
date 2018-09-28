# -*- coding: utf-8 -*-

"""
Module implementing mainwin.
"""
import os
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,  QMessageBox

from .Ui_main import Ui_mainwin


class mainwin(QMainWindow, Ui_mainwin):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(mainwin, self).__init__(parent)
        self.setupUi(self)
        self._dicts_vms = self._get_vms_info()
        self._insert_vms_to_list()
        
    def _insert_vms_to_list(self):
        for vm in self._dicts_vms:
            if vm["status"] == "Running" and vm["name"] != "dom0":
                self.list_vms.addItem(vm['name'])
        # TODO: comprobar antes si esta vacía
        self.list_vms.setCurrentRow(0)

    # devuelve lista de diccionarios con los datos de las vm
    def _get_vms_info(self):
        raw = os.popen("qvm-ls --raw-data").read()
        all_data = raw.split("\n")
        lista = list()
        for vm_raw in all_data:
            if vm_raw != "":
                datos = vm_raw.split("|")
                vm = {"name": datos[0],  "status": datos[1]}
                lista.append(vm)
        return lista
    
    @pyqtSlot()
    def on_btn_help_released(self):
        """
        Slot documentation goes here.
        """
        res = QMessageBox.information(
            self,
            self.tr("Help"),
            self.tr("""This application will copy all contents of folder QubesOutcoming from any VM to dom0.

* If any file exist in destination, will be replaced."""),
            QMessageBox.StandardButtons(
                QMessageBox.Close),
            QMessageBox.Close)
        
    
    @pyqtSlot()
    def on_btn_copy_released(self):
        """
        Slot documentation goes here.
        """
        source_vm = self.list_vms.currentItem().text()
        source_folder = "/home/user/QubesOutcoming"
        tar_filename = "/tmp/qubes2dom.zip"
        dest_folder = "/home/q/QubesIncoming/%s" % source_vm
        # borramos los temporales de origen y destino
        os.system("qvm-run %s 'rm %s'" % (source_vm,  tar_filename))
        os.system("rm %s" % tar_filename)
        # creamos carpeta destino i origen si no existen
        os.system("mkdir -p %s" % dest_folder)
        os.system("qvm-run %s 'mkdir -p %s'" %  (source_vm,  source_folder))
        # comprimimos la carpeta
        os.system("qvm-run %s 'zip %s %s/*'" % (source_vm,  tar_filename, source_folder))
        # copiamos fichero
        cmd = "qvm-run --pass-io %s 'cat %s' > %s" % (source_vm,  tar_filename,  tar_filename)
        os.system(cmd)
        # descomprimimos en dom0
        cmd = "unzip -j -u %s -d %s" % (tar_filename,  dest_folder)
        os.system(cmd)
