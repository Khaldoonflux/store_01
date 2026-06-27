<!DOCTYPE html>
<html lang="ar" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>مصروف</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Almarai:wght@300;400;700;800&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg:        #3a5bd9;
  --card:      #0f0f0f;
  --card2:     #1a1a1a;
  --subcard:   #2a2a2e;
  --text:      #ffffff;
  --text-mid:  rgba(255,255,255,0.6);
  --text-low:  rgba(255,255,255,0.3);
  --expense:   #ff9f43;
  --income:    #2ecc71;
  --gold:      #d4af37;
  --save-red:  #c0392b;
  --save-red2: #96281b;
  --save-green:  #27ae60;
  --save-green2: #1e8449;
  --gap:   14px;
  --pad:   16px;
  --r-lg:  28px;
  --r-md:  18px;
  --font:  'Almarai', sans-serif;
}

html, body {
  height: 100%;
  background: var(--bg);
  color: var(--text);
  font-family: var(--font);
  -webkit-font-smoothing: antialiased;
  overscroll-behavior: none;
}

body {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
}

.screen {
  display: none; width: 100%; max-width: 430px;
  flex-direction: column; min-height: 100vh;
}
.screen.active { display: flex; }

/* ══════════════════════════════
   LOGIN
══════════════════════════════ */
#screen-login {
  align-items: center; justify-content: center;
  padding: 40px var(--pad) 60px;
  gap: 0;
}

.login-badge {
  width: 80px; height: 80px;
  background: var(--card);
  border-radius: 26px;
  display: flex; align-items: center; justify-content: center;
  margin-bottom: 28px;
}
.login-badge-letter { font-size: 36px; font-weight: 800; color: var(--gold); }

.login-title {
  font-size: 32px; font-weight: 800; color: var(--text);
  margin-bottom: 12px; letter-spacing: -0.5px;
}

.login-sub {
  font-size: 15px; color: rgba(255,255,255,0.75); text-align: center;
  line-height: 1.9; margin-bottom: 48px; max-width: 280px;
}

.login-features {
  width: 100%; display: flex; flex-direction: column;
  gap: var(--gap); margin-bottom: 44px;
}

.login-feature {
  background: var(--card);
  border-radius: var(--r-md); padding: 16px 20px;
  display: flex; align-items: center; gap: 16px;
  overflow: hidden;
}

.feature-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
.feature-dot.blue   { background: #4a9eff; }
.feature-dot.green  { background: var(--income); }
.feature-dot.orange { background: var(--expense); }
.feature-text { font-size: 14px; color: var(--text-mid); line-height: 1.6; }

.google-btn {
  width: 100%; padding: 18px 24px;
  border-radius: var(--r-md); border: none;
  background: #fff; color: #1a1a2e;
  font-family: var(--font); font-size: 15px; font-weight: 700;
  cursor: pointer; display: flex; align-items: center;
  justify-content: center; gap: 10px;
  transition: transform 0.15s; overflow: hidden;
}
.google-btn:active { transform: scale(0.98); }
.google-g { width: 20px; height: 20px; flex-shrink: 0; }

/* ══════════════════════════════
   TOP BAR
══════════════════════════════ */
.topbar {
  width: 100%; padding: var(--pad) var(--pad) 12px;
  display: flex; align-items: center; justify-content: space-between;
  flex-shrink: 0;
}

.mode-btn {
  background: var(--card); border: none;
  border-radius: 999px; padding: 9px 20px;
  font-family: var(--font); font-size: 13px; font-weight: 700;
  color: var(--text); cursor: pointer;
  transition: background 0.2s; overflow: hidden;
}
.mode-btn:active { background: var(--subcard); }

.user-pill {
  background: var(--card); border: none;
  border-radius: 999px; padding: 9px 20px;
  font-size: 13px; font-weight: 700; color: var(--text);
  cursor: pointer; transition: background 0.2s; overflow: hidden;
}
.user-pill:active { background: var(--subcard); }

/* ══════════════════════════════
   SWIPE
══════════════════════════════ */
.swipe-container {
  flex: 1; display: flex; flex-direction: column;
  overflow: hidden; position: relative;
}

.swipe-viewport {
  display: flex; flex-direction: row;
  width: 100%; height: 100%;
  overflow-x: scroll;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: auto;
  scrollbar-width: none;
}
.swipe-viewport::-webkit-scrollbar { display: none; }

.swipe-page {
  min-width: 100%; width: 100%;
  flex-shrink: 0;
  scroll-snap-align: start;
  scroll-snap-stop: always;
  display: flex; flex-direction: column;
  gap: var(--gap);
  padding: 0 var(--pad) 40px;
  overflow-y: auto;
}

/* ══════════════════════════════
   PANELS
══════════════════════════════ */
.panels {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: var(--gap);
}

.panel {
  aspect-ratio: 1/1; border-radius: var(--r-lg);
  display: flex; align-items: center; justify-content: center;
  flex-direction: column; overflow: hidden;
  cursor: pointer; position: relative;
  background: var(--card);
}

.date-day-num {
  font-size: clamp(64px, 18vw, 86px);
  font-weight: 300; line-height: 0.9;
  letter-spacing: -4px;
  display: block; width: 100%; text-align: center;
  color: var(--text);
}

.date-names {
  width: 100%; text-align: center; margin-top: 10px;
  padding: 0 6px;
}

.date-ar {
  display: block;
  font-size: clamp(16px, 4.8vw, 22px);
  font-weight: 700; color: var(--gold);
  line-height: 1.3;
}

.date-en {
  display: block;
  font-size: clamp(11px, 3vw, 14px);
  font-weight: 400; color: var(--text-low);
  text-transform: uppercase; letter-spacing: 0.6px;
  line-height: 1.4;
}

.panel-type.expense { background: #1a0a00; }
.panel-type.income  { background: #001a0a; }

.type-label {
  font-size: clamp(18px, 5vw, 24px);
  font-weight: 800; color: var(--text);
  transition: color 0.3s;
}
.panel-type.expense .type-label { color: var(--expense); }
.panel-type.income  .type-label { color: var(--income); }

/* ══════════════════════════════
   FIELDS
══════════════════════════════ */
.field-card {
  background: var(--card);
  border-radius: var(--r-lg);
  display: flex; align-items: center; justify-content: center;
  overflow: hidden;
}

.field-card input,
.field-card textarea {
  width: 100%; background: transparent;
  border: none; outline: none;
  color: var(--text); font-family: var(--font);
  caret-color: var(--gold); text-align: center;
}

.amount-card { padding: 26px var(--pad); }
.amount-inp {
  font-size: clamp(38px, 11vw, 52px);
  font-weight: 300; letter-spacing: -1px; line-height: 1;
}
.amount-inp::placeholder { color: var(--text-low); }

.desc-card { padding: 20px var(--pad); }
.desc-inp {
  font-size: 16px; font-weight: 400;
  line-height: 1.7; resize: none;
  overflow: hidden; min-height: 28px;
}
.desc-inp::placeholder { color: var(--text-low); }

/* ══════════════════════════════
   SAVE
══════════════════════════════ */
.save-btn {
  width: 100%; padding: 20px;
  border-radius: var(--r-lg); border: none;
  font-family: var(--font); font-size: 17px; font-weight: 800;
  cursor: pointer; color: #fff;
  background: linear-gradient(160deg, var(--save-red), var(--save-red2));
  transition: background 0.35s, transform 0.1s;
  overflow: hidden;
}
.save-btn.ok {
  background: linear-gradient(160deg, var(--save-green), var(--save-green2));
}
.save-btn:active { transform: scale(0.98); }

/* ══════════════════════════════
   REPORT TABS
══════════════════════════════ */
.report-tabs {
  display: grid; grid-template-columns: repeat(3,1fr); gap: 12px;
}

.report-tab {
  padding: 15px 10px; border-radius: var(--r-md);
  border: none; background: var(--card);
  font-family: var(--font); font-size: 14px; font-weight: 700;
  color: var(--text); cursor: pointer;
  transition: background 0.2s;
  overflow: hidden;
}
.report-tab.active { background: var(--subcard); }

/* ══════════════════════════════
   CALENDAR MODAL
══════════════════════════════ */
.modal {
  position: fixed; inset: 0;
  background: rgba(0,0,0,0.75);
  display: none; align-items: center; justify-content: center;
  z-index: 1000;
}
.modal.open { display: flex; }

.modal-box {
  background: var(--card2);
  border-radius: var(--r-lg);
  padding: 24px; width: 340px;
  overflow: hidden;
}

.modal-header {
  display: flex; justify-content: space-between;
  align-items: center; margin-bottom: 18px;
}

.modal-title { font-size: 17px; font-weight: 700; color: var(--text); }

.modal-nav { display: flex; gap: 10px; }

.modal-nav button {
  background: var(--subcard); border: none;
  border-radius: 10px; padding: 7px 14px;
  color: var(--text); font-family: var(--font);
  font-size: 14px; cursor: pointer; overflow: hidden;
}
.modal-nav button:active { opacity: 0.7; }

.modal-weekdays {
  display: grid; grid-template-columns: repeat(7, 1fr);
  gap: 6px; margin-bottom: 10px;
}

.weekday {
  text-align: center; font-size: 12px; font-weight: 700;
  color: var(--text-low); padding: 6px 0;
}

.modal-grid {
  display: grid; grid-template-columns: repeat(7, 1fr); gap: 6px;
}

.day-btn {
  aspect-ratio: 1; border: none;
  background: var(--subcard);
  border-radius: 10px;
  color: var(--text); font-family: var(--font);
  font-size: 14px; font-weight: 400;
  cursor: pointer; position: relative; overflow: hidden;
}
.day-btn:active { opacity: 0.7; }
.day-btn.empty  { background: transparent; cursor: default; }

.day-btn.today::after {
  content: '';
  position: absolute; width: 6px; height: 6px;
  border-radius: 50%; background: var(--gold);
  bottom: 4px; left: 50%; transform: translateX(-50%);
}

.day-btn.selected {
  background: var(--gold); color: #111; font-weight: 700;
}

/* ══════════════════════════════
   REPORT OVERLAY
══════════════════════════════ */
.panel-overlay {
  display: none; position: fixed; inset: 0;
  background: rgba(0,0,0,0.75); z-index: 100;
  align-items: flex-end; justify-content: center;
}
.panel-overlay.open { display: flex; animation: fadeIn 0.2s ease; }
@keyframes fadeIn { from { opacity:0; } to { opacity:1; } }

.slide-panel {
  width: 100%; max-width: 430px;
  background: var(--card2);
  border-radius: 32px 32px 0 0;
  padding: 24px var(--pad) 48px;
  animation: slideUp 0.3s cubic-bezier(0.4,0,0.2,1);
  overflow: hidden;
}
@keyframes slideUp { from { transform:translateY(100%); } to { transform:translateY(0); } }

.slide-handle {
  width: 44px; height: 5px; background: var(--subcard);
  border-radius: 999px; margin: 0 auto 24px;
}
.slide-title {
  font-size: 14px; font-weight: 700; letter-spacing: 1.2px;
  text-transform: uppercase; color: var(--text-mid);
  margin-bottom: 22px; text-align: center;
}

.report-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px; }

.report-card { border-radius: var(--r-md); padding: 18px; overflow: hidden; }
.income-card  { background: #001a0a; }
.expense-card { background: #1a0a00; }

.rc-label {
  font-size: 12px; font-weight: 700; letter-spacing: 0.9px;
  text-transform: uppercase; color: var(--text-low);
  margin-bottom: 10px; display: block;
}
.rc-amount { font-size: 24px; font-weight: 300; letter-spacing: -0.5px; }
.income-card  .rc-amount { color: var(--income); }
.expense-card .rc-amount { color: var(--expense); }

.net-card {
  background: var(--subcard);
  border-radius: var(--r-md); padding: 18px 22px;
  display: flex; align-items: center; justify-content: space-between;
  overflow: hidden;
}
.net-label { font-size: 14px; font-weight: 700; color: var(--text-mid); }
.net-amount { font-size: 30px; font-weight: 300; letter-spacing: -1px; }
.net-amount.positive { color: var(--income); }
.net-amount.negative { color: var(--expense); }
.net-amount.zero     { color: var(--text-mid); }

/* ══════════════════════════════
   LIGHT MODE
══════════════════════════════ */
body.light {
  --bg:      #3a5bd9;
  --card:    #ffffff;
  --card2:   #f0f0f5;
  --subcard: #e0e0e8;
  --text:    #1c1c1e;
  --text-mid: rgba(28,28,30,0.6);
  --text-low: rgba(28,28,30,0.35);
}
body.light .panel-type.expense { background: #fff0e6; }
body.light .panel-type.income  { background: #e6fff2; }
body.light .income-card  { background: #e6fff2; }
body.light .expense-card { background: #fff0e6; }
</style>
</head>
<body>

<!-- ════ LOGIN ════ -->
<div class="screen active" id="screen-login">
  <div class="login-badge"><span class="login-badge-letter">م</span></div>
  <h1 class="login-title">مصروف</h1>
  <p class="login-sub">سجّل مصاريفك ودخلك بسرعة، وبياناتك محفوظة في Google Drive</p>
  <div class="login-features">
    <div class="login-feature">
      <div class="feature-dot blue"></div>
      <span class="feature-text">بياناتك محفوظة في Google Sheets في حسابك</span>
    </div>
    <div class="login-feature">
      <div class="feature-dot orange"></div>
      <span class="feature-text">تتبع المصاريف والدخل يومياً وأسبوعياً وشهرياً</span>
    </div>
    <div class="login-feature">
      <div class="feature-dot green"></div>
      <span class="feature-text">تقارير فورية بالرصيد الصافي</span>
    </div>
  </div>
  <button class="google-btn" id="google-login-btn">
    <svg class="google-g" viewBox="0 0 24 24">
      <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
      <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
      <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z" fill="#FBBC05"/>
      <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
    </svg>
    تسجيل الدخول بـ Google
  </button>
</div>

<!-- ════ MAIN ════ -->
<div class="screen" id="screen-main">
  <div class="topbar">
    <button class="mode-btn" id="mode-btn" onclick="toggleMode()">فاتح</button>
    <div class="user-pill" id="user-pill" onclick="signOut()">خروج</div>
  </div>
  <div class="swipe-container">
    <div class="swipe-viewport" id="swipe-viewport"></div>
  </div>
</div>

<!-- ════ CALENDAR ════ -->
<div class="modal" id="calendar-modal" onclick="closeCalendar(event)">
  <div class="modal-box">
    <div class="modal-header">
      <span class="modal-title" id="modal-month-year"></span>
      <div class="modal-nav">
        <button onclick="prevMonth()">◀</button>
        <button onclick="nextMonth()">▶</button>
      </div>
    </div>
    <div class="modal-weekdays">
      <div class="weekday">ح</div><div class="weekday">ن</div>
      <div class="weekday">ث</div><div class="weekday">ر</div>
      <div class="weekday">خ</div><div class="weekday">ج</div>
      <div class="weekday">س</div>
    </div>
    <div class="modal-grid" id="modal-grid"></div>
  </div>
</div>

<!-- ════ REPORT ════ -->
<div class="panel-overlay" id="report-overlay" onclick="closeReport(event)">
  <div class="slide-panel">
    <div class="slide-handle"></div>
    <div class="slide-title" id="report-title">التقرير اليومي</div>
    <div class="report-grid">
      <div class="report-card income-card">
        <span class="rc-label">الدخل</span>
        <span class="rc-amount" id="r-income">0</span>
      </div>
      <div class="report-card expense-card">
        <span class="rc-label">المصاريف</span>
        <span class="rc-amount" id="r-expense">0</span>
      </div>
    </div>
    <div class="net-card">
      <span class="net-label">الصافي</span>
      <span class="net-amount zero" id="r-net">0</span>
    </div>
  </div>
</div>

<script>
const CLIENT_ID = 'YOUR_GOOGLE_CLIENT_ID';
const AR_DAYS = ['الأحد','الاثنين','الثلاثاء','الأربعاء','الخميس','الجمعة','السبت'];
const EN_DAYS = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];

let isDark = true;
let userEmail = '';
let saveTimer = null;
let records = [];
let viewMonth = new Date();
let selectedDate = new Date();

function fmtDate(d) {
  return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
}
function todayStr() { return fmtDate(new Date()); }
function fmt(n) { return Number(n).toLocaleString('en-US',{minimumFractionDigits:0,maximumFractionDigits:2}); }
function genId() { return Date.now().toString(36)+Math.random().toString(36).slice(2); }

function openCalendar(dateInput) {
  viewMonth = new Date(selectedDate);
  document.getElementById('calendar-modal').classList.add('open');
  renderCalendar();
  window.currentDateInput = dateInput;
}

function closeCalendar(e) {
  if (e.target.id==='calendar-modal')
    document.getElementById('calendar-modal').classList.remove('open');
}

function renderCalendar() {
  const y=viewMonth.getFullYear(), m=viewMonth.getMonth();
  document.getElementById('modal-month-year').textContent =
    viewMonth.toLocaleDateString('ar-EG',{month:'long',year:'numeric'});
  const first=new Date(y,m,1);
  const days=new Date(y,m+1,0).getDate();
  const grid=document.getElementById('modal-grid');
  grid.innerHTML='';
  for(let i=0;i<first.getDay();i++){
    const e=document.createElement('div'); e.className='day-btn empty'; grid.appendChild(e);
  }
  const tStr=todayStr(), selStr=fmtDate(selectedDate);
  for(let d=1;d<=days;d++){
    const date=new Date(y,m,d);
    const dStr=fmtDate(date);
    const btn=document.createElement('button');
    btn.className='day-btn'; btn.textContent=d;
    if(dStr===tStr)   btn.classList.add('today');
    if(dStr===selStr) btn.classList.add('selected');
    btn.addEventListener('click',()=>{
      selectedDate=new Date(date);
      document.getElementById('calendar-modal').classList.remove('open');
      if(window.currentDateInput){
        window.currentDateInput.value=fmtDate(selectedDate);
        window.currentDateInput.dispatchEvent(new Event('change'));
      }
    });
    grid.appendChild(btn);
  }
}

function prevMonth(){ viewMonth.setMonth(viewMonth.getMonth()-1); renderCalendar(); }
function nextMonth(){ viewMonth.setMonth(viewMonth.getMonth()+1); renderCalendar(); }

function buildPage(rec) {
  const isNew   = rec===null;
  const dateObj = isNew ? new Date() : (()=>{const[y,m,d]=rec.date.split('-').map(Number);return new Date(y,m-1,d);})();
  const income  = !isNew && rec.type==='Income';
  const amount  = isNew ? '' : fmt(rec.amount);
  const desc    = isNew ? '' : (rec.description||'');
  const recId   = isNew ? '' : rec.id;

  const page=document.createElement('div');
  page.className='swipe-page';
  page.dataset.recId=recId;

  page.innerHTML=`
    <div class="panels">
      <div class="panel panel-date" onclick="openCalendarForPage(this)">
        <input type="date" class="date-input-hidden" value="${fmtDate(dateObj)}" style="display:none;">
        <span class="date-day-num">${dateObj.getDate()}</span>
        <div class="date-names">
          <span class="date-ar">${AR_DAYS[dateObj.getDay()]}</span>
          <span class="date-en">${EN_DAYS[dateObj.getDay()]}</span>
        </div>
      </div>
      <div class="panel panel-type ${income?'income':'expense'}" onclick="toggleType(this)">
        <span class="type-label">${income?'إيراد':'مصروف'}</span>
      </div>
    </div>
    <div class="field-card amount-card">
      <input class="amount-inp" type="text" inputmode="decimal" placeholder="0" autocomplete="off" value="${amount}">
    </div>
    <div class="field-card desc-card">
      <textarea class="desc-inp" rows="1" placeholder="التفاصيل">${desc}</textarea>
    </div>
    <button class="save-btn">حفظ</button>
    <div class="report-tabs">
      <button class="report-tab" data-period="daily">يومي</button>
      <button class="report-tab" data-period="weekly">أسبوعي</button>
      <button class="report-tab" data-period="monthly">شهري</button>
    </div>
  `;

  const dateInput=page.querySelector('.date-input-hidden');
  const dateNumEl=page.querySelector('.date-day-num');
  const dateArEl=page.querySelector('.date-ar');
  const dateEnEl=page.querySelector('.date-en');

  dateInput.addEventListener('change',()=>{
    if(!dateInput.value)return;
    const[y,m,d]=dateInput.value.split('-').map(Number);
    const nd=new Date(y,m-1,d);
    dateNumEl.textContent=nd.getDate();
    dateArEl.textContent=AR_DAYS[nd.getDay()];
    dateEnEl.textContent=EN_DAYS[nd.getDay()];
  });

  const amountInp=page.querySelector('.amount-inp');
  amountInp.addEventListener('input',()=>{
    const raw=amountInp.value.replace(/,/g,'').replace(/[^0-9.]/g,'');
    const parts=raw.split('.');
    parts[0]=parts[0].replace(/\B(?=(\d{3})+(?!\d))/g,',');
    amountInp.value=parts.length>1?parts[0]+'.'+parts[1]:parts[0];
  });

  const descInp=page.querySelector('.desc-inp');
  setTimeout(()=>{descInp.style.height='auto';descInp.style.height=descInp.scrollHeight+'px';},0);
  descInp.addEventListener('input',()=>{descInp.style.height='auto';descInp.style.height=descInp.scrollHeight+'px';});

  const typePanel=page.querySelector('.panel-type');
  const saveBtn=page.querySelector('.save-btn');

  saveBtn.addEventListener('click',()=>{
    const rawAmt=amountInp.value.replace(/,/g,'');
    if(!rawAmt||isNaN(parseFloat(rawAmt)))return;
    const amount=parseFloat(rawAmt);
    const type=typePanel.classList.contains('income')?'Income':'Expense';
    const date=dateInput.value||todayStr();
    const desc=descInp.value.trim();
    const ts=new Date().toISOString();
    const existId=page.dataset.recId;

    if(existId){
      const idx=records.findIndex(r=>r.id===existId);
      if(idx!==-1){records[idx]={...records[idx],date,type,amount,description:desc,timestamp:ts};localPersist();}
    } else {
      const newRec={id:genId(),date,type,amount,description:desc,timestamp:ts};
      records.push(newRec);
      page.dataset.recId=newRec.id;
      localPersist();
      appendBlankPage();
    }

    if(saveTimer)clearTimeout(saveTimer);
    saveBtn.classList.add('ok'); saveBtn.textContent='✓ تم الحفظ';
    saveTimer=setTimeout(()=>{saveBtn.classList.remove('ok');saveBtn.textContent='حفظ';},2000);
  });

  page.querySelectorAll('.report-tab').forEach(btn=>
    btn.addEventListener('click',()=>openReport(btn.dataset.period)));

  return page;
}

function openCalendarForPage(panelEl){
  openCalendar(panelEl.closest('.swipe-page').querySelector('.date-input-hidden'));
}

function toggleType(panelEl){
  const isIncome=panelEl.classList.contains('income');
  panelEl.classList.toggle('income',!isIncome);
  panelEl.classList.toggle('expense',isIncome);
  panelEl.querySelector('.type-label').textContent=isIncome?'مصروف':'إيراد';
}

function appendBlankPage(){
  const vp=document.getElementById('swipe-viewport');
  vp.appendChild(buildPage(null));
  setTimeout(()=>{vp.scrollLeft=vp.scrollWidth;},50);
}

function renderAllPages(){
  const vp=document.getElementById('swipe-viewport');
  vp.innerHTML='';
  records.forEach(r=>vp.appendChild(buildPage(r)));
  appendBlankPage();
  setTimeout(()=>{vp.scrollLeft=vp.scrollWidth;},50);
}

function localPersist(){localStorage.setItem('masraf-txns',JSON.stringify(records));}
function localLoad(){records=JSON.parse(localStorage.getItem('masraf-txns')||'[]');}

function toggleMode(){
  isDark=!isDark;
  document.body.classList.toggle('light',!isDark);
  document.getElementById('mode-btn').textContent=isDark?'فاتح':'داكن';
  localStorage.setItem('masraf-mode',isDark?'dark':'light');
}

(function initMode(){
  const saved=localStorage.getItem('masraf-mode')||'dark';
  isDark=saved==='dark';
  document.body.classList.toggle('light',!isDark);
  document.getElementById('mode-btn').textContent=isDark?'فاتح':'داكن';
})();

const REPORT_TITLES={daily:'التقرير اليومي',weekly:'التقرير الأسبوعي',monthly:'التقرير الشهري'};

function openReport(period){
  document.getElementById('report-title').textContent=REPORT_TITLES[period];
  const now=new Date();
  const filtered=records.filter(t=>{
    const d=new Date(t.date);if(isNaN(d))return false;
    if(period==='daily') return t.date===todayStr();
    if(period==='weekly'){const s=new Date(now);s.setDate(now.getDate()-now.getDay());const e=new Date(s);e.setDate(s.getDate()+6);return d>=s&&d<=e;}
    if(period==='monthly') return d.getMonth()===now.getMonth()&&d.getFullYear()===now.getFullYear();
  });
  let income=0,expense=0;
  filtered.forEach(t=>{if(t.type==='Income')income+=t.amount;else expense+=t.amount;});
  const net=income-expense;
  document.getElementById('r-income').textContent=fmt(income);
  document.getElementById('r-expense').textContent=fmt(expense);
  const netEl=document.getElementById('r-net');
  netEl.textContent=(net<0?'-':'')+fmt(Math.abs(net));
  netEl.className='net-amount '+(net>0?'positive':net<0?'negative':'zero');
  document.getElementById('report-overlay').classList.add('open');
}

function closeReport(e){
  if(e.target===document.getElementById('report-overlay'))
    document.getElementById('report-overlay').classList.remove('open');
}

function loadGSI(){
  if(CLIENT_ID==='YOUR_GOOGLE_CLIENT_ID')return;
  const s=document.createElement('script');s.src='https://accounts.google.com/gsi/client';
  s.onload=()=>google.accounts.id.initialize({client_id:CLIENT_ID,callback:handleCredential});
  document.head.appendChild(s);
}

function handleCredential(resp){
  const b=resp.credential.split('.')[1].replace(/-/g,'+').replace(/_/g,'/');
  const p=JSON.parse(decodeURIComponent(atob(b).split('').map(c=>'%'+('00'+c.charCodeAt(0).toString(16)).slice(-2)).join('')));
  userEmail=p.email;
  document.getElementById('user-pill').textContent=userEmail.split('@')[0];
  localStorage.setItem('masraf-user',userEmail);
  showMain();
}

function signOut(){localStorage.removeItem('masraf-user');showLogin();}

function showMain(){
  document.getElementById('screen-login').classList.remove('active');
  document.getElementById('screen-main').classList.add('active');
  localLoad();renderAllPages();
}

function showLogin(){
  document.getElementById('screen-main').classList.remove('active');
  document.getElementById('screen-login').classList.add('active');
}

document.getElementById('google-login-btn').addEventListener('click',()=>{
  if(CLIENT_ID==='YOUR_GOOGLE_CLIENT_ID'){
    userEmail='demo@example.com';
    document.getElementById('user-pill').textContent='demo';
    showMain();return;
  }
  google.accounts.id.prompt();
});

loadGSI();
(function checkReturning(){
  const u=localStorage.getItem('masraf-user');
  if(u){userEmail=u;document.getElementById('user-pill').textContent=u.split('@')[0];showMain();}
})();
</script>
</body>
</html>
