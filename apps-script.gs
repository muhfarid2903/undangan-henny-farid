/* ============================================================
   Google Apps Script — Backend RSVP untuk Undangan Digital
   Tempel seluruh isi file ini ke editor Apps Script.
   Lihat langkah lengkap di CARA-RSVP-GOOGLE-SHEETS.md
   ============================================================ */

const SHEET_NAME = 'RSVP';

// Tamu mengirim ucapan (POST)
function doPost(e) {
  const lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);
    const data = JSON.parse(e.postData.contents);
    const sheet = getSheet();
    sheet.appendRow([
      new Date(),
      String(data.name || '').slice(0, 100),
      String(data.attend || '').slice(0, 30),
      String(data.msg || '').slice(0, 500)
    ]);
    return json({ ok: true });
  } catch (err) {
    return json({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

// Menampilkan daftar ucapan di halaman (GET) — terbaru di atas
function doGet() {
  const sheet = getSheet();
  const rows = sheet.getDataRange().getValues();
  rows.shift(); // buang baris header
  const list = rows.map(function (r) {
    return { t: r[0], name: r[1], attend: r[2], msg: r[3] };
  }).reverse();
  return json(list);
}

function getSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    sheet.appendRow(['Waktu', 'Nama', 'Kehadiran', 'Ucapan']);
  }
  return sheet;
}

function json(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
