# GitHub Pages + Jekyll Modern CV Projesi - İş Planı

## 📋 Proje Özeti
Burak Kalafat'ın özgeçmişini GitHub Pages + Jekyll Modern Resume Theme kullanarak web sitesine dönüştürme ve GitHub Actions ile otomatik PDF/DOCX oluşturma projesi.

## 🎯 Hedefler
- ✅ Modern ve profesyonel görünümlü web CV
- ✅ Tek kaynak (Markdown/YAML) - çoklu çıktı (Web/PDF/DOCX)
- ✅ GitHub Actions ile otomatik build
- ✅ Kolay güncelleme ve bakım

---

## 📝 Görevler (Tasks)

### Task 1: 🏗️ Proje Yapısını Oluştur
**Durum:** ⏳ Yapılacak  
**Açıklama:** GitHub Pages + Jekyll için temel dizin yapısını oluştur
**Detaylar:**
- Jekyll projesi için gerekli klasörleri oluştur
- `_config.yml` (Jekyll konfigürasyon dosyası)
- `_data/` klasörü (CV verilerini içerecek)
- `assets/` klasörü (görseller, CSS, vb.)
- `.github/workflows/` klasörü (GitHub Actions için)
- `Gemfile` (Ruby bağımlılıkları)
- `.gitignore` dosyası

---

### Task 2: 📄 CV İçeriğini Markdown/YAML Formatına Çevir
**Durum:** ⏳ Yapılacak  
**Açıklama:** Mevcut CV'deki bilgileri modern-resume-theme formatına uygun YAML dosyalarına dönüştür
**Detaylar:**
- PDF/DOCX'ten bilgileri çıkar
- `_config.yml` dosyasına kişisel bilgileri ekle
- İletişim bilgileri (email, GitHub, LinkedIn)
- Özet/Profil bölümü
- Deneyim bilgileri
- Eğitim bilgileri
- Beceriler (Skills)
- Projeler
- Sertifikalar/Başarılar

---

### Task 3: 🎨 Modern Resume Theme'i Entegre Et
**Durum:** ⏳ Yapılacak  
**Açıklama:** Jekyll Modern Resume Theme'i projeye ekle ve yapılandır
**Detaylar:**
- `Gemfile`'a theme bağımlılığını ekle
- `_config.yml`'de theme'i aktifleştir
- Modern resume theme layout'larını yapılandır
- Renk şeması ve stil ayarları
- Responsive tasarım kontrolü

---

### Task 4: 🔧 GitHub Pages Yapılandırması
**Durum:** ⏳ Yapılacak  
**Açıklama:** GitHub Pages için gerekli ayarları yap
**Detaylar:**
- `_config.yml`'de GitHub Pages URL'lerini ayarla
- Base URL ve site URL ayarları
- Repository ayarları
- GitHub Pages branch yapılandırması (genellikle `gh-pages` veya `main`)
- `index.md` veya `index.html` oluştur

---

### Task 5: ⚙️ GitHub Actions Workflow - PDF Oluşturma
**Durum:** ⏳ Yapılacak  
**Açıklama:** Her commit'te otomatik PDF oluşturan GitHub Actions workflow'u ekle
**Detaylar:**
- `.github/workflows/build-resume.yml` dosyası oluştur
- Jekyll site'ı build et
- Headless Chrome veya wkhtmltopdf ile HTML'i PDF'e çevir
- Alternatif: Pandoc ile Markdown'dan direkt PDF
- PDF'i artifact olarak kaydet veya repository'ye commit et
- Trigger: push to main branch

---

### Task 6: 📝 GitHub Actions Workflow - DOCX Oluşturma
**Durum:** ⏳ Yapılacak  
**Açıklama:** Pandoc kullanarak Markdown'dan DOCX oluşturan workflow ekle
**Detaylar:**
- Pandoc'u GitHub Actions'a yükle
- Markdown dosyalarını DOCX'e çevir
- Template kullanarak profesyonel görünüm
- DOCX'i artifact olarak kaydet veya repository'ye commit et
- PDF ile aynı workflow'da birleştir

---

### Task 7: 🖼️ Görseller ve Assets
**Durum:** ⏳ Yapılacak  
**Açıklama:** Profil fotoğrafı ve diğer görselleri ekle
**Detaylar:**
- `assets/images/` klasörü oluştur
- Profil fotoğrafı ekle (varsa)
- Favicon oluştur
- Gerekli icon'ları ekle
- Görselleri optimize et

---

### Task 8: 📱 Responsive ve Accessibility Kontrolleri
**Durum:** ⏳ Yapılacak  
**Açıklama:** Mobil uyumluluk ve erişilebilirlik testleri
**Detaylar:**
- Mobil görünüm testi
- Tablet görünüm testi
- Desktop görünüm testi
- Accessibility kontrolleri (ARIA labels, alt texts)
- Print CSS kontrolleri (web'den PDF alırken)

---

### Task 9: 📦 Repository Oluştur ve Deploy Et
**Durum:** ⏳ Yapılacak  
**Açıklama:** GitHub'da repository oluştur ve ilk deployment'ı yap
**Detaylar:**
- GitHub'da yeni public repository oluştur (örn: `cv` veya `resume`)
- Local projeyi GitHub'a push et
- GitHub Pages'i aktifleştir (Settings → Pages)
- İlk build'in başarılı olduğunu kontrol et
- Web sitesinin çalıştığını doğrula (username.github.io/repo-name)

---

### Task 10: 🧪 Test ve Doğrulama
**Durum:** ⏳ Yapılacak  
**Açıklama:** Tüm özelliklerin çalıştığını test et
**Detaylar:**
- Web sitesi erişilebilirliği
- Tüm linklerin çalıştığını kontrol et
- PDF oluşturma workflow'unun çalıştığını test et
- DOCX oluşturma workflow'unun çalıştığını test et
- Responsive tasarımı farklı cihazlarda test et
- Print to PDF özelliğini tarayıcıdan test et

---

### Task 11: 📖 README.md ve Dokümantasyon
**Durum:** ⏳ Yapılacak  
**Açıklama:** Proje dokümantasyonunu oluştur
**Detaylar:**
- `README.md` dosyası oluştur
- Proje açıklaması
- Kurulum talimatları (local development)
- CV'yi güncelleme rehberi
- Deployment rehberi
- Lisans bilgisi
- Teşekkürler ve kaynaklar

---

### Task 12: ⚡ Optimizasyon ve İyileştirmeler
**Durum:** ⏳ Yapılacak  
**Açıklama:** Performance ve SEO optimizasyonları
**Detaylar:**
- SEO meta tagları ekle
- Open Graph tagları (sosyal medya paylaşımları için)
- Google Analytics entegrasyonu (opsiyonel)
- Sitemap oluştur
- robots.txt ekle
- Sayfa yükleme hızı optimizasyonu

---

## 🛠️ Kullanılacak Teknolojiler

### Ana Teknolojiler
- **Jekyll**: Static site generator
- **modern-resume-theme**: Jekyll teması
- **GitHub Pages**: Hosting
- **GitHub Actions**: CI/CD
- **Pandoc**: Markdown → DOCX/PDF dönüşümü

### Yardımcı Araçlar
- **YAML**: Veri yapılandırma
- **Markdown**: İçerik yazımı
- **Ruby Gems**: Jekyll bağımlılıkları
- **wkhtmltopdf veya puppeteer**: HTML → PDF

---

## 📚 Kaynaklar
- [modern-resume-theme GitHub](https://github.com/sproogen/modern-resume-theme)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Pandoc Documentation](https://pandoc.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

## 🎓 Öğrenme Hedefleri
- Jekyll static site generator kullanımı
- GitHub Pages deployment
- GitHub Actions workflow oluşturma
- YAML veri yapılandırma
- Markdown best practices
- CI/CD pipeline kurulumu

---

## ✅ Başarı Kriterleri
- [ ] Web sitesi username.github.io/repo-name adresinden erişilebilir
- [ ] CV bilgileri güncel ve eksiksiz
- [ ] Her commit'te otomatik PDF ve DOCX üretiliyor
- [ ] Site mobile-responsive
- [ ] Print-to-PDF tarayıcıdan düzgün çalışıyor
- [ ] Tüm linkler çalışıyor
- [ ] README dokümantasyonu tamamlanmış

---

## 📅 Tahmini Süre
- **Toplam**: 2-3 saat
- Task 1-4: 45 dakika (Temel yapı)
- Task 5-6: 45 dakika (GitHub Actions)
- Task 7-10: 45 dakika (Test ve içerik)
- Task 11-12: 30 dakika (Dokümantasyon ve optimizasyon)

---

## 📝 Notlar
- Modern resume theme Jekyll 3.9+ gerektirir
- GitHub Pages otomatik Jekyll build yapar
- PDF/DOCX'ler `output/` klasöründe veya GitHub Releases'de saklanabilir
- Her güncelleme sonrası ~2-3 dakika deployment süresi
- Custom domain opsiyonel olarak eklenebilir

---

**Oluşturulma Tarihi:** 8 Ekim 2025  
**Proje Sahibi:** Burak Kalafat  
**Versiyon:** 1.0
