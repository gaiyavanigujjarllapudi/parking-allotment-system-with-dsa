# parking-allotment-system-with-dsa
<div align="center">

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![DSA](https://img.shields.io/badge/DSA-HashMap%20%2B%20PQ-brightgreen?style=for-the-badge)

**A data-structure-driven smart parking manager built with pure HTML/CSS/JS.**  
Demonstrates HashMap-based O(1) slot tracking, Priority Queue nearest-slot assignment, and full vehicle entry/exit lifecycle management.

[🚀 Live Demo](#) · [📖 Design Doc](#system-design) · [⚡ DSA Breakdown](#dsa-breakdown)

</div>

---

## 📸 Preview

> Open `index.html` in any browser — no build tools, no dependencies, no install needed.

---

## ✨ Features

- **Real-time Floor Map** — Color-coded live view of all 18 slots across 3 floors (A, B, C)
- **O(1) Slot Assignment** — Always assigns the nearest available slot using a Priority Queue
- **HashMap-Based Tracking** — Three Maps form a bidirectional index for instant lookups
- **Entry / Exit System** — Type any plate number to park or release a vehicle
- **Event Log** — Timestamped log of all parking events
- **DSA Visualizer** — Live view of HashMap buckets, algorithm walkthrough, and time complexity table
- **System Design Panel** — Architecture breakdown with scale considerations
- **Click-to-Park** — Click any free slot on the map to instantly assign a guest vehicle

---

## 🗂️ Project Structure

```
smart-parking-lot/
├── index.html          # Complete app — all HTML, CSS, JS in one file
├── README.md           # This file
└── DESIGN.md           # Detailed system design notes
```

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/smart-parking-lot.git

# Open in browser — that's it!
open index.html
```

No npm, no webpack, no framework. Just open the file.

**Or deploy to GitHub Pages in 2 minutes:**
1. Go to repo **Settings → Pages**
2. Source: `main` branch, `/ (root)`
3. Your live URL: `https://YOUR_USERNAME.github.io/smart-parking-lot`

---

## 🧠 DSA Breakdown

### Data Structures Used

| Structure | Usage | Why |
|-----------|-------|-----|
| `HashMap` (Map) | `slotStatus`, `vehicleMap`, `slotToVeh` | O(1) insert, lookup, delete |
| `Priority Queue` | `nearestQueue` — sorted free slots | O(1) peek nearest free slot |
| `Reverse Index` | `slotToVeh` maps slot → plate | Bidirectional O(1) lookup |

### The 3-HashMap Design

```js
const slotStatus = new Map();  // slotId  → "free" | "occupied"
const vehicleMap = new Map();  // plate   → { slot, entryTime }
const slotToVeh  = new Map();  // slotId  → plate  (reverse index)
```

This is the same **bidirectional index** pattern used in:
- **LRU Cache** (LeetCode #146) — HashMap + Doubly Linked List
- **Database indexes** — primary key → row, row → primary key
- **Operating system page tables** — virtual → physical, physical → virtual

### Why Not a Single Array?

```
Array search for plate:    O(n)  — scan every element
HashMap lookup for plate:  O(1)  — direct hash → bucket → value

With 10,000 vehicles: array = ~10,000 ops, HashMap = ~1 op
```

---

## ⏱️ Time Complexity

| Operation | Data Structure | Time | Space |
|-----------|---------------|------|-------|
| Assign nearest slot | Priority Queue (peek) | **O(1)** | O(1) |
| Park vehicle | 3× HashMap.set() | **O(1)*** | O(1) |
| Plate → slot lookup | vehicleMap.get() | **O(1)** | O(1) |
| Slot → plate lookup | slotToVeh.get() | **O(1)** | O(1) |
| Check slot status | slotStatus.get() | **O(1)** | O(1) |
| Vehicle exit | 3× HashMap.delete() | **O(1)*** | O(1) |
| Re-insert free slot | PQ push + sort | O(n log n) | O(1) |
| List all vehicles | vehicleMap iterate | O(n) | O(n) |

> *O(1) amortized — queue filter is O(n) but HashMap ops dominate in practice.
> With a true binary Min-Heap, re-insert becomes O(log n).

---

## 🏗️ System Design

```
[Vehicle Arrives]
      │
      ▼
[Entry Gate] ── plate scan ──► vehicleMap.has(plate)?
      │                              │ YES → reject (already parked)
      │ NO                           │
      ▼
[Slot Manager]
  nearestQueue[0]  ← O(1) peek
      │
      ▼
  slotStatus.set(slot, "occupied")   ← O(1)
  vehicleMap.set(plate, {slot,time}) ← O(1)
  slotToVeh.set(slot, plate)         ← O(1)
      │
      ▼
[Issue Ticket: Floor A, Slot 3]
      │
      ▼
[Vehicle Exits]
  vehicleMap.get(plate) → slot       ← O(1)
  Release all 3 maps                 ← O(1) each
  Re-sort priority queue             ← O(n log n)
```

### Scale Improvements (Future Scope)

- **True Min-Heap** — reduces exit re-sort from O(n log n) → O(log n)
- **Multiple vehicle types** — separate Maps for bikes/cars/trucks with different slot sizes
- **Persistence** — swap JS Map with Redis for crash recovery and multi-server support
- **Billing** — `entryTime` is already stored; fee calculation is O(1) on exit
- **Multi-gate concurrency** — mutex on PQ pop to handle simultaneous entries

---

## 🛠️ Tech Stack

- **HTML5** — Semantic markup, single-file architecture
- **CSS3** — Custom properties, CSS Grid, keyframe animations
- **Vanilla JavaScript** — ES6+ Maps, arrow functions, destructuring
- **No dependencies** — Zero npm packages, zero build step

---

## 📚 Concepts Demonstrated

- [x] HashMap / Hash Table design and collision handling
- [x] Priority Queue (min-heap simulation)
- [x] Bidirectional index (reverse map)
- [x] Amortized time complexity analysis
- [x] System design thinking (entry/exit gates, slot lifecycle)
- [x] Real-world DSA application

---

## 🤝 Contributing

Pull requests welcome! Some ideas:

- Implement a real binary Min-Heap class
- Add vehicle type support (bikes, trucks, EV charging)
- Add a billing/fee calculator
- Add floor navigation (elevator/stairs routing)
- Backend version using Node.js + Redis

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

<div align="center">
Made with ❤️ as a college DSA project &nbsp;·&nbsp; System Design + Data Structures
</div>
