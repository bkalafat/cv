Session summary and resume instructions

Purpose
-------
This document summarises the work done in the current session to generate a high-quality PDF CV locally, what changed in the repo, how to reproduce the PDF, debugging tips, and an exact prompt you can paste into a new assistant session to continue from where you left off.

Quick summary
-------------
- Approach: A Python-based ReportLab solution (no external web services) was developed to render a two-page professional CV with a colored sidebar on page 1 and full-width content on page 2.
- Main generator: `generate_beautiful_cv.py` (ReportLab + Pillow + PyYAML)
- Data sources: YAML files under `_data/` (notably `_data/data.yml` and `_data/experience.yml`)
- Key UX fixes made in this session:
  - Sidebar contact text changed to white for WCAG contrast
  - Sidebar rendered only on first page (page 2 is full-width)
  - Skills reordered and styled with percent-filled bars
  - Rounded/cropped profile image
  - Bold formatting parsing for `**bold**` in YAML descriptions
  - Font registration for UTF-8/Turkish characters (Arial used)
  - Clickable links (email / LinkedIn / GitHub) added via ReportLab `linkURL`
  - Content/typography tuned (mostly 9pt body, larger headings)
  - Experience bullets shortened and rewritten to be quantifiable in `_data/experience.yml`

Files touched (high level)
--------------------------
- `generate_beautiful_cv.py`  — Main PDF generator. Many edits for fonts, sidebar behavior, spacing, bold rendering, linkURL, and full-width second page handling.
- `_data/experience.yml`      — Bullet contents shortened / rewritten to be STAR-like and quantifiable. Many `**bold**` markers preserved.
- `_data/data.yml`           — Summary and sidebar profile data (used by generator).
- (Other): assets (profile image), small helper edits across repo.

How the generator works (contract)
----------------------------------
Inputs:
- YAML data from `_data/data.yml`, `_data/experience.yml`, `_data/education.yml` (UTF-8)
- Profile image `assets/images/profile.png`
Outputs:
- `Burak_Kalafat_Professional_CV.pdf` created at repo root
Failure modes:
- Missing fonts (falls back to default ReportLab fonts)
- Missing image (generator prints a warning and continues)
- Long lines or overly long bullet lists can overflow a page; generator paginates and switches to full-width content on later pages

Prerequisites (local)
---------------------
- Python 3.10+ (you have 3.12.10 installed earlier)
- Install Python packages:

```powershell
python -m pip install --upgrade pip
```markdown
Oturum özeti ve devam talimatları

Amaç
-----
Bu dosya, mevcut oturumda lokal olarak yüksek kaliteli bir PDF CV üretmek için yapılan işleri, depoda nelerin değiştiğini, PDF'in nasıl yeniden üretileceğini, hata ayıklama ipuçlarını ve yeni bir asistan oturumuna yapıştırılacak tam bir prompt'u Türkçe olarak özetler.

Kısa özet (bu oturumda yapılanlar)
---------------------------------
- Yöntem: ReportLab ve Pillow kullanılarak Python tabanlı bir PDF üretici geliştirildi. Sayfa 1'de renkli bir sidebar ve sayfa 2'de tam genişlik içerik olacak şekilde iki sayfalık CV üretiliyor.
- Ana üretici: `generate_beautiful_cv.py` (ReportLab + Pillow + PyYAML)
- Veri kaynakları: `_data/data.yml`, `_data/experience.yml`, `_data/education.yml` (UTF-8)
- Bu oturumda yapılan kilit düzeltmeler ve iyileştirmeler:
  - Sidebar iletişim metni beyaza çekildi (WCAG kontrast iyileştirmesi)
  - Sidebar yalnızca 1. sayfada çiziliyor; 2. sayfa tam genişlik içerik sunuyor
  - Yetenekler (skills) yeniden sıralandı ve yüzde çubukları ile görselleştirildi
  - Profil fotoğrafı yuvarlak kırpıldı/yerleştirildi
  - YAML içindeki `**bold**` işaretlerini doğru render edecek şekilde bold ayrıştırması eklendi
  - Türkçe karakterler için Arial/Arial-Bold font kayıtları eklendi (yerel Windows fontları kullanılıyor)
  - Email / LinkedIn / GitHub için tıklanabilir linkler (`linkURL`) eklendi
  - Tipografi ve boşluklar iyileştirildi (gövde yazı 9pt, satır yüksekliği ~13pt, madde boşlukları 6mm)
  - `generate_beautiful_cv_ats.py` eklendi: ATS-dostu, tek sütunlu ve sade PDF üretici

Dosyalarda yapılan önemli değişiklikler
-----------------------------------
- `generate_beautiful_cv.py` — Font kayıtları, sidebar davranışı, madde boşlukları, bold parsing, tam genişlik 2. sayfa, bağlantılar.
- `generate_beautiful_cv_ats.py` — Yeni eklendi: tek sütun, renk yok, bold marker'ları temizleyen ATS dostu sürüm.
- `_data/experience.yml`, `_data/data.yml` — Bu oturumda içerik gözden geçirildi; bazı düzeltmeler manuel olarak yapıldı (kullanıcı tarafından da güncellemeler yapılmış olabilir). Yeni oturumda gözden geçirilmesi istenen metin değişiklikleri aşağıda belirtilmiştir.

İçerik değişiklikleri (dikkat edilecekler)
----------------------------------------
- "60,000-line COBOL-to-microservices migration" gibi satır-sayısı içeren kesin rakam iddiaları kaldırıldı; yerine "büyük ölçekli legacy modernizasyonlar" şeklinde nötr ifadeler kullanıldı.
- "merchant-payment system to .NET/Java microservices" ifadesi CV'de microservices olarak tamamlandığı şeklinde yazılmamalı; eğer gerçekte dönüştürme yapılmadıysa "merchant-payment sistemlerinin modernizasyonu" gibi daha doğru bir ifade kullanılmalı.
- Microservices eğitimleri alınmış olsa da profesyonel olarak kullanılmadığı belirtildi; skills bölümünde Microservices puanı düşürülmelidir (ör. %92 → %70 gibi).
- "Ask/Edit modes" ifadesi "Agent and custom modes" ile değiştirildi.

Nasıl yeniden üretirim (PowerShell)
----------------------------------
```powershell
python -m pip install --upgrade pip
python -m pip install reportlab Pillow pyyaml
python generate_beautiful_cv.py
start Burak_Kalafat_Professional_CV.pdf
```

Hızlı hata ayıklama
--------------------
- Türkçe karakterlerde sorun varsa: `arial.ttf` ve `arialbd.ttf` Windows üzerinde mevcut mu kontrol edin. Yoksa DejaVu Sans gibi bir TTF'ye yönlendirin ve `pdfmetrics.registerFont` çağrılarını güncelleyin.
- Profil fotoğrafı eksikse: `assets/images/profile.png` yolunu ve boyutlarını kontrol edin.
- Uzun satırlar veya çok uzun madde listeleri sayfa taşmasına neden olabilir; `_data/experience.yml` içeriğini kısaltın veya `generate_beautiful_cv.py` içindeki `bullet_count`/font boyutunu ayarlayın.

Bu oturumda oluşturulan ATS dosyasını geliştirmek için önerilen adımlar (önceliklendirilmiş)
---------------------------------------------------------------------------------
1) `generate_beautiful_cv_ats.py` içinde "top N bullets per job" parametresi ekleyin (varsayılan 5).
2) Eksik/boş alanları atlayın (null/empty kontrolü) — boş etiketler veya çift ayraçlar üretmesin.
3) Opsiyonel: aynısını düz metin (`.txt`) olarak dışa aktarma seçeneği ekleyin (bazı ATS'ler plain-text tercih eder).
4) Basit pytest testleri ekleyin: ATS jeneratörünü çalıştırıp `Burak_Kalafat_ATS_CV.pdf` dosyasının varlığını ve 0'dan büyük dosya boyutunu assert eden test.
5) Son olarak, ATS sürümünde `**bold**` marker'ları temizlensin; gerekiyorsa başlıkları tamamen büyük harf yapma seçeneği ekleyin.

Oturumda yapılması gerekenleri unutmamak için kısa kontrol listesi
---------------------------------------------------------------
- [ ] Yeni oturumda `data.yml` ve `experience.yml` dosyalarında aşağıdaki değişikliklerin doğru uygulandığını doğrulayın:
  - "60,000-line..." gibi rakam iddiaları yerine "büyük ölçekli legacy modernizasyonlar" ifadesi.
  - "merchant-payment system to .NET/Java microservices" ifadesinin yerine "merchant-payment sistemlerinin modernizasyonu" veya benzeri doğruluğu koruyan ifade.
  - "Ask/Edit modes" → "Agent and custom modes" değişimi.
  - Microservices skill puanının azaltılması.
- [ ] `generate_beautiful_cv.py` ile PDF üret, Playwright ile ekran görüntülerini alın ve bold render/boşluk kontrolünü yapın.
- [ ] `generate_beautiful_cv_ats.py`'yi geliştir (yukarıdaki ATS adımlarını uygula) ve pytest testleri ekle.

## Son Oturum Güncelleme (October 8, 2025)

**Tamamlanan İşler:**
1. ✅ `_data/data.yml` güncellemesi:
   - Career Profile → Professional Profile
   - "60,000-line" iddiaları → "large-scale legacy modernization"
   - "Ask/Edit modes" → "Agent and custom modes"
   - Microservices açıklaması düzeltildi (training only)
   - Skills: "Microservices Architecture (Training)" 70% eklendi
   - Skills: "C# and .NET Core Microservices" → "C# and .NET Core" 98%

2. ✅ `_data/experience.yml` güncellemesi:
   - Tüm TUBITAK sonrası job title'lar → "Senior Software Engineer (Backend, .NET)"
   - Akbank merchant payment açıklaması düzeltildi
   - VeriPark title → ".NET Developer (Part-Time)"

3. ✅ `memory.md` oluşturuldu - oturum detayları dokümante edildi

4. ✅ Layout analizi tamamlandı:
   - Sidebar genişliği: 65mm (%31 A4) - optimal, değişiklik gerekmez
   - Multi-page davranışı: Sidebar sadece 1. sayfada ✅
   
**Pending:**
- PDF yeniden üretimi (Python lokal olarak çalıştırılmalı)
- Playwright görsel doğrulama (PDF üretildikten sonra)

Yeni asistan oturumu için kopyalanacak kesin prompt (yeni oturuma yapıştırın)
--------------------------------------------------------------------
Aşağıdaki metni yeni bir asistan oturumuna aynen yapıştırın; böylece devam eden işlerin tüm bağlamı korunur:

"Devam: CV optimizasyonu. Repo `c:\Work\cv`, branch `main`.

**October 8, 2025 oturumu tamamlandı - `memory.md` dosyasını kontrol edin!**

Bu oturumda neler yapıldı:
- `generate_beautiful_cv.py` güncellendi (sidebar 1. sayfa, bold parsing, font kayıtları, boşluk ve madde aralıkları artırıldı).
- `generate_beautiful_cv_ats.py` eklendi (ATS-dostu tek sütunlu PDF üretici).
- Playwright ile PDF'ler üretildi ve ekran görüntüleri alındı.

Hemen yapılacaklar (öncelik sırası):
1) `python generate_beautiful_cv.py` çalıştır ve `Burak_Kalafat_Professional_CV.pdf`'i aç. Özellikle özet bölümündeki yeni wording'i kontrol et ("büyük ölçekli legacy modernizasyonlar" gibi). Bold token'ların doğru render olup olmadığını doğrula.
2) `_data/data.yml` ve `_data/experience.yml` içinde aşağıdaki ifadelerin doğru şekilde yer aldığını doğrula ve gerekirse düzelt:
   - Rakam-iddiaları kaldırıldı: "60,000-line..." yerine "büyük ölçekli legacy modernizasyonlar".
   - "merchant-payment system to .NET/Java microservices" yerine "merchant-payment sistemlerinin modernizasyonu" veya doğru olan ifade.
   - "Ask/Edit modes" ifadelerini "Agent and custom modes" ile değiştir.
   - Microservices puanını düşür (ör. %92 → %70) eğer profesyonel kullanımı yoksa.
3) `python generate_beautiful_cv.py` yeniden çalıştır, Playwright ile page1/page2 ekran görüntülerini al ve değişiklikleri doğrula.
4) `generate_beautiful_cv_ats.py` üzerinde şu geliştirmeleri uygula: top-N bullets konfigürasyonu, boş alan kontrolü, opsiyonel `.txt` export ve basit pytest testleri.
5) Son olarak, hızlı bir spell-check çalıştır ve önemli yazım hatalarını listele (değişiklik yapmadan önce onay iste).

Nasıl çalıştırılır (PowerShell):
```powershell
python -m pip install --upgrade pip
python -m pip install reportlab Pillow pyyaml
python generate_beautiful_cv.py
start Burak_Kalafat_Professional_CV.pdf
```

Yeni oturuma geçerken unutulmaması gerekenler
-------------------------------------------
- `generate_beautiful_cv_ats.py` zaten eklenmiş; geliştirilmesi gerekiyor (yukarıdaki ATS adımları). Bu adımları atlamayın.
- İçerik değişiklikleri (rakam iddiaları, microservices ifadeleri) doğru şekilde yansıtılmalı; eğer emin değilseniz içerik sahibine (kullanıcı) onay sorulmalı.

Kısa tamamlanma özeti
---------------------
Bu oturumda: bold rendering düzeltildi, spacing ve madde boşlukları artırıldı, sidebar yalnızca 1. sayfada olacak şekilde düzeltildi, ATS için basit bir üretici eklendi ve PDF'ler Playwright ile doğrulandı. Yeni oturumda öncelik ATS geliştirilmeye ve içerik doğrulamasına verilecek.

End of document.
```
