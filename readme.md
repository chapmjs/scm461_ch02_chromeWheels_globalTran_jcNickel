# Little's Law Homework Assignment
## Operations Management - Spring 2025

---

## 📚 Table of Contents
1. [Assignment Overview](#assignment-overview)
2. [What You'll Learn](#what-youll-learn)
3. [Files in This Package](#files-in-this-package)
4. [Step-by-Step Instructions](#step-by-step-instructions)
5. [Deployment Guide](#deployment-guide)
6. [Troubleshooting](#troubleshooting)
7. [Grading Rubric](#grading-rubric)
8. [Resources](#resources)

---

## 🎯 Assignment Overview

In this homework, you'll apply **Little's Law** (I = R × T) to solve three real-world operations management problems:

1. **Problem 4: Chrome Wheels Inc.** - Manufacturing with priority systems
2. **Problem 5: Global Trans Co.** - Logistics and fleet management
3. **Problem 6: J.C. Nickel Retail** - Multi-server queuing systems

**Deliverables:**
- ✅ Completed calculations using Little's Law
- ✅ Working Streamlit web application
- ✅ Published app on Streamlit Cloud
- ✅ GitHub repository with your code

---

## 🧠 What You'll Learn

### Operations Management Concepts
- Understanding Little's Law and its applications
- Analyzing inventory, throughput, and flow time relationships
- Working with priority systems and queuing theory
- Evaluating "what-if" scenarios in operations

### Technical Skills
- Python programming basics
- Data analysis and calculations
- Creating visualizations with Plotly
- Building web applications with Streamlit
- Version control with Git and GitHub
- Deploying applications to the cloud

**No prior programming experience required!** This assignment is designed to be accessible to beginners.

---

## 📦 Files in This Package

```
littles-law-homework/
├── README.md                          # This file
├── littles_law_homework_template.py   # Your calculation template (use in Colab)
├── streamlit_app.py                   # Your web app code
├── requirements.txt                   # Python dependencies
└── .gitignore                        # Files to ignore in Git
```

---

## 📝 Step-by-Step Instructions

### Phase 1: Complete Your Calculations (Google Colab)

#### Step 1: Open Google Colab
1. Go to https://colab.research.google.com/
2. Sign in with your Google account
3. Click **File → Upload notebook**
4. Upload `littles_law_homework_template.py`

#### Step 2: Install Packages
Run in first cell:
```python
!pip install pandas numpy matplotlib plotly streamlit -q
```

#### Step 3: Work Through Problems
- Read each problem carefully
- Fill in TODO sections
- Use Little's Law: I = R × T
- Run cells to check your work

#### Step 4: Save Your Work
**File → Download → Download .py**

---

### Phase 2: Create GitHub Repository

#### Step 5: Create Repository
1. Go to https://github.com and sign in
2. Click **+** → **New repository**
3. Name it: `littles-law-homework`
4. Make it **Public**
5. Add README file
6. Click **Create repository**

#### Step 6: Upload Files
1. Click **Add file** → **Upload files**
2. Upload:
   - `streamlit_app.py` (with YOUR calculated values!)
   - `requirements.txt`
   - `littles_law_homework_template.py`
3. Click **Commit changes**

**Or use Git command line:**
```bash
git clone https://github.com/yourusername/littles-law-homework.git
cd littles-law-homework
# Copy your files here
git add .
git commit -m "Add homework files"
git push origin main
```

---

### Phase 3: Deploy to Streamlit

#### Step 7: Deploy Your App
1. Go to https://streamlit.io/cloud
2. Sign in with GitHub
3. Click **New app**
4. Select:
   - Repository: `yourusername/littles-law-homework`
   - Branch: `main`
   - Main file: `streamlit_app.py`
5. Click **Deploy!**

#### Step 8: Test and Submit
1. Wait 2-5 minutes for deployment
2. Test your app URL
3. Submit the URL for grading

---

## 🔧 Troubleshooting

### Issue 1: Missing Packages

**Error:** `ModuleNotFoundError: No module named 'plotly'`

**Fix:** Create `requirements.txt` with:
```
streamlit
pandas
numpy
plotly
```

**AI Prompt:**
```
I'm getting ModuleNotFoundError for plotly in my Streamlit app. 
My requirements.txt has: [paste content]
How do I fix this?
```

---

### Issue 2: Placeholder Values Showing

**Problem:** App shows example values, not YOUR calculations

**Fix:**
1. Open `streamlit_app.py`
2. Find line ~42 (CALCULATIONS section)
3. Replace ALL TODO values with your results
4. Save and push to GitHub

**AI Prompt:**
```
My Streamlit app shows placeholder values instead of my calculations.
I calculated total_inventory = 192, but app shows wrong value.
How do I update the values in streamlit_app.py?
```

---

### Issue 3: Git Authentication Error

**Error:** `authentication failed`

**Fix:**
Use Personal Access Token:
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate token with 'repo' scope
3. Use token as password when git asks

**AI Prompt:**
```
Getting 'authentication failed' when pushing to GitHub.
Using HTTPS URL. How do I authenticate properly?
```

---

### Issue 4: Division by Zero

**Error:** `ZeroDivisionError`

**Fix:**
- Check your R (throughput) isn't 0
- Check your T (flow time) isn't 0
- Use helper functions with built-in checks

**AI Prompt:**
```
Getting division by zero error calculating T = I/R.
I = [value], R = [value]
What's wrong with my Little's Law calculation?
```

---

### Issue 5: Charts Not Showing

**Problem:** Blank space where charts should be

**Fix:**
1. Check imports: `import plotly.graph_objects as go`
2. Verify `plotly` in requirements.txt
3. Check chart syntax matches template

**AI Prompt:**
```
My Streamlit app loads but charts don't display.
Using plotly with this code: [paste code]
What's the issue?
```

---

### Issue 6: Indentation Error

**Error:** `IndentationError: unexpected indent`

**Fix:**
- Use consistent spaces (4 spaces recommended)
- Don't mix tabs and spaces
- Use VS Code's "Format Document"

**AI Prompt:**
```
Getting IndentationError on line X.
Here's my code: [paste 5 lines around error]
How do I fix indentation?
```

---

### General Debugging Tips

**Use AI Effectively:**

Good prompt structure:
```
Problem: [What's wrong]
Context: [What you're doing]
What I tried: [Your attempts]
Code: [Relevant snippet]
Error: [Exact message]
Question: [Specific question]
```

**Add Debug Prints:**
```python
print(f"R = {R}, T = {T}, I = {I}")
print(f"Type of R: {type(R)}")
```

**Test Locally First:**
```bash
cd your-project-folder
streamlit run streamlit_app.py
```

---

## 📊 Grading Rubric

| Category | Points | Details |
|----------|--------|---------|
| **Calculations** | 40 | Correct Little's Law applications |
| - Problem 4 | 15 | All three calculations |
| - Problem 5 | 10 | Earnings & travel time |
| - Problem 6 | 15 | Multi-part analysis |
| **Streamlit App** | 30 | Functionality & presentation |
| **GitHub Repo** | 15 | Complete, clean repository |
| **Deployment** | 15 | Live, working app |
| **Total** | **100** | |

---

## 📚 Resources

### Learning Little's Law
- Textbook: Iravani's Operations Management
- Khan Academy: Operations Management
- YouTube: "Little's Law Explained"

### Python & Streamlit
- Python.org Beginner's Guide
- Streamlit Documentation: https://docs.streamlit.io
- Real Python Tutorials
- Google Colab Tutorials

### Git & GitHub
- GitHub Skills: https://skills.github.com/
- Git Handbook
- GitHub Desktop (GUI option)

### Plotly Visualization
- Plotly Python: https://plotly.com/python/
- Plotly Express Tutorial
- Graph Objects Documentation

---

## ✅ Submission Checklist

Before submitting:

- [ ] Calculations completed and verified
- [ ] Values updated in streamlit_app.py (not placeholders!)
- [ ] Name added to app
- [ ] All files in GitHub
- [ ] requirements.txt includes all packages
- [ ] App deployed on Streamlit Cloud
- [ ] App URL accessible and working
- [ ] Charts display correctly
- [ ] Submitted URL in course system

---

## ❓ FAQ

**Q: How long should this take?**
A: 4-6 hours total (2-3 for calculations, 1-2 for deployment, 1 for debugging)

**Q: Can I work with a partner?**
A: Ask your instructor. Usually individual work, but can help with technical issues.

**Q: What if I'm completely stuck?**
A: 
1. Check troubleshooting section
2. Ask in discussion forum with specific details
3. Attend office hours
4. Email instructor with:
   - What you tried
   - Exact error message
   - Your code/repository link

**Q: Can I enhance the app with extra features?**
A: Yes! But get the basics working first.

---

## 🎓 Learning Outcomes

After this assignment, you'll be able to:

1. ✅ Apply Little's Law to operational problems
2. ✅ Decompose complex systems  
3. ✅ Write Python code for calculations
4. ✅ Create data visualizations
5. ✅ Build and deploy web apps
6. ✅ Use Git/GitHub for version control
7. ✅ Debug technical problems systematically
8. ✅ Present quantitative analysis effectively

---

## 🚀 Quick Start for Experienced Students

```bash
# 1. Complete calculations in Colab
# 2. Clone template
git clone https://github.com/yourusername/littles-law-homework.git

# 3. Add your files & update values in streamlit_app.py

# 4. Push to GitHub
git add .
git commit -m "Complete homework"
git push

# 5. Deploy on streamlit.io/cloud
# 6. Submit app URL
```

---

**Questions?** Contact instructor or post in discussion forum.

**Good luck!** 🎯
