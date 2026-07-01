/* ============================================================
   Google Apps Script — Backend Undangan Digital
   - RSVP & ucapan tamu
   - Check-in QR saat acara
   Tempel seluruh isi file ini ke editor Apps Script, lalu DEPLOY
   ULANG (New version). Lihat CARA-RSVP-GOOGLE-SHEETS.md
   ============================================================ */

const RSVP_SHEET = 'RSVP';
const CHECKIN_SHEET = 'CheckIn';
const SITE = 'https://hennyfarid.balanglompo.com/';  // alamat undangan

/* ============================================================
   SETUP DAFTAR TAMU TERPUSAT
   Jalankan SEKALI dari editor: pilih fungsi "setupDaftarTamu"
   di toolbar lalu klik Run. Tab "DaftarTamu" akan terbentuk
   dengan kolom Link & Kirim WA otomatis. (Tidak perlu deploy.)
   ============================================================ */
function setupDaftarTamu() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  // Pakai locale US agar pemisah argumen rumus = koma (sesuai rumus di bawah).
  ss.setSpreadsheetLocale('en_US');
  let sh = ss.getSheetByName('DaftarTamu');
  if (!sh) sh = ss.insertSheet('DaftarTamu');
  sh.clear();

  sh.getRange('A1:F1')
    .setValues([['Nama Tamu', 'No. WA (opsional)', 'PIC / Petugas', 'Catatan', 'Link Undangan', 'Kirim WhatsApp']])
    .setFontWeight('bold').setBackground('#f3ece2');

  setDaftarFormulas(sh);

  sh.setFrozenRows(1);
  sh.setColumnWidth(1, 200);
  sh.setColumnWidth(5, 340);
  sh.setColumnWidth(6, 360);
  SpreadsheetApp.getUi().alert('Tab "DaftarTamu" siap! Bagikan spreadsheet ini (akses Editor) ke pegawai.');
}

// Pasang rumus kolom E (link undangan) & F (link WA). Dipanggil saat setup dan
// setiap kali menghapus baris, agar ARRAYFORMULA (jangkar di baris 2) selalu ada.
function setDaftarFormulas(sh) {
  // Kolom E: Link undangan personal (otomatis untuk setiap nama di kolom A)
  sh.getRange('E2').setFormula(
    '=ARRAYFORMULA(IF(A2:A="","","' + SITE + '?to="&SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(A2:A,"&","%26"),",","%2C")," ","%20")))'
  );

  // Kolom F: Link kirim WhatsApp (nomor otomatis dinormalkan ke 62, pesan + link terenkode)
  var ph = 'IF(B2:B="","",IF(LEFT(B2:B&"",1)="0","62"&MID(B2:B&"",2,30),IF(LEFT(B2:B&"",2)="62",B2:B&"",IF(LEFT(B2:B&"",1)="8","62"&(B2:B&""),B2:B&""))))';
  // Kata-kata pesan WA per baris (baris kosong = jeda paragraf). Ubah di sini bila perlu,
  // lalu jalankan ulang setupDaftarTamu agar kolom F diperbarui.
  var parts = [
    '"Kepada Yth."',
    '"Bapak/Ibu/Saudara/i"',
    'A2:A',
    '"___________________"',
    '""',
    '"Tanpa mengurangi rasa hormat, perkenankan kami mengundang Bapak/Ibu/Saudara/i, teman sekaligus sahabat, untuk menghadiri acara pernikahan kami."',
    '""',
    '"Berikut link undangan kami, untuk info lengkap dari acara, bisa kunjungi :"',
    '""',
    'E2:E',
    '""',
    '"Merupakan suatu kebahagiaan bagi kami apabila Bapak/Ibu/Saudara/i berkenan untuk hadir dan memberikan doa restu."',
    '""',
    '"Terima Kasih"',
    '""',
    '"Hormat kami,"',
    '"Henny & Farid"',
    '"__________________"'
  ];
  var msg = parts.join('&CHAR(10)&');
  var enc = function (x) {
    return 'SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(' + x +
      ',"%","%25"),":","%3A"),"/","%2F"),"?","%3F"),"=","%3D"),"&","%26")," ","%20"),",","%2C"),CHAR(10),"%0A")';
  };
  sh.getRange('F2').setFormula(
    '=ARRAYFORMULA(IF(A2:A="","","https://wa.me/"&(' + ph + ')&"?text="&' + enc(msg) + '))'
  );
}

// ---------- POST ----------
function doPost(e) {
  const lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
    const data = JSON.parse(e.postData.contents);

    // --- Check-in dari halaman scanner ---
    if (data.type === 'checkin') {
      const sheet = getCheckinSheet();
      const name = String(data.name || '').trim().slice(0, 100);
      if (!name) return json({ ok: false, error: 'nama kosong' });

      // cek apakah sudah pernah check-in
      const names = sheet.getRange(2, 2, Math.max(sheet.getLastRow() - 1, 1), 1)
                         .getValues().map(function (r) { return String(r[0]).trim().toLowerCase(); });
      const already = names.indexOf(name.toLowerCase()) !== -1;
      if (!already) sheet.appendRow([new Date(), name]);
      return json({ ok: true, name: name, already: already });
    }

    // --- Tambah tamu ke DaftarTamu (dari kelola-tamu.html) ---
    if (data.type === 'tamu') {
      const sheet = getDaftarSheet();
      if (!sheet) return json({ ok: false, error: 'Tab DaftarTamu belum ada. Jalankan setupDaftarTamu dulu.' });
      const name = String(data.name || '').trim().slice(0, 100);
      if (!name) return json({ ok: false, error: 'nama kosong' });
      sheet.appendRow([
        name,
        String(data.phone || '').slice(0, 30),
        String(data.pic || '').slice(0, 50),
        String(data.note || '').slice(0, 200)
      ]);
      return json({ ok: true });
    }

    // --- Hapus tamu dari DaftarTamu (dari kelola-tamu.html) ---
    if (data.type === 'hapus-tamu') {
      const sheet = getDaftarSheet();
      if (!sheet) return json({ ok: false, error: 'Tab DaftarTamu belum ada.' });
      const row = parseInt(data.row, 10);
      if (!row || row < 2) return json({ ok: false, error: 'baris tidak valid' });
      if (row > sheet.getLastRow()) return json({ ok: false, error: 'Data sudah berubah, muat ulang dulu.' });
      // Verifikasi nama di baris cocok agar tidak salah hapus bila urutan berubah.
      const expect = String(data.name || '').trim().toLowerCase();
      const actual = String(sheet.getRange(row, 1).getValue()).trim().toLowerCase();
      if (expect && expect !== actual) {
        return json({ ok: false, error: 'Data sudah berubah, muat ulang dulu.' });
      }
      sheet.deleteRow(row);
      // Pasang ulang rumus kolom E & F (jangkar ARRAYFORMULA di baris 2 bisa
      // ikut terhapus bila baris 2 yang dihapus).
      setDaftarFormulas(sheet);
      return json({ ok: true });
    }

    // --- RSVP & ucapan ---
    const sheet = getRsvpSheet();
    sheet.appendRow([
      new Date(),
      String(data.name || '').slice(0, 100),
      String(data.attend || '').slice(0, 30),
      String(data.msg || '').slice(0, 500),
      String(data.guests || '').slice(0, 10)
    ]);
    return json({ ok: true });
  } catch (err) {
    return json({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

// ---------- GET ----------
// ?type=checkin -> daftar check-in; selain itu -> daftar ucapan
function doGet(e) {
  const type = e && e.parameter ? e.parameter.type : '';
  if (type === 'checkin') {
    const sheet = getCheckinSheet();
    const rows = sheet.getDataRange().getValues();
    rows.shift();
    const list = rows.map(function (r) { return { t: r[0], name: r[1] }; }).reverse();
    return json({ count: list.length, list: list });
  }
  if (type === 'tamu') {
    const sheet = getDaftarSheet();
    if (!sheet || sheet.getLastRow() < 2) return json({ list: [] });
    const rows = sheet.getRange(2, 1, sheet.getLastRow() - 1, 6).getValues();
    const list = [];
    rows.forEach(function (r, i) {
      if (String(r[0]).trim() === '') return;
      // row = nomor baris asli di Sheet (dipakai kelola-tamu.html untuk hapus)
      list.push({ row: i + 2, name: r[0], phone: r[1], pic: r[2], note: r[3], link: r[4], wa: r[5] });
    });
    return json({ list: list });
  }
  const sheet = getRsvpSheet();
  const rows = sheet.getDataRange().getValues();
  rows.shift();
  const list = rows.map(function (r) {
    return { t: r[0], name: r[1], attend: r[2], msg: r[3], guests: r[4] };
  }).reverse();
  return json(list);
}

// ---------- helpers ----------
function getRsvpSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(RSVP_SHEET);
  if (!sheet) {
    sheet = ss.insertSheet(RSVP_SHEET);
    sheet.appendRow(['Waktu', 'Nama', 'Kehadiran', 'Ucapan', 'Jumlah Tamu']);
  }
  return sheet;
}

function getDaftarSheet() {
  return SpreadsheetApp.getActiveSpreadsheet().getSheetByName('DaftarTamu');
}

function getCheckinSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(CHECKIN_SHEET);
  if (!sheet) {
    sheet = ss.insertSheet(CHECKIN_SHEET);
    sheet.appendRow(['Waktu Datang', 'Nama Tamu']);
  }
  return sheet;
}

function json(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
