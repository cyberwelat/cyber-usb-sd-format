import sys
import subprocess
import platform
import time
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
                             QListWidget, QMessageBox, QProgressBar, QTextEdit, QHBoxLayout)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class USBFormatter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Güvenli USB Format Aracı - cyberwelat")
        self.setGeometry(300, 200, 650, 520)
        self.setWindowIcon(QIcon("icon.ico"))  # İkon dosyan varsa ekle

        main_layout = QVBoxLayout()

        title_label = QLabel("<h2>Güvenli USB Format Aracı</h2>")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        self.list_widget = QListWidget()
        main_layout.addWidget(QLabel("Bulunan USB Sürücüler:"))
        main_layout.addWidget(self.list_widget)

        button_layout = QHBoxLayout()
        self.refresh_btn = QPushButton("USB Sürücüleri Yenile")
        self.refresh_btn.clicked.connect(self.refresh_devices)
        button_layout.addWidget(self.refresh_btn)

        self.format_btn = QPushButton("Seçili USB Sürücüyü Sıfırla ve Formatla")
        self.format_btn.clicked.connect(self.format_selected)
        self.format_btn.setEnabled(False)
        button_layout.addWidget(self.format_btn)

        main_layout.addLayout(button_layout)

        main_layout.addWidget(QLabel("İşlem Günlükleri:"))
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        main_layout.addWidget(self.log_text)

        self.progress = QProgressBar()
        main_layout.addWidget(self.progress)

        footer_label = QLabel('<i>Geliştirici: cyberwelat | GitHub: <a href="https://github.com/cyberwelat" style="color:#0000ff;">github.com/cyberwelat</a></i>')
        footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer_label.setOpenExternalLinks(True)
        main_layout.addWidget(footer_label)

        self.setLayout(main_layout)
        self.refresh_devices()

    def log(self, message):
        self.log_text.append(message)
        QApplication.processEvents()

    def refresh_devices(self):
        self.list_widget.clear()
        devices = self.get_usb_devices()
        if not devices:
            self.log("USB sürücü bulunamadı.")
        else:
            for dev in devices:
                self.list_widget.addItem(f"{dev['name']} - {dev['size']} - {dev['model']}")
            self.log(f"{len(devices)} adet USB sürücü bulundu.")
        self.format_btn.setEnabled(bool(devices))

    def get_usb_devices(self):
        system = platform.system()
        devices = []
        try:
            if system == "Linux":
                # Linux'ta lsblk komutu ile usb aygıtları tespit et
                result = subprocess.run(['lsblk', '-o', 'NAME,SIZE,MODEL,RM,TRAN', '-J'], capture_output=True, text=True)
                import json
                data = json.loads(result.stdout)
                for block in data['blockdevices']:
                    if block.get('rm') == 1 and block.get('tran') == 'usb':
                        devices.append({
                            'name': '/dev/' + block['name'],
                            'size': block['size'],
                            'model': block.get('model', 'Bilinmiyor')
                        })
            elif system == "Windows":
                # Windows'ta WMIC ile USB sürücüleri al
                cmd = ['wmic', 'diskdrive', 'where', 'InterfaceType="USB"', 'get', 'DeviceID,Model,Size', '/format:csv']
                result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
                lines = result.stdout.strip().splitlines()
                for line in lines[1:]:
                    parts = line.split(',')
                    if len(parts) >= 4:
                        dev_id = parts[1].strip()
                        model = parts[2].strip()
                        size_raw = parts[3].strip()
                        try:
                            size_gb = f"{int(size_raw) / (1024**3):.2f} GB"
                        except:
                            size_gb = "Bilinmiyor"
                        devices.append({
                            'name': dev_id,
                            'size': size_gb,
                            'model': model if model else 'Bilinmiyor'
                        })
            else:
                self.log(f"{system} platformu desteklenmiyor.")
        except Exception as e:
            self.log(f"Hata: {e}")
        return devices

    def format_selected(self):
        current = self.list_widget.currentItem()
        if not current:
            QMessageBox.warning(self, "Hata", "Lütfen bir USB sürücü seçin!")
            return
        device = current.text().split()[0]

        confirm1 = QMessageBox.question(self, "Onay",
                                       f"{device} üzerindeki tüm veriler geri alınamaz şekilde silinecek!\nDevam etmek istediğinize emin misiniz?",
                                       QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm1 != QMessageBox.StandardButton.Yes:
            self.log("İşlem kullanıcı tarafından iptal edildi.")
            return

        confirm2 = QMessageBox.question(self, "Kesin Onay",
                                       "Bu işlem geri alınamaz!\nGerçekten devam etmek istiyor musunuz?",
                                       QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm2 != QMessageBox.StandardButton.Yes:
            self.log("İşlem kullanıcı tarafından iptal edildi.")
            return

        self.format_btn.setEnabled(False)
        self.refresh_btn.setEnabled(False)
        self.log(f"{device} üzerinde sıfırlama ve formatlama işlemi başlatıldı.")
        self.progress.setValue(0)
        QApplication.processEvents()

        try:
            system = platform.system()
            if system == "Linux":
                self.wipe_device_linux(device)
            elif system == "Windows":
                self.wipe_device_windows(device)
            else:
                raise RuntimeError(f"{system} platformu desteklenmiyor.")

            self.progress.setValue(100)
            self.log("İşlem tamamlandı!")
            QMessageBox.information(self, "Başarılı", "USB sürücü başarıyla sıfırlandı ve formatlandı.")
        except Exception as e:
            self.log(f"Hata oluştu: {e}")
            QMessageBox.critical(self, "Hata", f"İşlem başarısız oldu:\n{e}")
        finally:
            self.format_btn.setEnabled(True)
            self.refresh_btn.setEnabled(True)

    def wipe_device_linux(self, device, passes=3):
        for i in range(passes):
            self.log(f"{i+1}. pass: Rastgele veri yazılıyor...")
            self.progress.setValue(int((i / passes) * 100))
            QApplication.processEvents()
            cmd = ['dd', 'if=/dev/urandom', f'of={device}', 'bs=4M', 'status=progress', 'conv=fsync']
            result = subprocess.run(cmd)
            if result.returncode != 0:
                raise RuntimeError(f"{i+1}. pass sırasında hata oluştu!")
            time.sleep(1)

        self.progress.setValue(90)
        QApplication.processEvents()
        self.log("Son pass: Sıfırlarla dolduruluyor...")
        cmd = ['dd', 'if=/dev/zero', f'of={device}', 'bs=4M', 'status=progress', 'conv=fsync']
        result = subprocess.run(cmd)
        if result.returncode != 0:
            raise RuntimeError("Sıfırlama sırasında hata oluştu!")

        self.log("Unmount işlemi yapılıyor...")
        subprocess.run(['umount', device], check=False)

        self.log("FAT32 formatlanıyor...")
        result = subprocess.run(['mkfs.vfat', '-F', '32', device])
        if result.returncode != 0:
            raise RuntimeError("Formatlama başarısız oldu!")
        self.log("Formatlama başarılı.")

    def wipe_device_windows(self, device):
        import ctypes

        # Windows'da USB disk ID'si genelde \\\\.\\PhysicalDriveX formatında
        # Örneğin: \\.\PhysicalDrive1

        # 1) Disk üzerindeki tüm partitionları sil
        self.log("Disk partitionları temizleniyor...")
        disk_number = None
        try:
            if device.lower().startswith(r'\\.\physicaldrive'):
                disk_number = int(device.lower().replace(r'\\.\physicaldrive', ''))
            else:
                raise RuntimeError("Disk numarası tespit edilemedi.")
        except Exception as e:
            raise RuntimeError(f"Disk numarası alınamadı: {e}")

        # Diskpart komutu ile tüm partitionları silmek için script yazalım:
        diskpart_script = f"""
select disk {disk_number}
clean
create partition primary
format fs=fat32 quick
assign
exit
"""
        script_path = "diskpart_script.txt"
        with open(script_path, "w") as f:
            f.write(diskpart_script)

        # Diskpart'ı çalıştır
        result = subprocess.run(["diskpart", "/s", script_path], capture_output=True, text=True, shell=True)
        if result.returncode != 0:
            raise RuntimeError(f"Diskpart formatlama hatası:\n{result.stderr}")

        self.log("Disk başarıyla temizlendi ve FAT32 olarak formatlandı.")

        # Güvenli silme Windows'da genellikle 3-pass random data yazma değil, bu adım isteğe bağlı
        # İstersen daha derin güvenli silme için başka yöntemler entegre edilebilir

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = USBFormatter()
    window.show()
    sys.exit(app.exec())
