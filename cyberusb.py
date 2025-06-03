<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 Cyberwelat USB Formatter | Ultimate Silme Aracı</title>
    <style>
        body {
            background-color: #000;
            color: #0f0;
            font-family: 'Courier New', monospace;
            margin: 0;
            padding: 20px;
            overflow-x: hidden;
        }
        
        .matrix-rain {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.3;
            pointer-events: none;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            border: 1px dashed #0f0;
            padding: 20px;
            position: relative;
            background-color: rgba(0, 0, 0, 0.7);
        }
        
        h1, h2, h3 {
            color: #0f0;
            text-shadow: 0 0 5px #0f0;
        }
        
        h1 {
            border-bottom: 1px solid #0f0;
            padding-bottom: 10px;
            text-align: center;
            font-size: 2.5em;
        }
        
        a {
            color: #0ff;
            text-decoration: none;
        }
        
        a:hover {
            text-decoration: underline;
            text-shadow: 0 0 10px #0ff;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        
        th, td {
            border: 1px solid #0f0;
            padding: 10px;
            text-align: left;
        }
        
        th {
            background-color: #020;
        }
        
        .code-block {
            background-color: #111;
            padding: 15px;
            border-left: 3px solid #0f0;
            margin: 15px 0;
            overflow-x: auto;
        }
        
        .warning {
            color: #f00;
            animation: blink 1s infinite;
        }
        
        @keyframes blink {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        
        .floating {
            position: absolute;
            animation: float 10s infinite ease-in-out;
            opacity: 0.7;
            font-size: 0.8em;
        }
        
        @keyframes float {
            0% { transform: translate(0, 0) rotate(0deg); }
            25% { transform: translate(50px, 20px) rotate(5deg); }
            50% { transform: translate(100px, 0) rotate(0deg); }
            75% { transform: translate(50px, -20px) rotate(-5deg); }
            100% { transform: translate(0, 0) rotate(0deg); }
        }
    </style>
</head>
<body>
    <canvas id="matrix" class="matrix-rain"></canvas>
    
    <!-- Uçan elementler -->
    <div class="floating" style="top: 10%; left: 5%;">01010101</div>
    <div class="floating" style="top: 30%; left: 80%;">01110011</div>
    <div class="floating" style="top: 70%; left: 15%;">01100010</div>
    <div class="floating" style="top: 85%; left: 70%;">01000110</div>
    <div class="floating" style="top: 20%; left: 50%;">01101111</div>
    
    <div class="container">
        <h1>🔥 Cyberwelat USB Formatter</h1>
        <h2>🚀 Ultimate Güvenli Silme Aracı</h2>
        
        <p><strong>⚡ Ne Yapar?</strong><br>
        Bu araç, USB belleklerinizi <strong>askeri standartlarda</strong> temizler. Önce rastgele verilerle üzerine yazar, sonra sıfırlarla doldurur ve <strong>FAT32</strong> format atar. Verileriniz <span class="warning">kurtarılamaz</span> hale gelir!</p>
        
        <h3>⏱️ Tahmini Süre Hesaplama</h3>
        <p>Süre, USB'nizin boyutuna ve pass sayısına göre değişir:</p>
        
        <table>
            <tr>
                <th>Kapasite</th>
                <th>1-Pass Süresi</th>
                <th>3-Pass Süresi</th>
                <th>7-Pass Süresi</th>
            </tr>
            <tr>
                <td><strong>16GB</strong></td>
                <td>~2-3 dakika</td>
                <td>~6-8 dakika</td>
                <td>~15-20 dakika</td>
            </tr>
            <tr>
                <td><strong>32GB</strong></td>
                <td>~4-5 dakika</td>
                <td>~12-15 dakika</td>
                <td>~25-35 dakika</td>
            </tr>
            <tr>
                <td><strong>64GB</strong></td>
                <td>~8-10 dakika</td>
                <td>~20-25 dakika</td>
                <td>~45-60 dakika</td>
            </tr>
        </table>
        
        <p><em>💡 Not: USB 3.0 cihazlarda 2x daha hızlı!</em></p>
        
        <h3>🛠️ Nasıl Kullanılır?</h3>
        <div class="code-block">
            1. [✔] USB Tak ➔ Aracı <strong>Yönetici Olarak</strong> Aç<br>
            2. [🔍] <strong>Cihazı Seç</strong> ➔ "Formatla" Butonuna Bas<br>
            3. [⚠️] <strong>Çift Onay Ver</strong> ➔ İşlem Başlasın!<br>
            4. [✓] <strong>Bittiğinde</strong> ➔ USB'niz tertemiz!
        </div>
        
        <h3>⚙️ Ayarlar Menüsü</h3>
        <ul>
            <li><strong>Pass Sayısı</strong> (1-7 arası seçim)</li>
            <ul>
                <li><em>1-Pass</em>: Hızlı (Temel güvenlik)</li>
                <li><em>3-Pass</em>: Önerilen (DOD 5220.22-M standartı)</li>
                <li><em>7-Pass</em>: Paranoyak mod (NSA seviye silme)</li>
            </ul>
        </ul>
        
        <h3>💡 Pro Tavsiyeler</h3>
        <ul>
            <li>🔒 <strong>Gizli veriler</strong> için 3-Pass+ kullanın</li>
            <li>⚠️ USB'yi <strong>çıkarmayın</strong> ve PC'nin <strong>uyku moduna</strong> geçmesine izin vermeyin</li>
            <li>🖥️ <strong>Arka plan programlarını</strong> kapatın (hızı artırır)</li>
        </ul>
        
        <h3>🌟 Neden Bu Araç?</h3>
        <ul>
            <li>🛡️ <strong>%100 Güvenli</strong>: Verileriniz fiziksel olarak silinir</li>
            <li>🚀 <strong>Tek Tıkla Format</strong>: Karmaşık işlem yok</li>
            <li>📛 <strong>Veri Sızıntısı Yok</strong>: Disk bölümlerini bile temizler</li>
        </ul>
        
        <blockquote>
            "Bir pass yeter diyenlere inat, verilerim 7 pass gider!"<br>
            - <strong>Cyberwelat</strong>
        </blockquote>
        
        <div class="warning">
            <h3>⚠️ Uyarı</h3>
            <p>Bu araç USB'nizdeki TÜM verileri siler! Yedek almayı unutmayın!</p>
        </div>
        
        <p><strong>📥 Download & Detaylar:</strong><br>
        <a href="/cyberusbv2.exe" target="_blank"> CYBER USB V2 /cyberwelat</a><br>
        <strong>🔐 GPLv3 Lisansı</strong> - Özgürce kullanın, paylaşın!</p>
    </div>

    <script>
        // Matrix rain effect
        const canvas = document.getElementById('matrix');
        const ctx = canvas.getContext('2d');
        
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        const katakana = 'アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズブヅプエェケセテネヘメレヱゲゼデベペオォコソトノホモヨョロヲゴゾドボポヴッン';
        const latin = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        const nums = '0123456789';
        
        const alphabet = katakana + latin + nums;
        
        const fontSize = 16;
        const columns = canvas.width / fontSize;
        
        const rainDrops = [];
        
        for (let x = 0; x < columns; x++) {
            rainDrops[x] = 1;
        }
        
        const draw = () => {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.fillStyle = '#0f0';
            ctx.font = fontSize + 'px monospace';
            
            for (let i = 0; i < rainDrops.length; i++) {
                const text = alphabet.charAt(Math.floor(Math.random() * alphabet.length));
                ctx.fillText(text, i * fontSize, rainDrops[i] * fontSize);
                
                if (rainDrops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    rainDrops[i] = 0;
                }
                rainDrops[i]++;
            }
        };
        
        setInterval(draw, 30);
        
        // Floating elements animation
        const floatingElements = document.querySelectorAll('.floating');
        floatingElements.forEach(el => {
            const duration = 10 + Math.random() * 20;
            const delay = Math.random() * 10;
            el.style.animationDuration = `${duration}s`;
            el.style.animationDelay = `${delay}s`;
        });
        
        // Resize handler
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });
    </script>
</body>
</html>
