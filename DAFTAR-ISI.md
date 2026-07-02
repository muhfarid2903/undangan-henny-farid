# 📋 Daftar Isi Lengkap Undangan — Henny & Farid
### (file: `index.html`)

---

## 0. Loading Screen
- Teks **"Memuat Undangan…"** + progress bar (0–100%)
- Nama pasangan: **Henny & Farid**
- Background: foto `galeri14.webp` (tampil utuh / `contain` + veil gelap)
- Durasi minimal **2,5 detik** (agar kesan memuat terasa di koneksi cepat); selesai begitu foto cover siap, batas maksimal 3,5 detik

---

## 1. Cover (Sampul)
- Video latar: `bg/cover-video.mp4` (sekali putar, tidak loop), poster `cover.webp`
- Foto mempelai dalam bingkai melengkung: `cover.webp` (`cover.jpg` dipertahankan untuk preview WhatsApp/og:image)
- Nama pasangan + nama tamu undangan (otomatis dari `?to=` di URL)
- Tombol **"Buka Undangan"**

---

## 2. Intro — 5 slide berurutan (cross-fade, lalu mengulang)
| # | Type | Background | Isi |
|---|------|-----------|-----|
| 1 | `hero` | 🎥 `intro-1-2.mp4` (±10 dtk, tanpa veil) | Video slide 1 & 2 — teks sudah di dalam video |
| 2 | `photo` | `galeri2.webp` | Foto layar penuh (slide 3) |
| 3 | `photo` | `intro-4.webp` | Foto layar penuh (slide 4) |
| 4 | `couple` | 🎥 `intro-5-6.mp4` (±10 dtk, tanpa veil) | Video slide 5 & 6 — teks sudah di dalam video |
| 5 | `photo` | `intro-7.webp` | Foto layar penuh (slide 7) |

---

## 3. Opening (Ayat)
- Foto berbingkai melengkung: `opening-ayat.webp`
- Eyebrow: basmalah (maroon)
- **Ayat:** *"Dan di antara tanda-tanda kekuasaan-Nya diciptakan-Nya untukmu pasangan hidup dari jenismu sendiri supaya kamu mendapat ketenangan hati..."*
- **Sumber:** QS. Ar-Rum: 21

---

## 4. Couple — Mempelai Wanita
- Foto: `mempelai-wanita.webp`
- Nama: **Henny** — Henny Puspita Syarifuddin, S.Pd., Gr.
- Putri pertama dari Bapak Syarifuddin Achmad & Ibu Habrita, S.Ag.
- IG: [@hennysyr](https://instagram.com/hennysyr)

## 5. Couple — Mempelai Pria
- Foto: `mempelai-pria.webp`
- Nama: **Farid** — dr. Muhammad Farid
- Putra ketiga dari Bapak Abdul Salam Karim, S.Pd. & Ibu St. Rabiatul Adawiah Balido
- IG: [@muhfarid2994](https://instagram.com/muhfarid2994)

---

## 6. Countdown
- Hitung mundur ke **16 Juli 2026, 10.00 WITA** (Hari/Jam/Menit/Detik)
- Tombol **"+ Simpan ke Kalender"**

---

## 7. Events (Acara)
**Akad**
- Kamis, 16 Juli 2026 · 10.00 WITA – Selesai
- Gedung Dewakkang, Samalewa, Kec. Bungoro, Kab. Pangkep, Sulsel 90617
- Tombol **"📍 Lihat Lokasi"**

**Resepsi**
- Kamis, 16 Juli 2026 · 12.00 WITA – Selesai
- Lokasi sama (Gedung Dewakkang) + tombol peta

---

## 8. Story — Our Love Story (3 bagian)
- **Bagian 01 · Pertemuan** — Berawal dari izin berkenalan, pertemuan pertama di kafe, hingga buka puasa bersama keluarganya.
- **Bagian 02 · Komitmen** — Datang ke rumah dengan niat tulus untuk melangkah lebih serius.
- **Bagian 03 · Pernikahan** — Tanpa tanggal jadian; hanya tanggal lamaran & pernikahan. Berani melangkah dengan cara yang benar.
- Tiap bagian: label "Bagian 0x", judul, narasi, dan satu kutipan (italic bergaris emas).

---

## 9. Gallery (Galeri)
- Grid **masonry** 21 foto (urutan acak, tinggi bervariasi / berseni) + lightbox geser kiri/kanan
- File: `galeri1.webp` – `galeri21.webp` — grid memakai thumbnail ringan di `thumb/` (nama sama); foto penuh hanya dimuat saat lightbox dibuka

---

## 10. RSVP
- Form: nama, hadir/tidak, jumlah tamu, ucapan & doa
- Terhubung ke Google Sheets
- Tombol **"💌 Lihat Ucapan & Doa"** (popup)

---

## 11. Check-in QR
- QR code check-in otomatis + nama tamu (muncul hanya bila ada nama tamu di link)

---

## 12. Gift (Amplop Digital)
- Tombol **"🎁 Kirim Hadiah"** (popup), berisi:
  - BANK BRI — 022301051237503 — a.n. Henny Puspita Syarifuddin
  - BANK BCA — 3900928440 — a.n. Muhammad Farid

---

## 13. Closing (Penutup)
- Background video: `bg/penutup.mp4` (sekali putar) — pesan penutup & nama pasangan **sudah di dalam video**
- Tanpa kartu/teks tambahan

---

## 🧩 Elemen Mengambang & Pengaturan
- **Bottom Nav** — navigasi cepat antar bagian
- **Tombol Musik ♪** — musik latar: `musik.mp3` (tanpa jingle pembuka)
- **Popup Ucapan & Doa** · **Popup Amplop Digital** · **Lightbox** galeri
- **Efek:** kelopak bunga jatuh (`petals`), partikel emas (`sparkles`), auto-scroll pelan
- **Desktop:** foto besar sisi kiri (`cover.webp`)

---

## ✍️ Tipografi (4 kategori / 2 font)
- **Judul utama** (Bride & Groom, Our Love Story, dll.) → **Carattere**
- **Nama panggilan** (Henny & Farid) → **Carattere**
- **Nama lengkap** (di kartu mempelai) → **Carattere**
- **Teks body** (semua paragraf, label, tombol, countdown) → **Lora**

---

## 🎨 Background per Segmen
- Semua segmen berteks (opening, couple, countdown, events, story, rsvp, checkin, gift): foto `bg/segmen.webp` + video latar `bg/segmen-video.mp4`
- Cover: `bg/cover-video.mp4` · Penutup: `bg/penutup.mp4`
