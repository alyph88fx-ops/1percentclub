/**
 * 1 Percent Club: website sign-ups → this Google Sheet.
 *
 * Setup (once):
 *  1. Open the Google Sheet that should collect sign-ups.
 *  2. Extensions → Apps Script. Delete what is there, paste this whole file, click Save.
 *  3. Deploy → New deployment → type "Web app".
 *     Execute as: Me.  Who has access: Anyone.  → Deploy, allow access when Google asks.
 *  4. Copy the Web app URL (it ends in /exec) and put it in SIGNUP_URL in index.html.
 *
 * Each sign-up becomes a row on the "Signups" tab: time (UTC), email, page, source.
 * Repeat sign-ups with the same email are ignored.
 */
const SHEET = 'Signups';

function doPost(e) {
  const p = (e && e.parameter) || {};
  if (p.company) return out({ ok: true });                 // hidden field only bots fill in
  const email = String(p.email || '').trim().toLowerCase();
  if (email.length > 254 || !/^[^\s@=+\-][^\s@]*@[^\s@]+\.[^\s@]{2,}$/.test(email)) return out({ ok: false, error: 'invalid_email' });
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const sh = ss.getSheetByName(SHEET) || ss.insertSheet(SHEET);
    if (sh.getLastRow() === 0) { sh.appendRow(['Signed up (UTC)', 'Email', 'Page', 'Source']); sh.setFrozenRows(1); }
    const n = sh.getLastRow() - 1;
    if (n > 0 && sh.getRange(2, 2, n, 1).getValues().some(r => r[0] === email)) return out({ ok: true, duplicate: true });
    sh.appendRow([new Date(), email, clean(p.page, 200), clean(p.source, 60)]);
    return out({ ok: true });
  } finally {
    lock.releaseLock();
  }
}

function doGet() { return out({ ok: true, service: '1 Percent Club sign-ups' }); }

// keep page/source as plain text: never let a value start a spreadsheet formula
function clean(v, max) { const s = String(v || '').slice(0, max); return /^[=+\-@]/.test(s) ? "'" + s : s; }

function out(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
