# Menghubungkan RSVP ke Google Sheets

Ikuti langkah ini sekali saja. Setelah selesai, semua RSVP & ucapan tamu otomatis
masuk ke Google Sheet kamu, dan tampil di halaman undangan.

## 1. Buat Spreadsheet
1. Buka https://sheets.google.com → **Blank spreadsheet**.
2. Beri nama, misal **"RSVP Undangan"**. (Tab/sheet "RSVP" akan dibuat otomatis.)

## 2. Pasang Apps Script
1. Di spreadsheet itu, menu **Extensions → Apps Script**.
2. Hapus kode contoh yang ada, lalu **tempel seluruh isi file `apps-script.gs`**.
3. Klik ikon **Simpan** (💾).

## 3. Deploy sebagai Web App
1. Klik tombol **Deploy → New deployment**.
2. Klik ikon gerigi ⚙️ di sebelah "Select type" → pilih **Web app**.
3. Isi:
   - **Description**: bebas (mis. "RSVP")
   - **Execute as**: **Me (email kamu)**
   - **Who has access**: **Anyone**  ← WAJIB, supaya tamu bisa kirim
4. Klik **Deploy**.
5. Klik **Authorize access** → pilih akun Google kamu → bila muncul "Google hasn't
   verified this app", klik **Advanced → Go to (nama proyek) (unsafe)** → **Allow**.
   (Aman — ini aplikasi milikmu sendiri.)
6. **Salin "Web app URL"** yang muncul. Bentuknya:
   `https://script.google.com/macros/s/AKfyc..../exec`

## 4. Tempel URL ke undangan
Buka `index.html`, cari di blok `CONFIG`:

```js
sheetUrl: "",
```

Ganti jadi (tempel URL kamu):

```js
sheetUrl: "https://script.google.com/macros/s/AKfyc..../exec",
```

Simpan, lalu push ke GitHub:

```bash
git add -A && git commit -m "Aktifkan RSVP Google Sheets" && git push
```

Selesai! Coba isi form RSVP di undangan → cek spreadsheet, datanya akan muncul.

---

## Kalau nanti mengubah kode Apps Script
Setelah edit, **Deploy → Manage deployments → ✏️ (edit) → Version: New version → Deploy**.
URL tetap sama, jadi tidak perlu ganti `sheetUrl`.

## Catatan
- Kolom di sheet: **Waktu | Nama | Kehadiran | Ucapan**.
- Ucapan yang tampil di halaman diambil real-time dari sheet (terbaru di atas).
- Jika `sheetUrl` dikosongkan, undangan tetap jalan dalam mode demo (tersimpan di
  browser tamu saja).
