# 📊 Review Profesional & Rencana Bisnis Undangan Digital

> Hasil review menyeluruh atas project ini (`index.html`, `apps-script.gs`, `checkin.html`,
> `kelola-tamu.html`, aset, riwayat git) — 2 Juli 2026.
> Konteks: undangan live Henny & Farid (16 Juli 2026) sekaligus calon produk bisnis.

---

## Kesimpulan Utama

Produk ini **sudah setara — di beberapa sisi melampaui — layanan undangan digital komersial
kelas menengah di Indonesia.** QR check-in + dashboard kelola tamu + link WA otomatis per tamu
adalah fitur yang biasanya dijual sebagai paket premium (Rp 100–300rb ekstra) oleh kompetitor.
Arsitektur static hosting + Google Sheets membuat biaya operasional nyaris nol — margin kotor >95%.

Tiga hal terpenting sebelum jadi produk jualan:
1. **Bobot halaman ±11MB** — berat di jaringan seluler.
2. **Keamanan data tamu** — dashboard tanpa login, endpoint terbuka.
3. **Lisensi musik** — lagu berhak cipta berisiko hukum jika dikomersialkan.

⚠️ **Aturan emas:** `index.html` adalah undangan LIVE (acara 16 Juli 2026). Pengembangan bisnis
dilakukan di template/fork terpisah — jangan utak-atik file live.

---

## 1. Kekuatan Produk (Layak Dijual)

1. **Fitur setara kompetitor premium**: cover video personal per tamu (`?to=`), intro slideshow
   video, countdown + simpan kalender, love story, galeri masonry + lightbox, RSVP + feed ucapan
   gaya Instagram, amplop digital, QR check-in per tamu, halaman scanner panitia, dashboard
   kelola tamu dengan blast WhatsApp.
2. **Disiplin engineering**: preload aset berurutan (ramah koneksi lambat), video pause di luar
   layar (hemat baterai), escaping XSS konsisten, `LockService` anti race-condition, timeout RSVP
   12 detik dengan pesan gagal yang jujur, verifikasi nama sebelum hapus baris.
3. **Sudah template-ready**: seluruh konten di blok `CONFIG`, tema warna di CSS variables —
   fondasi produksi massal.
4. **SEO & share**: Open Graph (preview kaya di WhatsApp), JSON-LD Event, canonical.
5. **Alur distribusi selesai**: kolom Link + Kirim WA otomatis di Sheet, dashboard kelola tamu.
   Kompetitor umumnya menyerahkan urusan sebar undangan ke klien.

---

## 2. Perbaikan Prioritas Tinggi (Undangan Live, Sebelum 16 Juli)

| # | Temuan | Status |
|---|---|---|
| 1 | **Bug `decodeURIComponent`**: nama tamu ber-`%` liar (mis. "Diskon 100%") melempar `URIError` di top-level → seluruh JS mati (countdown, RSVP, galeri). Ada di 2 titik: blok guest-name & blok QR check-in. | ✅ **Diperbaiki 2 Juli 2026** — helper `safeDecode` (try/catch), diverifikasi headless Chrome: nama ber-`%`, nama normal, dan link lama encode-ganda semuanya bekerja. |
| 2 | **Duplikasi check-in berbasis nama**: dua tamu bernama sama ("Andi") → yang kedua ditolak "sudah check-in". Mitigasi hari-H: panitia catat manual. Solusi bisnis: QR berisi ID unik per tamu, bukan `CHECKIN:nama`. | ⬜ Belum |
| 3 | **Bobot halaman ±11MB**: 21 foto galeri (100–430KB) dimuat penuh ke sel grid ±220px; musik 2,2MB. (Video justru sudah optimal: 160–970KB.) Solusi: thumbnail WebP ±400px untuk grid (~30–50KB/foto, hemat ±4MB), foto penuh hanya di lightbox; konversi JPEG→WebP (hemat 30–50%). Target muatan awal <3MB. | ⬜ Belum |

---

## 3. Perbaikan untuk Versi Produk Bisnis

### Keamanan & privasi (paling serius)
- `kelola-tamu.html` **tanpa autentikasi** — siapa pun yang tahu URL bisa lihat semua nama +
  nomor WA tamu dan **menghapus tamu**. Endpoint `?type=tamu` menyerahkan daftar tamu + nomor
  telepon ke siapa saja. Untuk bisnis (data ribuan tamu banyak klien) ini liabilitas UU PDP.
  Minimal: token rahasia diperiksa server-side di Apps Script untuk baca-daftar/tambah/hapus.
- **Satu spreadsheet + deployment Apps Script per klien** — sekaligus menyelesaikan kuota
  Apps Script (~20rb eksekusi/hari; cukup untuk 1 pernikahan, tidak untuk 50).

### Lisensi musik
Musik saat ini ("Aku Memilihmu" — Brisia Jodie) berhak cipta. Untuk undangan pribadi = praktik
umum walau area abu-abu; **untuk bisnis = pelanggaran nyata**. Kebijakan aman: klien menyediakan
musik sendiri (tanggung jawab pindah ke klien, tulis di S&K) atau pustaka royalty-free.

### Fitur penambah harga jual (urut rasio effort/nilai)
1. **Analitik tamu** — catat siapa sudah buka undangan (ping Apps Script saat load). Fitur
   penjual kuat, nyaris gratis dibuat.
2. **Mode pasca-acara** — hero "Terima Kasih" + galeri foto acara (peluang upsell).
3. **Konfirmasi hadiah** — form "saya sudah transfer". Kompetitor punya.
4. **Embed live streaming** (YouTube) — standar paket atas.
5. **Varian non-Islami** — template sekarang sangat spesifik Islami; pasar nasional butuh varian
   netral/Kristen/Hindu. (Fokus Sulsel: Islami memang mayoritas.)
6. **Opsi mematikan seed wishes & angka suka semu per klien** — ucapan contoh fiktif & jumlah
   suka generate cocok untuk pribadi; menjualnya tanpa opsi off = risiko etika/kepercayaan.
7. **RSVP dedupe** — tamu sama bisa submit berkali-kali; tampilkan yang terakhir saja.

### Kebersihan repo
`foto-asli/` 163MB — pindah ke Git LFS atau simpan di luar repo (Drive per klien).

---

## 4. Rencana Bisnis

### Posisi pasar
Pasar ramai (Katsudoto, Datangya, Sebarundangan, ratusan reseller IG/TikTok):

| Segmen | Harga pasar | Isi |
|---|---|---|
| Template murah | Rp 35–100rb | Isi form, jadi otomatis, fitur dasar |
| Menengah | Rp 150–350rb | Semi-custom, RSVP, amplop digital |
| Premium/custom | Rp 500rb–2jt+ | Desain khusus, video, QR check-in, domain sendiri |

**Jangan perang harga di segmen bawah.** Kekuatan ada di **menengah-atas**: kualitas engineering,
video intro custom, check-in yang benar-benar dipakai di venue.

**Diferensiasi jujur yang bisa diklaim:**
1. QR check-in + dashboard tamu **termasuk paket** (kompetitor jual terpisah).
2. **Teruji di pernikahan sendiri** — setelah 16 Juli ada data nyata (X tamu, Y RSVP, Z check-in).
3. Video intro custom (mayoritas kompetitor statis).
4. Performa jaringan lambat (setelah optimasi) — kompetitor banyak yang berat.

### Struktur harga disarankan

| Paket | Harga | Isi |
|---|---|---|
| **Hemat** | Rp 149rb | Template tema, RSVP + ucapan, amplop digital, galeri, musik dari klien |
| **Favorit** | Rp 299rb | + QR check-in & scanner, dashboard tamu, link WA per tamu, analitik pembuka |
| **Eksklusif** | Rp 750rb–1,5jt | + Video intro custom, subdomain sendiri, love story ditulis khusus, pendampingan hari-H |

Paket tengah = target utama (anchor); paket atas menyerap klien tak sensitif harga.

### Fase eksekusi

**Fase 0 — sekarang s/d 16 Juli:** jangan sentuh undangan live (bug `%` sudah beres).
Saat resepsi: **dokumentasikan check-in QR bekerja** (video panitia scan, counter naik) →
konten pemasaran perdana.

**Fase 1 — bulan 1–3 (validasi, 5–10 klien):**
- Fork `index.html` → repo template; `CONFIG` → JSON per klien.
- 3–5 varian tema dari CSS variables (manfaatkan `tema-warna.html`).
- Satu spreadsheet + deployment Apps Script per klien.
- Hosting pindah ke **Cloudflare Pages** (gratis, banyak subdomain custom, cepat di Indonesia);
  domain bisnis → `namaklien.domainanda.com`.
- Kanal: IG/TikTok (screen-recording undangan di-scroll) + **kemitraan WO & fotografer
  Makassar/Pangkep** (komisi 20–30% / harga reseller). QR check-in menyelesaikan pain WO di venue.
- 2–3 klien pertama harga diskon sebagai portofolio (bukan gratis).

**Fase 2 — bulan 3–9 (semi-otomasi, 20–40 klien/bulan):**
- Generator: form → config JSON → deploy otomatis (GitHub Actions). Produksi <30 menit/undangan.
- Otomasi provisioning spreadsheet (copy template + deploy programatis).
- Pembayaran: transfer manual dulu; Midtrans/Xendit saat >15/bulan.
- **Rekrut 1 paruh waktu** untuk input konten & CS — waktu (dokter) adalah kendala utama.
  Jalan realistis: otomasi teknis + delegasi CS.
- Program reseller — mesin volume terbesar industri ini.

**Fase 3 — bulan 9+ (hanya jika traksi terbukti):** editor self-service, backend sungguhan
(Supabase/Firebase), dashboard klien. Jangan bangun SaaS sebelum punya pelanggan.

### Proyeksi kasar
- Biaya marginal per undangan ~Rp 0 + waktu produksi.
- Fase 1: 8 × Rp 299rb = **Rp 2,4jt/bln** (±16 jam kerja) — validasi sambilan.
- Fase 2: 30 × rata-rata Rp 250rb = **Rp 7,5jt/bln**, minus asisten Rp 1,5–2jt →
  bersih ±Rp 5jt/bln sebagai bisnis sampingan.
- Musiman: puncak setelah Lebaran & Desember; sepi saat Ramadan.

### Risiko & mitigasi
1. **Waktu terbatas (dokter)** → otomasi sejak awal, delegasi CS, jangan janji lead time <24 jam.
2. **Perang harga** → jual nilai (check-in, kecepatan, keandalan hari-H), bukan harga.
3. **Kuota Apps Script** → deployment per klien (Fase 1), DB saat volume tinggi (Fase 3).
4. **Kebocoran data tamu** → token auth sebelum klien pertama; bukan opsional.
5. **Hak cipta musik** → kebijakan "musik dari klien" + S&K tertulis sejak klien pertama.
6. **Legalitas** → mulai personal brand; saat stabil → PT Perorangan.

---

## 5. Prioritas 30 Hari

1. ✅ ~~Perbaiki bug `decodeURIComponent` di undangan live~~ (selesai 2 Juli 2026).
2. ⬜ **16 Juli:** dokumentasikan check-in QR di resepsi (video + angka).
3. ⬜ Minggu 3–4: fork template, 3 tema, optimasi foto (thumbnail WebP), token auth Apps Script,
   S&K sederhana (musik, foto, refund), akun IG bisnis + demo pernikahan sendiri sebagai portofolio.
4. ⬜ Akhir bulan: 1 klien berbayar pertama (mulai dari lingkaran terdekat).
