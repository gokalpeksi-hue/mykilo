# 📉 MyKilo — Kilo & Vücut Analizi Takip

Günlük kilonu gir, otomatik hafızaya alınsın. Her tartında **VKİ (Vücut Kitle İndeksi)**
ve **kilo dilimin** (zayıf / sağlıklı / fazla kilolu / obez) anında hesaplanır. Gelişimini
**günlük · haftalık · aylık · yıllık** olarak hem grafik hem sayısal takip et.

> Telefonda **"Ana ekrana ekle"** dediğinde tam ekran bir uygulama gibi açılır,
> internet olmadan da çalışır (PWA).

**Canlı:** https://gokalpeksi-hue.github.io/mykilo/

---

## Özellikler

- **📷 Ekran görüntüsünden / fotoğraftan otomatik okuma** — Akıllı tartı uygulamanın
  (Mi Fitness, Zepp Life, vb.) ekran görüntüsünü yükle; **kilo, vücut yağı %, iskelet kas
  kütlesi, viseral yağ, bazal metabolizma, su oranı, kemik mineral, protein %, yağsız kütle**
  değerleri otomatik okunup forma yazılır. (Claude vision; sunucu üzerinden.)
- **VKİ + kilo dilimi** — Boy bilgisiyle her kiloda otomatik hesaplanır ve renkli rozetle gösterilir.
- **Profil** — Yaş, boy, cinsiyet, hedef kilo. Hedefe kaç kilo kaldığını söyler;
  hedef yoksa sağlıklı kilo aralığını gösterir.
- **Trend grafikleri** — Günlük / haftalık / aylık / yıllık kilo gelişimi (SVG çizgi grafik) +
  her dönem için sayısal tablo (ortalama, değişim Δ, min, max, adet).
- **Özet panosu** — Güncel kilo, VKİ, başlangıçtan değişim, son 7/30 gün değişimi, toplam kayıt.
- **💾 Yedek (Drive)** — Tek tuşla tüm verini `.json` indir, Google Drive'a yükle;
  yeni cihazda dosyayı seçerek geri yükle.
- **☁️ Cihazlar arası senkron** — Bir "senkron kodu" gir; web ve mobilde aynı kod girilince
  veriler sunucuda saklanıp otomatik eşitlenir. Çevrimdışıyken cihazda durur, internet gelince yüklenir.
- **Çevrimdışı çalışır** — Tüm veriler tarayıcıda (localStorage) tutulur; service worker ile çevrimdışı açılır.

---

## Kilo dilimleri (VKİ)

| VKİ | Dilim |
|----|------|
| < 18,5 | Zayıf |
| 18,5 – 24,9 | Sağlıklı |
| 25,0 – 29,9 | Fazla kilolu |
| 30,0 – 34,9 | Obez (I. derece) |
| 35,0 – 39,9 | Obez (II. derece) |
| ≥ 40,0 | Aşırı obez (III. derece) |

> VKİ bir sağlık taramasıdır, tıbbi teşhis değildir. Kas kütlesi yüksek kişilerde yanıltıcı olabilir.

---

## Kurulum / Yayın

Statik bir PWA'dır; backend gerektirmez (yalnızca fotoğraftan okuma ve senkron için bir API kullanılır).

- **GitHub Pages:** Repo ayarlarından Pages → `main` / `root` seçilir.
- **Görsel okuma sunucusu:** Uygulama, Ayarlar > Gelişmiş alanında belirtilen API'yi
  (`/api/vision-weight`) çağırır. Varsayılan: `https://urun-fiyat-takip.onrender.com`.
  Bu uç nokta `ANTHROPIC_API_KEY` ile çalışır ve anahtar yalnızca sunucuda tutulur.

## Teknoloji

- Tek dosya HTML/CSS/JS (framework yok), SVG grafikler, localStorage.
- PWA: `manifest.webmanifest` + `sw.js` (offline-first).
- İkon/logo: `tools/make_icons.py` (Pillow) ile üretilir; iç logo `logo.svg`.

## Gizlilik

Verilerin cihazında kalır. Senkron kodu kullanırsan sadece o veri sunucuda saklanır.
Fotoğraftan okuma sırasında görsel, değer çıkarımı için görüntü işleme sunucusuna gönderilir.
