# Daftar Tamu Terpusat (Google Sheets, multi-pegawai)

Satu daftar tamu yang bisa diisi banyak pegawai sekaligus dari komputer
masing-masing. Link undangan & tombol kirim WhatsApp muncul otomatis.

## 1. Pasang fungsi setup (sekali)
1. Buka spreadsheet RSVP kamu → **Extensions → Apps Script**.
2. Tempel ulang seluruh isi `apps-script.gs` (sudah ada fungsi baru `setupDaftarTamu`).
3. Klik **Simpan** 💾.

## 2. Jalankan setup (sekali)
1. Di toolbar editor Apps Script, pada dropdown fungsi pilih **`setupDaftarTamu`**.
2. Klik **Run** ▶.
3. Bila diminta izin, **Authorize** (akun kamu).
4. Muncul notifikasi "Tab DaftarTamu siap!". Tutup editor.

> Catatan: ini cuma membuat tab, **tidak perlu Deploy ulang**.

## 3. Bagikan ke pegawai
1. Di spreadsheet, klik tombol **Share / Bagikan** (kanan atas).
2. Tambahkan email pegawai sebagai **Editor**.
   - Atau set "Siapa saja yang memiliki link" → **Editor** lalu bagikan link
     spreadsheet-nya (lebih praktis untuk banyak pegawai).
3. Minta pegawai membuka spreadsheet → pindah ke tab **DaftarTamu**.

## 4. Cara pegawai mengisi
- Ketik **nama tamu** di kolom **A** (satu baris per tamu).
- (Opsional) isi **No. WA** di kolom **B**, **nama petugas** di kolom **C**.
- Kolom **E (Link Undangan)** & **F (Kirim WhatsApp)** terisi **otomatis**.
- Klik link di kolom F untuk langsung membuka WhatsApp dengan pesan + link siap kirim.

Karena semua menulis ke sheet yang sama, kamu otomatis punya **rekap daftar
tamu lengkap** secara real-time — tanpa perlu mengumpulkan file dari tiap pegawai.

## Hubungannya dengan tab lain
- **DaftarTamu** : daftar undangan yang disebar (kelola di sini).
- **RSVP**       : konfirmasi kehadiran & ucapan dari tamu (otomatis dari undangan).
- **CheckIn**    : kehadiran nyata saat acara (otomatis dari scanner QR).
