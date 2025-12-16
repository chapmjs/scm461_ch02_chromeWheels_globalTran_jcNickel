# Quick Start Guide
## Little's Law Homework - Get Started in 10 Minutes!

---

## 🚀 What You'll Do

This homework has 4 main steps:
1. **Calculate** (Google Colab) - 2-3 hours
2. **Code** (Update Streamlit app) - 30 min
3. **Commit** (Push to GitHub) - 15 min
4. **Deploy** (Streamlit Cloud) - 5 min

Total time: ~4-6 hours for first-time Python users

---

## 📋 Before You Start - Checklist

Create accounts (all free):
- [ ] Google account (for Colab)
- [ ] GitHub account
- [ ] Streamlit Cloud account (sign up with GitHub)

Download files from this folder:
- [ ] littles_law_homework_template.py
- [ ] streamlit_app.py
- [ ] requirements.txt
- [ ] .gitignore

Read these guides:
- [ ] README.md (full instructions)
- [ ] VISUAL_GUIDE.md (understand the problems)

---

## ⚡ 10-Minute Quick Start

### Minute 1-2: Understand Little's Law

```
Little's Law: I = R × T

I (Inventory)  = Number of items in the system
R (Throughput) = Rate items flow through  
T (Flow Time)  = Time each item spends in system

Example: Restaurant with 30 customers (I), 
         serving 10/hour (R), each stays 3 hours (T)
         Check: 30 = 10 × 3 ✓
```

### Minute 3-5: Scan the Problems

**Problem 4: Chrome Wheels**
- 3 order types with different priorities
- Find: total orders, wait times by priority
- Key challenge: decomposing by priority level

**Problem 5: Global Trans**  
- 30 ships, some in port, some traveling
- Find: monthly earnings, travel time
- Key challenge: closed system (fixed ships)

**Problem 6: J.C. Nickel**
- Cashiers + self-checkout
- Find: wait times, throughput split
- Key challenge: parallel multi-server system

### Minute 6-8: Set Up Colab

1. Go to https://colab.research.google.com
2. File → Upload notebook
3. Upload `littles_law_homework_template.py`
4. Run first cell to install packages:
```python
!pip install pandas numpy matplotlib plotly -q
```

### Minute 9-10: Start Problem 4

1. Read the problem statement
2. Draw a simple diagram (on paper!)
3. List what you know vs. what you need to find
4. Start with: Total throughput = 20 + 4 + 8 = ?

---

## 🎯 Focus Areas for Each Problem

### Problem 4: Chrome Wheels

**Key insight:** Use Little's Law twice
1. First for TOTAL system (find total inventory)
2. Then for EACH priority level (find individual wait times)

**Start here:**
```python
# Total system
R_total = 20 + 4 + 8  # orders/day
T_total = 6  # days
I_total = R_total * T_total  # TODO: Calculate!
```

### Problem 5: Global Trans

**Key insight:** Port is the bottleneck
1. Find throughput at port using Little's Law
2. This is throughput for whole system!
3. Use total system to find travel time

**Start here:**
```python
# At the port
I_port = 6  # ships
T_port = 2  # days
R = I_port / T_port  # TODO: Calculate deliveries/day
```

### Problem 6: J.C. Nickel

**Key insight:** Two separate subsystems
1. Analyze cashier system first
2. Then analyze self-checkout
3. Combine for overall metrics

**Start here:**
```python
# Cashier throughput
busy_cashiers = 6 - 1  # 5 busy
service_time = 3  # minutes per customer
R_per_cashier = 1 / service_time
R_total_cashiers = busy_cashiers * R_per_cashier  # TODO: in customers/min
```

---

## 🔍 How to Check Your Work

### Sanity Checks

**Are your values reasonable?**
- ✓ All times positive?
- ✓ Flow time makes sense vs. service time?
- ✓ Inventory ≥ 0?
- ✓ Percentages between 0 and 1?

**Do the parts add up?**
- ✓ Problem 4: I_ultra + I_ex + I_standard = I_total?
- ✓ Problem 5: Port time + Travel time = Total cycle?
- ✓ Problem 6: Cashier + Self-checkout = 120 customers/hr?

**Common mistakes:**
- ❌ Mixed units (days with hours)
- ❌ Used arrivals instead of throughput
- ❌ Forgot to account for idle servers
- ❌ Used service time instead of rate

---

## 💡 Pro Tips

### Calculation Tips
1. **Always draw first** - Visual understanding beats formulas
2. **Label everything** - What's I? What's R? What's T?
3. **Check units** - Days? Hours? Minutes? Customers? Orders?
4. **Verify conservation** - Flow in = Flow out

### Coding Tips
1. **Use helper functions** - They handle edge cases
2. **Add print statements** - See intermediate values
3. **Test incrementally** - One problem at a time
4. **Comment your logic** - Future you will thank you

### Deployment Tips
1. **Test locally first** - Run streamlit app on your computer
2. **Update values** - Don't forget to replace TODOs!
3. **Check requirements.txt** - Include all packages
4. **Commit often** - Small changes are easier to debug

---

## 🆘 When You Get Stuck

### Quick Debugging

**Division by zero?**
```python
# Before:
T = I / R  # Error if R = 0!

# After:
if R == 0:
    print(f"ERROR: R is zero! Check your calculation.")
else:
    T = I / R
```

**Wrong answer?**
```python
# Add debug prints
print(f"I = {I}, R = {R}, T = {T}")
print(f"Expected approximately: [your estimate]")
```

**Not sure what to do?**
1. Re-read the problem statement
2. Check VISUAL_GUIDE.md for diagrams
3. Look at the example code in template
4. Ask: "What do I know? What do I need to find?"

---

## 📚 Resources at a Glance

**Need help with:**
- **Concepts** → VISUAL_GUIDE.md (this folder)
- **Instructions** → README.md (this folder)
- **Python** → Template has examples and comments
- **Streamlit** → https://docs.streamlit.io
- **Git** → https://skills.github.com
- **Debugging** → README.md Troubleshooting section

---

## ✅ Daily Goals

### Day 1: Understand & Calculate
- [ ] Read all three problem statements
- [ ] Draw system diagrams
- [ ] Complete Problem 4 calculations
- [ ] Verify answers make sense

### Day 2: Calculate & Code
- [ ] Complete Problem 5 calculations
- [ ] Complete Problem 6 calculations
- [ ] Update streamlit_app.py with your values
- [ ] Test locally if possible

### Day 3: Deploy & Submit
- [ ] Create GitHub repository
- [ ] Push all files
- [ ] Deploy to Streamlit Cloud
- [ ] Test your live app
- [ ] Submit app URL

---

## 🎓 Learning Philosophy

**This homework teaches TWO things:**

1. **Operations Management**
   - How systems flow
   - How to measure performance
   - How to analyze bottlenecks

2. **Technical Skills**  
   - Python programming basics
   - Data visualization
   - Cloud deployment

**Don't worry if technical parts are challenging!**
- That's expected for first-timers
- Focus on understanding concepts first
- Use the troubleshooting guide
- Ask for help when stuck

---

## 🎉 Success Criteria

You'll know you're done when:

- [ ] All three problems calculated correctly
- [ ] Streamlit app shows YOUR values (not placeholders)
- [ ] App deployed and accessible via URL
- [ ] Charts display properly
- [ ] You can explain your approach

**Most importantly:** You understand how Little's Law helps analyze operational systems!

---

## 🚀 Ready to Start?

1. Open Google Colab
2. Upload `littles_law_homework_template.py`
3. Start with Problem 4
4. Use VISUAL_GUIDE.md when you need help

**You've got this!** 💪

---

**Questions?** Check README.md for detailed help or contact your instructor.

**Good luck!** 🎯
