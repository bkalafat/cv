# LaTeX CV Generator

Bu proje, Jekyll web CV'nizden otomatik olarak profesyonel bir LaTeX CV oluşturur.

## 🎯 Özellikler

- ✅ **AltaCV Template**: Yazılım mühendisleri arasında en popüler LaTeX CV template'i
- ✅ **Otomatik Generate**: YAML verilerinizden otomatik LaTeX üretir
- ✅ **Tek Kaynak**: CV verilerinizi tek yerden yönetin (YAML dosyaları)
- ✅ **Profesyonel Tasarım**: Modern, temiz ve ATS-uyumlu

## 📋 Gereksinimler

- Python 3.12+ (✅ Yüklendi)
- PyYAML (✅ Yüklendi)
- LaTeX distribution (MiKTeX veya TeX Live) - PDF oluşturmak için

## 🚀 Kullanım

### 1. LaTeX CV Oluşturma

```powershell
python generate_latex_cv.py
```

Bu komut:
- `_data/data.yml`, `_data/experience.yml`, `_data/education.yml` dosyalarını okur
- `latex-cv/cv.tex` dosyası oluşturur
- Tüm bilgilerinizi LaTeX formatına çevirir

### 2. PDF Oluşturma (3 Seçenek)

#### Seçenek A: Overleaf (En Kolay - Önerilen) ⭐

1. [Overleaf.com](https://www.overleaf.com)'a gidin ve ücretsiz hesap oluşturun
2. "New Project" → "Upload Project" seçin
3. `latex-cv` klasörünü ZIP'leyip yükleyin
4. Projeyi açın ve "Recompile" butonuna basın
5. PDF'i indirin!

**Avantajlar:**
- ✅ Kurulum gerektirmez
- ✅ Online, her yerden erişilebilir
- ✅ Otomatik compile
- ✅ Gerçek zamanlı önizleme

#### Seçenek B: MiKTeX (Windows için lokal kurulum)

1. [MiKTeX](https://miktex.org/download) indirin ve kurun
2. Terminal'de şu komutları çalıştırın:

```powershell
cd latex-cv
pdflatex cv.tex
```

#### Seçenek C: TeX Live (Cross-platform)

1. [TeX Live](https://www.tug.org/texlive/) indirin ve kurun
2. Terminal'de şu komutları çalıştırın:

```powershell
cd latex-cv
pdflatex cv.tex
```

## 🔄 Workflow

### CV Güncelleme İş Akışı

1. **YAML dosyalarını güncelleyin** (`_data/*.yml`)
2. **Web CV'yi test edin** (Jekyll serve)
3. **LaTeX CV'yi generate edin**: `python generate_latex_cv.py`
4. **PDF oluşturun** (Overleaf veya lokal LaTeX)

### Tek Komutla Güncelleme

```powershell
# CV verilerini güncelle ve LaTeX generate et
python generate_latex_cv.py
```

## 📁 Dosya Yapısı

```
cv/
├── _data/
│   ├── data.yml          # Kişisel bilgiler, yetenekler
│   ├── experience.yml    # İş deneyimleri
│   └── education.yml     # Eğitim bilgileri
├── latex-cv/
│   ├── altacv.cls       # AltaCV template class dosyası
│   └── cv.tex           # Generate edilen LaTeX CV (otomatik)
└── generate_latex_cv.py # Python generator script
```

## 🎨 Özelleştirme

### Renk Teması Değiştirme

`generate_latex_cv.py` dosyasında renk kodlarını değiştirebilirsiniz:

```python
\definecolor{PrimaryColor}{HTML}{0E4C92}    # Ana renk (başlıklar)
\definecolor{SecondaryColor}{HTML}{1A73E8}  # İkincil renk (tagline)
\definecolor{AccentColor}{HTML}{34A853}     # Vurgu rengi (linkler)
```

### Layout Ayarları

`cv.tex` dosyasında:

```latex
\columnratio{0.6}  # Sol/sağ kolon oranı (0.6 = %60 sol, %40 sağ)
```

## 🌟 AltaCV Template Hakkında

AltaCV, yazılım mühendisleri ve teknik profesyoneller arasında **en popüler LaTeX CV template'lerinden biri**:

- ⭐ GitHub'da binlerce star
- ✅ Modern ve temiz tasarım
- ✅ ATS (Applicant Tracking System) uyumlu
- ✅ İki kolonlu responsive layout
- ✅ Overleaf tarafından önerilen

**Kaynak:** [AltaCV GitHub Repo](https://github.com/liantze/altacv)

## 📝 Notlar

- Python script her çalıştırıldığında `cv.tex` dosyası yeniden oluşturulur
- YAML dosyalarınızda **special characters** (%, $, #, &, _) varsa otomatik escape edilir
- Markdown formatı (`**bold**`, `- bullets`) otomatik LaTeX'e çevrilir

## 🆘 Sorun Giderme

### "Package not found" hatası

Overleaf kullanıyorsanız: Otomatik çözülür, tüm paketler mevcuttur.

Lokal kullanıyorsanız: MiKTeX eksik paketleri otomatik indirir.

### Font bulunamadı hatası

`cv.tex` dosyasında font satırlarını yorum satırı yapın:

```latex
% \usepackage[rm]{roboto}
% \usepackage[defaultsans]{lato}
```

### Python bulunamadı

PowerShell'i kapatıp yeniden açın veya:

```powershell
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
```

## 🎓 Kaynaklar

- [Overleaf Learn LaTeX](https://www.overleaf.com/learn)
- [AltaCV Documentation](https://github.com/liantze/altacv/blob/main/README.md)
- [CTAN: Comprehensive TeX Archive Network](https://www.ctan.org/)

## 📧 Destek

Sorularınız için:
- GitHub Issues açın
- [Overleaf Gallery - CV Templates](https://www.overleaf.com/gallery/tagged/cv)

---

**Not:** Bu sistem Jekyll web CV'nizi ve LaTeX PDF CV'nizi **tek bir veri kaynağından** (YAML) besler. Bilgilerinizi güncellediğinizde, hem web hem de PDF otomatik güncellenir! 🚀
