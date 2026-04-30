<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Smart Parking Lot System</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Syne:wght@400;600;700&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --font-display: 'Syne', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --bg: #0f1117;
      --surface: #1a1d27;
      --surface2: #22263a;
      --border: rgba(255,255,255,0.08);
      --text: #e8eaf0;
      --muted: #6b7080;
      --free: #1D9E75;
      --free-bg: rgba(29,158,117,0.12);
      --occ: #D85A30;
      --occ-bg: rgba(216,90,48,0.12);
      --near: #378ADD;
      --near-bg: rgba(55,138,221,0.13);
      --accent: #7F77DD;
    }

    body {
      font-family: var(--font-display);
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
    }

    /* NAV */
    nav {
      display: flex; align-items: center; justify-content: space-between;
      padding: 16px 32px; border-bottom: 1px solid var(--border);
      background: rgba(15,17,23,0.85); backdrop-filter: blur(12px);
      position: sticky; top: 0; z-index: 100;
    }
    .nav-brand { display: flex; align-items: center; gap: 10px; }
    .nav-brand svg { width: 28px; height: 28px; }
    .nav-brand span { font-size: 17px; font-weight: 700; letter-spacing: -0.4px; }
    .nav-badge {
      font-size: 11px; padding: 3px 10px; border-radius: 20px;
      background: rgba(127,119,221,0.15); color: var(--accent);
      border: 1px solid rgba(127,119,221,0.3); font-family: var(--font-mono);
    }
    .nav-links { display: flex; gap: 6px; }
    .nav-link {
      padding: 6px 14px; border-radius: 7px; font-size: 13px; font-weight: 600;
      cursor: pointer; border: 1px solid var(--border); color: var(--muted);
      background: transparent; text-decoration: none; transition: all .15s;
    }
    .nav-link:hover { color: var(--text); border-color: rgba(255,255,255,0.2); }
    .nav-link.active { color: var(--text); background: var(--surface2); border-color: rgba(255,255,255,0.15); }

    /* HERO */
    .hero {
      padding: 48px 32px 32px;
      background: radial-gradient(ellipse at 20% 0%, rgba(127,119,221,0.08) 0%, transparent 60%),
                  radial-gradient(ellipse at 80% 0%, rgba(55,138,221,0.06) 0%, transparent 60%);
    }
    .hero h1 { font-size: 32px; font-weight: 700; letter-spacing: -0.8px; margin-bottom: 8px; }
    .hero h1 span { color: var(--accent); }
    .hero p { color: var(--muted); font-size: 15px; max-width: 520px; line-height: 1.6; }
    .hero-tags { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 16px; }
    .tag {
      font-size: 11px; font-family: var(--font-mono); padding: 4px 10px;
      border-radius: 5px; border: 1px solid var(--border); color: var(--muted);
    }
    .tag.green { color: var(--free); border-color: rgba(29,158,117,0.3); background: var(--free-bg); }
    .tag.blue  { color: var(--near); border-color: rgba(55,138,221,0.3); background: var(--near-bg); }
    .tag.purple{ color: var(--accent); border-color: rgba(127,119,221,0.3); background: rgba(127,119,221,0.08); }

    /* MAIN LAYOUT */
    .container { padding: 24px 32px; max-width: 1200px; margin: 0 auto; }
    .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; }
    .grid-2 { display: grid; grid-template-columns: 1.4fr 1fr; gap: 16px; }
    @media(max-width: 900px) { .grid-3, .grid-2 { grid-template-columns: 1fr; } nav { padding: 12px 16px; } .container { padding: 16px; } }

    /* STAT CARDS */
    .stat-card {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 12px; padding: 16px 20px;
    }
    .stat-label { font-size: 11px; color: var(--muted); font-weight: 600; text-transform: uppercase; letter-spacing: .6px; margin-bottom: 6px; }
    .stat-val { font-size: 28px; font-weight: 700; }
    .stat-val.green { color: var(--free); }
    .stat-val.red   { color: var(--occ); }
    .stat-val.blue  { color: var(--near); }
    .stat-sub { font-size: 12px; color: var(--muted); margin-top: 4px; font-family: var(--font-mono); }

    /* PANELS */
    .panel {
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 14px; overflow: hidden;
    }
    .panel-head {
      padding: 14px 18px; border-bottom: 1px solid var(--border);
      display: flex; align-items: center; justify-content: space-between;
    }
    .panel-title { font-size: 13px; font-weight: 600; color: var(--text); }
    .panel-body { padding: 16px 18px; }

    /* LOT GRID */
    .floor-section { margin-bottom: 14px; }
    .floor-label {
      font-size: 10px; font-weight: 700; color: var(--muted);
      text-transform: uppercase; letter-spacing: .8px; margin-bottom: 8px;
    }
    .slot-row { display: flex; gap: 6px; flex-wrap: wrap; }
    .slot {
      width: 44px; height: 32px; border-radius: 6px;
      display: flex; align-items: center; justify-content: center;
      font-family: var(--font-mono); font-size: 11px; font-weight: 600;
      cursor: pointer; transition: transform .12s, box-shadow .12s;
      border: 1.5px solid transparent; position: relative;
    }
    .slot.free     { background: var(--free-bg); color: var(--free); border-color: rgba(29,158,117,0.3); }
    .slot.occupied { background: var(--occ-bg); color: var(--occ); border-color: rgba(216,90,48,0.2); cursor: default; }
    .slot.nearest  { background: var(--near-bg); color: var(--near); border-color: rgba(55,138,221,0.5); animation: pulse 1.8s ease-in-out infinite; }
    .slot.free:hover, .slot.nearest:hover { transform: scale(1.1); box-shadow: 0 4px 12px rgba(0,0,0,.3); }
    @keyframes pulse { 0%,100%{box-shadow:0 0 0 0 rgba(55,138,221,.2)} 50%{box-shadow:0 0 0 5px rgba(55,138,221,.05)} }

    .legend { display: flex; gap: 14px; flex-wrap: wrap; margin-top: 12px; }
    .legend-item { display: flex; align-items: center; gap: 6px; font-size: 12px; color: var(--muted); }
    .ld { width: 12px; height: 12px; border-radius: 3px; }
    .ld-free { background: var(--free-bg); border: 1px solid rgba(29,158,117,0.3); }
    .ld-occ  { background: var(--occ-bg);  border: 1px solid rgba(216,90,48,0.2); }
    .ld-near { background: var(--near-bg); border: 1px solid rgba(55,138,221,0.5); }

    /* CONTROLS */
    .action-label { font-size: 11px; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: .5px; margin-bottom: 7px; }
    .input-row { display: flex; gap: 8px; }
    .plate-input {
      flex: 1; padding: 9px 12px; border: 1px solid var(--border); border-radius: 8px;
      font-family: var(--font-mono); font-size: 13px; font-weight: 600;
      background: var(--surface2); color: var(--text); text-transform: uppercase; outline: none;
    }
    .plate-input:focus { border-color: rgba(255,255,255,0.2); }
    .btn {
      padding: 9px 16px; border-radius: 8px; font-family: var(--font-display);
      font-size: 12px; font-weight: 600; cursor: pointer; border: 1px solid var(--border);
      transition: opacity .15s, transform .1s; background: var(--surface2); color: var(--text);
    }
    .btn:hover { opacity: .8; }
    .btn:active { transform: scale(.97); }
    .btn-enter { background: var(--free-bg); color: var(--free); border-color: rgba(29,158,117,0.4); }
    .btn-exit  { background: var(--occ-bg);  color: var(--occ);  border-color: rgba(216,90,48,0.3); }

    /* LOG */
    .log-area {
      background: var(--bg); border-radius: 8px; padding: 10px 12px;
      min-height: 100px; max-height: 160px; overflow-y: auto;
      font-family: var(--font-mono); font-size: 11px;
      border: 1px solid var(--border);
    }
    .log-entry { padding: 4px 0; border-bottom: 1px solid rgba(255,255,255,0.04); display: flex; gap: 10px; }
    .log-entry:last-child { border-bottom: none; }
    .log-time { color: var(--muted); min-width: 56px; }
    .log-ok   { color: var(--free); }
    .log-err  { color: var(--occ); }
    .log-info { color: var(--near); }

    /* VEHICLE LIST */
    .veh-row {
      display: flex; align-items: center; gap: 10px;
      padding: 7px 0; border-bottom: 1px solid var(--border); font-size: 12px;
    }
    .veh-row:last-child { border-bottom: none; }
    .veh-plate { font-family: var(--font-mono); font-weight: 600; min-width: 100px; }
    .veh-slot {
      background: var(--near-bg); color: var(--near);
      padding: 2px 8px; border-radius: 4px; font-family: var(--font-mono); font-size: 11px; font-weight: 600;
    }
    .veh-floor {
      font-size: 10px; padding: 2px 6px; border-radius: 4px;
      background: var(--surface2); color: var(--muted); font-family: var(--font-mono);
    }
    .veh-time { color: var(--muted); font-size: 11px; margin-left: auto; font-family: var(--font-mono); }
    .no-veh { color: var(--muted); font-size: 12px; text-align: center; padding: 24px 0; }

    /* DSA SECTION */
    .dsa-tabs { display: flex; gap: 6px; margin-bottom: 14px; flex-wrap: wrap; }
    .dsa-tab {
      padding: 6px 14px; border-radius: 7px; border: 1px solid var(--border);
      font-size: 12px; font-weight: 600; cursor: pointer;
      background: var(--surface2); color: var(--muted); transition: all .15s;
    }
    .dsa-tab.active { background: var(--near-bg); color: var(--near); border-color: rgba(55,138,221,0.4); }
    .code-block {
      background: var(--bg); border-radius: 8px; padding: 14px 16px;
      overflow-x: auto; font-family: var(--font-mono); font-size: 12px;
      line-height: 1.75; color: var(--text); border: 1px solid var(--border);
      white-space: pre;
    }
    .kw  { color: #c586c0; }
    .fn  { color: #dcdcaa; }
    .str { color: #ce9178; }
    .cm  { color: #6a9955; }
    .num { color: #b5cea8; }

    .cplx-table { width: 100%; border-collapse: collapse; font-size: 12px; }
    .cplx-table th {
      text-align: left; padding: 7px 10px; background: var(--surface2);
      border-bottom: 1px solid var(--border); font-weight: 600; color: var(--muted);
      font-size: 10px; text-transform: uppercase; letter-spacing: .5px;
    }
    .cplx-table td { padding: 7px 10px; border-bottom: 1px solid var(--border); }
    .cplx-table tr:last-child td { border-bottom: none; }
    .badge-o1  { background: var(--free-bg); color: var(--free); padding: 1px 7px; border-radius: 4px; font-weight: 700; font-family: var(--font-mono); font-size: 11px; }
    .badge-on  { background: var(--occ-bg);  color: var(--occ);  padding: 1px 7px; border-radius: 4px; font-weight: 700; font-family: var(--font-mono); font-size: 11px; }
    .badge-olog{ background: rgba(127,119,221,0.12); color: var(--accent); padding: 1px 7px; border-radius: 4px; font-weight: 700; font-family: var(--font-mono); font-size: 11px; }

    .info-box {
      background: var(--surface2); border-radius: 8px; padding: 12px 14px;
      font-size: 12px; color: var(--muted); margin-top: 12px; line-height: 1.6;
      border-left: 3px solid var(--accent);
    }
    .info-box strong { color: var(--text); }

    .hash-vis { display: flex; gap: 5px; align-items: flex-end; height: 80px; margin-top: 10px; }
    .hbucket { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; gap: 3px; }
    .hbar { width: 100%; border-radius: 4px 4px 0 0; transition: height .4s ease; min-height: 4px; }
    .hbl { font-size: 9px; font-family: var(--font-mono); color: var(--muted); }

    .section-gap { margin-bottom: 20px; }

    /* FOOTER */
    footer {
      text-align: center; padding: 24px; color: var(--muted);
      font-size: 12px; border-top: 1px solid var(--border); margin-top: 32px;
    }
    footer a { color: var(--accent); text-decoration: none; }
    footer a:hover { text-decoration: underline; }
  </style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="nav-brand">
    <svg viewBox="0 0 28 28" fill="none">
      <rect x="2" y="10" width="24" height="16" rx="4" fill="rgba(55,138,221,0.15)" stroke="#378ADD" stroke-width="1"/>
      <rect x="5" y="13" width="5" height="4" rx="1.5" fill="#1D9E75"/>
      <rect x="12" y="13" width="5" height="4" rx="1.5" fill="#D85A30"/>
      <rect x="19" y="13" width="5" height="4" rx="1.5" fill="#1D9E75"/>
      <rect x="5" y="19" width="5" height="4" rx="1.5" fill="#D85A30"/>
      <rect x="12" y="19" width="5" height="4" rx="1.5" fill="#1D9E75"/>
      <rect x="19" y="19" width="5" height="4" rx="1.5" fill="#1D9E75"/>
      <path d="M9 10V7a5 5 0 0 1 10 0v3" stroke="#378ADD" stroke-width="1" stroke-linecap="round"/>
    </svg>
    <span>ParkSmart</span>
  </div>
  <span class="nav-badge">DSA Project · HashMap + PQ</span>
  <div class="nav-links">
    <a href="#lot" class="nav-link active">Lot View</a>
    <a href="#dsa" class="nav-link">DSA</a>
    <a href="https://github.com" class="nav-link" target="_blank">GitHub</a>
  </div>
</nav>

<!-- HERO -->
<section class="hero">
  <h1>Smart <span>Parking</span> Lot System</h1>
  <p>A data-structure-driven parking manager. HashMap-based O(1) slot tracking, priority-queue nearest-slot assignment, and full entry/exit lifecycle management.</p>
  <div class="hero-tags">
    <span class="tag green">HashMap O(1) Lookup</span>
    <span class="tag blue">Priority Queue</span>
    <span class="tag purple">System Design</span>
    <span class="tag">3 Floors · 18 Slots</span>
    <span class="tag">Live DSA Visualizer</span>
  </div>
</section>

<div class="container">

  <!-- STATS -->
  <div class="grid-3 section-gap" id="lot">
    <div class="stat-card">
      <div class="stat-label">Total Capacity</div>
      <div class="stat-val" id="s-total">18</div>
      <div class="stat-sub">3 floors × 6 slots</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Available Slots</div>
      <div class="stat-val green" id="s-free">18</div>
      <div class="stat-sub" id="s-free-pct">100% capacity free</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Nearest Free Slot</div>
      <div class="stat-val blue" id="s-near">A1</div>
      <div class="stat-sub">Priority Queue head</div>
    </div>
  </div>

  <!-- LOT + CONTROLS -->
  <div class="grid-2 section-gap">
    <!-- LOT MAP -->
    <div class="panel">
      <div class="panel-head">
        <span class="panel-title">Floor Map — Live View</span>
        <span style="font-size:11px;color:var(--muted);font-family:var(--font-mono)" id="occ-ratio">0/18 occupied</span>
      </div>
      <div class="panel-body">
        <div id="lot-render"></div>
        <div class="legend">
          <div class="legend-item"><div class="ld ld-free"></div>Free (click to park)</div>
          <div class="legend-item"><div class="ld ld-occ"></div>Occupied</div>
          <div class="legend-item"><div class="ld ld-near"></div>Nearest</div>
        </div>
      </div>
    </div>

    <!-- CONTROLS + LOG + VEHICLES -->
    <div style="display:flex;flex-direction:column;gap:14px">

      <!-- ENTRY/EXIT -->
      <div class="panel">
        <div class="panel-head"><span class="panel-title">Entry / Exit Gate</span></div>
        <div class="panel-body">
          <div class="action-label" style="margin-bottom:7px">Vehicle Plate Number</div>
          <div class="input-row">
            <input class="plate-input" id="plate-in" maxlength="10" placeholder="TS09AB1234" autocomplete="off"/>
          </div>
          <div class="input-row" style="margin-top:8px">
            <button class="btn btn-enter" onclick="vehicleEntry()">↓ Enter</button>
            <button class="btn btn-exit"  onclick="vehicleExit()">↑ Exit</button>
            <button class="btn" onclick="randomEntry()" title="Park random vehicle">⚡ Random</button>
          </div>
        </div>
      </div>

      <!-- LOG -->
      <div class="panel">
        <div class="panel-head"><span class="panel-title">Event Log</span></div>
        <div class="panel-body" style="padding:12px">
          <div class="log-area" id="log-area"></div>
        </div>
      </div>

      <!-- PARKED VEHICLES -->
      <div class="panel">
        <div class="panel-head">
          <span class="panel-title">Parked Vehicles</span>
          <span style="font-size:11px;font-family:var(--font-mono);color:var(--muted)" id="veh-count">0 vehicles</span>
        </div>
        <div class="panel-body" style="padding:10px 14px;max-height:180px;overflow-y:auto">
          <div id="vehicle-list"><div class="no-veh">No vehicles parked</div></div>
        </div>
      </div>
    </div>
  </div>

  <!-- DSA SECTION -->
  <div class="panel" id="dsa">
    <div class="panel-head"><span class="panel-title">DSA Internals — System Design</span></div>
    <div class="panel-body">
      <div class="dsa-tabs">
        <button class="dsa-tab active" onclick="showDSA('hashmap')">HashMap Structure</button>
        <button class="dsa-tab" onclick="showDSA('algo')">Nearest Slot Algorithm</button>
        <button class="dsa-tab" onclick="showDSA('complexity')">Time Complexity</button>
        <button class="dsa-tab" onclick="showDSA('design')">System Design</button>
      </div>
      <div id="dsa-content"></div>
    </div>
  </div>

</div>

<!-- FOOTER -->
<footer>
  Built with HTML · CSS · Vanilla JS &nbsp;·&nbsp;
  Data Structures: HashMap, Priority Queue, Reverse Index &nbsp;·&nbsp;
  <a href="https://github.com" target="_blank">View on GitHub</a>
</footer>

<script>
// ================================================================
//  SMART PARKING LOT — DATA STRUCTURES
// ================================================================

const FLOORS = ['A', 'B', 'C'];
const SLOTS_PER_FLOOR = 6;
const RANDOM_PLATES = ['AP28CD1234','TS09AB5678','KA03EF9012','MH12GH3456','DL01IJ7890','UP32KL2345','RJ14MN6789','TN22OP0123'];

// Core HashMaps
const slotStatus = new Map();   // slotId  → "free" | "occupied"
const vehicleMap = new Map();   // plate   → { slot, entryTime }
const slotToVeh  = new Map();   // slotId  → plate  (reverse index)

// Priority Queue (min-heap simulation via sorted array)
let nearestQueue = [];

function slotIndex(id) {
  return FLOORS.indexOf(id[0]) * SLOTS_PER_FLOOR + (parseInt(id.slice(1)) - 1);
}

function sortQueue() {
  nearestQueue.sort((a, b) => slotIndex(a) - slotIndex(b));
}

function getNearestFree() {
  return nearestQueue.length ? nearestQueue[0] : null;
}

// Initialize all slots
(function init() {
  for (const f of FLOORS) {
    for (let n = 1; n <= SLOTS_PER_FLOOR; n++) {
      const id = f + n;
      slotStatus.set(id, 'free');
      nearestQueue.push(id);
    }
  }
  sortQueue();
  const demos = [
    ['AP28CD1234', 'A2'], ['TS09XY5678', 'A5'],
    ['KA03CD9999', 'B2'], ['DL01EF3311', 'B4'],
    ['MH12GH7777', 'C1'],
  ];
  for (const [p, s] of demos) parkVehicle(p, s, true);
  addLog('System initialized — 18 slots ready', 'info');
  addLog('5 demo vehicles pre-parked', 'info');
})();

// ================================================================
//  CORE OPERATIONS
// ================================================================

function parkVehicle(plate, slotOverride, silent) {
  if (vehicleMap.has(plate)) {
    if (!silent) addLog(`${plate} already parked at ${vehicleMap.get(plate).slot}`, 'err');
    return false;
  }
  const slot = slotOverride || getNearestFree();
  if (!slot) {
    if (!silent) addLog('Lot is FULL — no free slots available', 'err');
    return false;
  }
  slotStatus.set(slot, 'occupied');
  vehicleMap.set(plate, { slot, entryTime: new Date() });
  slotToVeh.set(slot, plate);
  nearestQueue = nearestQueue.filter(s => s !== slot);
  if (!silent) addLog(`${plate} → slot ${slot} assigned (nearest)`, 'ok');
  refreshAll();
  return true;
}

function releaseVehicle(plate) {
  if (!vehicleMap.has(plate)) {
    addLog(`${plate} not found in parking system`, 'err');
    return false;
  }
  const { slot, entryTime } = vehicleMap.get(plate);
  const mins = Math.floor((new Date() - entryTime) / 60000);
  slotStatus.set(slot, 'free');
  vehicleMap.delete(plate);
  slotToVeh.delete(slot);
  nearestQueue.push(slot);
  sortQueue();
  addLog(`${plate} exited slot ${slot} · Duration: ${mins}m`, 'info');
  refreshAll();
  return true;
}

// ================================================================
//  UI ACTIONS
// ================================================================

function vehicleEntry() {
  const p = document.getElementById('plate-in').value.toUpperCase().trim();
  if (!p) { addLog('Please enter a vehicle plate number', 'err'); return; }
  document.getElementById('plate-in').value = '';
  parkVehicle(p, null, false);
}

function vehicleExit() {
  const p = document.getElementById('plate-in').value.toUpperCase().trim();
  if (!p) { addLog('Please enter a vehicle plate number', 'err'); return; }
  document.getElementById('plate-in').value = '';
  releaseVehicle(p);
}

function randomEntry() {
  const available = RANDOM_PLATES.filter(p => !vehicleMap.has(p));
  if (!available.length) { addLog('All demo plates already parked', 'err'); return; }
  const p = available[Math.floor(Math.random() * available.length)];
  parkVehicle(p, null, false);
}

function quickPark(slot) {
  const plate = 'GUEST' + Math.floor(Math.random() * 9000 + 1000);
  parkVehicle(plate, slot, false);
}

// ================================================================
//  RENDER
// ================================================================

function refreshAll() {
  renderLot(); renderStats(); renderVehicleList(); renderDSA(activeDSA);
}

function renderLot() {
  const near = getNearestFree();
  let html = '';
  for (const f of FLOORS) {
    html += `<div class="floor-section"><div class="floor-label">Floor ${f}</div><div class="slot-row">`;
    for (let n = 1; n <= SLOTS_PER_FLOOR; n++) {
      const id = f + n;
      const st = slotStatus.get(id);
      const isNearest = id === near;
      const cls = isNearest ? 'nearest' : st === 'occupied' ? 'occupied' : 'free';
      const plate = slotToVeh.get(id) || '';
      const onclick = cls !== 'occupied' ? `onclick="quickPark('${id}')"` : '';
      const title = plate ? plate : (cls === 'nearest' ? 'Nearest — click to park' : 'Click to park');
      html += `<div class="slot ${cls}" title="${title}" ${onclick}>${id}</div>`;
    }
    html += '</div></div>';
  }
  document.getElementById('lot-render').innerHTML = html;
}

function renderStats() {
  const total = slotStatus.size;
  const occ = [...slotStatus.values()].filter(v => v === 'occupied').length;
  const free = total - occ;
  const near = getNearestFree() || '—';
  const pct = Math.round((free / total) * 100);
  document.getElementById('s-total').textContent = total;
  document.getElementById('s-free').textContent = free;
  document.getElementById('s-free-pct').textContent = `${pct}% capacity free`;
  document.getElementById('s-near').textContent = near;
  document.getElementById('occ-ratio').textContent = `${occ}/${total} occupied`;
}

function renderVehicleList() {
  const el = document.getElementById('vehicle-list');
  const cnt = document.getElementById('veh-count');
  cnt.textContent = `${vehicleMap.size} vehicle${vehicleMap.size !== 1 ? 's' : ''}`;
  if (vehicleMap.size === 0) { el.innerHTML = '<div class="no-veh">No vehicles parked</div>'; return; }
  const now = new Date();
  let html = '';
  for (const [plate, { slot, entryTime }] of vehicleMap) {
    const mins = Math.floor((now - entryTime) / 60000);
    const floor = `Floor ${slot[0]}`;
    html += `<div class="veh-row">
      <span class="veh-plate">${plate}</span>
      <span class="veh-slot">${slot}</span>
      <span class="veh-floor">${floor}</span>
      <span class="veh-time">${mins}m</span>
    </div>`;
  }
  el.innerHTML = html;
}

// ================================================================
//  LOG
// ================================================================

function addLog(msg, type) {
  const la = document.getElementById('log-area');
  const t = new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
  const div = document.createElement('div');
  div.className = 'log-entry';
  div.innerHTML = `<span class="log-time">${t}</span><span class="log-${type || 'info'}">${msg}</span>`;
  la.prepend(div);
  if (la.children.length > 25) la.removeChild(la.lastChild);
}

// ================================================================
//  DSA VIEWS
// ================================================================

let activeDSA = 'hashmap';

function showDSA(tab) {
  activeDSA = tab;
  document.querySelectorAll('.dsa-tab').forEach((t, i) => {
    t.classList.toggle('active', ['hashmap','algo','complexity','design'][i] === tab);
  });
  renderDSA(tab);
}

function renderDSA(tab) {
  const el = document.getElementById('dsa-content');
  if      (tab === 'hashmap')    el.innerHTML = renderHashmap();
  else if (tab === 'algo')       el.innerHTML = renderAlgo();
  else if (tab === 'complexity') el.innerHTML = renderComplexity();
  else                           el.innerHTML = renderDesign();
}

function hashFn(key, buckets) {
  let h = 0;
  for (const c of key) h = (h * 31 + c.charCodeAt(0)) >>> 0;
  return h % buckets;
}

function renderHashmap() {
  const B = 8;
  const counts = new Array(B).fill(0);
  for (const [k] of slotStatus) counts[hashFn(k, B)]++;
  const max = Math.max(...counts) || 1;
  const colors = ['#378ADD','#1D9E75','#D85A30','#7F77DD','#BA7517','#C04878','#639922','#888780'];
  const bars = counts.map((c, i) => `
    <div class="hbucket">
      <div class="hbar" style="height:${Math.round((c/max)*60)+6}px;background:${colors[i]}22;border:1px solid ${colors[i]}55"></div>
      <div class="hbl">[${i}] ×${c}</div>
    </div>`).join('');

  let entries = '';
  let n = 0;
  for (const [k, v] of slotStatus) {
    if (n++ >= 6) break;
    const h = hashFn(k, B);
    const plate = slotToVeh.get(k) || '—';
    entries += `<div style="display:flex;align-items:center;gap:8px;padding:4px 0;border-bottom:1px solid rgba(255,255,255,0.05);font-family:var(--font-mono);font-size:11px">
      <span style="color:var(--muted);min-width:26px">[${h}]</span>
      <span style="color:var(--near);font-weight:600;min-width:34px">"${k}"</span>
      <span style="color:var(--muted)">→</span>
      <span style="color:${v==='free'?'var(--free)':'var(--occ)'};font-weight:600">${v}</span>
      ${plate !== '—' ? `<span style="color:var(--muted);font-size:10px;margin-left:auto">${plate}</span>` : ''}
    </div>`;
  }

  return `<div style="font-size:12px;color:var(--muted);margin-bottom:12px">
    Three HashMaps form a bidirectional index — every operation is <span style="color:var(--free);font-family:var(--font-mono)">O(1)</span>.
    Live distribution of <strong style="color:var(--text)">${slotStatus.size}</strong> slot keys across 8 hash buckets:
  </div>
  <div style="display:flex;gap:20px;flex-wrap:wrap">
    <div style="flex:1;min-width:140px">
      <div style="font-size:10px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin-bottom:8px">Hash Distribution</div>
      <div style="display:flex;gap:4px;align-items:flex-end;height:80px">${bars}</div>
      <div style="font-size:10px;color:var(--muted);margin-top:4px">hash(key) % 8  →  bucket index</div>
    </div>
    <div style="flex:1.4;min-width:180px">
      <div style="font-size:10px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin-bottom:8px">Live slotStatus entries</div>
      ${entries}
    </div>
  </div>
  <div class="code-block" style="margin-top:14px"><span class="cm">// The 3 HashMaps — all O(1) operations</span>
<span class="kw">const</span> slotStatus = <span class="kw">new</span> <span class="fn">Map</span>();  <span class="cm">// slotId  → "free" | "occupied"</span>
<span class="kw">const</span> vehicleMap = <span class="kw">new</span> <span class="fn">Map</span>();  <span class="cm">// plate   → { slot, entryTime }</span>
<span class="kw">const</span> slotToVeh  = <span class="kw">new</span> <span class="fn">Map</span>();  <span class="cm">// slot    → plate  (reverse index)</span>

slotStatus.<span class="fn">get</span>(<span class="str">"A1"</span>);          <span class="cm">// O(1) → "free"</span>
vehicleMap.<span class="fn">get</span>(<span class="str">"TS09AB1234"</span>);  <span class="cm">// O(1) → { slot: "A2", ... }</span>
slotToVeh.<span class="fn">get</span>(<span class="str">"A2"</span>);          <span class="cm">// O(1) → "TS09AB1234"</span></div>`;
}

function renderAlgo() {
  const q = nearestQueue.slice(0, 8);
  const qViz = q.map((s, i) => `
    <div style="display:flex;align-items:center;justify-content:center;flex-direction:column;min-width:44px">
      <div style="width:38px;height:28px;border-radius:5px;background:${i===0?'var(--near-bg)':'var(--surface2)'};border:1px solid ${i===0?'rgba(55,138,221,.5)':'var(--border)'};display:flex;align-items:center;justify-content:center;font-family:var(--font-mono);font-size:11px;font-weight:600;color:${i===0?'var(--near)':'var(--muted)'}">${s}</div>
      ${i===0?'<div style="font-size:9px;color:var(--near);margin-top:3px;font-family:var(--font-mono)">head</div>':''}
    </div>`).join(`<div style="color:var(--muted);font-size:14px;align-self:center;padding-bottom:12px">›</div>`);

  return `<div style="font-size:12px;color:var(--muted);margin-bottom:12px">
    The <strong style="color:var(--text)">Priority Queue</strong> (min-heap simulation) always keeps the nearest slot at index 0.
  </div>
  <div style="font-size:10px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin-bottom:8px">Current Queue State (${nearestQueue.length} free slots)</div>
  <div style="display:flex;align-items:center;gap:4px;flex-wrap:wrap;padding:10px;background:var(--bg);border-radius:8px;border:1px solid var(--border)">${q.length ? qViz : '<span style="color:var(--occ);font-size:12px;font-family:var(--font-mono)">LOT IS FULL</span>'}</div>
  <div class="code-block" style="margin-top:14px"><span class="cm">// Assign nearest slot — O(1) peek</span>
<span class="kw">function</span> <span class="fn">getNearestFree</span>() {
  <span class="kw">return</span> nearestQueue[<span class="num">0</span>];
}

<span class="cm">// Park vehicle</span>
<span class="kw">function</span> <span class="fn">parkVehicle</span>(plate) {
  <span class="kw">const</span> slot = <span class="fn">getNearestFree</span>();
  slotStatus.<span class="fn">set</span>(slot, <span class="str">"occupied"</span>);
  vehicleMap.<span class="fn">set</span>(plate, { slot, entryTime: <span class="kw">new</span> <span class="fn">Date</span>() });
  slotToVeh.<span class="fn">set</span>(slot, plate);
  nearestQueue = nearestQueue.<span class="fn">filter</span>(s => s !== slot);
}

<span class="cm">// Release slot</span>
<span class="kw">function</span> <span class="fn">releaseVehicle</span>(plate) {
  <span class="kw">const</span> { slot } = vehicleMap.<span class="fn">get</span>(plate);
  slotStatus.<span class="fn">set</span>(slot, <span class="str">"free"</span>);
  vehicleMap.<span class="fn">delete</span>(plate);
  slotToVeh.<span class="fn">delete</span>(slot);
  nearestQueue.<span class="fn">push</span>(slot);
  nearestQueue.<span class="fn">sort</span>((a, b) => <span class="fn">slotIndex</span>(a) - <span class="fn">slotIndex</span>(b));
}</div>`;
}

function renderComplexity() {
  return `<table class="cplx-table">
    <tr><th>Operation</th><th>Data Structure Used</th><th>Time</th><th>Space</th></tr>
    <tr><td>Assign nearest slot</td><td>Priority Queue (peek)</td><td><span class="badge-o1">O(1)</span></td><td>O(1)</td></tr>
    <tr><td>Park vehicle</td><td>3× HashMap set</td><td><span class="badge-o1">O(1)*</span></td><td>O(1)</td></tr>
    <tr><td>Plate → slot lookup</td><td>vehicleMap.get()</td><td><span class="badge-o1">O(1)</span></td><td>O(1)</td></tr>
    <tr><td>Slot → plate lookup</td><td>slotToVeh.get()</td><td><span class="badge-o1">O(1)</span></td><td>O(1)</td></tr>
    <tr><td>Check slot status</td><td>slotStatus.get()</td><td><span class="badge-o1">O(1)</span></td><td>O(1)</td></tr>
    <tr><td>Vehicle exit</td><td>3× HashMap delete</td><td><span class="badge-o1">O(1)*</span></td><td>O(1)</td></tr>
    <tr><td>Re-insert free slot</td><td>PQ push + sort</td><td><span class="badge-olog">O(n log n)</span></td><td>O(1)</td></tr>
    <tr><td>List all parked vehicles</td><td>vehicleMap iterate</td><td><span class="badge-on">O(n)</span></td><td>O(n)</td></tr>
  </table>
  <div class="info-box">
    <strong>* O(1) amortized</strong> — queue filter is O(n) but HashMap ops dominate in the average case.
    With a true Min-Heap, re-insert becomes O(log n). n = total number of parking slots.
  </div>
  <div class="info-box" style="margin-top:8px;border-left-color:var(--free)">
    <strong>Why 3 HashMaps instead of 1?</strong><br>
    A single array would require O(n) linear search to find a plate. The three-map design creates a
    bidirectional index — same pattern as <strong>LRU Cache (LeetCode #146)</strong> and database indexes.
    Every lookup is O(1) in any direction.
  </div>`;
}

function renderDesign() {
  return `<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;flex-wrap:wrap">
    <div>
      <div style="font-size:11px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin-bottom:10px">Architecture</div>
      <div style="font-size:12px;color:var(--muted);line-height:1.8">
        <div style="padding:6px 10px;background:var(--surface2);border-radius:6px;margin-bottom:6px;border-left:2px solid var(--accent)">
          <span style="color:var(--text);font-weight:600">Entry Gate</span><br>Plate scan → vehicleMap lookup → assign nearest PQ slot
        </div>
        <div style="padding:6px 10px;background:var(--surface2);border-radius:6px;margin-bottom:6px;border-left:2px solid var(--free)">
          <span style="color:var(--text);font-weight:600">Slot Manager</span><br>slotStatus HashMap + nearestQueue for real-time tracking
        </div>
        <div style="padding:6px 10px;background:var(--surface2);border-radius:6px;margin-bottom:6px;border-left:2px solid var(--occ)">
          <span style="color:var(--text);font-weight:600">Exit Gate</span><br>Plate → O(1) lookup → release slot → re-sort PQ
        </div>
        <div style="padding:6px 10px;background:var(--surface2);border-radius:6px;border-left:2px solid var(--near)">
          <span style="color:var(--text);font-weight:600">Reverse Index</span><br>slotToVeh for O(1) slot→plate (admin / enforcement)
        </div>
      </div>
    </div>
    <div>
      <div style="font-size:11px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.5px;margin-bottom:10px">Scale Considerations</div>
      <div style="font-size:12px;color:var(--muted);line-height:1.9">
        <div>🔷 <strong style="color:var(--text)">Multi-level floors</strong> — extend FLOORS array, O(1) unchanged</div>
        <div>🔷 <strong style="color:var(--text)">Multiple lot types</strong> — separate Maps per vehicle class</div>
        <div>🔷 <strong style="color:var(--text)">Persistence</strong> — swap Map with Redis / IndexedDB</div>
        <div>🔷 <strong style="color:var(--text)">True Min-Heap</strong> — O(log n) insert vs current O(n log n)</div>
        <div>🔷 <strong style="color:var(--text)">Pricing</strong> — entryTime already stored, billing trivial to add</div>
        <div>🔷 <strong style="color:var(--text)">Concurrent access</strong> — mutex on PQ pop for multi-gate</div>
      </div>
    </div>
  </div>`;
}

document.getElementById('plate-in').addEventListener('keydown', e => {
  if (e.key === 'Enter') vehicleEntry();
});

refreshAll();
</script>
</body>
</html>
