# 🎉 Deployment Guide - GitHub'a Yükleme

Bu dosya, projenizi GitHub'a yüklemek ve GitHub Pages'i aktifleştirmek için adım adım talimatlar içerir.

## 📋 Ön Hazırlık

### 1. Profil Fotoğrafı Ekleyin (Opsiyonel)
```bash
# Profil fotoğrafınızı şu konuma kopyalayın:
assets/images/profile.jpg
```
**Not:** 400x400 piksel, kare format önerilir.

---

## 🚀 GitHub'a Yükleme Adımları

### Adım 1: Git Repository'yi Başlat
```powershell
# Proje klasörüne gidin
cd c:\Work\cv

# Git repository'yi başlatın (eğer yoksa)
git init

# Tüm dosyaları stage'e ekleyin
git add .

# İlk commit'i yapın
git commit -m "Initial commit: Professional CV website with auto PDF/DOCX generation"
```

### Adım 2: GitHub'da Repository Oluşturun
1. https://github.com/new adresine gidin
2. Repository ayarları:
   - **Repository name:** `cv` (veya istediğiniz isim)
   - **Description:** "Professional CV/Resume website with automatic PDF and DOCX generation"
   - **Visibility:** Public (GitHub Pages için gerekli)
   - **Initialize with README:** ❌ İşaretsiz bırakın (zaten var)
3. "Create repository" butonuna tıklayın

### Adım 3: Local Repository'yi GitHub'a Bağlayın
```powershell
# GitHub repository URL'inizi buraya yazın
git remote add origin https://github.com/KULLANICI_ADINIZ/cv.git

# Ana branch'i main olarak ayarlayın
git branch -M main

# Kodu GitHub'a push edin
git push -u origin main
```

**⚠️ ÖNEMLİ:** `KULLANICI_ADINIZ` yerine kendi GitHub kullanıcı adınızı yazın!

Örnek:
```powershell
git remote add origin https://github.com/bkalafat/cv.git
```

---

## 🌐 GitHub Pages'i Aktifleştirme

### Adım 4: GitHub Pages Ayarları
1. GitHub repository'nizde **Settings** sekmesine gidin
2. Sol menüden **Pages** seçin
3. **Source** bölümünde:
   - **Source:** Deploy from a branch
   - **Branch:** `gh-pages` seçin (workflow tarafından otomatik oluşturulacak)
   - **Folder:** `/ (root)` seçin
4. **Save** butonuna tıklayın

### Adım 5: URL'leri Güncelleyin
`_config.yml` dosyasını düzenleyin:

```yaml
baseurl: "/cv"  # Repository adınız
url: "https://KULLANICI_ADINIZ.github.io"  # GitHub kullanıcı adınız
```

Örnek:
```yaml
baseurl: "/cv"
url: "https://bkalafat.github.io"
```

Değişiklikleri commit ve push edin:
```powershell
git add _config.yml
git commit -m "Update URLs for GitHub Pages"
git push
```

---

## ⏳ İlk Build'i Bekleyin

### Adım 6: GitHub Actions'ı Kontrol Edin
1. Repository'de **Actions** sekmesine gidin
2. "Build and Deploy CV" workflow'unun çalıştığını görmelisiniz
3. Yaklaşık 2-3 dakika bekleyin
4. ✅ Yeşil tik işareti görünce build başarılı demektir

---

## 🎊 Web Sitenizi Ziyaret Edin!

Build tamamlandıktan sonra:

**🌐 CV Web Siteniz:** https://KULLANICI_ADINIZ.github.io/cv

Örnek: https://bkalafat.github.io/cv

---

## 📥 PDF ve DOCX'i İndirin

### Actions Artifacts'tan İndirme
1. Repository'de **Actions** sekmesine gidin
2. Son başarılı workflow'a tıklayın
3. Sayfanın altında **Artifacts** bölümünü bulun
4. İndirin:
   - `cv-pdf`: HTML'den oluşturulan PDF
   - `cv-docx`: Markdown'dan oluşturulan DOCX ve PDF

### Manuel PDF İndirme
1. Web sitenizi açın
2. `Ctrl+P` (Windows) veya `Cmd+P` (Mac) basın
3. "Save as PDF" seçin
4. Kaydedin

---

## 🔄 CV'nizi Güncellemek

CV'nizi her güncellemek istediğinizde:

```powershell
# Değişiklikleri yapın (_data/*.yml dosyalarını düzenleyin)

# Git'e ekleyin
git add .

# Commit edin
git commit -m "Update CV: [değişiklik açıklaması]"

# GitHub'a push edin
git push
```

**🚀 Otomatik:** Push sonrası GitHub Actions otomatik olarak:
- Web sitesini yeniden build eder
- GitHub Pages'e deploy eder
- Yeni PDF ve DOCX oluşturur

---

## 🛠️ Troubleshooting

### Build Hatası
**Sorun:** Actions'da kırmızı X işareti görüyorum
**Çözüm:**
1. Actions'da hatalı workflow'a tıklayın
2. Hata mesajını okuyun
3. YAML syntax hatası varsa düzeltin
4. Tekrar push edin

### GitHub Pages Açılmıyor
**Sorun:** Site URL'i 404 hatası veriyor
**Çözüm:**
1. Settings → Pages'den GitHub Pages'in aktif olduğunu kontrol edin
2. `gh-pages` branch'inin oluştuğunu kontrol edin
3. 5 dakika bekleyin (ilk deployment biraz uzun sürebilir)
4. Browser cache'i temizleyin (`Ctrl+F5`)

### Workflow Çalışmıyor
**Sorun:** Actions'da workflow görünmüyor
**Çözüm:**
1. `.github/workflows/` klasörünün doğru konumda olduğunu kontrol edin
2. YAML dosyalarının `.yml` uzantısı olduğunu kontrol edin
3. Bir değişiklik yapıp push edin (workflow'u tetiklemek için)

---

## 📞 Yardım

Sorun yaşarsanız:
1. README.md dosyasındaki troubleshooting bölümüne bakın
2. GitHub Issues'da benzer sorunları arayın
3. Yeni issue açın

---

## ✅ Checklist

Deploy ettikten sonra kontrol edin:
- [ ] Web sitesi açılıyor
- [ ] Tüm bilgiler doğru görünüyor
- [ ] Linkler çalışıyor (GitHub, LinkedIn)
- [ ] Mobil görünüm düzgün
- [ ] PDF oluşturma çalışıyor
- [ ] DOCX oluşturma çalışıyor
- [ ] Print to PDF tarayıcıdan çalışıyor

---

**🎉 Tebrikler! CV web siteniz hazır!**

---

**Son Güncelleme:** Ekim 2025
