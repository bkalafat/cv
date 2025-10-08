# 🎯 Şık CV - Jake's Resume Template (Fotoğraflı)

Bu, **Google, Facebook, Amazon'da en çok kullanılan** CV template'i (6.2k+ GitHub stars)!

## ✨ Özellikler

- ✅ **FAANG Standardı**: Google, Facebook, Amazon mühendisleri tarafından kullanılıyor
- ✅ **Fotoğraflı**: Profesyonel yuvarlak profil fotoğrafı
- ✅ **ATS-Friendly**: Başvuru takip sistemleri tarafından kolayca okunur
- ✅ **Tek Sayfa**: Öz ve güçlü, tüm önemli bilgiler tek sayfada
- ✅ **Modern Tasarım**: Temiz, minimal ve profesyonel

## 🚀 Hemen Başla (3 Adım)

### 1️⃣ Overleaf'e Yükle (EN KOLAY)

1. [Overleaf.com](https://www.overleaf.com)'a git (ücretsiz hesap oluştur)
2. "New Project" → "Upload Project" seç
3. `latex-cv` klasörünü ZIP'le ve yükle
4. Projeyi aç, "Recompile" butonuna bas → **PDF hazır!** 🎉

### 2️⃣ Dosyalar

```
latex-cv/
├── burak_kalafat_resume.tex  ⭐ ANA DOSYA (Jake's Resume)
├── cv.tex                     (AltaCV - alternatif)
├── altacv.cls
├── profile.png                ✅ Sizin fotoğrafınız
└── README-jake.md             (Bu dosya)
```

### 3️⃣ Fotoğrafı Değiştir

Fotoğrafınızı değiştirmek isterseniz:
- `profile.png` dosyasını kendi fotoğrafınızla değiştirin
- Yuvarlak kesim otomatik yapılır
- PNG veya JPG formatı olabilir

## 📊 Template Karşılaştırması

| Template | Popülerlik | Stil | Sayfa | ATS |
|----------|-----------|------|-------|-----|
| **Jake's Resume** ⭐ | 6.2k stars | Modern, Minimal | 1 | ✅✅✅ |
| AltaCV | 2k+ stars | Renkli, 2-kolon | 1-2 | ✅✅ |

## 🎨 Özelleştirme

### Renkleri Değiştir

`burak_kalafat_resume.tex` dosyasında:

```latex
% Başlık rengini değiştir
\color{blue}  % veya red, green, teal, vb.
```

### Bölüm Sırası

Bölümleri istediğiniz sırada düzenleyebilirsiniz:
- Experience (Deneyim)
- Skills (Yetenekler)
- Education (Eğitim)
- Certifications (Sertifikalar)

### Fotoğrafı Kaldır

Fotoğraf istemiyorsanız, dosyanın başındaki bu kısmı silin:

```latex
\begin{minipage}[t]{0.15\textwidth}
...
\end{minipage}%
```

## 🔥 Neden Jake's Resume?

1. **FAANG Onaylı**: En büyük tech şirketleri bu formatı kabul ediyor
2. **ATS Puanı Yüksek**: Otomatik sistemler %95+ oranında doğru okuyor
3. **Recruiter Dostu**: 6 saniyede okunabilir tasarım
4. **GitHub Popüler**: 6.2k star, 1.7k fork

## 📝 İçerik İpuçları

### Deneyim Bölümü
- **Sayılarla Başarı**: "6-8× hızlandırma", "60,000 satır kod"
- **Eylem Fiilleri**: "Migrated", "Architected", "Delivered"
- **Teknolojiler**: Her pozisyon için kullanılan tech stack

### Yetenekler Bölümü
- **Kategorize Et**: Languages, Frameworks, Tools, etc.
- **İlgili Olanlar**: Sadece başvuru için gerekli olanlar

### Özet Bölümü
- **2-3 Cümle**: Kim olduğunuz, ne yaptınız, neden farklısınız
- **Rakamlarla Destekle**: Somut başarılar

## 🆘 Sorun Giderme

### Fotoğraf Görünmüyor
```latex
% Bu satırı kontrol edin:
\includegraphics[width=3cm]{profile.png}
```

### Tek Sayfaya Sığmıyor
- Font boyutunu küçült: `11pt` → `10pt`
- Gereksiz detayları kaldır
- Bullet point sayısını azalt

### Overleaf'te Compile Hatası
- "Recompile from scratch" seçeneğini dene
- Dosya adlarının doğru olduğunu kontrol et

## 📚 Kaynaklar

- [Orijinal Template](https://github.com/sb2nov/resume)
- [Overleaf Galerisi](https://www.overleaf.com/latex/templates/software-engineer-resume/gqxmqsvsbdjf)
- [Resume Best Practices](https://www.techinterviewhandbook.org/resume/)

## 🎓 Pro İpuçları

1. **Action Words Kullan**: Led, Architected, Developed, Implemented
2. **STAR Method**: Situation, Task, Action, Result
3. **Quantify Everything**: Sayılarla kanıtla (%, X×, $, etc.)
4. **Tailored Content**: Her başvuru için özelleştir
5. **Keep it Simple**: Fancy değil, etkili ol

---

**Hazırsınız!** 🚀 Bu CV ile FAANG ve fintech şirketlerine başvurabilirsiniz.

**Önemli:** Overleaf'e yükledikten sonra PDF'i indirin ve `Burak_Kalafat_Resume.pdf` olarak kaydedin.
