import sys
import subprocess
import time
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
                             QListWidget, QMessageBox, QProgressBar, QTextEdit, QHBoxLayout)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class SDFormatter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Güvenli SD Kart Format Aracı")
        self.setGeometry(300, 200, 600, 500)
        self.setWindowIcon(QIcon("icon.png"))  # Eğer özel ikon eklenecekse

        main_layout = QVBoxLayout()

        title_label = QLabel("<h2>Güvenli SD Kart Format Aracı</h2>")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        self.list_widget = QListWidget()
        main_layout.addWidget(QLabel("Bulunan SD Kartlar:"))
        main_layout.addWidget(self.list_widget)

        button_layout = QHBoxLayout()
        self.refresh_btn = QPushButton("SD Kartları Yenile")
        self.refresh_btn.clicked.connect(self.refresh_devices)
        button_layout.addWidget(self.refresh_btn)

        self.format_btn = QPushButton("Seçili SD Kartı Sıfırla ve Formatla")
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
        devices = self.get_sd_cards()
        if not devices:
            self.log("SD kart bulunamadı.")
        else:
            for dev in devices:
                self.list_widget.addItem(f"{dev['name']} - {dev['size']} - {dev['model']}")
            self.log(f"{len(devices)} adet SD kart bulundu.")
        self.format_btn.setEnabled(bool(devices))

    def get_sd_cards(self):
        try:
            result = subprocess.run(['lsblk', '-o', 'NAME,SIZE,MODEL,RM', '-J'], capture_output=True, text=True)
            import json
            data = json.loads(result.stdout)
            sd_cards = []
            for block in data['blockdevices']:
                if block.get('rm') == 1:
                    sd_cards.append({
                        'name': '/dev/' + block['name'],
                        'size': block['size'],
                        'model': block.get('model', 'Bilinmiyor')
                    })
            return sd_cards
        except Exception as e:
            self.log(f"Hata: {e}")
            return []

    def format_selected(self):
        current = self.list_widget.currentItem()
        if not current:
            QMessageBox.warning(self, "Hata", "Lütfen bir SD kart seçin!")
            return
        device = current.text().split()[0]

        # 1. onay
        confirm1 = QMessageBox.question(self, "Onay",
                                       f"{device} üzerindeki tüm veriler geri alınamaz şekilde silinecek!\nDevam etmek istediğinize emin misiniz?",
                                       QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm1 != QMessageBox.StandardButton.Yes:
            self.log("İşlem kullanıcı tarafından iptal edildi.")
            return

        # 2. onay (fazla emin olmak için)
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
            self.wipe_device(device)
            self.progress.setValue(100)
            self.log("İşlem tamamlandı!")
            QMessageBox.information(self, "Başarılı", "SD kart başarıyla sıfırlandı ve formatlandı.")
        except Exception as e:
            self.log(f"Hata oluştu: {e}")
            QMessageBox.critical(self, "Hata", f"İşlem başarısız oldu:\n{e}")
        finally:
            self.format_btn.setEnabled(True)
            self.refresh_btn.setEnabled(True)

    def wipe_device(self, device, passes=3):
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SDFormatter()
    window.show()
    sys.exit(app.exec())
