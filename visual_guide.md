# Little's Law Problems - Visual Guide
## Understanding the Systems

This guide provides visual representations and detailed explanations of each problem to help you understand the systems before applying Little's Law.

---

## Problem 4: Chrome Wheels Inc. - Priority Manufacturing System

### System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    CHROME WHEELS INC.                        │
│                  Production System                           │
└─────────────────────────────────────────────────────────────┘

INPUTS (Arrival Rates):
┌──────────────┐
│ Ultra-chrome │ ──── 8 orders/day ───┐
│ (Priority 1) │                       │
└──────────────┘                       │
                                       ├──> [PRODUCTION] ──> Shipment
┌──────────────┐                       │      (6 days)
│  Ex-chrome   │ ──── 4 orders/day ───┤
│ (Priority 2) │                       │
└──────────────┘                       │
                                       │
┌──────────────┐                       │
│   Standard   │ ──── 20 orders/day ──┘
│ (Priority 3) │
└──────────────┘

INVENTORY (Work in Process):
┌──────────────────────────────────┐
│ Ultra-chrome:    10 orders       │ ← Known
│ Ex-chrome:       8 orders        │ ← Known  
│ Standard:        ??? orders      │ ← TO FIND
│ TOTAL:           ??? orders      │ ← TO FIND
└──────────────────────────────────┘
```

### How Priority Works

```
Production Queue (Simplified View):

Time t=0:
[Ultra][Ultra][Ultra] | [Ex][Ex] | [Standard][Standard][Standard]...
  ↑ Start here first     ↑ Next      ↑ Last (only when others done)

Priority Rule:
1. Process ALL ultra-chrome orders first
2. Then process ALL ex-chrome orders
3. Finally process standard orders
4. If new ultra arrives, it jumps ahead
```

### Little's Law Application

```
For ENTIRE SYSTEM:
┌────────────────────────────────────────────┐
│  I_total = R_total × T_system              │
│                                            │
│  Where:                                    │
│  - R_total = 20 + 4 + 8 = 32 orders/day   │
│  - T_system = 6 days (given)               │
│  - I_total = ? (calculate this)           │
└────────────────────────────────────────────┘

For EACH ORDER TYPE:
┌────────────────────────────────────────────┐
│  Standard:                                  │
│  I_standard = I_total - I_ultra - I_ex     │
│  T_standard = I_standard / R_standard      │
│                                            │
│  Ex-chrome:                                │
│  T_ex = I_ex / R_ex                        │
│         = 8 / 4 = 2 days                   │
│                                            │
│  Ultra-chrome:                             │
│  T_ultra = I_ultra / R_ultra               │
│          = 10 / 8 = 1.25 days              │
└────────────────────────────────────────────┘
```

### Key Insight

Lower priority orders accumulate more inventory because they wait longer!

---

## Problem 5: Global Trans Co. - Closed Loop System

### System Diagram

```
┌──────────────────────────────────────────────────────────────┐
│           GLOBAL TRANS CO. - SHIP FLOW SYSTEM                │
└──────────────────────────────────────────────────────────────┘

                 ┌─────────────────────┐
                 │  PORT (France)      │
                 │                     │
                 │  • Load/Unload      │
    ┌───────────>│  • 6 ships here     │────────────┐
    │            │  • 2 days avg       │            │
    │            └─────────────────────┘            │
    │                                                │
    │                                                │
    │            AT SEA (Traveling)                  │
    │            • 24 ships                          │
    │            • ??? days (to find)                │
    │                                                │
    │                                                │
    │            ┌─────────────────────┐             │
    └────────────│   DELIVERY POINT    │<────────────┘
                 │   (Europe)          │
                 │                     │
                 │ $50,000 per         │
                 │ delivery            │
                 └─────────────────────┘

TOTAL SYSTEM:
• 30 ships total (constant)
• Ships continuously cycle
• Steady state system
```

### System Breakdown

```
SUBSYSTEM 1: The Port
┌──────────────────────────────────────┐
│  I = 6 ships                         │
│  T = 2 days                          │
│  R = I/T = 6/2 = 3 ships/day        │
│                                      │
│  (This is the throughput of the      │
│   entire system!)                    │
└──────────────────────────────────────┘

SUBSYSTEM 2: Traveling
┌──────────────────────────────────────┐
│  Ships at sea = Total - In port      │
│                = 30 - 6 = 24 ships   │
│                                      │
│  R = 3 ships/day (same as port)     │
│  I = 24 ships                        │
│  T = I/R = 24/3 = 8 days            │
└──────────────────────────────────────┘

COMPLETE CYCLE:
┌──────────────────────────────────────┐
│  Total cycle = Port + Travel         │
│              = 2 + 8 = 10 days       │
│                                      │
│  Can verify with total system:       │
│  T = I/R = 30/3 = 10 days ✓         │
└──────────────────────────────────────┘
```

### Revenue Calculation

```
Monthly Earnings Calculation:
┌────────────────────────────────────────┐
│  Step 1: Daily deliveries              │
│  R = 3 ships/day                       │
│                                        │
│  Step 2: Revenue per delivery          │
│  $50,000 per ship                      │
│                                        │
│  Step 3: Monthly total                 │
│  = 3 ships/day × $50,000 × 30 days     │
│  = $4,500,000                          │
└────────────────────────────────────────┘
```

### Key Insight

This is a **closed system** - total inventory (30 ships) is fixed!
The bottleneck determines throughput for the entire system.

---

## Problem 6: J.C. Nickel - Parallel Multi-Server System

### System Layout

```
┌────────────────────────────────────────────────────────────────┐
│                    J.C. NICKEL RETAIL STORE                     │
│                   Checkout System (120 customers/hour)          │
└────────────────────────────────────────────────────────────────┘

                         CUSTOMERS ARRIVE
                              ↓ 120/hr
                              ↓
              ┌───────────────┴───────────────┐
              ↓                               ↓
    ┌─────────────────┐              ┌──────────────────┐
    │  CASHIER LINE   │              │ SELF-CHECKOUT    │
    │                 │              │     LINE         │
    └────────┬────────┘              └────────┬─────────┘
             │                                │
      (10 waiting)                      (? waiting)
             │                                │
             ↓                                ↓
    ┌─────────────────┐              ┌──────────────────┐
    │  6 CASHIERS     │              │  2 MACHINES      │
    │  (1 idle)       │              │  (1 idle)        │
    │                 │              │                  │
    │  Service: 3 min │              │  Total: 5 min    │
    └─────────────────┘              └──────────────────┘
             │                                │
             └────────────┬───────────────────┘
                          ↓
                    EXIT STORE
```

### Detailed Subsystem Analysis

```
SUBSYSTEM A: Cashiers
━━━━━━━━━━━━━━━━━━━━━━━━━

SERVERS:
┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
│ Cash 1  │ Cash 2  │ Cash 3  │ Cash 4  │ Cash 5  │ Cash 6  │
│  BUSY   │  BUSY   │  BUSY   │  BUSY   │  BUSY   │  IDLE   │
└─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
   ↑ 5 busy cashiers

THROUGHPUT:
• Busy servers = 6 - 1 = 5
• Service rate per cashier = 1/3 min = 0.333 customers/min
• Total throughput = 5 × (1/3) = 5/3 customers/min
• In customers/hour = (5/3) × 60 = 100 customers/hour

QUEUE:
• I = 10 customers waiting
• R = 5/3 customers/min
• T_wait = 10 ÷ (5/3) = 6 minutes

TOTAL TIME AT CASHIER:
• Wait (6 min) + Service (3 min) = 9 minutes


SUBSYSTEM B: Self-Checkout
━━━━━━━━━━━━━━━━━━━━━━━━━

MACHINES:
┌──────────────┬──────────────┐
│   Machine 1  │   Machine 2  │
│     BUSY     │     IDLE     │
└──────────────┴──────────────┘
   ↑ 1 busy machine

THROUGHPUT:
• Total customers = 120/hr
• Cashier customers = 100/hr (calculated above)
• Self-checkout = 120 - 100 = 20 customers/hour
• Fraction = 20/120 = 16.7% (approx)

SYSTEM ANALYSIS (5 min total given):
• I_system = R × T = (20/60) × 5 = 1.67 customers in system
• I_being_served = 1 (busy machines)
• I_waiting = 1.67 - 1 = 0.67 customers
• T_wait = 0.67 ÷ (20/60) = 2 minutes
• T_service = 5 - 2 = 3 minutes
```

### Scenario Analysis: Adding 2 Cashiers

```
CURRENT SCENARIO:
┌────────────────────────────────────┐
│ Cashiers: 6 (5 busy)               │
│ Queue: 10 customers                │
│ Throughput: 5/3 per min            │
│ Wait time: 6 minutes               │
└────────────────────────────────────┘

PROPOSED SCENARIO:
┌────────────────────────────────────┐
│ Cashiers: 8 (assume 7 busy)       │
│ Queue: 5 customers (IF cut in half)│
│ Throughput: 7/3 per min            │
│ Wait time: 5 ÷ (7/3) = 2.14 min   │
└────────────────────────────────────┘

CLAIM EVALUATION:
✓ IF queue is cut in half (big assumption!)
✗ Wait time would be 2.14 min (not < 2 min)

WHAT QUEUE IS NEEDED FOR 2 MIN WAIT?
• I = R × T = (7/3) × 2 = 4.67 customers
• Need queue ≤ 4.67 (not 5)
```

### Key Insight

Multi-server systems are complex! 
- Adding servers increases throughput
- But wait time depends on queue length
- Can't assume queue reduction is proportional

---

## Quick Reference: Little's Law Formulas

### The Three Forms

```
┌─────────────────────────────────────────────┐
│  STANDARD FORM                              │
│  I = R × T                                  │
│                                             │
│  Use when: Finding inventory                │
│  Example: Total orders at Chrome Wheels     │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  SOLVE FOR THROUGHPUT                       │
│  R = I / T                                  │
│                                             │
│  Use when: Finding flow rate                │
│  Example: Ships per day at Global Trans     │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  SOLVE FOR FLOW TIME                        │
│  T = I / R                                  │
│                                             │
│  Use when: Finding wait/cycle time          │
│  Example: Standard order wait at CW         │
└─────────────────────────────────────────────┘
```

### Common Pitfalls

```
❌ WRONG: Using arrival rate when system is at capacity
   → Use actual throughput (may be less than arrivals!)

❌ WRONG: Forgetting to convert units (days ↔ hours ↔ minutes)
   → Always check your time units!

❌ WRONG: Applying to unstable systems (growing queue)
   → Little's Law requires steady state

❌ WRONG: Using inventory in queue when you need total inventory
   → Total I = Queue + Being Served

✓ RIGHT: Verify your answer makes sense
   → Negative time? Impossible!
   → Wait time > total time? Check your logic!
```

---

## Problem-Solving Strategy

### Step 1: Draw the System
```
Identify:
• Where do items enter?
• Where do they exit?
• What are the subsystems?
• What flows between them?
```

### Step 2: List What You Know
```
Given values:
• Arrival rates (R)
• Inventories (I)  
• Times (T)
• Number of servers
• Service rates
```

### Step 3: Identify What You Need to Find
```
Questions asking for:
• "Average number" → Inventory (I)
• "How many per time" → Throughput (R)
• "How long" → Flow Time (T)
```

### Step 4: Choose the Right Form of Little's Law
```
Have R and T, need I? → I = R × T
Have I and T, need R? → R = I / T
Have I and R, need T? → T = I / R
```

### Step 5: Verify Your Answer
```
Sanity checks:
• Are values positive?
• Do units make sense?
• Is the magnitude reasonable?
• Do sub-parts add up to totals?
```

---

## Tips for Success

### 1. Unit Consistency
```
✓ GOOD: R = 20 orders/day, T = 6 days → I = 120 orders
✗ BAD:  R = 20 orders/day, T = 6 hours → I = ??? (mixed units!)
```

### 2. Steady State Assumption
```
Little's Law assumes:
• Average rates (not just one moment in time)
• System is stable (not growing/shrinking)
• Long-run averages (not short-term fluctuations)
```

### 3. Subsystem Analysis
```
For complex systems:
1. Analyze each subsystem separately
2. Find throughput of each part
3. Verify flow conservation (what goes in = what comes out)
4. Combine for total system analysis
```

### 4. Common Calculations
```
Utilization = (Busy servers) / (Total servers)

Service rate = 1 / (Service time)
   Example: 3 min service → 1/3 customers/min rate

Throughput = (Busy servers) × (Service rate per server)
```

---

## Visualization Tips for Your App

### Good Practices
- Use different colors for different order types/systems
- Show relationships (Sankey diagrams for flow)
- Compare scenarios side-by-side
- Highlight key metrics with metric cards
- Add tooltips to explain calculations

### Chart Types
- **Bar charts**: Compare quantities (inventory levels)
- **Pie charts**: Show proportions (customer split)
- **Line/scatter**: Show relationships (scenarios)
- **Gauge charts**: Show rates/throughput
- **Sankey**: Show flows through system

---

**Ready to start?** Use this guide while working through the problems!

Remember: Understanding the system is half the battle. Once you see how things flow, Little's Law becomes much easier to apply.

Good luck! 🎓
